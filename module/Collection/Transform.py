import pandas as pd
from datetime import datetime
import json
"""
with open("setting.json", encoding="UTF-8") as f:
    SETTING = json.loads(f.read())

DataLoadingType = SETTING['MODULE']['DataLoadingType']
"""

def AssetOrgDaily(parserData):
    PDLC = len(parserData)
    DFL = []
    ADL = []
    for i in range(PDLC):
        CI = parserData[i]['computer_id']
        AI = parserData[i]['asset_item']
        OI = parserData[i]['os_platform']
        DI = parserData[i]['disk_total_space']
        LI = parserData[i]['last_seen_at'].split('T')[0]
        AIPer = AI.lower()
        if AIPer.startswith('macbook'):
            AI = 'Notebook'
        if AIPer.startswith('imac'):
            AI = 'Desktop'
        DFL.append([CI, AI, OI, DI, LI])

        ADL.append({'computer_id': CI, 'asset_item': AI, 'os_platform': OI, 'disk_total_space': DI, 'last_seen_at': LI})
    DL = []
    for AssetData in ADL:
        CID = AssetData['computer_id']
        AI = AssetData['asset_item']
        OI = AssetData['os_platform']
        DTS = AssetData['disk_total_space']
        LSA = AssetData['last_seen_at']
        DL.append([CID, AI, OI, DTS, LSA])
    DFCNM = ['id', 'assetItem', 'os', 'driveSize', 'lastLogin']
    DF = pd.DataFrame(DL, columns=DFCNM)
    return DF

def StatisticsYesterday(ESYDL) :
    yesterdayDataList = []
    ATNM = []
    ATC = []
    AINM = []
    AIC = []
    OSNM = []
    OSC = []
    LLNM = []
    LLNC = []

    for i in range(len(ESYDL)):
        if ESYDL[i][0] == 'asset' :
            if ESYDL[i][1] == 'all' :
                ATNM.append("Asset Total Count")
                ATC.append(int(ESYDL[i][2]))
            else :
                AINM.append(ESYDL[i][1])
                AIC.append(int(ESYDL[i][2]))
        elif ESYDL[i][0] == 'os' :
            OSNM.append(ESYDL[i][1])
            OSC.append(int(ESYDL[i][2]))
        elif ESYDL[i][0] == 'login' :
            LLNM.append(ESYDL[i][1])
            LLNC.append(int(ESYDL[i][2]))
            #yesterdayDataList.append({"name": SYDL[i][1], "count" : SYDL[i][2]})
    RD = {
        "AA": {"name": ATNM, "value": ATC},
        "AIS": {"name": AINM, "value": AIC},
        "OS": {"name": OSNM, "value": OSC},
        "LS": {"name": LLNM, "value": LLNC},
    }

    return RD

def StatisticsFiveDay(ESFDL, ASDCL) :
    today = datetime.today().strftime("%Y-%m-%d")
    ADL =[]
    for i in range(len(ESFDL)):
        if not ESFDL[i][1] == 'all':
            name = ESFDL[i][1]
            price = int(ESFDL[i][2])
            date = ESFDL[i][3].strftime("%Y-%m-%d")
            ADL.append([name, price, date])

    for j in range(len(ASDCL['AIS']['name'])) :
        name = ASDCL['AIS']['name'][j]
        price = int(ASDCL['AIS']['value'][j])
        date = today
        ADL.append([name, price, date])
    #print(ADL)
    ACNM = ['name', 'value', 'date']
    ADF = pd.DataFrame(ADL, columns=ACNM)
    #ADFL = ADF.groupby('name')['date']['value'].apply(list)
    #print(ADFL)

    return ADF


