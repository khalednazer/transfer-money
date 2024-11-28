from .models import Pay

from django.forms import ModelForm

class Form(ModelForm):
    class Meta:
        model = Pay
        fields='__all__'
        exclude=['cash']


class Ac(ModelForm):
    class Meta:
        model = Pay
        fields = [ 'credit_No', 'crPass']