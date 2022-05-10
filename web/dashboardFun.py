from api.views import DashboardData

def DashboardDataList() :
    DCDL = DashboardData()
    barChartData = DCDL["barChartData"]
    pieChartData = DCDL["pieChartData"]
    #bannerList = DCDL['bannerDataList']
    returnData = {'barChartDataList': barChartData, 'pieChartDataList': pieChartData}
    #returnData = {'barChartDataList': barChartData, 'pieChartDataList': pieChartData, 'bannerDataList': bannerList}
    return returnData






