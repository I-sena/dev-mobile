from django import forms
from anuncio.models import Anuncio


class FormularioAnuncio(forms.ModelForm):

    """
    Formulario para o model Anuncio
    """
    class Meta():
        model = Anuncio
        exclude = []