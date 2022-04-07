from web.ApiCall import External

def DataParsing():
    items = External.ApiModels()
    itemsCount = len(items)
    stationNameList = []
    pm10ValueList = []
    for i in range(0, itemsCount):
        stationName = items[i]['stationName']
        pm10Value = items[i]['pm10Value']
        stationNameList.append(stationName)
        pm10ValueList.append(pm10Value)
    dataDict = {stationNameList[i] : pm10ValueList[i] for i in range(0, itemsCount)}

    return dataDict