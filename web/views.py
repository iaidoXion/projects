from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from web.forms import UserForm
from .dataParsing import External
from .API.Common.Auth import ApiAuth
from .API.Call.SessionLogin import Login
from .API.Call.System import Status
from .API.Call.Server import Info, Host
from .commonFun import MenuList


def index(request):
    return render(request, 'common/login.html')

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

def SessionLogin(request):
    sessionKey = ApiAuth()
    sesstionLoginList = Login(sessionKey)
    print(sesstionLoginList)
    return render(request, 'API/sessionLogin.html')

def SystemStatus(request):
    sessionKey = ApiAuth()
    systemStatusList = Status(sessionKey)
    return render(request, 'API/systemStatus.html', systemStatusList)

def ServerInfo(request):
    sessionKey = ApiAuth()
    serverInfoList = Info(sessionKey)
    return render(request, 'API/server/info.html', serverInfoList)

def ServerHost(request):
    sessionKey = ApiAuth()
    serverHostList = Host(sessionKey)
    return render(request, 'API/server/host.html', serverHostList)

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