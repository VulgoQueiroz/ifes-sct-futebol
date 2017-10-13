from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.inicio, name='inicio'),
	url(r'^pesquisa/', views.pesquisa, name='pesquisa'),
	url(r'^resultado_pesquisa$', views.resultado_pesquisa, name='resultado_pesquisa'),
    url(r'^lista', views.lista, name='lista'),
    url(r'^perfil/(?P<jogador_id>[0-9]+)/$', views.perfil, name='perfil')
]

