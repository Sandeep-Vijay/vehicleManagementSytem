from django import forms
from VMSapp.models import Vms 

class CarCreateForm(forms.ModelForm):
    class Meta:
        model=Vms
        fields=[
            'carname','fueltype','carnumber','model'
        ]
        widgets={
            'carname':forms.TextInput(attrs={'class':'form-control'}),
            'fueltype':forms.TextInput(attrs={'class':'form-control'}),
            'carnumber':forms.TextInput(attrs={'class':'form-control'}),
            'model':forms.TextInput(attrs={'class':'form-control'}),


        }