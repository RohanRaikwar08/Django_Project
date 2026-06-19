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
    path('testlist/', views.test_list),
    path('adduser/', views.add_user),
    path('userlist/', views.user_list),
    path('logout/', views.user_logout),
    path('list/', views.user_list),
    path('delete/<int:id>/', views.delete_user),
    path('save/', views.user_save),
    path('save/<int:id>/', views.user_save),
]
