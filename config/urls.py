from django.contrib import admin
from django.urls import path, include
from web import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('web/', include('web.urls')),
    path('api/', include('api.urls')),
    path('xion/', include('xion.urls')),
    path('', views.index, name='index'),  # '/' 에 해당되는 path
    path('signup/', views.signup, name='signup'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('asset/', views.asset, name='asset'),
    path('software/', views.software, name='software'),
    path('security/', views.security, name='security'),
    path('report/', views.report, name='report'),
    path('setting/', views.setting, name='setting'),
    path('sessionLogin/', views.SessionLogin, name='SessionLogin'),
    path('systemStatus/', views.SystemStatus, name='systemStatus'),
    path('serverInfo/', views.ServerInfo, name='serverInfo'),
    path('serverHost/', views.ServerHost, name='serverHost'),
    path('externalAPI/', views.ExternalApi, name='ExternalApi'),
    path('externalApiDetail/', views.ExternalApiDetail, name='ExternalApiDetail'),
]