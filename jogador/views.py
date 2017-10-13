from django.shortcuts import render
from .models import Jogador 

def inicio(request):
	return render(request, 'jogador/inicio.html', {})
	
def pesquisa(request):
	return render(request, 'jogador/pesquisa.html',{})

def resultado_pesquisa(request):

	range_valores = {'0':[0,100], '1':[0,20], '2':[21,40], '3':[41,60], '4':[61,80], '5':[81,100]}

	jogadores_list = Jogador.objects.filter(
		ritmo__range=range_valores[request.POST['ritmo']],
		chute__range=range_valores[request.POST['chute']],
		passe__range=range_valores[request.POST['passe']],
		drible__range=range_valores[request.POST['drible']],
		defesa__range=range_valores[request.POST['defesa']],
		fisico__range=range_valores[request.POST['fisico']],
	)
	return render(request, 'jogador/resultado_pesquisa.html', {'jogadores_list':jogadores_list})

def lista(request):
	jogadores_list = Jogador.objects.order_by('nome')
	return render(request, 'jogador/lista.html', {'jogadores_list':jogadores_list})

def perfil(request, jogador_id):
	jogador = Jogador.objects.get(id=jogador_id)
	return render(request, 'jogador/perfil.html', {'jogador':jogador})