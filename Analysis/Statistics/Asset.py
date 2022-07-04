from datetime import datetime, timedelta

import pandas as pd

weekAgo = (datetime.today() - timedelta(7)).strftime("%Y-%m-%d")
today = datetime.today().strftime("%Y-%m-%d")

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

    LLSNM = "No Login History"
    DSNM = "Drive Size No Change"
    LPSNM = "Listen Port Count No Change"
    EPSNM = "Established Port Count No Change"
    RUSNM = "RAM Size No Change"

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

def FiveDay(SFDTDL):
    DGL = []
    DSL = []
    DNM = []
    SFDTDLG = SFDTDL.groupby('name')
    for SFDTD in SFDTDLG:
        DGL.append(SFDTD[1])
        DNM.append(SFDTD[0])
    dataGroupListLen = len(DGL)
    for i in range(dataGroupListLen) :
        DSL.append(DGL[i].sort_values(by="date", ascending=True))
    RD = [DNM,DSL]
    return RD

def BannerRoc(SDL) :
    bannerDataList = []
    TAA = SDL['TAA']
    YAA = SDL['YAA']
    AAROC = TAA['value'][0] - YAA['value'][0]
    AASDL = {"name" : TAA['name'][0], "count" :  TAA['value'][0], "roc" : AAROC }
    bannerDataList.append(AASDL)

    TLS = SDL['TLS']
    YLS = SDL['YLS']
    LSROC = TLS['value'][0] - YLS['value'][0]
    LSSDL = {"name" : TLS['name'][0], "count" :  TLS['value'][0], "roc" : LSROC }
    bannerDataList.append(LSSDL)

    TAIS = SDL['TAIS']
    TAISSorting = TAIS.sort_values(by="name", ascending=True)
    TAISNM = TAISSorting.name
    TAISV = TAISSorting.value
    YAIS = SDL['YAIS']
    YAISSorting = YAIS.sort_values(by="name", ascending=True)
    YAISNM = YAISSorting.name
    YAISV = YAISSorting.value

    for i in range(len(TAISNM)) :
        if TAISNM[i] == YAISNM[i] :
            bannerDataList.append({"name" : TAISNM[i]+" Count", "count" :  TAISV[i], "roc" : TAISV[i]-YAISV[i]})
        else :
            bannerDataList.append({"name": TAISNM[i] + " Count", "count": TAISV[i], "roc": 0})

    TOS = SDL['TOS']
    TOSSorting = TOS.sort_values(by="name", ascending=True)
    TOSNM = TOSSorting.name
    TOSV = TOSSorting.value
    YOS = SDL['YOS']
    YOSSorting = YOS.sort_values(by="name", ascending=True)
    YOSNM = YOSSorting.name
    YOSV = YOSSorting.value
    for j in range(len(TOSNM)) :
        if TOSNM[i] == YOSNM[i] :
            bannerDataList.append({"name" : TOSNM[j]+" Count", "count" :  TOSV[j], "roc" : TOSV[j]-YOSV[j]})
        else :
            bannerDataList.append({"name" : TOSNM[j]+" Count", "count" :  TOSV[j], "roc" : 0})

    TDS = SDL['TDS']
    YDS = SDL['YDS']
    DSROC = TDS['value'][0] - YDS['value'][0]
    DSSDL = {"name": TDS['name'][0], "count": TDS['value'][0], "roc": DSROC}
    bannerDataList.append(DSSDL)

    TLP = SDL['TLP']
    YLP = SDL['YLP']
    LPROC = TLP['value'][0] - YLP['value'][0]
    LPSDL = {"name": TLP['name'][0], "count": TLP['value'][0], "roc": LPROC}
    bannerDataList.append(LPSDL)

    TEP = SDL['TEP']
    YEP = SDL['YEP']
    EPROC = TEP['value'][0] - YEP['value'][0]
    EPSDL = {"name": TEP['name'][0], "count": TEP['value'][0], "roc": EPROC}
    bannerDataList.append(EPSDL)

    TRUS = SDL['TRUS']
    YRUS = SDL['YRUS']
    RUSROC = TRUS['value'][0] - YRUS['value'][0]
    RUSDL = {"name": TRUS['name'][0], "count": TRUS['value'][0], "roc": RUSROC}
    bannerDataList.append(RUSDL)

    RD = bannerDataList
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

    LLSNM = "No Login History"
    DSNM = "Drive Size No Change"
    LPSNM = "Listen Port Count No Change"
    EPSNM = "Established Port Count No Change"
    RUSSNM = "RAM Size No Change"
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
            dfmerge.point[s] = 'false'
        groupNameCount = int(dfmerge.group[s].split('.')[2]) + 1
        nodeDataList.append({'group':dfmerge.group[s], 'alarmCount':str(dfmerge.alarmCount[s]), 'id':dfmerge.id[s], 'name':dfmerge.name[s], 'alarmCase':dfmerge.alarmCase[s], 'point':dfmerge.point[s]})
        linksDataList.append({'source': dfmerge.id[s], 'target': 'groupCenter' + str(groupNameCount)})



    RD = {'nodeDataList':nodeDataList, 'linksDataList':linksDataList}

    return RD





