from datetime import datetime, timedelta

import pandas as pd
import json
weekAgo = (datetime.today() - timedelta(7)).strftime("%Y-%m-%d")
today = datetime.today().strftime("%Y-%m-%d")

with open("setting.json", encoding="UTF-8") as f:
    SETTING = json.loads(f.read())

AlarmStandard = SETTING['PROJECT']['AlarmStandardDate']
AlarmRamUsage = SETTING['PROJECT']['AlarmRamUsage']


def Calculation(pastData, todayData) :
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

def AlarmList(data, type) :
    TDL = data[0]
    PDL = data[1]
    DLMerge = pd.merge(left=TDL, right=PDL, how="outer", on="id").sort_values(by="id", ascending=True).reset_index(drop=True).drop(['ip_y'], axis=1)
    DLMerge.columns = ['id', 'Today', 'ip', 'Past']
    DL = []
    DLC =['name', 'value']
    for j in range(len(DLMerge)):
        if type == 'LH':
            if DLMerge['Today'][j] < AlarmStandard :
                AI = DLMerge['id'][j]
                IP = DLMerge['ip'][j]
                DL.append([AI, IP])
        elif type == 'RUS':
            if DLMerge['Today'][j] != 0 and DLMerge['Past'][j] != 0 :
                usage = DLMerge['Past'][j]/DLMerge['Today'][j]*100
                if usage > AlarmRamUsage :
                    AI = DLMerge['id'][j]
                    IP = DLMerge['ip'][j]
                    DL.append([AI, IP])
        else:
            if DLMerge['Today'][j] == DLMerge['Past'][j]:
                AI = DLMerge['id'][j]
                IP = DLMerge['ip'][j]
                DL.append([AI, IP])
    DF = pd.DataFrame(DL, columns=DLC)
    RD = DF
    return RD
