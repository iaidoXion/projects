from django.contrib import admin
from django.urls import path, include
from web import views

urlpatterns = [
    path('web/', include('web.urls')),
    path('api/', include('api.urls')),
    path('xion/', include('xion.urls')),
    path('', views.index, name='index'),  # '/' 에 해당되는 path
    path('admin/', admin.site.urls),
    path('signup/', views.signup, name='signup'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('asset/', views.assetWeb, name='asset'),
    path('software/', views.software, name='software'),
    path('security/', views.security, name='security'),
    path('report/', views.report, name='report'),
    path('setting/', views.setting, name='setting'),
]