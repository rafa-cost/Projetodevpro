from django.db import models


# Create your models here.
class UrlRedirect(models.Model):                 #endereço do site com (url). E a url reduzida
    destino = models.URLField(max_length=512)
    slug = models.SlugField(max_length=128, unique=True)   #esse campo é unico(unique=True) portanto não conseguimos salvar outro slug com o mesmo nome
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'UrlRedirect para {self.destino}'   #é a msg que aparece assim que salva um Url redirects



class UrlLog(models.Model):                                 #informações dos acessos dos url logs
    criado_em = models.DateTimeField(auto_now_add=True)
    origem = models.URLField(max_length=512, null=True, blank=True)
    user_agent = models.CharField(max_length=512, null=True, blank=True)
    host = models.CharField(max_length=512, null=True, blank=True)
    ip = models.GenericIPAddressField(null=True, blank=True)
    url_redirect = models.ForeignKey(UrlRedirect, models.DO_NOTHING, related_name='logs') #"related_name='logs'" Qual sera o nome da propriedade se eu quiser referenciar todos os logs conectados ao UrlRedirect. Esse logs ele é a referencia que faz a ligação entre UrlLog e UrlRedirect. Aqui esta contando a quantidade de cliques.
                                                  # ele não fara nada se por acaso eu apagar a class UrlLog"models.DO_NOTHING".






