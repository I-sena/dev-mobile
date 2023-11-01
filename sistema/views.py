from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.views.generic import View
#from django.http import HttpResponse
from django.conf import settings
import logging

logger = logging.getLogger('sistema')


class Login(View):

    def get(self, request):
        contexto = {'mensagem': ""}

        if not request.user.is_authenticated:
            return render(request, "autenticacao.html", contexto)
        else:
            return redirect("/veiculo")

    def post(self, request):

        #Obtém as credenciais de autenticação do formulario
        usuario = request.POST.get('usuario', None)
        senha = request.POST.get('senha', None)

        logger.info('Usuário: {}'.format(usuario))
        logger.info('Senha: {}'.format(senha))
        
        user = authenticate(request, username=usuario, password=senha)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect("/veiculo")
            return render(request, 'autenticacao.html', {'mensagem': 'Usuário inativo.'})
        return render(request, 'autenticacao.html', {'mensagem': 'Usuário ou senha inválida.'})

class Logout(View):
    """
    Class based view para realizar logout de usuarios.
    """

    def get(self, request):
        logout(request)
        return redirect(settings.LOGIN_URL)