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
    PTDLMerge = PTDLMerge.fillna(0)
    for i in range(len(PTDLMerge['name'])) :
        value = int(PTDLMerge['value_y'][i]) - int(PTDLMerge['value_x'][i])
        ROCDFDL.append([PTDLMerge['name'][i], value])
    ROCDF = pd.DataFrame(ROCDFDL, columns=ROCDFCNM)
    DLMerge = pd.merge(left=PTDLMerge, right=ROCDF, how="outer", on="name").sort_values(by="name", ascending=True).reset_index(drop=True)
    RD = DLMerge
    return RD

def alarm_case_detection(data, case) :
    #print(data)
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
            if type(DLMerge['Today'][j]) != float and DLMerge['Today'][j] != '[current result unavailable]':
                #date = datetime.strptime(DLMerge['Today'][j].split(' +')[0], "%a, %d %b %Y %H:%M:%S")
                #date = str(date).split(' ')[0]
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
        if data['value'][0]:
            for i in range(len(data['value'])):
                IPS = data['value'][i].split('.')
                if len(IPS) == 4 :
                    IP = IPS[0] + '.' + IPS[1] + '.' + IPS[2]
                ADL.append([IP])
        RD = pd.DataFrame(ADL, columns=['group']).groupby(['group']).size().reset_index(name='counts')
        RD['alarmCase'] = AT
    elif type == 'max' :
        nodeDataList = []
        linksDataList = []
        odf = pd.DataFrame(data[1], columns=data[0])
        MDF = odf.loc[odf.groupby(['group'])['alarmCount'].idxmax()]
        MDF['point'] = 'true'
        df = pd.merge(left=odf, right=MDF, how="left",on=['id', 'group', 'alarmCount', 'name', 'alarmCase']).sort_values(by="id", ascending=True).reset_index()

        DFG = df.groupby(['group']).sum(['alarmCount']).reset_index()
        for j in range(len(DFG.group)):
            groupNameCountSplit = DFG.group[j].split('.')
            groupNameCount = groupNameCountSplit[0]+groupNameCountSplit[1]+groupNameCountSplit[2]
            nodeDataList.append({'group': DFG.group[j],'alarmCount': str(DFG.alarmCount[j]), 'id': 'groupCenter'+str(groupNameCount), 'name': DFG.group[j], 'alarmCase': DFG.group[j]})
        for i in range(len(df.id)) :
            groupNameCountSplit = df.group[i].split('.')
            groupNameCount = groupNameCountSplit[0] + groupNameCountSplit[1] + groupNameCountSplit[2]
            if df.point[i] == 'true' :
                point = 'true'
            else :
                point = 'false'
            nodeDataList.append({'group' : df.group[i], 'alarmCount': str(df.alarmCount[i]), 'id':df.id[i], 'name':df.name[i], 'alarmCase':df.alarmCase[i], 'point':point})
            linksDataList.append({'source': df.id[i], 'target': 'groupCenter'+str(groupNameCount)})
        RD ={'nodeDataList':nodeDataList, 'linksDataList':linksDataList}

    return RD




