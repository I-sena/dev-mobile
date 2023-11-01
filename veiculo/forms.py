from django import forms
from veiculo.models import Veiculo


class FormularioVeiculo(forms.ModelForm):
    class Meta():
        model = Veiculo
        exclude = []