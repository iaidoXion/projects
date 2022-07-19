import pandas as pd
from datetime import datetime

"""
with open("setting.json", encoding="UTF-8") as f:
    SETTING = json.loads(f.read())

DataLoadingType = SETTING['MODULE']['DataLoadingType']
"""


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

def Banner(data, type) :
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


def LineChart(data) :
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


def AlaemList(data, type) :
    ALDL = []
    if type == 'DUS':
        AT = 'Drive Size No Change'
    elif type == 'RUS':
        AT = 'Ram Size No Change'
    elif type == 'LPC':
        AT = 'Listen Port No Change'
    elif type == 'EPC':
        AT = 'Established Port No Change'
    elif type == 'LH' :
        AT = 'No Login History'
        #print(data['name'])
    if data['name'][0] :
        FDL = [{'id' :data['name'][0], 'ip':data['value'][0], 'alarmText':AT}]
        for i in range(len(data['name'])) :
            ALDL.append({'id' : data['name'][i], 'ip': data['value'][i], 'alarmText':AT})
    else :
        FDL =[{'id' :'-', 'ip':'-', 'alarmText':AT}]
        ALDL =[{'id' :'-', 'ip':'-', 'alarmText':AT}]
    RD ={'firstData': FDL, 'dataList' : ALDL}
    #print(RD)
    return RD











def ChartDataNew(data,type) :
    ChartDataList = []
    for i in range(len(data['name'])):
        if type == 'Bar' or type == 'Pie':
            ChartDataList.append({"name": data['name'][i], "value": data['value'][i]})
        elif type == 'Banner' :
            ChartDataList.append({"name": data['name'][i], "value": data['value_y'][i], "roc" : data['ROC'][i]})
        elif type == 'Line' :
            ChartDataList.append({"name": data['name'][i], "value": data['value'][i], "date" : data['date'][i]})
        #elif type == 'alarmList' :
        #    print({'firstData':{"name" : data['name'][i],"value": data['value'][i] }})
    RD = ChartDataList
    return RD










