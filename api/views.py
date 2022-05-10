from api.Call.Auth import SessionKey
from api.Call.Extract import Asset as AssetAPI
from api.Parsing.Transform import AssetOrgDaily as TAOD, StatisticsDaily as TSD
from api.Analysis.Statistics import DailyCount as ASDC
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
"""
class mainclass :
    def __init__(self):
        self.sk = SessionKey()

    def Asset(self) :
        baseAssetData = AssetAPI(self.sk)
        AssetData = TAOD(baseAssetData['dataList'])
        ASDCL = ASDC(AssetData)
        TSD(ASDCL)
"""
def DashboardChartData() :
    SK = SessionKey()
    baseAssetData = AssetAPI(SK)
    AssetData = TAOD(baseAssetData['dataList'])
    ASDCL = ASDC(AssetData)
    RD = TSD(ASDCL)
    return RD


