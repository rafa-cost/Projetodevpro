from django.contrib import admin

from devpro.encurtador.models import UrlRedirect, UrlLog

#os campos que vamos ter no admin(banco de dados)
# Register your models here.
@admin.register(UrlRedirect)
class UrlRedirectAdmin(admin.ModelAdmin):
    list_display = ('destino', 'slug', 'criado_em', 'atualizado_em')

@admin.register(UrlLog)
class UrlLogAdmin(admin.ModelAdmin):
    list_display = ('origem', 'criado_em', 'user_agent', 'host', 'ip', 'url_redirect')


    def has_change_permission(self, request, obj=None):    #esses 3 campos é o seguinte na tabaela UrlLog, não pode alterar, não pode deletar e nem adicionar
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request):
        return False
