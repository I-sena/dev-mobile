from django.http import FileResponse, Http404
from django.urls import reverse_lazy
from sistema.bibliotecas import LoginObrigatorio
from veiculo.models import Veiculo
from django.core.exceptions import ObjectDoesNotExist
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from veiculo.forms import FormularioVeiculo
from veiculo.serializers import SerializadorVeiculo
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.authentication import TokenAuthentication
from rest_framework import permissions



class ListarVeiculos(LoginObrigatorio, ListView):

    """
    View para listar veiculos cadastrados.
    """

    model = Veiculo
    context_object_name = 'veiculos'
    template_name = 'veiculo/listar.html'

    def get_queryset(self, **kwargs):
        pesquisa = self.request.GET.get('pesquisa', None)
        queryset = Veiculo.objects.all()
        if pesquisa is not None:
          queryset = queryset.filter(modelo__icontains=pesquisa)  
        return queryset
    
class FotoVeiculo(LoginObrigatorio):

    """
    View para retornar a foto dos veiculos.
    """

    def get(self, request, arquivo):
        try:
            veiculo = Veiculo.objects.get(foto='veiculo/fotos/{}'.format(arquivo))
            return FileResponse(veiculo.foto)
        
        except ObjectDoesNotExist:
            raise Http404("Foto não encontrada ou acesso não autorizado!")
        
        except Exception as exception:
            raise exception
        
class CriarVeiculos(LoginObrigatorio, CreateView):

    """
    View para a criação de novos veiculos.
    """

    model = Veiculo
    form_class = FormularioVeiculo
    template_name = 'veiculo/novo.html'
    success_url = reverse_lazy('listar-veiculos')

class EditarVeiculos(LoginObrigatorio, UpdateView):

    """
    View para editar veiculos ja cadastrados.
    """
    
    model = Veiculo
    form_class = FormularioVeiculo
    template_name = 'veiculo/editar.html'
    success_url = reverse_lazy('listar-veiculos')

class DeletarVeiculo(LoginObrigatorio, DeleteView):

    """
    View para deletar veiculos.
    """

    model = Veiculo
    template_name = 'veiculo/deletar.html'
    success_url = reverse_lazy('listar-veiculos')

class APIListarCriarVeiculos(ListCreateAPIView):

    serializer_class = SerializadorVeiculo
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Veiculo.objects.all()

class APIObterEditarDeletarVeiculos(RetrieveUpdateDestroyAPIView):
    
    serializer_class = SerializadorVeiculo
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Veiculo.objects.all()