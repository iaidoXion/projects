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


def chart_data(data, type, statistics) :
    if statistics == 'group' :
        if type == 'assetItem' :
            GBI = 'assetItem'
        elif type == 'osItem' :
            GBI = 'os'
        IG = data.groupby([GBI])
        IGR = IG.size().reset_index(name='counts')
        if type == 'assetItem':
            INML = IGR.assetItem
        elif type == 'osItem':
            INML = IGR.os
        INM = INML.tolist()
        ICL = IGR.counts
        IC = ICL.tolist()

    elif statistics == 'count' :
        todayDL = data[0]
        yesterdayDL = data[1]
        DLMerge = pd.merge(left=todayDL, right=yesterdayDL, how="outer", on="id").sort_values(by="id", ascending=True).reset_index(drop=True)
        DTC = len(DLMerge)
        if type == 'DUS' :
            DUSCY = len(DLMerge['driveSize_x'].compare(DLMerge['driveSize_y']))
            INM = [alarmCaseFirst]
        elif type == 'LH':
            DUSCY = len(DLMerge[(DLMerge['lastLogin_x'] < AlarmStandard)])
            INM = [alarmCaseSecond]
        elif type == 'RUE':
            DUSCY = 0
            for i in range(len(DLMerge['id'])):
                if DLMerge['ramSize_x'][i] != 0 and DLMerge['ramSize_y'][i] != 0 :
                    usage = DLMerge['ramSize_y'][i]/DLMerge['ramSize_x'][i]*100
                    if usage > AlarmRamUsage :
                        DUSCY = DUSCY+1
            INM = [alarmCaseThird]
        elif type == 'LPC':
            DUSCY = len(DLMerge['listenPortCount_x'].compare(DLMerge['listenPortCount_y']))
            INM = [alarmCaseFourth]
        elif type == 'EPC':
            DUSCY = len(DLMerge['establishedPortCount_x'].compare(DLMerge['establishedPortCount_y']))
            INM = [alarmCaseFifth]
        if type == 'LH' or type == 'RUE':
            IC = [DUSCY]
        else :
            IC = [DTC-DUSCY]


    RD = {"name": INM, "value": IC}
    return RD


