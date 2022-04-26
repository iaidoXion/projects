from django.contrib import admin
from django.urls import path, include
from web import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('web/', include('web.urls')),
    path('api/', include('api.urls')),
    path('xion/', include('xion.urls')),

    path('', views.index, name='index'),  # '/' 에 해당되는 path
    path('loginT/', views.LoginT, name='loginT'),
    path('logout/', views.Logout, name='logout'),
    path('apiTokens/', views.ApiTokens, name='apiTokens'),
    path('signup/', views.signup, name='signup'),
    path('userInfo/', views.UserGet, name='userInfo'),


    path('dashboard/', views.dashboard, name='dashboard'),
    path('asset/', views.asset, name='asset'),
    path('software/', views.software, name='software'),
    path('security/', views.security, name='security'),
    path('report/', views.report, name='report'),
    path('setting/', views.setting, name='setting'),

    path('system/status/', views.SystemStatus, name='systemStatus'),
    path('server/info/', views.ServerInfo, name='serverInfo'),
    path('server/host/', views.ServerHost, name='serverHost'),

    path('export/', views.Export, name='export'),

    path('externalAPI/', views.ExternalApi, name='ExternalApi'),
    path('externalApiDetail/', views.ExternalApiDetail, name='ExternalApiDetail'),

]