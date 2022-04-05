from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from web.forms import UserForm

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
    return render(request, 'tanium/dashboard.html')

@login_required(login_url='common:login')
def asset(request):
    return render(request, 'tanium/asset.html')

@login_required(login_url='common:login')
def software(request):
    return render(request, 'tanium/software.html')

@login_required(login_url='common:login')
def security(request):
    return render(request, 'tanium/security.html')

@login_required(login_url='common:login')
def report(request):
    return render(request, 'tanium/report.html')

@login_required(login_url='common:login')
def setting(request):
    return render(request, 'common/setting.html')
