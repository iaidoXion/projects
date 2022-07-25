from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from web.forms import UserForm
from web.commonFun import MenuList
from web.dashboardFun import DashboardDataList
import urllib3
import json
with open("setting.json", encoding="UTF-8") as f:
    SETTING = json.loads(f.read())
ProjectType = SETTING['PROJECT']['TYPE']
Customer = SETTING['PROJECT']['CUSTOMER']
WorldUse = SETTING['PROJECT']['MAP']['World']
KoreaUse = SETTING['PROJECT']['MAP']['Korea']
AreaUse = SETTING['PROJECT']['MAP']['Area']
ZoneUse = SETTING['PROJECT']['MAP']['Zone']


urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
menuSettingList = MenuList()

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
    chartData = DashboardDataList()
    MapUse = {"WorldUse" : WorldUse, "KoreaUse" : KoreaUse, "AreaUse" : AreaUse, "ZoneUse" : ZoneUse}
    returnData = { 'menuList': menuSettingList, 'chartData' : chartData, 'MapUse' : MapUse, 'Customer' : Customer}
    #print(chartData)
    return render(request, 'tanium/dashboard.html', returnData)

@login_required(login_url='common:login')
def assetWeb(request):
    returnData = { 'menuList': menuSettingList }
    return render(request, 'tanium/asset.html', returnData)

@login_required(login_url='common:login')
def software(request):
    return render(request, 'tanium/software.html', menuSettingList)

@login_required(login_url='common:login')
def security(request):
    returnData = {'menuList': menuSettingList}
    return render(request, 'tanium/security.html', returnData)

@login_required(login_url='common:login')
def report(request):
    returnData = { 'menuList': menuSettingList }
    return render(request, 'tanium/report.html', returnData)

@login_required(login_url='common:login')
def setting(request):
    returnData = {'menuList': menuSettingList}
    return render(request, 'common/setting.html', returnData)
