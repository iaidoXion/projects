from datetime import datetime, timedelta

import pandas as pd

weekAgo = (datetime.today() - timedelta(7)).strftime("%Y-%m-%d")
today = datetime.today().strftime("%Y-%m-%d")



def BannerRoc(SDL) :
    #print(SDL)
    bannerDataList = []
    """
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
    bannerDataList.append(RUSDL)"""

    RD = bannerDataList
    #print(RD)
    return RD


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