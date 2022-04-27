from rest_framework.response import Response
from api.models import Menulist
from rest_framework.views import APIView
from api.serializers import MenulistSerializer
from django.shortcuts import render
from config import settings
from api.Call.Common.API import Auth, Tokens
from api.Call.Common.User import SessionLogin, UserGet, SessionLogout
from api.Call.Asset import AssetGet
from api.Call.System import Status
from api.Call.Server import Info, Host
from api.Call.Export import Export
from web.dataParsing.API import External
from web.dataParsing.API.AssetParser import AssetParsing
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
sessionKey = Auth()


def LoginT(request):
    username = request.POST.get('username', False)
    password = request.POST.get('password', False)
    sessionLoginList = SessionLogin(username, password)
    return render(request, 'common/loginT.html')


def SessionLogout(request):
    SessionLogout(sessionKey)
    logoutPage = settings.LOGOUT_REDIRECT_URL
    return render(request, 'common/logout.html')


def UserGet(request):
    userInfoList = UserGet(sessionKey)
    return render(request, 'common/userInfo.html', userInfoList)


def Asset(request):
    assetList = AssetGet(sessionKey)
    AssetParsing(assetList)
    return render(request, 'API/asset/asset.html', assetList)


def SystemStatus(request):
    systemStatusList = Status(sessionKey)
    return render(request, 'API/system/status.html', systemStatusList)


def ServerInfo(request):
    serverInfoList = Info(sessionKey)
    return render(request, 'API/server/info.html', serverInfoList)


def ServerHost(request):
    serverHostList = Host(sessionKey)
    return render(request, 'API/server/host.html', serverHostList)


def Export(request):
    ExportList = Export(sessionKey)
    return render(request, 'API/export.html')


def ApiTokens(request):
    tokensList = Tokens(sessionKey)
    return render(request, 'common/apiTokens.html', tokensList)


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
