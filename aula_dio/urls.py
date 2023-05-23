from django.contrib import admin
from django.urls import path
from app_wpp import views
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.lista_eventos),
    path('home/evento/', views.Evento),
    path('home/evento/submit', views.submit_Evento),
    path('home/evento/delete/<int:id_evento>/', views.delete_Evento),
    path('', RedirectView.as_view(url='/home/')),
    path('login/', views.login_user),
    path('login/submit', views.submit_login),
    path('logout/', views.logout_user)    
]
