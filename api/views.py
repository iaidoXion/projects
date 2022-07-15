from api.Call.Auth import SessionKey
from api.Call.Asset import Data as AssetAPI
from api.Call.Sensor import Data as SensorAPI
from DataParsing.Extract.Asset import Yesterday as EAY
from DataParsing.Extract.Zabbix import Yesterday as EZY
from DataParsing.Extract.Statistics import Yesterday as ESY, FiveDay as ESF
from DataParsing.Transform.Asset import OrgDaily as AODT, DataFrame as TACD
from DataParsing.Transform.Statistics import Yesterday as SYT, FiveDay as SFDT, Banner as SBT, ChartData as SDT, DataFrame as TSDF, List as TLD, ChartDataNew as TSCD
from Analysis.Statistics.Asset import DailyCount as ASDC, FiveDay as SFDS, BannerRoc as BR, Association, ChartData as SACD
from Analysis.Statistics.Statistics import Calculation as ASSC
import urllib3
import json
import pandas as pd
with open("setting.json", encoding="UTF-8") as f:
    SETTING = json.loads(f.read())

core = SETTING['PROJECT']['CORE']
projectType = SETTING['PROJECT']['TYPE']

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def DashboardData() :
    if core == 'Tanium' :
        SK = SessionKey()                                                           # API Sesstion KEY Call
        assetData = AssetAPI(SK)                                                    # API Asset(Now) Data Call
        EAYL = EAY()                                                                # DB Asset(yesterday) Data Select
        sensorData = SensorAPI(SK)                                                  # API Sensor(Now) Data Call
        if projectType == 'System' :
            TDL = AODT(assetData['dataList'], EAYL, sensorData['dataList'])         # API Asset(Now), DB Asset(yesterday) Data & API Sensor(Now) Data Transform
            print(TDL)
            ASDCL = ASDC(TDL)                                                       # Count Statistics
            AssociationS = Association(TDL)                                         # Association Statistics

            RD = SDT(ASDCL, AssociationS)
    return RD

def DashboardDataNew() :
    if core == 'Tanium' :
        SK = SessionKey()                                                       # API Sesstion KEY Call
        assetData = AssetAPI(SK)                                                # API Asset(Now) Data Call
        EAYL = EAY()                                                            # DB Asset(yesterday) Data Select
        sensorData = SensorAPI(SK)                                              # API Sensor(Now) Data Call
        if projectType == 'System' :
            # Asset Item Statistics
            TAIDL = TACD(assetData['dataList'], "today", "assetItem", 'asset')
            SAIDL = SACD(TAIDL, "assetItem", "group")

            # OS Item Statistics
            TOIDL = TACD(assetData['dataList'], "today", "osItem", 'asset')
            SOIDL = SACD(TOIDL, "osItem", "group")

            # Drive Use Size Statistics
            ## Today compare Count (now Asset API Data & yesterday Asset Table Data)
            TDUSDLT = TACD(assetData['dataList'], "today", "driveUseSize", 'asset')
            TDUSDLY = TACD(EAYL, "yesterday", "driveUseSize", '')
            DUSCTDL = [TDUSDLT, TDUSDLY]
            SDUSDLT = SACD(DUSCTDL, "driveUseSize", "count")

            # No Login History Statistics
            ## Today compare Count (now Asset API Data & yesterday Asset Table Data)
            TNLHDLT = TACD(assetData['dataList'], "today", "noLoginHistory", 'asset')
            TNLHDLY = TACD(EAYL, "yesterday", "noLoginHistory", '')
            NLHCTDL = [TNLHDLT, TNLHDLY]
            SNLHDLT = SACD(NLHCTDL, "noLoginHistory", "count")

            # RAM USE Size Statistics
            ## Today compare Count (now sensor API Data & yesterday Asset Table Data)
            TRUSDLT = TACD(sensorData['dataList'], "today", "ramUseSize", 'sensor')
            TRUSDLY = TACD(EAYL, "yesterday", "ramUseSize", '')
            RUSCTDL = [TRUSDLT, TRUSDLY]
            SRUSDLT = SACD(RUSCTDL, "ramUseSize", "count")

            # Listen Port Count Statistics
            ## Today compare Count (now sensor API Data & yesterday Asset Table Data)
            TLPCDLT = TACD(sensorData['dataList'], "today", "listenPortCount", 'sensor')
            TLPCDLY = TACD(EAYL, "yesterday", "listenPortCount", '')
            LPCCTDL = [TLPCDLT, TLPCDLY]
            LPCDLT = SACD(LPCCTDL, "listenPortCount", "count")

            # Established Port Count Statistics
            ## Today compare Count (now sensor API Data & yesterday Asset Table Data)
            TEPCDLT = TACD(sensorData['dataList'], "today", "establishedPortCount", 'sensor')
            TEPCDLY = TACD(EAYL, "yesterday", "establishedPortCount", '')
            EPCCTDL = [TEPCDLT, TEPCDLY]
            EPCDLT = SACD(EPCCTDL, "establishedPortCount", "count")



            # Banner ROC Calculation (yesterday Statistics Table Data & API Data Statistics)
            ## Yesterday Statistics Table Data Extract & Transform
            ESDLY = ESY()                                                                               # yesterday Statistics Table Data Extract
            TSDLY = TSDF(ESDLY, 'past', 'Banner')                                                            # yesterday Statistics Data Transform
            ## Today Statistics Data Transform
            ## Today Asset Total Count Calculation
            ATCDL = {'name': ['Asset Total'], 'value': [sum(SAIDL['value'])]}
            TSDL = ATCDL, SAIDL, SOIDL, SDUSDLT, SNLHDLT, SRUSDLT, LPCDLT, EPCDLT                        # today Statistics Data List
            TSDLT = TSDF(TSDL, 'today', 'Banner')
            ## Banner ROC Calculation
            SBNDL = ASSC(TSDLY, TSDLT)

            # 5Days Asset Item Statistics Data Combination
            ## Past Data Extract(Statistics Table Data 5Days ago)
            ESDLF = ESF('asset')
            ## Past & Today Data Combination Transform
            AIFD = [ESDLF, SAIDL]
            ESAIDL = TLD(AIFD)


            # alarm

            ADL = [DUSCTDL, NLHCTDL, RUSCTDL, LPCCTDL, EPCCTDL]
            ## Drive Use Size
            #print(ADL)
            ## No Login History
            #print(NLHCTDL)
            ## RAM USE Size
            #print(RUSCTDL)
            ## Listen Port Count
            #print(LPCCTDL)
            ## Established Port
            #print(EPCCTDL)







            # BAR Chart
            BDL = TSCD(SAIDL, "Bar")
            # Line Chart
            LDL = TSCD(ESAIDL, "Line")
            # Pie Chart
            PDL = TSCD(SOIDL, "Pie")
            # Banner
            BNL = TSCD(SBNDL, "Banner")



        elif projectType == 'Service':
            print()
    elif core == 'Zabbix':
        EZYL = EZY()

    RD = {
        "barChartData": BDL,
        "lineChartData" : LDL,
        "pieChartData" : PDL,
        "bannerData" : BNL
    }

    return RD





