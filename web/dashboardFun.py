from api.views import DashboardData, DashboardDataNew

def DashboardDataList() :
    DCDL = DashboardDataNew()
   

    barChartData = DCDL["barChartData"]
    lineChartData = DCDL["lineChartData"]
    pieChartData = DCDL["pieChartData"]
    bannerData = DCDL["bannerData"]
    alarmData = DCDL["alarmListData"]

    DCDLO = DashboardData()
    AssociationData = DCDLO['AssociationDataList']
    #print(AssociationData)
    returnData = {'barChartDataList': barChartData,'lineChartDataList' : lineChartData, 'pieChartDataList': pieChartData, 'bannerDataList': bannerData, 'alarmDataList': alarmData, 'AssociationDataList' : AssociationData}
    return returnData






