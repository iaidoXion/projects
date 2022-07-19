import pandas as pd
from datetime import datetime

"""
with open("setting.json", encoding="UTF-8") as f:
    SETTING = json.loads(f.read())

DataLoadingType = SETTING['MODULE']['DataLoadingType']
"""


def Yesterday(ESYDL) :
    yesterdayDataList = []
    ATNM = []
    ATC = []
    AINM = []
    AIC = []
    OSNM = []
    OSC = []
    LLNM = []
    LLNC = []
    DSNM = []
    DSNC = []
    LPCSNM = []
    LPCSC = []
    EPCSNM = []
    EPCSC = []
    RUSSNM = []
    RUSSC = []

    for i in range(len(ESYDL)):
        if ESYDL[i][0] == 'asset' :
            if ESYDL[i][1] == 'all' :
                ATNM.append("Asset Total Count")
                ATC.append(int(ESYDL[i][2]))
            else :
                AINM.append(ESYDL[i][1])
                AIC.append(int(ESYDL[i][2]))
        elif ESYDL[i][0] == 'os' :
            OSNM.append(ESYDL[i][1])
            OSC.append(int(ESYDL[i][2]))
        elif ESYDL[i][0] == 'login_history' :
            LLNM.append(ESYDL[i][1])
            LLNC.append(int(ESYDL[i][2]))
        elif ESYDL[i][0] == 'drive_size' :
            DSNM.append(ESYDL[i][1])
            DSNC.append(int(ESYDL[i][2]))
        elif ESYDL[i][0] == 'listen_port_count':
            LPCSNM.append(ESYDL[i][1])
            LPCSC.append(int(ESYDL[i][2]))
        elif ESYDL[i][0] == 'established_port_count':
            EPCSNM.append(ESYDL[i][1])
            EPCSC.append(int(ESYDL[i][2]))
            #yesterdayDataList.append({"name": SYDL[i][1], "count" : SYDL[i][2]})
        elif ESYDL[i][0] == 'ram_use_size':
            RUSSNM.append(ESYDL[i][1])
            RUSSC.append(int(ESYDL[i][2]))
    RD = {
        "AA": {"name": ATNM, "value": ATC},
        "AIS": {"name": AINM, "value": AIC},
        "OS": {"name": OSNM, "value": OSC},
        "LS": {"name": LLNM, "value": LLNC},
        "DS": {"name": DSNM, "value": DSNC},
        "LPS": {"name": LPCSNM, "value": LPCSC},
        "EPS": {"name": EPCSNM, "value": EPCSC},
        "RUSS" : {"name": RUSSNM, "value": RUSSC},
    }
    #print(RD)
    return RD

def FiveDay(ESFDL, ASDCL) :
    today = datetime.today().strftime("%Y-%m-%d")
    ADL =[]
    for i in range(len(ESFDL)):
        if not ESFDL[i][1] == 'all':
            name = ESFDL[i][1]
            price = int(ESFDL[i][2])
            date = ESFDL[i][3].strftime("%Y-%m-%d")
            ADL.append([name, price, date])

    for j in range(len(ASDCL['AIS']['name'])) :
        name = ASDCL['AIS']['name'][j]
        price = int(ASDCL['AIS']['value'][j])
        date = today
        ADL.append([name, price, date])
    ACNM = ['name', 'value', 'date']
    ADF = pd.DataFrame(ADL, columns=ACNM)

    return ADF


def Banner(ASDCL,SYDL) :
    #print(SYDL.keys())
    TAA = ASDCL['AA']
    YAA = SYDL['AA']
    TLS = ASDCL['LS']
    YLS = SYDL['LS']
    TAIS = ASDCL['AIS']
    YAIS = SYDL['AIS']
    TOS = ASDCL['OS']
    YOS = SYDL['OS']
    TDS = ASDCL['DS']
    YDS = SYDL['DS']
    TLP = ASDCL['LP']
    YLP = SYDL['LPS']
    TEP = ASDCL['EP']
    YEP = SYDL['EPS']
    TRUS = ASDCL['RUS']
    YRUS = SYDL['RUSS']
    DFCNM = ['name', 'value']
    TAIDL = []
    for i in range(len(TAIS['name'])) :
        TAIDL.append([TAIS['name'][i],TAIS['value'][i]])
    TAIDF = pd.DataFrame(TAIDL, columns=DFCNM)
    YAIDL = []
    for j in range(len(YAIS['name'])):
        YAIDL.append([YAIS['name'][j], YAIS['value'][j]])
    YAIDF = pd.DataFrame(YAIDL, columns=DFCNM)
    TOSDL = []
    for k in range(len(TOS['name'])):
        TOSDL.append([TOS['name'][k], TOS['value'][k]])
    TOSDF = pd.DataFrame(TOSDL, columns=DFCNM)
    YOSDL = []
    for l in range(len(YOS['name'])):
        YOSDL.append([YOS['name'][l], YOS['value'][l]])
    YOSDF = pd.DataFrame(YOSDL, columns=DFCNM)
    RD = {"TAA" : TAA, "YAA" : YAA, "TLS" : TLS, "YLS" : YLS, "TAIS" : TAIDF, "YAIS" : YAIDF, "TOS" : TOSDF, "YOS": YOSDF, "TDS" : TDS, "YDS" : YDS, "TLP" : TLP, "YLP" : YLP, "TEP" : TEP, "YEP" : YEP, "TRUS" : TRUS, "YRUS" : YRUS}
    return RD




