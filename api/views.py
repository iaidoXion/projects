from rest_framework.response import Response
from api.models import Menulist
from rest_framework.views import APIView
from api.serializers import MenulistSerializer
from django.shortcuts import render
from config import settings
from api.Call.Auth import SessionKey
from api.Call.Common.API import Tokens
from api.Call.Common.User import UserInfoGet, SessionLogin, SessionLogout
from api.Call.Asset import Info as AssetInfoAPI, Attributes
from api.Call.System import Status
from api.Call.Server import Info as SInfo, Host
from api.Call.Export import Export
from web.dataParsing.API import External
from web.dataParsing.API.AssetParser import InfoParsing as AIP
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)



def LoginT(request):
    username = request.POST.get('username', False)
    password = request.POST.get('password', False)
    SessionLogin(username, password)
    return render(request, 'common/loginT.html')


def SessionLogout(request):
    sessionKey = SessionKey()
    SessionLogout(sessionKey)
    logoutPage = settings.LOGOUT_REDIRECT_URL
    return render(request, 'common/logout.html')


def UserGet(request):
    sessionKey = SessionKey()
    returnList = UserInfoGet(sessionKey)
    return render(request, 'common/userInfo.html', returnList)


def AssetInfo(request):
    sessionKey = SessionKey()
    AIDL = AssetInfoAPI(sessionKey)
    parserData = AIDL['dataList']
    returnList = AIP(parserData)
    return render(request, 'API/asset/info.html', returnList)


def AssetAttributes(request) :
    sessionKey = SessionKey()
    returnList = Attributes(sessionKey)
    #print(assetAttributesList)
    return render(request, 'API/asset/attributes.html', returnList)


def SystemStatus(request):
    sessionKey = SessionKey()
    returnList = Status(sessionKey)
    return render(request, 'API/system/status.html', returnList)


def ServerInfo(request):
    sessionKey = SessionKey()
    returnList = SInfo(sessionKey)
    return render(request, 'API/server/info.html', returnList)


def ServerHost(request):
    sessionKey = SessionKey()
    returnList = Host(sessionKey)
    return render(request, 'API/server/host.html', returnList)


def Export(request):
    sessionKey = SessionKey()
    returnList = Export(sessionKey)
    return render(request, 'API/export.html')


def ApiTokens(request):
    sessionKey = SessionKey()
    returnList = Tokens(sessionKey)
    return render(request, 'common/apiTokens.html', returnList)


def ExternalApi(request):
    res = External.DataParsing()
    pm10 = res.get('남산1동')
    context = {'station': '남산1동', 'pm10': pm10}
    return render(request, 'API/external.html', context)


def ExternalApiDetail(request):
    res = External.DataParsing()
    context = {'dust': res}
    print(res.keys())
    return render(request, 'API/externalApiDetail.html')


class MenuListAPI(APIView):
    def get(self, request):
        queryset = Menulist.objects.all()
        print(queryset)
        serializer = MenulistSerializer(queryset, many=True)
        return Response(serializer.data)


def DashboardChartData():
    sessionKey = SessionKey()
    AIDL = AssetInfoAPI(sessionKey)
    parserData = AIDL['dataList']
    returnList = AIP(parserData)
    return returnList
