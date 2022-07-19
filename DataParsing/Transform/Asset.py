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
        DI = parserData[i]['drive_use_size']
        LI = parserData[i]['last_seen_at'].split('T')[0]
        IP = parserData[i]['ip_address']
        AIPer = AI.lower()
        if AIPer.startswith('macbook'):
            AI = 'Notebook'
        if AIPer.startswith('imac'):
            AI = 'Desktop'
        DFL.append([CI, AI, OI, DI, LI, IP])
        ADL.append({'computer_id': CI, 'asset_item': AI, 'os_platform': OI, 'drive_use_size': DI, 'last_seen_at': LI, 'ip_address':IP})
    TDL = []
    for AssetData in ADL:
        CID = AssetData['computer_id']
        AI = AssetData['asset_item']
        OI = AssetData['os_platform']
        DTS = AssetData['drive_use_size']
        LSA = AssetData['last_seen_at']
        IP = AssetData['ip_address']
        TDL.append([CID, AI, OI, DTS, LSA, IP])
    TDFCNM = ['id', 'assetItem', 'os', 'driveSize', 'lastLogin', 'ip_address']
    TDF = pd.DataFrame(TDL, columns=TDFCNM)
    TDFS = TDF.sort_values(by="id", ascending=False).reset_index(drop=True)

    TSDL = []
    for SD in sensorData :
        CID = SD[0]
        LPC = SD[10]
        EP = SD[11]
        RUS = SD[12].split(' ')[0]
        TSDL.append([CID, LPC, EP, RUS])
    TSDLDNM = ['id', 'listenPortCount', 'establishedPort', 'ram_use_size']
    TSDF = pd.DataFrame(TSDL, columns=TSDLDNM)
    TSDFS = TSDF.sort_values(by="id", ascending=False).reset_index(drop=True)

    TDFJ = pd.merge(left = TDFS , right = TSDFS, how = "left", on = "id").sort_values(by="id", ascending=True).reset_index(drop=True)
    YDL = []
    for j in range(len(EAYL)) :
        CID = EAYL[j][0]
        DTS = EAYL[j][1]
        LPC = EAYL[j][2]
        EP = EAYL[j][3]
        RUS = EAYL[j][4]

        YDL.append([CID,DTS,LPC,EP, RUS])
    YDFCNM = ['id', 'YdriveSize', 'YListenPortCount', 'YEstablishedPort', 'YRamUseSize']
    YDF = pd.DataFrame(YDL, columns=YDFCNM).sort_values(by="id", ascending=True).reset_index(drop=True)
    DL = pd.merge(left=TDFJ, right=YDF, how="left", on="id").sort_values(by="id", ascending=True).reset_index(drop=True)
    return DL


def DataFrame(data, day, type, api):
    PDLC = len(data)
    DFL = []
    for i in range(PDLC):
        if day == 'today' :
            if api == 'asset' :
                CI = data[i]['computer_id']
                IP = data[i]['ip_address']
                if type == 'assetItem' :
                    item = data[i]['asset_item']
                    itemPer = item.lower()
                    if itemPer.startswith('macbook'):
                        item = 'Notebook'
                    if itemPer.startswith('imac'):
                        item = 'Desktop'
                    itemIndex = 'assetItem'
                elif type == 'osItem' :
                    item = data[i]['os_platform']
                    itemIndex = 'os'
                elif type == 'driveUseSize' :
                    item = data[i]['drive_use_size']
                    itemIndex = 'driveSize'
                elif type == 'noLoginHistory':
                    item = data[i]['last_seen_at'].split('T')[0]
                    itemIndex = 'lastLogin'
                #elif type == 'ramUseSize' :
                    #print(data[i]['ram'])
                    #    item = data[i]['ram']
                    #print(item)
                    #print(int(item))
                    #if item.isdigit():
                    # item = int(item)
                        #   print(item)
                    #itemIndex = 'ramSize'
            elif api == 'sensor' :
                CI = data[i][0]
                IP = data[i][9]
                if type == 'ramUseSizeT' :
                    item = data[i][13].split(' ')[0]
                    if item.isdigit() :
                        item = int(item)
                    else :
                        item = 0
                        #print(item)
                    itemIndex = 'ramSize'
                elif type == 'ramUseSizeU' :
                    item = data[i][12].split(' ')[0]
                    if item.isdigit():
                        item = int(item)
                    else:
                        item = 0
                        #print(item)
                    itemIndex = 'ramSize'
                elif type == 'listenPortCount' :
                    item = data[i][10]
                    itemIndex = 'listenPortCount'
                elif type == 'establishedPortCount' :
                    item = data[i][11]
                    itemIndex = 'establishedPortCount'
        elif day == 'yesterday' :
            CI = data[i][0]
            IP = ''
            if type == 'driveUseSize' :
                item = data[i][1]
                itemIndex = 'driveSize'
            elif type == 'noLoginHistory':
                item = str(data[i][5]).split(' ')[0]
                itemIndex = 'lastLogin'
            #elif type == 'ramUseSize':
                #    item = str(data[i][4])
                #itemIndex = 'ramSize'
            elif type == 'listenPortCount':
                item = str(data[i][2])
                itemIndex = 'listenPortCount'
            elif type == 'establishedPortCount':
                item = str(data[i][3])
                itemIndex = 'establishedPortCount'

        DFL.append([CI, item, IP])
    DFC = ['id', itemIndex, 'ip']
    DF = pd.DataFrame(DFL, columns=DFC).sort_values(by="id", ascending=False).reset_index(drop=True)
    #print(DF)
    return DF










