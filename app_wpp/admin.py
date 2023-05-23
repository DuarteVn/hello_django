from django.contrib import admin
from app_wpp.models import evento

class EventoAdmin(admin.ModelAdmin):
    list_display =('id','titulo', 'data_evento', 'data_criacao')
    list_filter = ('usuario','data_evento',)

admin.site.register(evento, EventoAdmin)