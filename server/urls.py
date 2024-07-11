from django.contrib import admin
from django.urls import path
from django.conf import settings
from home.views import *
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    #home path
    path('', home),
    path('data_input/', data_input, name='data_input'),
    path('profile/<int:id>/', profile, name='profile')
]