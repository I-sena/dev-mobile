from django.urls import path
from veiculo.views import FotoVeiculo, ListarVeiculos, CriarVeiculos, EditarVeiculos, DeletarVeiculo, APIListarVeiculos

urlpatterns = [
  path('', ListarVeiculos.as_view(), name='listar-veiculos'),
  path('novo/', CriarVeiculos.as_view(), name='criar-veiculo'),
  path('fotos/<str:arquivo>/', FotoVeiculo.as_view(), name='foto-veiculo'),
  path('<int:pk>/', EditarVeiculos.as_view(), name='editar-veiculo'),
  path('deletar/<int:pk>/', DeletarVeiculo.as_view(), name='deletar-veiculo'),
  path('api/', APIListarVeiculos.as_view(), name='api-listar-veiculos')
]