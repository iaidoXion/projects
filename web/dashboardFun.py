from api.views import DashboardData, DashboardDataNew

def DashboardDataList() :
    DCDL = DashboardDataNew()

    barChartData = DCDL["barChartData"]
    lineChartData = DCDL["lineChartData"]
    pieChartData = DCDL["pieChartData"]
    bannerData = DCDL["bannerData"]
    DCDLO = DashboardData()
    alarmData = DCDLO['alarmDataList']
    #print(alarmData)
    AssociationData = DCDLO['AssociationDataList']
    returnData = {'barChartDataList': barChartData,'lineChartDataList' : lineChartData, 'pieChartDataList': pieChartData, 'bannerDataList': bannerData, 'alarmDataList': alarmData, 'AssociationDataList' : AssociationData}
    return returnData






