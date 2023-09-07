"""devpro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from devpro.encurtador import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('<slug:slug>', views.redirecionar),              #aqui é o seguinte, assim que o usuario clicar em 'reduce' ou 'url_reduzida', ele sera redirecionado para a pagina do slug.
    path('relatorios/<slug:slug>', views.relatorios),     # para entrar na pagina inicial tem que colocar relatorios/slug
]
