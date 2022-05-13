from api.views import DashboardData

def DashboardDataList() :
    DCDL = DashboardData()
    barChartData = DCDL["barChartData"]
    lineChartData = DCDL["lineChartData"]
    pieChartData = DCDL["pieChartData"]
    bannerData = DCDL["bannerData"]
    returnData = {'barChartDataList': barChartData,'lineChartDataList' : lineChartData, 'pieChartDataList': pieChartData, 'bannerDataList': bannerData}
    return returnData






