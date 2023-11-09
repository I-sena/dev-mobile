from django.urls import path
from veiculo.views import FotoVeiculo, ListarVeiculos, CriarVeiculos, EditarVeiculos, DeletarVeiculo, APIListarCriarVeiculos, APIObterEditarDeletarVeiculos

urlpatterns = [
  path('', ListarVeiculos.as_view(), name='listar-veiculos'),
  path('novo/', CriarVeiculos.as_view(), name='criar-veiculo'),
  path('fotos/<str:arquivo>/', FotoVeiculo.as_view(), name='foto-veiculo'),
  path('<int:pk>/', EditarVeiculos.as_view(), name='editar-veiculo'),
  path('deletar/<int:pk>/', DeletarVeiculo.as_view(), name='deletar-veiculo'),
  path('api/', APIListarCriarVeiculos.as_view(), name='api-listar-criar-veiculos'),
  path('api/<int:pk>/', APIObterEditarDeletarVeiculos.as_view(), name='api-obter-editar-deletar-veiculos')
]