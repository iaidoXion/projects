import pandas as pd

def data_frame(data, day, type, api):
    #print(data)
    PDLC = len(data)
    DFL = []
    for i in range(PDLC):
        if day == 'today' :
            if api == 'asset' :
                CI = data[i]['computer_id']
                IP = data[i]['ip_address']
                if type == 'assetItem' :
                    if data[i]['asset_item'] != None :
                        item = data[i]['asset_item']
                        itemPer = item.lower()
                    if itemPer.startswith('macbook'):
                        item = 'Notebook'
                    if itemPer.startswith('imac'):
                        item = 'Desktop'
                    itemIndex = 'assetItem'
                elif type == 'osItem' :
                    item = data[i]['os_platform']
                    itemIndex = 'os'
                elif type == 'DUS' :
                    item = data[i]['drive_use_size']
                    itemIndex = 'driveSize'
                elif type == 'LH':
                    item = data[i]['last_seen_at'].split('T')[0]
                    itemIndex = 'lastLogin'
            elif api == 'sensor' :
                CI = data[i][0]
                IP = data[i][9]
                if type == 'RUET' :
                    item = data[i][13].split(' ')[0]
                    if item.isdigit() :
                        item = int(item)
                    else :
                        item = 0
                    itemIndex = 'ramSize'
                elif type == 'RUEU' :
                    item = data[i][12].split(' ')[0]
                    if item.isdigit():
                        item = int(item)
                    else:
                        item = 0
                    itemIndex = 'ramSize'
                elif type == 'LPC' :
                    item = data[i][10]
                    itemIndex = 'listenPortCount'
                elif type == 'EPC' :
                    item = data[i][11]
                    itemIndex = 'establishedPortCount'
        elif day == 'yesterday' :
            CI = data[i][0]
            IP = ''
            if type == 'DUS' :
                item = data[i][1]
                itemIndex = 'driveSize'
            elif type == 'LH':
                item = str(data[i][5]).split(' ')[0]
                itemIndex = 'lastLogin'
            #elif type == 'ramUseSize':
                #    item = str(data[i][4])
                #itemIndex = 'ramSize'
            elif type == 'LPC':
                item = str(data[i][2])
                itemIndex = 'listenPortCount'
            elif type == 'EPC':
                item = str(data[i][3])
                itemIndex = 'establishedPortCount'

        DFL.append([CI, item, IP])
    DFC = ['id', itemIndex, 'ip']
    DF = pd.DataFrame(DFL, columns=DFC).sort_values(by="id", ascending=False).reset_index(drop=True)
    #print(DF)
    return DF










