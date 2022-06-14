from django import forms
from django.core.exceptions import ValidationError

class NameDateForm(forms.Form):
    DATE_INPUT_FORMATS = ['%d/%m/%Y']
    name = forms.CharField(label='Seu nome', max_length=100, required=False)
    dt_nasc = forms.DateField(label='Data de Nascimento', required=False,input_formats=DATE_INPUT_FORMATS)

    def clean_name(self):
        data = self.cleaned_data['name']
        if (len(data)<3):
            raise ValidationError("O nome deve conter mais de três caracteres")

        return data