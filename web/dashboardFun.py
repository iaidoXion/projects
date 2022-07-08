from api.views import DashboardData, DashboardDataNew

def DashboardDataList() :
    DCDL =DashboardDataNew()

    barChartData = DCDL["barChartData"]
    pieChartData = DCDL["pieChartData"]
    DCDLO = DashboardData()

    lineChartData = DCDLO["lineChartData"]
    bannerData = DCDLO["bannerData"]
    alarmData = DCDLO['alarmDataList']
    AssociationData = DCDLO['AssociationDataList']
    returnData = {'barChartDataList': barChartData,'lineChartDataList' : lineChartData, 'pieChartDataList': pieChartData, 'bannerDataList': bannerData, 'alarmDataList': alarmData, 'AssociationDataList' : AssociationData}
    #returnData = {'barChartDataList': barChartData, 'pieChartDataList': pieChartData}
    #print(returnData['AssociationDataList'])
    return returnData






