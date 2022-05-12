from api.views import DashboardData

def DashboardDataList() :
    DCDL = DashboardData()
    barChartData = DCDL["barChartData"]
    pieChartData = DCDL["pieChartData"]
    bannerData = DCDL["bannerData"]
    returnData = {'barChartDataList': barChartData, 'pieChartDataList': pieChartData, 'bannerDataList': bannerData}
    return returnData






