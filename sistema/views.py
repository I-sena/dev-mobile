from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.views.generic import View
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
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
    
class LoginAPI(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(
            data=request.data,
            context={
                'request': request
            }
        )

        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'id': user.id,
            'user.first_name': user.first_name,
            'email': user.email,
            'token': token.key
        })