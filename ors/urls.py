from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ors/', views.test_ors),
    path('', views.welcome),
    path('welcome/', views.welcome),
    path('signup/', views.user_signup),
    path('signin/', views.user_signin),
]
