from django import forms
from django.core.exceptions import ValidationError

class NameDateForm(forms.Form):
    DATE_INPUT_FORMATS = ['%d/%m/%Y','%d%m%Y']
    name = forms.CharField(label='Nome', max_length=100)
    dt_nasc = forms.DateField(label='Data de Nascimento',input_formats=DATE_INPUT_FORMATS)


    def clean_name(self):
        data = self.cleaned_data['name']
        if (len(data)<3):
            raise ValidationError("O nome deve conter mais de três caracteres")

        return data