def ChartData(ASDCL,AssociationS):
    LHAL = {'firstData':[ASDCL['ADL']['LHAL'][0]], 'dataList' : ASDCL['ADL']['LHAL']}
    if ASDCL['ADL']['DSAL'] :
        DSAL = {'firstData':[ASDCL['ADL']['DSAL'][0]], 'dataList' : ASDCL['ADL']['DSAL']}
    else :
        DSAL = {'firstData': [], 'dataList': []}
    LPCAL = {'firstData':[ASDCL['ADL']['LPCAL'][0]], 'dataList' : ASDCL['ADL']['LPCAL']}
    EPCAL = {'firstData':[ASDCL['ADL']['EPCAL'][0]], 'dataList' : ASDCL['ADL']['EPCAL']}
    RUSAL = {'firstData':[ASDCL['ADL']['RUSCAL'][0]], 'dataList' : ASDCL['ADL']['RUSCAL']}
    RD = {'alarmDataList':{'LHAL' : LHAL, 'DSAL': DSAL, 'LPCAL': LPCAL, 'EPCAL':EPCAL, 'RUSAL' : RUSAL}, 'AssociationDataList' : AssociationS}
    return RD

def DataFrame(data, period, type) :
    if type == 'Banner':
        DFDL = []
        for i in range(len(data)):
            if period == 'past' :
                if data[i][0] == 'asset' or data[i][0] == 'os' :
                    if data[i][1] == 'all' :
                        name = 'Asset Total'
                    else :
                        name = data[i][1]
                elif data[i][0] == 'drive_size' :
                    name = 'Drive Size No Change'
                elif data[i][0] == 'login_history' :
                    name = 'No Login History'
                elif data[i][0] == 'ram_use_size' :
                    name = 'Ram Size No Change'
                elif data[i][0] == 'listen_port_count' :
                    name = 'Listen Port No Change'
                elif data[i][0] == 'established_port_count' :
                    name = 'Established Port No Change'
                DFDL.append([name, data[i][2]])
            elif period == 'today' :
                for j in range(len(data[i]['name'])) :
                    name = data[i]['name'][j]
                    value = data[i]['value'][j]
                    DFDL.append([name, value])
        DFCNM=['name', 'value']
        RD = pd.DataFrame(DFDL, columns=DFCNM)
    return RD

def List(data) :
    NMDL = []
    VDL = []
    DDL = []
    today = datetime.today().strftime("%Y-%m-%d")
    for i in range(len(data[1]['name'])) :
        NMDL.append(data[1]['name'][i])
        VDL.append(data[1]['value'][i])
        DDL.append(today)
    for j in range(len(data[0])) :
        if data[0][j][1] != 'all':
            NMDL.append(data[0][j][1])
            VDL.append(data[0][j][2])
            DDL.append(data[0][j][3].strftime("%Y-%m-%d"))
    RD = {'name' : NMDL, 'value' : VDL, 'date' : DDL}
    return RD

def ChartDataNew(data,type) :
    ChartDataList = []
    for i in range(len(data['name'])):
        if type == 'Bar' or type == 'Pie':
            ChartDataList.append({"name": data['name'][i], "value": data['value'][i]})
            #print(ChartDataList)
        elif type == 'Banner' :
            ChartDataList.append({"name": data['name'][i], "value": data['value_y'][i], "roc" : data['ROC'][i]})
        elif type == 'Line' :
            ChartDataList.append({"name": data['name'][i], "value": data['value'][i], "date" : data['date'][i]})
    RD = ChartDataList
    return RD
    print(RD)










