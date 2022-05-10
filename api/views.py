from api.Call.Auth import SessionKey
from api.Call.Extract import Asset as AssetAPI
from module.Collection.Transform import AssetOrgDaily as TAOD, StatisticsToday as STD, StatisticsYesterday as SYD, StatisticsDaily as SD
from module.Analysis.Statistics import DailyCount as ASDC, bannerRoc as BR
from module.Collection.Extract import StatisticsYesterday as ESY

import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def DashboardData() :
    SK = SessionKey()
    baseAssetData = AssetAPI(SK)
    AssetData = TAOD(baseAssetData['dataList'])
    ASDCL = ASDC(AssetData)
    RD = STD(ASDCL)

    ESYDL = ESY()
    SYDL = SYD(ESYDL)
    SDL = SD(ASDCL, SYDL)
    BR(SDL)
    #TSYL = TSY(SYDL)

    #RD = TSD(ASDCL, TSYL)
    return RD




