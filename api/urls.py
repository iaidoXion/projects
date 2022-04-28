from django.urls import path
from api.views import MenuListAPI
from api import views
app_name = 'api'
app_version = 'v1'

urlpatterns = [
    path(app_version+'/menuList/', MenuListAPI.as_view()),
    path(app_version+'/loginT/', views.LoginT, name='loginT'),
    #path(app_version+'/logout/', views.Logout, name='logout'),
    path(app_version+'/apiTokens/', views.ApiTokens, name='apiTokens'),
    path(app_version+'/user/info/', views.UserGet, name='userInfo'),
    path(app_version+'/asset/info/', views.AssetInfo, name='assetInfo'),
    path(app_version+'/asset/attributes/', views.AssetAttributes, name='assetAttributes'),
    path(app_version+'/system/status/', views.SystemStatus, name='systemStatus'),
    path(app_version+'/server/info/', views.ServerInfo, name='serverInfo'),
    path(app_version+'/server/host/', views.ServerHost, name='serverHost'),
    path(app_version+'/export/', views.Export, name='export'),
    path(app_version+'/externalAPI/', views.ExternalApi, name='ExternalApi'),
    path(app_version+'/externalApiDetail/', views.ExternalApiDetail, name='ExternalApiDetail'),
]