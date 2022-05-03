import pandas as pd
from datetime import datetime

def AssetInfoDay(parserData) :
    PDLC = len(parserData)
    DFL = []
    SDFL = []
    assetDataList = []
    for i in range(PDLC):
        ################## Asset, OS, login ##################
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
        today= datetime.today().strftime("%Y-%m-%d %H:%M:%S")
        assetDataList.append({'today':today, 'computer_id':CI, 'asset_item' : AI, 'os_platform' : OI, 'disk_total_space' : DI, 'last_seen_at' : LI})
    return assetDataList
    """
        ################## Application ##################
        CIA = parserData[i]['ci_installed_application']
        if CIA is not None:
            for j in range(len(CIA)):
                SID=CIA[j]['id']
                SI=CIA[j]['normalized_name']
                SDFL.append([CI, SID, SI])

    
    AOCNM = ["id", "asset", "os", "drive", "login"]
    DF = pd.DataFrame(DFL, columns=AOCNM)
    dayAssetList = []
    for DAC in range(len(DF.id)) :
        dayAssetData ={'computer_id' : DF.id[DAC]}
        dayAssetList.append(dayAssetData)
    print(dayAssetList)
    
    ################## Asset, OS, login group by count ##################
    ################## asset ##################
    AG = DF.groupby(["asset"])
    AGB = AG.size().reset_index(name='counts')
    ADL = AGB.asset
    ACDL = AGB.counts
    ################## os ##################
    OG = DF.groupby(["os"])
    OGB = OG.size().reset_index(name='counts')
    ODL = OGB.os
    OCDL = OGB.counts
    ################## login ##################
    LG = DF.groupby(["login"])
    LGB = LG.size().reset_index(name='counts')
    LDL = LGB.login
    LCDL = LGB.counts
    ################## sw group by count  ##################
    SCNM = ["aid", "sid", "sw"]
    SDF = pd.DataFrame(SDFL, columns=SCNM)
    SG = SDF.groupby(["sw"])
    SGB = SG.size().reset_index(name='counts')
    #SGBT = SGB.sort_values(by="counts", ascending=False).head(5)
    #print(SGBT.sw)
    #print(SGBT.counts)
    SDL = SGB.sw
    SCDL = SGB.counts
    date = datetime.today().strftime("%Y-%m-%d %H:%M:%S")
    comparisonDate = datetime.today().strftime("%Y-%m-%d")

    AT =[]
    AT.append({'date' : date, 'classification' : 'asset', 'item' : 'all', 'Count' : PDLC})
    AS = []
    for AC in range(len(ADL)) :
        AS.append({'date' : date, 'classification' : 'asset', 'item' : ADL[AC], 'Count' : ACDL[AC]})
    OS = []
    for OC in range(len(ODL)):
        OS.append({'date' : date, 'classification' : 'os', 'item': ODL[OC], 'Count' : OCDL[OC]})
    LS = []
    for LC in range(len(LDL)):
        if LDL[LC] == comparisonDate :
            count = LCDL[LC]
            action = 'Y'
            LS.append({'date': date, 'classification': 'login', 'item': action, 'Count': count})
    ST = []
    STC = len(SDFL)
    ST.append({'date': date, 'classification': 'asset', 'item': 'all', 'Count': STC})
    SS = []
    for SC in range(len(SDL)):
        SS.append({'date' : date, 'classification' : 'sw', 'item': SDL[SC], 'Count' : SCDL[SC]})
        #print(SCDL[SC])

    #returnList = {'asset':{'all' : AT, 'Statistics' : AS}, 'osStatistics' : OS, 'sw':{'all' : ST,'Statistics' : SS}, 'loginStatistics' : LS}
    returnList = {'asset':{'all' : AT, 'Statistics' : AS}, 'osStatistics' : OS, 'loginStatistics' : LS, 'assetDataList' : assetDataList}
    #print(returnList)
    return returnList
    """