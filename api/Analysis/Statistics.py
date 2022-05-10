from datetime import datetime, timedelta

def DailyCount(TSDL):

    #{"classification": "login", "item": "N", "count": LHNC}
    ATNM = "all"
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
        "OS" : {"name": OSNM.tolist(), "value": OSC.tolist(),"color":["#df7454","#e08a0b", "#f4c17c"]},
        "LS" : {"name": [LLNM], "value": [LLNC]},
    }
    return RD






