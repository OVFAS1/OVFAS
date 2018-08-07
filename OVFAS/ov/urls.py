from django.contrib import admin
from django.urls import path,include
from django.contrib.auth import views as auth_views
from . import views


app_name="ov"

urlpatterns = [

    path('admin/', admin.site.urls),
    path('',views.index,name="index"),
    path('outingform/',views.outingform,name='outingform'),
    path('registration/',views.registration,name='registration')


]
