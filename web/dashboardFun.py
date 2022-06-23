from api.views import DashboardData

def DashboardDataList() :
    DCDL = DashboardData()
    barChartData = DCDL["barChartData"]
    lineChartData = DCDL["lineChartData"]
    pieChartData = DCDL["pieChartData"]
    bannerData = DCDL["bannerData"]
    alarmData = DCDL['alarmDataList']
    returnData = {'barChartDataList': barChartData,'lineChartDataList' : lineChartData, 'pieChartDataList': pieChartData, 'bannerDataList': bannerData, 'alarmDataList': alarmData}
    #print(returnData)
    return returnData






