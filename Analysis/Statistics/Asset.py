from datetime import datetime, timedelta
import pandas as pd
import json

weekAgo = (datetime.today() - timedelta(7)).strftime("%Y-%m-%d")
today = datetime.today().strftime("%Y-%m-%d")

with open("setting.json", encoding="UTF-8") as f:
    SETTING = json.loads(f.read())
AlarmRamUsage = SETTING['PROJECT']['Alarm']['RamUsage']
alarmCaseFirst = SETTING['PROJECT']['Alarm']['Case']['First']
alarmCaseSecond = SETTING['PROJECT']['Alarm']['Case']['Second']
alarmCaseThird = SETTING['PROJECT']['Alarm']['Case']['Third']
alarmCaseFourth = SETTING['PROJECT']['Alarm']['Case']['Fourth']
alarmCaseFifth = SETTING['PROJECT']['Alarm']['Case']['Fifth']

def DailyCount(TDL):

    ATNM = "Asset Total Count"
    ATC = len(TDL)

    DF = TDL
    LLNM = "No Login History"
    LLNC = len(DF[(DF['lastLogin'] < weekAgo)])

    AIG = DF.groupby(['assetItem'])
    AIGBR = AIG.size().reset_index(name='counts')
    AINM = AIGBR.assetItem
    AIC = AIGBR.counts

    OSG = DF.groupby(['os'])
    OSGBR = OSG.size().reset_index(name='counts')
    OSGBRS = OSGBR.sort_values(by="counts", ascending=False).head(3)
    OSNM = OSGBRS.os
    OSC = OSGBRS.counts

    DC = 0
    LPC = 0
    EPC = 0
    RUSC = 0


    DSNM = alarmCaseFirst
    LLSNM = alarmCaseSecond
    RUSNM = alarmCaseThird
    LPSNM = alarmCaseFourth
    EPSNM = alarmCaseFifth


    alarmDataList = []
    LHAlarmList = []
    DSAlarmList = []
    LPCAlarmList = []
    EPCAlarmList = []
    RUSCAlarmList = []
    for i in range(len(TDL.id)):
        if TDL.lastLogin[i] < today :
            CID = TDL.id[i]
            IP = TDL.ip_address[i]
            alarmText = LLSNM
            LHAlarmList.append({'id': CID, 'ip': IP, 'alarmText': alarmText})
        if TDL.driveSize[i] != TDL.YdriveSize[i] :
            DC = DC + 1
            CID = TDL.id[i]
            IP = TDL.ip_address[i]
            alarmText = DSNM
            DSAlarmList.append({'id': CID, 'ip': IP, 'alarmText': alarmText})
        if TDL.listenPortCount[i] != TDL.YListenPortCount[i] :
            LPC = LPC+1
            CID = TDL.id[i]
            IP = TDL.ip_address[i]
            alarmText = LPSNM
            LPCAlarmList.append({'id': CID, 'ip': IP, 'alarmText': alarmText})
        if TDL.establishedPort[i] != TDL.YEstablishedPort[i] :
            EPC = EPC+1
            CID = TDL.id[i]
            IP = TDL.ip_address[i]
            alarmText = EPSNM
            EPCAlarmList.append({'id': CID, 'ip': IP, 'alarmText': alarmText})
        if TDL.ram_use_size[i] != TDL.YRamUseSize[i] :
            RUSC = RUSC+1
            CID = TDL.id[i]
            IP = TDL.ip_address[i]
            alarmText = RUSNM
            RUSCAlarmList.append({'id': CID, 'ip': IP, 'alarmText': alarmText})

    DSNC = DC
    LPSC = LPC
    EPSC = EPC
    RUSSC = RUSC
    #print(alarmDataList)

    RD = {
        "AA": {"name": [ATNM], "value": [ATC]},
        "AIS" : {"name": AINM.tolist(), "value": AIC.tolist()},
        "OS" : {"name": OSNM.tolist(), "value": OSC.tolist(),"color":["#e08a0b","#f4c17c", "#df7454"]},
        "LS" : {"name": [LLNM], "value": [LLNC]},
        "DS": {"name": [DSNM], "value": [DSNC]},
        "LP" : {"name":[LPSNM], "value": [LPSC]},
        "EP" : {"name" : [EPSNM], "value": [EPSC]},
        "RUS" : {"name" : [RUSNM], "value" : [RUSSC]},
        "ADL" : {"LHAL" : LHAlarmList, "DSAL" : DSAlarmList, "LPCAL" : LPCAlarmList, "EPCAL" : EPCAlarmList, "RUSCAL" :RUSCAlarmList }
    }
    #print(RD)
    return RD






