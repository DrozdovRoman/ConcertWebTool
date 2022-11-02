from django import forms
from .models import Concert

class ConcertForm(forms.ModelForm):
    class Meta:
        model = Concert
        fields = '__all__'
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['name'].widget.attrs['class'] = 'form-control mb-3 '
        self.fields['city'].widget.attrs['class'] = 'form-select mb-3 '
        self.fields['concert_date'].widget.attrs['class'] = 'form-control mb-3'
        self.fields['status'].widget.attrs['class'] = 'form-select mb-3'