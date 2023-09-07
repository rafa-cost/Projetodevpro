from django.db.models import Count
from django.db.models.functions import TruncDate
from django.http import HttpResponse
from django.shortcuts import render, redirect

from devpro.encurtador.models import UrlRedirect, UrlLog


def relatorios(requisicao, slug):
    url_redirect = UrlRedirect.objects.get(slug=slug)    # e aqui é o endereço original. Estamos buscando dados no banco a principio o slug. E passando para a variavel "url_redirect"
    url_reduzida = requisicao.build_absolute_uri(f'/{slug}')  # "requisicao.build_absolute_uri" isso aqui constrói a url completa com esquema e o dominio. Ela recebe como parametro o path que eu quero acrescentar aqui (f'/{slug}')
    #ele fez esse código abaixo pelo debugger na parte do console
    redirecionamentos_por_data = list(
        UrlRedirect.objects.filter(
            slug=slug
        ).annotate(
            data=TruncDate('logs__criado_em')         #"logs" é a referencia que faz a ligação entre UrlRedirect e UrlLog. Esse TruncDate ira só pegar a data do  "criado_em". Bem dizer aqui indica o endereço do site e os dias dos cliques.
        ).annotate(
            cliques=Count('data')                     #ele ira contar as datas que houve os cliques no mesmo dia, ou seja ira contar o numero de cliques por dia
        ).order_by('data')                            # e aqui ele esta ordenando por data
    )    #esta filtrando essas informações da tabela UrlRedirect de dentro do banco de dados e passando para variavel "redirecionamentos_por_data"
    #o contexto é um dicionario com informações que eu posso passar para o meu relatório
    contexto = {'reduce': url_redirect, 'url_reduzida': url_reduzida,
                'redirecionamentos_por_data': redirecionamentos_por_data,             #comparando as variaveis daqui com as do html
                'total_cliques': sum(r.cliques for r in redirecionamentos_por_data)   #aqui esta somando a quantidade total de cliques e passando para variavel "total_cliques" do html. "cliques" são os cliques diarios e sum esta fazendo a soma dos cliques totais e passando para varial total_cliques.
                }

    return render(requisicao, 'encurtador/relatorio.html', contexto)     #renderizando para o endereço de template e passando o contexto como parametro





# Create your views here.
def redirecionar(requisicao, slug):
    url_redirect = UrlRedirect.objects.get(slug=slug)   #estamos buscando dados no banco , aqui no caso o slug e passando para a variavel
    UrlLog.objects.create(                           #Estamos consultando a tabela UrlLog no banco de dados . Aqui acho que esse código abaixo esta direcionando o slug para o endereço do site correto, por isso ao final esta rediecionando para a url_redirect.destino
        origem=requisicao.META.get('HTTP_REFERER'),
        user_agent=requisicao.META.get('HTTP_USER_AGENT'),
        host=requisicao.META.get('HTTP_HOST'),
        ip=requisicao.META.get('REMOTE_ADDR'),
        url_redirect=url_redirect
    )
    return redirect(url_redirect.destino)







