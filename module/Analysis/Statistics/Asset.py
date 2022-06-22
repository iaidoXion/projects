from datetime import datetime, timedelta

def DailyCount(TDL):

    ATNM = "Asset Total Count"
    ATC = len(TDL)

    weekAgo = (datetime.today() - timedelta(7)).strftime("%Y-%m-%d")

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
    for i in range(len(TDL.id)):
        if TDL.driveSize[i] != TDL.YdriveSize[i] :
            DC = DC + 1
        if TDL.listenPortCount[i] != TDL.YListenPortCount[i] :
            LPC = LPC+1
        if TDL.establishedPort[i] != TDL.YEstablishedPort[i] :
            EPC = EPC+1
    DSNM = "Drive Size No Change"
    DSNC = DC
    LPSNM = "Listen Port Count No Change"
    LPSC = LPC
    EPSNM = "Established Port Count No Change"
    EPSC = EPC


    RD = {
        "AA": {"name": [ATNM], "value": [ATC]},
        "AIS" : {"name": AINM.tolist(), "value": AIC.tolist()},
        "OS" : {"name": OSNM.tolist(), "value": OSC.tolist(),"color":["#e08a0b","#f4c17c", "#df7454"]},
        "LS" : {"name": [LLNM], "value": [LLNC]},
        "DS": {"name": [DSNM], "value": [DSNC]},
        "LP" : {"name":[LPSNM], "value": [LPSC]},
        "EP" : {"name" : [EPSNM], "value": [EPSC]}
    }

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
    AASDL = {"name" : TAA['name'][0], "Count" :  TAA['value'][0], "roc" : AAROC }
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
    EPSDL = {"name": TEP['name'][0], "count": YEP['value'][0], "roc": EPROC}
    bannerDataList.append(EPSDL)

    RD = bannerDataList

    return RD









