from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import CrimeReport
from .models import Complaint

class ComplaintForm(forms.ModelForm):
    class Meta:
        model = Complaint
        fields = ['title', 'description']

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
    
    def save(self, commit=True):
        user = super(CustomUserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

class NewComplaintForm(forms.ModelForm):
    class Meta:
        model = CrimeReport
        fields = ['title', 'description', 'category']
class ComplaintForm(forms.ModelForm):
    class Meta:
        model = Complaint # type: ignore
        fields = ['title', 'description']