def Association(TDL) :
    LHAlarmList = []
    DSAlarmList = []
    LPCAlarmList = []
    EPCAlarmList = []
    RUSAlarmList = []
    AGL = []
    for i in range(len(TDL.id)):
        if TDL.lastLogin[i] < today:
            IPS = TDL.ip_address[i].split('.')
            IP =IPS[0]+'.'+IPS[1]+'.'+IPS[2]
            LHAlarmList.append([IP])
            AGL.append([IP])
        if TDL.driveSize[i] != TDL.YdriveSize[i]:
            IPS = TDL.ip_address[i].split('.')
            IP = IPS[0] + '.' + IPS[1] + '.' + IPS[2]
            DSAlarmList.append([IP])
            AGL.append([IP])
        if TDL.listenPortCount[i] != TDL.YListenPortCount[i]:
            IPS = TDL.ip_address[i].split('.')
            IP = IPS[0] + '.' + IPS[1] + '.' + IPS[2]
            LPCAlarmList.append([IP])
            AGL.append([IP])
        if TDL.establishedPort[i] != TDL.YEstablishedPort[i]:
            IPS = TDL.ip_address[i].split('.')
            IP = IPS[0] + '.' + IPS[1] + '.' + IPS[2]
            EPCAlarmList.append([IP])
            AGL.append([IP])
        if TDL.ram_use_size[i] != TDL.YRamUseSize[i]:
            IPS = TDL.ip_address[i].split('.')
            IP = IPS[0] + '.' + IPS[1] + '.' + IPS[2]
            RUSAlarmList.append([IP])
            AGL.append([IP])
    LHDF = pd.DataFrame(LHAlarmList, columns=['group'])
    DSDF = pd.DataFrame(DSAlarmList, columns=['group'])
    LPCDF = pd.DataFrame(LPCAlarmList, columns=['group'])
    EPCDF = pd.DataFrame(EPCAlarmList, columns=['group'])
    RUSDF = pd.DataFrame(RUSAlarmList, columns=['group'])
    AGLDF = pd.DataFrame(AGL,columns=['group'])

    LHG = LHDF.groupby('group').size().reset_index(name='alarmCount')
    DSG = DSDF.groupby('group').size().reset_index(name='alarmCount')
    LPCG = LPCDF.groupby('group').size().reset_index(name='alarmCount')
    EPCG = EPCDF.groupby('group').size().reset_index(name='alarmCount')
    RUSG = RUSDF.groupby('group').size().reset_index(name='alarmCount')
    AGLG = AGLDF.groupby('group').size().reset_index(name='groupCount')

    DSNM = alarmCaseFirst
    LLSNM = alarmCaseSecond
    RUSSNM = alarmCaseThird
    LPSNM = alarmCaseFourth
    EPSNM = alarmCaseFifth

    LHG['name'] = 'LH'
    LHG['alarmCase'] = LLSNM
    DSG['name'] = 'DUS'
    DSG['alarmCase'] = DSNM
    LPCG['name'] = 'LP'
    LPCG['alarmCase'] = LPSNM
    EPCG['name'] = 'EP'
    EPCG['alarmCase'] = EPSNM
    RUSG['name'] = 'RUS'
    RUSG['alarmCase'] = RUSSNM

    maxData = []
    for n in range(len(LHG.group)) :
        groupNameCount = int(LHG.group[n].split('.')[2]) + 1
        maxData.append([LHG.group[n], LHG.alarmCount[n], 'group' + str(groupNameCount) + LHG.name[n], LHG.name[n], LHG.alarmCase[n]])
    for o in range(len(DSG.group)):
        groupNameCount = int(DSG.group[o].split('.')[2]) + 1
        maxData.append([DSG.group[o], DSG.alarmCount[o], 'group' + str(groupNameCount) + DSG.name[o], DSG.name[o], DSG.alarmCase[o]])
    for p in range(len(LPCG.group)) :
        groupNameCount = int(LPCG.group[p].split('.')[2]) + 1
        maxData.append([LPCG.group[p], LPCG.alarmCount[p], 'group' + str(groupNameCount) + LPCG.name[p], LPCG.name[p], LPCG.alarmCase[p]])
    for q in range(len(EPCG.group)) :
        groupNameCount = int(EPCG.group[q].split('.')[2]) + 1
        maxData.append([EPCG.group[q], EPCG.alarmCount[q], 'group' + str(groupNameCount) + EPCG.name[q], EPCG.name[q], EPCG.alarmCase[q]])
    for r in range(len(RUSG.group)) :
        groupNameCount = int(RUSG.group[r].split('.')[2]) + 1
        maxData.append([RUSG.group[r], RUSG.alarmCount[r], 'group' + str(groupNameCount) + RUSG.name[r], RUSG.name[r], RUSG.alarmCase[r]])

    nodeDataList = []
    linksDataList = []
    for h in range(len(AGLG.group)):
        groupNameCount = int(AGLG.group[h].split('.')[2]) + 1
        nodeDataList.append( {'group': AGLG.group[h], 'alarmCount': str(AGLG.groupCount[h]), 'id': 'groupCenter' + str(groupNameCount), 'name': AGLG.group[h], 'alarmCase': AGLG.group[h]})
    maxDataDF = pd.DataFrame(maxData, columns=['group', 'alarmCount', 'id', 'name', 'alarmCase'])
    MDG = maxDataDF.loc[maxDataDF.groupby(['group'])['alarmCount'].idxmax()]
    MDG['point'] = 'true'
    dfmerge = pd.merge(left=maxDataDF, right=MDG, how="left", on=['id','group', 'alarmCount', 'name', 'alarmCase']).sort_values(by="id", ascending=True).reset_index()

    for s in range(len(dfmerge.id)) :
        if type(dfmerge.point[s]) == float :
            point = str(dfmerge.point[s])
            point = 'false'
        else :
            point = dfmerge.point[s]
        groupNameCount = int(dfmerge.group[s].split('.')[2]) + 1
        nodeDataList.append({'group':dfmerge.group[s], 'alarmCount':str(dfmerge.alarmCount[s]), 'id':dfmerge.id[s], 'name':dfmerge.name[s], 'alarmCase':dfmerge.alarmCase[s], 'point':point})
        linksDataList.append({'source': dfmerge.id[s], 'target': 'groupCenter' + str(groupNameCount)})



    RD = {'nodeDataList':nodeDataList, 'linksDataList':linksDataList}

    return RD


def ChartData(data, type, statistics) :
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
            DUSCY = len(DLMerge[(DLMerge['lastLogin_x'] < weekAgo)])
            INM = [alarmCaseSecond]
        elif type == 'RUE':
            DUSCY = 0
            for i in range(len(DLMerge['id'])):
                if DLMerge['ramSize_x'][i] != 0 and DLMerge['ramSize_y'][i] != 0 :
                    usage = DLMerge['ramSize_y'][i]/DLMerge['ramSize_x'][i]*100
                    if usage < AlarmRamUsage :
                        DUSCY = DUSCY+1
            INM = [alarmCaseThird]
        elif type == 'LPC':
            DUSCY = len(DLMerge['listenPortCount_x'].compare(DLMerge['listenPortCount_y']))
            INM = [alarmCaseFourth]
        elif type == 'EPC':
            DUSCY = len(DLMerge['establishedPortCount_x'].compare(DLMerge['establishedPortCount_y']))
            INM = [alarmCaseFifth]

        IC = [DTC-DUSCY]

    RD = {"name": INM, "value": IC}
    return RD


