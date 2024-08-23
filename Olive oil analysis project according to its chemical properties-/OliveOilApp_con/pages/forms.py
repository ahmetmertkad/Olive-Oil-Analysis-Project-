from django import forms
from .models import OliveOil

class OliveOilForm(forms.ModelForm):
    class Meta:
        model = OliveOil
        fields = [
            'name',
            'oil_type',
            'acidity',
            'peroxide_value',
            'k232',
            'k270',
            'delta_k',
            'total_polyphenols',
            'moisture_and_volatiles',
            'pyropheophytins',
            'dag_content',
        ]