def StatisticsBanner(ASDCL,SYDL) :
    TAA = ASDCL['AA']
    YAA = SYDL['AA']
    TLS = ASDCL['LS']
    YLS = SYDL['LS']
    TAIS = ASDCL['AIS']
    YAIS = SYDL['AIS']
    TOS = ASDCL['OS']
    YOS = SYDL['OS']
    TAIDL = []
    for i in range(len(TAIS['name'])) :
        TAIDL.append([TAIS['name'][i],TAIS['value'][i]])
    TAIDFCNM = ['name', 'value']
    TAIDF = pd.DataFrame(TAIDL, columns=TAIDFCNM)
    #print(TAIDL)
    YAIDL = []
    for j in range(len(YAIS['name'])):
        YAIDL.append([YAIS['name'][j], YAIS['value'][j]])
    YAIDFCNM = ['name', 'value']
    YAIDF = pd.DataFrame(YAIDL, columns=YAIDFCNM)

    TOSDL = []
    for k in range(len(TOS['name'])):
        TOSDL.append([TOS['name'][k], TOS['value'][k]])
    TOSDFCNM = ['name', 'value']
    TOSDF = pd.DataFrame(TOSDL, columns=TOSDFCNM)

    YOSDL = []
    for l in range(len(YOS['name'])):
        YOSDL.append([YOS['name'][l], YOS['value'][l]])
    YOSDFCNM = ['name', 'value']
    YOSDF = pd.DataFrame(YOSDL, columns=YOSDFCNM)
    RD = {"TAA" : TAA, "YAA" : YAA, "TLS" : TLS, "YLS" : YLS, "TAIS" : TAIDF, "YAIS" : YAIDF, "TOS" : TOSDF, "YOS": YOSDF}

    return RD

def StatisticsData(ASDCL, BRDL, SFDSDL):

    BarChartDataList = []
    LineChartDataList = []
    PieChartDataList = []
    LineChartKeyList = []
    for AISC in range(len(ASDCL['AIS']['name'])):
        BarChartDataList.append({"name": ASDCL['AIS']['name'][AISC], "value": ASDCL['AIS']['value'][AISC]})
    for OSC in range(len(ASDCL['OS']['name'])):
        PieChartDataList.append({"name": ASDCL['OS']['name'][OSC], "value": ASDCL['OS']['value'][OSC], "color": ASDCL['OS']['color'][OSC]})
    LineChartData = {}
    for SFDSC in range(len(SFDSDL[1])) :
        #LineChartKeyList.append(SFDSDL[0][SFDSC])
        LineChartData[SFDSDL[0][SFDSC].replace(" " , "")] = []
        for i in SFDSDL[1][SFDSC].index :
           LineChartData[SFDSDL[0][SFDSC].replace(" " , "")].append({"name":SFDSDL[1][SFDSC].name[i], "date":SFDSDL[1][SFDSC].date[i], "value": SFDSDL[1][SFDSC].value[i]})
    LineChartDataList.append(LineChartData)

    returnData = {"barChartData": BarChartDataList, "lineChartData" : LineChartDataList,  "pieChartData": PieChartDataList,"bannerData" : BRDL}
    return returnData


    """
    BannerDataList = []
    BarChartDataList = []
    PieChartDataList = []
    for AASC in range(len(ASDCL['AA']['name'])):
        todayAssetTotalCount = ASDCL['AA']['value'][AASC]
        yesterdayAssetTotalCount = TSYL['AA']['value'][AASC]
        ATROC = todayAssetTotalCount-yesterdayAssetTotalCount
        BannerDataList.append({"name": ASDCL['AA']['name'][AASC], "count": ASDCL['AA']['value'][AASC], "roc" : ATROC})
    for AISC in range(len(ASDCL['AIS']['name'])):
        BarChartDataList.append({"name": ASDCL['AIS']['name'][AISC], "value": ASDCL['AIS']['value'][AISC]})
        if ASDCL['AIS']['name'][AISC] == TSYL['AIS']['name'][AISC] :
            todayAssetItemCount = ASDCL['AIS']['value'][AISC]
            yesterdayAssetItemCount = ASDCL['AIS']['value'][AISC]
            AIROC = todayAssetItemCount-yesterdayAssetItemCount
            BannerDataList.append({"name": ASDCL['AIS']['name'][AISC]+" Count", "count": ASDCL['AIS']['value'][AISC], "roc" : AIROC})
    for OSC in range(len(ASDCL['OS']['name'])):
        PieChartDataList.append({"name": ASDCL['OS']['name'][OSC], "value": ASDCL['OS']['value'][OSC], "color": ASDCL['OS']['color'][OSC]})
    """
    """
    DL = []
    for OSAC in range(len(ASDCL['OSA']['name'])):
        ASDCL['OSA']['name'][OSAC]
    # DFCNM = ['id', 'assetItem', 'os', 'driveSize', 'lastLogin']
    # print(DL)
    # DF = pd.DataFrame(DL, columns=DFCNM)
    
    for OSAC in range(len(ASDCL['OSA']['name'])) :
        if ASDCL['OSA']['name'][OSAC] == TSYL['OS']['name'][OSAC] :
            todayOSCount = ASDCL['OSA']['value'][OSAC]
            yesterdayOSCount = TSYL['OS']['value'][OSAC]
            OSROC = todayOSCount - yesterdayOSCount
            print(ASDCL['OSA']['name'][OSAC],ASDCL['OSA']['value'][OSAC], TSYL['OS']['name'][OSAC], TSYL['OS']['value'][OSAC] )
            BannerDataList.append({"name": ASDCL['OSA']['name'][OSAC]+" OS Count", "count": ASDCL['OSA']['value'][OSAC], "roc" : OSROC })
    """
    """
    for LSC in range(len(ASDCL['LS']['name'])):
        todayLoginCount = ASDCL['LS']['value'][LSC]
        yesterdayLoginCount = TSYL['LS']['value'][LSC]
        LROC = todayLoginCount - yesterdayLoginCount
        BannerDataList.append({"name": ASDCL['LS']['name'][LSC], "count": ASDCL['LS']['value'][LSC], "roc" : LROC})

    returnData = {"barChartData" : BarChartDataList, "pieChartData" : PieChartDataList, "bannerDataList" : BannerDataList}
    #print(returnData)
    return returnData
    """


