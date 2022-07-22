from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from web import views

urlpatterns = [
    path('web/', include('web.urls')),
    path('login/', auth_views.LoginView.as_view(template_name='common/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    #path('api/', include('api.urls')),
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