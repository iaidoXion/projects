from django.http import HttpResponse


def index(request):
    return HttpResponse("안녕하세요 IPU Integrated Management System에 오신것을 환영합니다.")