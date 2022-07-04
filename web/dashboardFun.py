from api.views import DashboardData

def DashboardDataList() :
    DCDL = DashboardData()
    barChartData = DCDL["barChartData"]
    lineChartData = DCDL["lineChartData"]
    pieChartData = DCDL["pieChartData"]
    bannerData = DCDL["bannerData"]
    alarmData = DCDL['alarmDataList']
    AssociationData = DCDL['AssociationDataList']
    returnData = {'barChartDataList': barChartData,'lineChartDataList' : lineChartData, 'pieChartDataList': pieChartData, 'bannerDataList': bannerData, 'alarmDataList': alarmData, 'AssociationDataList' : AssociationData}
    #print(returnData['AssociationDataList'])
    return returnData






