from web.models import MenuSetting, Statistics

def MenuList() :
    menuListDB = MenuSetting.objects.order_by('id')
    menuList = {'menuList': menuListDB}
    return menuList

def StatisticsList() :
    StatisticsListDB = Statistics.objects.order_by('id')
    StatisticsList = {'StatisticsList': StatisticsListDB}
    return StatisticsList



