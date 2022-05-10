import pandas as pd
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

def StatisticsDaily(ASDCL) :
    AASDL = []
    for AASC in range(len(ASDCL['AA']['name'])):
        AASDL.append(
            {"item": ASDCL['AA']['name'][AASC], "count": ASDCL['AA']['value'][AASC]})
    AISDL = []
    for AISC in range(len(ASDCL['AIS']['name'])):
        AISDL.append(
            {"name": ASDCL['AIS']['name'][AISC], "value": ASDCL['AIS']['value'][AISC]})
    OSDL = []
    for OSC in range(len(ASDCL['OS']['name'])):
        OSDL.append({"name": ASDCL['OS']['name'][OSC], "value": ASDCL['OS']['value'][OSC], "color": ASDCL['OS']['color'][OSC]})
    LSDL = []
    for LSC in range(len(ASDCL['LS']['name'])):
        LSDL.append({"item": ASDCL['LS']['name'][LSC], "count": ASDCL['LS']['value'][LSC]})
    returnData = {"AAS": AASDL, "barChartData": AISDL, "pieChartData": OSDL, "LS": LSDL}

    return returnData

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











