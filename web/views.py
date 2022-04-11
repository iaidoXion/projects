from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from web.forms import UserForm
from .dataParsing import External
from .models import MenuSetting


def index(request):
    return render(request, 'common/login.html')

def MenuList(request) :
    menuList = MenuSetting.objects.order_by('id')
    context = {'menuList' : menuList}
    return render(request, 'navbar.html', context)

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
    menuList = MenuSetting.objects.order_by('id')
    context = {'menuList': menuList}

    return render(request, 'tanium/dashboard.html', context)

@login_required(login_url='common:login')
def asset(request):
    menuList = MenuSetting.objects.order_by('id')
    context = {'menuList': menuList}

    return render(request, 'tanium/asset.html', context)

@login_required(login_url='common:login')
def software(request):
    menuList = MenuSetting.objects.order_by('id')
    context = {'menuList': menuList}
    return render(request, 'tanium/software.html', context)

@login_required(login_url='common:login')
def security(request):
    menuList = MenuSetting.objects.order_by('id')
    context = {'menuList': menuList}
    return render(request, 'tanium/security.html', context)

@login_required(login_url='common:login')
def report(request):
    menuList = MenuSetting.objects.order_by('id')
    context = {'menuList': menuList}
    return render(request, 'tanium/report.html', context)

@login_required(login_url='common:login')
def setting(request):
    menuList = MenuSetting.objects.order_by('id')
    context = {'menuList': menuList}
    return render(request, 'common/setting.html', context)

def ExternalApi(request):
    res = External.DataParsing()
    #print(res)
    pm10 = res.get('남산1동')
    context = {'station': '남산1동', 'pm10': pm10}
    return render(request, 'API/external.html', context)

def ExternalApiDetail(request):
    res = External.DataParsing()
    context = {'dust': res}
    print(res.keys())
    return render(request, 'API/externalApiDetail.html')