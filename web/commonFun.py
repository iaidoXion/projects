from .models import MenuSetting
#from .API.Common import Auth
def MenuList() :
    menuListDB = MenuSetting.objects.order_by('id')
    menuList = {'menuList': menuListDB}
    return menuList


#def ApiSessionKey() :
#    sessionKey = Auth.ApiAuth()

#    sessionKeyList = {'sessionKey' : sessionKey}
#    return sessionKeyList


