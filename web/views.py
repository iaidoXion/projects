from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from config import settings
from web.forms import UserForm
from .API.dataParsing import External
from web.API.Call.Auth import SessionAuth
from web.API.Call.Common.ApiTokens import Tokens
from web.API.Call.Common.User import SessionLogin, Get, Logout
from .API.Call.System import Status
from .API.Call.Server import Info, Host
from .API.Call.Export import Export
from .commonFun import MenuList
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
sessionKey = SessionAuth()
LoginInfoList = []
def index(request):
    return render(request, 'common/login.html')

def LoginT(request) :
    username = request.POST.get('username', False)
    password = request.POST.get('password', False)
    sessionLoginList = SessionLogin(username, password)
    #LoginInfoList.append(sessionLoginList['sessionLoginList'])

    return render(request, 'common/loginT.html')

def Logout(request) :
    Logout(sessionKey)
    logoutPage = settings.LOGOUT_REDIRECT_URL
    print(logoutPage)
    return render(request, 'common/logout.html')

def ApiTokens(request):
    tokensList = Tokens(sessionKey)
    return render(request, 'common/apiTokens.html', tokensList)

def signup(request):
    """ 계정생성 """
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)  # 사용자 인증
            login(request, user)  # 로그인
            return redirect('index')
    else:
        form = UserForm()
    return render(request, 'common/signup.html', {'form': form})


@login_required(login_url='common:login')
def dashboard(request):
    menuSettingList = MenuList()
    return render(request, 'tanium/dashboard.html', menuSettingList)

@login_required(login_url='common:login')
def asset(request):
    menuSettingList = MenuList()
    return render(request, 'tanium/asset.html', menuSettingList)

@login_required(login_url='common:login')
def software(request):
    menuSettingList = MenuList()
    return render(request, 'tanium/software.html', menuSettingList)

@login_required(login_url='common:login')
def security(request):
    menuSettingList = MenuList()
    return render(request, 'tanium/security.html', menuSettingList)

@login_required(login_url='common:login')
def report(request):
    menuSettingList = MenuList()
    return render(request, 'tanium/report.html', menuSettingList)

@login_required(login_url='common:login')
def setting(request):
    menuSettingList = MenuList()
    return render(request, 'common/setting.html', menuSettingList)

def UserGet(request) :
    userInfoList = Get(sessionKey)
    return render(request, 'common/userInfo.html', userInfoList)

def SystemStatus(request):
    systemStatusList = Status(sessionKey)
    return render(request, 'API/systemStatus.html', systemStatusList)

def ServerInfo(request):
    serverInfoList = Info(sessionKey)
    return render(request, 'API/server/info.html', serverInfoList)

def ServerHost(request):
    serverHostList = Host(sessionKey)
    return render(request, 'API/server/host.html', serverHostList)

def Export(request):
    ExportList = Export(sessionKey)
    return render(request, 'API/export.html')


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