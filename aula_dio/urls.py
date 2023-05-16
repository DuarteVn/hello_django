
from django.contrib import admin
from django.urls import path
from app_wpp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/<nome>/<int:idade>/', views.hello, name='Hello World')
]
