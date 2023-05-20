
from django.contrib import admin
from django.urls import path
from app_wpp import views
from django.views.generic import RedirectView #Pra que?

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.lista_eventos),
    path('', RedirectView.as_view(url='/home/'))
]
