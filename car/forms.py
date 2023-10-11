

from django.forms import ModelForm

from car.models import Car


class CarForm(ModelForm):

    class Meta:
        model = Car
        fields = ['model','price']
