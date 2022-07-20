from datetime import datetime, timedelta

import pandas as pd
import json
weekAgo = (datetime.today() - timedelta(7)).strftime("%Y-%m-%d")
today = datetime.today().strftime("%Y-%m-%d")

with open("setting.json", encoding="UTF-8") as f:
    SETTING = json.loads(f.read())

AlarmStandard = SETTING['PROJECT']['Alarm']['StandardDate']
AlarmRamUsage = SETTING['PROJECT']['Alarm']['RamUsage']
alarmCaseFirst = SETTING['PROJECT']['Alarm']['Case']['First']
alarmCaseSecond = SETTING['PROJECT']['Alarm']['Case']['Second']
alarmCaseThird = SETTING['PROJECT']['Alarm']['Case']['Third']
alarmCaseFourth = SETTING['PROJECT']['Alarm']['Case']['Fourth']
alarmCaseFifth = SETTING['PROJECT']['Alarm']['Case']['Fifth']

def calculation(pastData, todayData) :
    PTDLMerge = pd.merge(left=pastData, right=todayData, how="outer", on="name").sort_values(by="name", ascending=True).reset_index(drop=True)
    ROCDFDL = []
    ROCDFCNM = ['name','ROC']
    for i in range(len(PTDLMerge['name'])) :
        value = int(PTDLMerge['value_y'][i]) - int(PTDLMerge['value_x'][i])
        ROCDFDL.append([PTDLMerge['name'][i], value])
    ROCDF = pd.DataFrame(ROCDFDL, columns=ROCDFCNM)
    DLMerge = pd.merge(left=PTDLMerge, right=ROCDF, how="outer", on="name").sort_values(by="name", ascending=True).reset_index(drop=True)
    RD = DLMerge
    return RD

def alarmCaseDetection(data, case) :
    if case == 'DUS':
        AT = alarmCaseFirst
    elif case == 'LH':
        AT = alarmCaseSecond
    elif case == 'RUE':
        AT = alarmCaseThird
    elif case == 'LPC':
        AT = alarmCaseFourth
    elif case == 'EPC':
        AT = alarmCaseFifth

    TDL = data[0]
    PDL = data[1]
    DLMerge = pd.merge(left=TDL, right=PDL, how="outer", on="id").sort_values(by="id", ascending=True).reset_index(drop=True).drop(['ip_y'], axis=1)
    DLMerge.columns = ['id', 'Today', 'ip', 'Past']
    DL = []
    DLC =['name', 'value', 'alarmText']
    for j in range(len(DLMerge)):
        if case == 'LH':
            if DLMerge['Today'][j] < AlarmStandard :
                AI = DLMerge['id'][j]
                IP = DLMerge['ip'][j]
                DL.append([AI, IP, AT])
        elif case == 'RUE':
            if DLMerge['Today'][j] != 0 and DLMerge['Past'][j] != 0 :
                usage = DLMerge['Past'][j]/DLMerge['Today'][j]*100
                if usage > AlarmRamUsage :
                    AI = DLMerge['id'][j]
                    IP = DLMerge['ip'][j]
                    DL.append([AI, IP, AT])
        else:
            if DLMerge['Today'][j] == DLMerge['Past'][j]:
                AI = DLMerge['id'][j]
                IP = DLMerge['ip'][j]
                DL.append([AI, IP, AT])
    RD = pd.DataFrame(DL, columns=DLC)
    return RD


def network(data, type, case) :
    if case == 'DUS':
        AT = alarmCaseFirst
    elif case == 'LH':
        AT = alarmCaseSecond
    elif case == 'RUE':
        AT = alarmCaseThird
    elif case == 'LPC':
        AT = alarmCaseFourth
    elif case == 'EPC':
        AT = alarmCaseFifth

    if type == 'group' :
        ADL = []
        if data['name'][0]:
            for i in range(len(data['name'])):
                IPS = data['value'][i].split('.')
                IP = IPS[0] + '.' + IPS[1] + '.' + IPS[2]
                ADL.append([IP])
        RD = pd.DataFrame(ADL, columns=['group']).groupby(['group']).size().reset_index(name='counts')
        RD['alarmCase'] = AT
    elif type == 'max' :
        odf = pd.DataFrame(data[1], columns=data[0])
        MDF = odf.loc[odf.groupby(['group'])['alarmCount'].idxmax()]
        MDF['point'] = 'true'
        df = pd.merge(left=odf, right=MDF, how="left",on=['id', 'group', 'alarmCount', 'name', 'alarmCase']).sort_values(by="id", ascending=True).reset_index()
        DFG = df.groupby(['group']).size().reset_index(name='counts')
        print(DFG)
        for i in range(len(df.id)) :
            if df.point[i] == 'true' :
                point = 'true'
            else :
                point = 'false'
            #print({'group' : df.group[i], 'alarmCount': str(df.alarmCount[i]), 'id':df.id[i], 'name':df.name[i], 'alarmCase':df.alarmCase[i], 'point':point})
        RD ={}
    return RD




