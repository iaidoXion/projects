from api.Call.Auth import SessionKey
from api.Call.Extract import Asset as AssetAPI
from module.Collection.Transform import AssetOrgDaily as AODT, StatisticsYesterday as SYT, StatisticsFiveDay as SFDT, StatisticsBanner as SBT,  StatisticsData as SDT
from module.Analysis.Statistics import DailyCount as ASDC, StatisticsFiveDay as SFDS, bannerRoc as BR
from module.Collection.Extract import StatisticsYesterday as ESY, StatisticsFiveDay as ESF

import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def DashboardData() :
    SK = SessionKey()
    baseAssetData = AssetAPI(SK)
    AssetData = AODT(baseAssetData['dataList'])
    ASDCL = ASDC(AssetData)
    ESYDL = ESY()
    SYDL = SYT(ESYDL)
    SDL = SBT(ASDCL, SYDL)
    BRDL= BR(SDL)
    ESFDL = ESF()
    SFDTDL = SFDT(ESFDL,ASDCL)
    SFDSDL = SFDS(SFDTDL)
    RD = SDT(ASDCL, BRDL, SFDSDL)

    return RD




