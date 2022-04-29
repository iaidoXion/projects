from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from web.forms import UserForm
from web.commonFun import MenuList, StatisticsList
from api.views import DashboardChartData
import urllib3
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
    #barChartData = DashboardChartData()
    yesterdayData = StatisticsList()
    #returnData = {'barChartData': barChartData, 'menuList': menuSettingList}
    returnData = { 'menuList': menuSettingList}
    #print(returnData)
    return render(request, 'tanium/dashboard.html', returnData)

@login_required(login_url='common:login')
def assetWeb(request):
    return render(request, 'tanium/info.html', menuSettingList)

@login_required(login_url='common:login')
def software(request):
    return render(request, 'tanium/software.html', menuSettingList)

@login_required(login_url='common:login')
def security(request):
    return render(request, 'tanium/security.html', menuSettingList)

@login_required(login_url='common:login')
def report(request):
    return render(request, 'tanium/report.html', menuSettingList)

@login_required(login_url='common:login')
def setting(request):
    return render(request, 'common/setting.html', menuSettingList)