"""
def StatisticsDaily(ASDCL) :

    if DataLoadingType == 'DB':
        AACL = []
        for AASC in range(len(ASDCL['AA']['name'])):
            AACL.append("asset")
        AICL = []
        for AISC in range(len(ASDCL['AIS']['name'])):
            AICL.append("asset")
        OCL = []
        for OSC in range(len(ASDCL['OS']['name'])):
            OCL.append("os")
        LCL = []
        for LSC in range(len(ASDCL['LS']['name'])):
            LCL.append("login")
        DC = AACL+AICL+OCL+LCL
        DNM = ASDCL['AA']['name']+ASDCL['AIS']['name']+ASDCL['OS']['name']+ASDCL['LS']['name']
        DV = ASDCL['AA']['value']+ASDCL['AIS']['value']+ASDCL['OS']['value']+ASDCL['LS']['value']
        returnData = {"classification" : DC, "item" : DNM, "count" : DV}

    elif DataLoadingType == 'FILE':
        AASDL = []
        for AASC in range(len(ASDCL['AA']['name'])) :
            AASDL.append({"classification": "asset", "item": ASDCL['AA']['name'][AASC], "count": ASDCL['AA']['value'][AASC]})
        AISDL = []
        for AISC in range(len(ASDCL['AIS']['name'])) :
            AISDL.append({"classification": "asset", "item": ASDCL['AIS']['name'][AISC], "count": ASDCL['AIS']['value'][AISC]})
        OSDL = []
        for OSC in range(len(ASDCL['OS']['name'])) :
            OSDL.append({"classification": "os", "item": ASDCL['OS']['name'][OSC], "count": ASDCL['OS']['value'][OSC]})
        LSDL =[]
        for LSC in range(len(ASDCL['LS']['name'])):
            LSDL.append({"classification": "login", "item": ASDCL['LS']['name'][LSC], "count": ASDCL['LS']['value'][LSC]})
        returnData = {"AAS" : AASDL, "AIS" : AISDL, "OS" : OSDL, "LS" : LSDL}

    return returnData

"""











