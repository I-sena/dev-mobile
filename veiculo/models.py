from django.db import models
from datetime import datetime
from veiculo.consts import OPCOES_MARCAS, OPCOES_CORES, OPCOES_COMBUSTIVEIS


# Create your models here.
class Veiculo(models.Model):
    marca = models.PositiveSmallIntegerField(choices=OPCOES_MARCAS)
    modelo = models.CharField(max_length=100)
    ano = models.IntegerField()
    cor = models.SmallIntegerField(choices=OPCOES_CORES)
    foto = models.ImageField(blank=True, null=True, upload_to='veiculo/fotos')
    combustivel = models.SmallIntegerField(choices=OPCOES_COMBUSTIVEIS)

    @property # Se comporta como um atributo mas nao fica na base de dados
    def veiculo_novo(self):
        return self.ano == datetime.now().year
    
    def __str__(self):
        return '{0} - {1} ({2}/{3})'.format(
            self.marca,
            self.modelo,
            self.ano,
            self.get_cor_display()
        )
    

    def ano_de_uso(self):
        return datetime.now().year - self.ano