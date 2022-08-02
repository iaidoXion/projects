import pandas as pd

from api.Call.Auth import SessionKey
from api.Call.Asset import data as AssetAPI
from api.Call.Sensor import data as SensorAPI
from DataParsing.Extract.Asset import past_data as EAY
from DataParsing.Extract.Statistics import Yesterday as ESY, FiveDay as ESF
from DataParsing.Transform.Asset import data_frame as TACD
from DataParsing.Transform.Statistics import banner as TSBA, alarm as TSAL, line_chart as TSLC, chart_data as TSCD
from Analysis.Statistics.Asset import chart_data as SACD
from Analysis.Statistics.Statistics import calculation as ASSC, alarm_case_detection as ASSACD, network as ASSN
import urllib3
import json

with open("setting.json", encoding="UTF-8") as f:
    SETTING = json.loads(f.read())
core = SETTING['PROJECT']['CORE']
ProjectType = SETTING['PROJECT']['TYPE']
Customer = SETTING['PROJECT']['CUSTOMER']

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def DashboardData() :

    if core == 'Tanium' :
        SK = SessionKey()                                                       # API Sesstion KEY Call
        assetData = AssetAPI(SK)                                                # API Asset(Now) Data Call
        EAYL = EAY()                                                            # DB Asset(yesterday) Data Select
        sensorData = SensorAPI(SK)                                              # API Sensor(Now) Data Call
        assetAPI = assetData['dataList']
        sensorAPI = sensorData['dataList']
        if Customer == 'NC' or 'Xfactor' :
            if ProjectType == 'System' :
                # Asset Item Statistics
                TAIDL = TACD(sensorAPI, "today", "assetItem")
                SAIDL = SACD(TAIDL, "assetItem", "group")

                # OS Item Statistics
                TOIDL = TACD(sensorAPI, "today", "osItem")
                SOIDL = SACD(TOIDL, "osItem", "group")

                # Drive Use Size Statistics
                ## Today compare Count (now Asset API Data & yesterday Asset Table Data)
                TDUSDLT = TACD(sensorAPI, "today", "DUS")
                TDUSDLY = TACD(EAYL, "yesterday", "DUS")
                DUSCTDL = [TDUSDLT, TDUSDLY]
                SDUSDLT = SACD(DUSCTDL, "DUS", "count")

                # No Login History Statistics
                ## Today compare Count (now Asset API Data & yesterday Asset Table Data)
                TNLHDLT = TACD(sensorAPI, "today", "LH")
                TNLHDLY = TACD(EAYL, "yesterday", "LH")
                NLHCTDL = [TNLHDLT, TNLHDLY]
                SNLHDLT = SACD(NLHCTDL, "LH", "count")
                #print(TNLHDLT)
                # RAM USE Size Statistics
                ## Today compare Count (now sensor API Data & yesterday Asset Table Data)
                TRUSDLT = TACD(sensorAPI, "today", "RUET")
                #print(TRUSDLT)
                TRUSDLU = TACD(sensorAPI, "today", "RUEU")
                #print(TRUSDLU)
                #TRUSDLY = TACD(EAYL, "yesterday", "ramUseSize", '')
                RUSCTDL = [TRUSDLT, TRUSDLU]
                SRUSDLT = SACD(RUSCTDL, "RUE", "count")

                # Listen Port Count Statistics
                ## Today compare Count (now sensor API Data & yesterday Asset Table Data)
                TLPCDLT = TACD(sensorAPI, "today", "LPC")
                TLPCDLY = TACD(EAYL, "yesterday", "LPC")
                LPCCTDL = [TLPCDLT, TLPCDLY]
                LPCDLT = SACD(LPCCTDL, "LPC", "count")

                # Established Port Count Statistics
                ## Today compare Count (now sensor API Data & yesterday Asset Table Data)
                TEPCDLT = TACD(sensorAPI, "today", "EPC")
                TEPCDLY = TACD(EAYL, "yesterday", "EPC")
                EPCCTDL = [TEPCDLT, TEPCDLY]
                EPCDLT = SACD(EPCCTDL, "EPC", "count")

                # Banner ROC Calculation (yesterday Statistics Table Data & API Data Statistics)
                ## Yesterday Statistics Table Data Extract & Transform
                ESDLY = ESY()                                                                               # yesterday Statistics Table Data Extract
                TSDLY = TSBA(ESDLY, 'past')                                                            # yesterday Statistics Data Transform
                ## Today Statistics Data Transform
                ## Today Asset Total Count Calculation
                ATCDL = {'name': ['Asset Total'], 'value': [sum(SAIDL['value'])]}
                TSDL = ATCDL, SAIDL, SOIDL, SDUSDLT, SNLHDLT, SRUSDLT, LPCDLT, EPCDLT                        # today Statistics Data List
                TSDLT = TSBA(TSDL, 'today')
                ## Banner ROC Calculation
                SBNDL = ASSC(TSDLY, TSDLT)

                # 5Days Asset Item Statistics Data Combination
                ## Past Data Extract(Statistics Table Data 5Days ago)
                ESDLF = ESF('asset')
                ## Past & Today Data Combination Transform
                AIFD = [ESDLF, SAIDL]
                ESAIDL = TSLC(AIFD)


                # Alarm
                ## Alarm Statistics(Alarm case detection)
                SDUSADL = ASSACD(DUSCTDL, 'DUS')
                SLHADL = ASSACD(NLHCTDL,  'LH')
                SRUSADL = ASSACD(RUSCTDL, 'RUE')
                SLPCADL = ASSACD(LPCCTDL, 'LPC')
                SEPCADL = ASSACD(EPCCTDL, 'EPC')

                ## List
                ### Transform by case
                TDUSALDL = TSAL(SDUSADL, 'list', 'DUS')
                TLHALDL = TSAL(SLHADL, 'list', 'LH')
                TRUSALDL = TSAL(SRUSADL, 'list', 'RUE')
                TLPCALDL = TSAL(SLPCADL, 'list', 'LPC')
                TEPCALDL = TSAL(SEPCADL, 'list', 'EPC')
                ALD = [TDUSALDL, TLHALDL, TRUSALDL, TLPCALDL, TEPCALDL]

                ## Network
                ### Data Grouping(Statistics) by case
                SDUSND = ASSN(SDUSADL, 'group', 'DUS')
                SLHND = ASSN(SLHADL, 'group', 'LH')
                SRUSND = ASSN(SRUSADL, 'group', 'RUE')
                SLPCND = ASSN(SLPCADL, 'group', 'LPC')
                SEPCND = ASSN(SEPCADL, 'group', 'EPC')

                TDUSND = TSAL(SDUSND, 'network', 'DUS')
                TLHND = TSAL(SLHND, 'network', 'LH')
                TRUSND = TSAL(SRUSND, 'network', 'RUE')
                TLPCND = TSAL(SLPCND, 'network', 'LPC')
                TEPCND = TSAL(SEPCND, 'network', 'EPC')

                NDL = [TDUSND[0], TDUSND[1]+TLHND[1]+TRUSND[1]+TLPCND[1]+TEPCND[1]]
                NCDL = ASSN(NDL, 'max', 'all')
                a = [NDL[0][0], NDL[0][1], NDL[0][4]]
                b = []
                for i in range(len(NDL[1])) :
                    b.append([NDL[1][i][0], NDL[1][i][1], NDL[1][i][4]])
                c = pd.DataFrame(b, columns = a)
                #print(c)
                # BAR Chart
                BDL = TSCD(SAIDL, "Bar")
                # Line Chart
                LDL = TSCD(ESAIDL, "Line")
                #LDL = {}
                # Pie Chart
                PDL = TSCD(SOIDL, "Pie")
                # Banner
                BNDL = TSCD(SBNDL, "Banner")
                # Alarm List
                ALDL = TSCD(ALD, "alarmList")

            elif ProjectType == 'Service':
                print()
    elif core == 'Zabbix':
        print()

    RD = {
        "barChartData": BDL,
        "lineChartData" : LDL,
        "pieChartData" : PDL,
        "bannerData" : BNDL,
        "alarmListData" : ALDL[0],
        "AssociationDataList" : NCDL
    }

    return RD





