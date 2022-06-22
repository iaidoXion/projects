import pandas as pd
from datetime import datetime

"""
with open("setting.json", encoding="UTF-8") as f:
    SETTING = json.loads(f.read())

DataLoadingType = SETTING['MODULE']['DataLoadingType']
"""

def OrgDaily(parserData, EAYL, sensorData):
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
    TDL = []
    for AssetData in ADL:
        CID = AssetData['computer_id']
        AI = AssetData['asset_item']
        OI = AssetData['os_platform']
        DTS = AssetData['disk_total_space']
        LSA = AssetData['last_seen_at']
        TDL.append([CID, AI, OI, DTS, LSA])
    TDFCNM = ['id', 'assetItem', 'os', 'driveSize', 'lastLogin']
    TDF = pd.DataFrame(TDL, columns=TDFCNM)
    TDFS = TDF.sort_values(by="id", ascending=False).reset_index(drop=True)

    TSDL = []
    for SD in sensorData :
        CID = SD[0]
        LPC = SD[10]
        EP = SD[11]
        TSDL.append([CID, LPC, EP])
    TSDLDNM = ['id', 'listenPortCount', 'establishedPort']
    TSDF = pd.DataFrame(TSDL, columns=TSDLDNM)
    TSDFS = TSDF.sort_values(by="id", ascending=False).reset_index(drop=True)

    TDFJ = pd.merge(left = TDFS , right = TSDFS, how = "left", on = "id").sort_values(by="id", ascending=True).reset_index(drop=True)
    YDL = []
    for j in range(len(EAYL)) :
        CID = EAYL[j][0]
        DTS = EAYL[j][1]
        LPC = EAYL[j][2]
        EP = EAYL[j][3]
        YDL.append([CID,DTS,LPC,EP])
    YDFCNM = ['id', 'YdriveSize', 'YListenPortCount', 'YEstablishedPort']
    YDF = pd.DataFrame(YDL, columns=YDFCNM).sort_values(by="id", ascending=True).reset_index(drop=True)
    DL = pd.merge(left=TDFJ, right=YDF, how="left", on="id").sort_values(by="id", ascending=True).reset_index(drop=True)
    return DL
