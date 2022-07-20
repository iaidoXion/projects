import pandas as pd
import json
from datetime import datetime


with open("setting.json", encoding="UTF-8") as f:
    SETTING = json.loads(f.read())

alarmCaseFirst = SETTING['PROJECT']['Alarm']['Case']['First']
alarmCaseSecond = SETTING['PROJECT']['Alarm']['Case']['Second']
alarmCaseThird = SETTING['PROJECT']['Alarm']['Case']['Third']
alarmCaseFourth = SETTING['PROJECT']['Alarm']['Case']['Fourth']
alarmCaseFifth = SETTING['PROJECT']['Alarm']['Case']['Fifth']



def chartData(ASDCL,AssociationS):
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

def banner(data, type) :
    DFDL = []
    DFCNM=['name', 'value']
    for i in range(len(data)):
        if type == 'past' :
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
                name = 'RAM Usage Exceeded'
            elif data[i][0] == 'listen_port_count' :
                name = 'Listen Port No Change'
            elif data[i][0] == 'established_port_count' :
                name = 'Established Port No Change'
            DFDL.append([name, data[i][2]])
        elif type == 'today' :
            for j in range(len(data[i]['name'])) :
                name = data[i]['name'][j]
                value = data[i]['value'][j]
                DFDL.append([name, value])

    RD = pd.DataFrame(DFDL, columns=DFCNM)
    return RD


def lineChart(data) :
    NMDL = []
    VDL = []
    TDL = []
    today = datetime.today().strftime("%Y-%m-%d")
    for i in range(len(data[1]['name'])) :
        NMDL.append(data[1]['name'][i])
        VDL.append(data[1]['value'][i])
        TDL.append(today)
    for j in range(len(data[0])) :
        if data[0][j][1] != 'all':
            NMDL.append(data[0][j][1])
            VDL.append(data[0][j][2])
            TDL.append(data[0][j][3].strftime("%Y-%m-%d"))
    RD = {'name' : NMDL, 'value' : VDL, 'date' : TDL}
    return RD


def alarm(data, type, case) :
    if case == 'DUS':
        AT = alarmCaseFirst
    elif case == 'LH':
        AT = alarmCaseSecond
    elif case == 'RUE':
        AT = alarmCaseThird
    elif case == 'LPC':
        AT = alarmCaseFourth
    elif case == 'EPC':
        AT = alarmCaseFifth
    if type == 'list' :
        ALDL = []
        if data['name'][0] :
            FDL = [{'id' :data['name'][0], 'ip':data['value'][0], 'alarmText':data['alarmText'][0]}]
            for i in range(len(data['name'])) :
                ALDL.append({'id' : data['name'][i], 'ip': data['value'][i], 'alarmText':data['alarmText'][i]})
        else :
            FDL =[{'id' :'-', 'ip':'-', 'alarmText':AT}]
            ALDL =[{'id' :'-', 'ip':'-', 'alarmText':AT}]
        RD = {'firstData': FDL, 'dataList' : ALDL}
    elif type == 'network' :
        DL = []
        DC = ['group','alarmCount','id','name','alarmCase']
        for i in range(len(data.group)) :
            groupNameCount = int(data.group[i].split('.')[2]) + 1
            DL.append([data.group[i], data.counts[i], 'group'+str(groupNameCount)+case, case, AT])
        RD=[DC,DL]


    return RD











def chartDataNew(data, type) :
    ChartDataList = []
    if type == 'alarmList' :
        DUSDL = data[0]
        LHDL = data[1]
        RUEDL = data[2]
        LPCDL = data[3]
        EPCDL = data[4]
        ChartDataList.append({'DUSDL': DUSDL, 'LHDL': LHDL, 'RUEDL': RUEDL, 'LPCDL': LPCDL, 'EPCDL': EPCDL})
    else :
        for i in range(len(data['name'])):
            if type == 'Bar' or type == 'Pie':
                ChartDataList.append({"name": data['name'][i], "value": data['value'][i]})
            elif type == 'Banner' :
                ChartDataList.append({"name": data['name'][i], "value": data['value_y'][i], "roc" : data['ROC'][i]})
            elif type == 'Line' :
                ChartDataList.append({"name": data['name'][i], "value": data['value'][i], "date" : data['date'][i]})
    RD = ChartDataList
    return RD
    #print(RD)










