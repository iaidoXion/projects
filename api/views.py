from api.Call.Auth import SessionKey
from api.Call.Extract import Asset as AssetAPI
from api.Call.Sensor import Data as SensorAPI
from DataParsing.Extract.Asset import Yesterday as EAY
from DataParsing.Extract.Statistics import Yesterday as ESY, FiveDay as ESF
from DataParsing.Transform.Asset import OrgDaily as AODT
from DataParsing.Transform.Statistics import Yesterday as SYT, FiveDay as SFDT, Banner as SBT,  ChartData as SDT
from Analysis.Statistics.Asset import DailyCount as ASDC, FiveDay as SFDS, BannerRoc as BR
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def DashboardData() :
    SK = SessionKey()
    baseAssetData = AssetAPI(SK)
    sensorData = SensorAPI(SK)
    EAYL = EAY()
    TDL = AODT(baseAssetData['dataList'], EAYL, sensorData['dataList'])
    ASDCL = ASDC(TDL)
    ESYDL = ESY()
    SYDL = SYT(ESYDL)
    SDL = SBT(ASDCL, SYDL)
    BRDL= BR(SDL)
    ESFDL = ESF()
    SFDTDL = SFDT(ESFDL,ASDCL)
    SFDSDL = SFDS(SFDTDL)
    RD = SDT(ASDCL, BRDL, SFDSDL)

    return RD




