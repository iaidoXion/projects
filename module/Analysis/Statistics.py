from datetime import datetime, timedelta

def DailyCount(TSDL):
    ATNM = "Asset Total Count"
    ATC = len(TSDL)
    today = datetime.today().strftime("%Y-%m-%d")
    weekAgo = (datetime.today() - timedelta(7)).strftime("%Y-%m-%d")
    DF = TSDL
    LLNM = "N"
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


    RD = {
        "AA": {"name": [ATNM], "value": [ATC]},
        "AIS" : {"name": AINM.tolist(), "value": AIC.tolist()},
        "OS" : {"name": OSNM.tolist(), "value": OSC.tolist(),"color":["#e08a0b","#f4c17c", "#df7454"]},
        "LS" : {"name": [LLNM], "value": [LLNC]},
    }
    return RD

def StatisticsFiveDay(SFDTDL):
    for date, value in SFDTDL.groupby('name'):
        print(date)
        print(value)

def bannerRoc(SDL) :
    bannerDataList = []
    TAA = SDL['TAA']
    YAA = SDL['YAA']
    AAROC = TAA['value'][0] - YAA['value'][0]
    AASDL = {"name" : TAA['name'][0], "count" :  TAA['value'][0], "roc" : AAROC }
    bannerDataList.append(AASDL)

    TLS = SDL['TLS']
    YLS = SDL['YLS']
    LSROC = TLS['value'][0] - YLS['value'][0]
    LSSDL = {"name" : "No Login History Count", "count" :  TLS['value'][0], "roc" : LSROC }
    bannerDataList.append(LSSDL)

    TAIS = SDL['TAIS']
    TAISSorting = TAIS.sort_values(by="name", ascending=True)
    TAISNM = TAISSorting.name
    TAISV = TAISSorting.value
    YAIS = SDL['YAIS']
    YAISSorting = YAIS.sort_values(by="name", ascending=True)
    YAISNM = YAISSorting.name
    YAISV = YAISSorting.value

    #if len(TAISNM) == len(YAISNM) :
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
    returnData = bannerDataList
    return returnData









