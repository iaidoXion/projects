from api.Call.Auth import SessionKey
from api.Call.Asset import Data as AssetAPI
from api.Call.Sensor import Data as SensorAPI
from DataParsing.Extract.Asset import Yesterday as EAY
from DataParsing.Extract.Zabbix import Yesterday as EZY
from DataParsing.Extract.Statistics import Yesterday as ESY, FiveDay as ESF
from DataParsing.Transform.Asset import OrgDaily as AODT
from DataParsing.Transform.Statistics import Yesterday as SYT, FiveDay as SFDT, Banner as SBT, ChartData as SDT
from Analysis.Statistics.Asset import DailyCount as ASDC, FiveDay as SFDS, BannerRoc as BR, Association
import urllib3
import json
with open("setting.json", encoding="UTF-8") as f:
    SETTING = json.loads(f.read())

core = SETTING['PROJECT']['CORE']
projectType = SETTING['PROJECT']['TYPE']

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def DashboardData() :
    if core == 'Tanium' :
        SK = SessionKey()                                                       # API Sesstion KEY Call
        assetData = AssetAPI(SK)                                                # API Asset(Now) Data Call
        EAYL = EAY()                                                            # DB Asset(yesterday) Data Select
        sensorData = SensorAPI(SK)                                              # API Sensor(Now) Data Call
        if projectType == 'System' :
            TDL = AODT(assetData['dataList'], EAYL, sensorData['dataList'])     # API Asset(Now), DB Asset(yesterday) Data & API Sensor(Now) Data Transform
            ASDCL = ASDC(TDL)                                                       # Count Statistics
            AssociationS = Association(TDL)                                         # Association Statistics
            ESYDL = ESY()                                                           # DB Statistics(yesterday) Data Select
            SYDL = SYT(ESYDL)                                                       # DB Statistics(yesterday) Data Transform
            SDL = SBT(ASDCL, SYDL)                                                  # DB Statistics(yesterday) Data & API Sensor(Now) Data
            BRDL= BR(SDL)
            ESFDL = ESF()
            SFDTDL = SFDT(ESFDL,ASDCL)
            SFDSDL = SFDS(SFDTDL)
            RD = SDT(ASDCL, BRDL, SFDSDL, AssociationS)
        elif projectType == 'Service' :
            print()
    elif core == 'Zabbix' :
        EZYL = EZY()
    return RD




