# -*- coding: utf-8 -*-
from django.http import Http404
from django.shortcuts import render, get_object_or_404
from .models import Prova, Questao, Opcao, Resposta, Usuario
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.views import generic
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import UsuarioForm, LoginForm, ProvaForm


def index(request):
	lista_de_provas = Prova.objects.all()
	cprova = request.POST.get('prova_selecionada')
	if request.method == 'POST':
		sprova = Prova.objects.get(cprova = cprova)
		sprova.add()
		return redirect('polls/detalhes.html')
	else:
		form = ProvaForm()
	return render(request, 'polls/index.html',{'form':form,'lista_de_provas': lista_de_provas})

	
def detalhes(request, idProva):
	prova = get_object_or_404(Prova,pk=idProva)
	try:
		questao_selec = prova.questao_set.get(pk=request.POST['questao'])
	except (KeyError,Questao.DoesNotExist):
		return render (request,'polls/detalhes.html',{
			'prova': prova,
		})
	else:
		#questao_selec.votes += 1
		questao_selec = Questao(textoQuestao=request.POST.get('textoQuestao'),imagemQuestao=request.FILES('imagemQuestao'),imagem2Questao=request.FILES('imagem2Questao'),perguntaQuestao=request.POST.get('perguntaQuestao'))
		questao_selec.save()
		return HttpResponseRedirect(reverse('polls:resultados',args=(prova.idProva,)))
	
	questao = get_object_or_404(Questao,pk=idQuestao)
	try:
		opcao_selec = questao.opcao_set.get(pk=request.POST['opcao'])
	except (KeyError,Opcao.DoesNotExist):
		return render (request,'polls/detalhes.html',{
			'questao': questao,
		})
	else:
		#opcao_selec.votes += 1

		opcao_selec.save()
		return HttpResponseRedirect(reverse('polls:resultados',args=(questao.idQuestao,)))




def user_login(request):
    if request.method == 'POST':
        logar = LoginForm(request.POST)
        if logar.is_valid():
            cd = logar.cleaned_data
            user = authenticate(matriculaUsuario=cd['matriculaUsuario'],
                   senhaUsuario=cd['senhaUsuario'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect('/')
                else:
                    return HttpResponseRedirect('/login/')
            else:
                return HttpResponse('Login inválido')
    else:
        logar = LoginForm()
    return render(request, 'polls/login.html', {'logar': logar})



def registrar(request):
	if request.method == 'POST':
		registro =UsuarioForm(request.POST)
		if registro.is_valid():
			registro.save()
			print ("teste")
			return HttpResponseRedirect('/')
		else:
			return HttpResponseRedirect('/registrar/')
	else:
		registro = UsuarioForm()
		return render(request, 'polls/registrar.html',{'registro':registro})





def resposta(request, idOpcao):
	opcao = get_object_or_404(Opcao,pk=idOpcao)
	try:
		resposta_selec = prova.questao.resposta_set.get(pk=request.POST['resposta'])
	except (KeyError,Resposta.DoesNotExist):
		return HttpResponseRedirect (request,'polls/resposta.html',{
			'opcao': opcao,
		})
	else:
		#questao_selec.votes += 1

		resposta_selec.save()
		return HttpResponseRedirect(reverse('polls:resultados',args=(prova.idOpcao,)))





def todasProvas(request):
	if request.POST:
		idProva = request.POST['prova_selecionada']
		redirect('polls/detalhes.html',idProva=idProva)











def resultados(request, idProva):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % idProva)

class IndexView(generic.ListView):
	template_name = 'polls/index.html'
	context_object_list = 'lista_de_provas'

	def get_queryset(self):
		return Prova.objects.order_by('anoProva')[:5]

class DetailView(generic.DetailView):
	model = Prova
	template_name = 'polls/detalhes.html'