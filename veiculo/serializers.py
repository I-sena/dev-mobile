import base64
from rest_framework import serializers
from veiculo.models import Veiculo

class SerializadorVeiculo(serializers.ModelSerializer):
    """
    serializador para o model veiculo
    """

    marca_display = serializers.SerializerMethodField()
    cor_display = serializers.SerializerMethodField()
    combustivel_display = serializers.SerializerMethodField()
    foto = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Veiculo
        exclude = []
    

    def get_marca_display(self, instancia):
        return instancia.get_marca_display()
    
    def get_cor_display(self, instancia):
        return instancia.get_cor_display()

    def get_combustivel_display(self, instancia):
        return instancia.get_combustivel_display()

    def get_foto(self, instancia):
        if instancia.foto:
            resultado = base64.b64encode(instancia.foto.read())
            return "data:image/jpeg;base64,{}".format(
                resultado.decode('utf-8')
            )
        return None