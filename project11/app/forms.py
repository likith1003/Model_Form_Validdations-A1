from django import forms
from .models import *

class RegisterForm(forms.ModelForm):
    class Meta:
        model = Register
        fields = '__all__'
    botcatcher = forms.CharField(required=False, widget=forms.HiddenInput)
    
    def clean_pno(self):
        pno = self.cleaned_data.get('pno')
        if pno.startswith('+91 ') and len(pno) == 14:
            return pno
        return None
    
    def clean_password(self):
        pw = self.cleaned_data.get('password')
        if len(pw) >= 8:
            return pw
        return None
    
    def clean_botcatcher(self):
        data = self.cleaned_data.get('botcatcher')
        if len(data) > 0:
            raise forms.ValidationError('bot found')