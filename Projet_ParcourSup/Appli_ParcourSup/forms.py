from django import forms
from .models import Formation
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

class FormationForm(forms.ModelForm):
    class Meta:
        model = Formation
        fields = ['nom', 'description', 'duree', 'etablissement', 'image']

class CustomUserCreationForm(UserCreationForm):
    status = forms.ChoiceField(choices=Profile.STATUS_CHOICES)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'status']

    def save(self, commit=True):
        user = super().save(commit)
        profile = Profile(user=user, status=self.cleaned_data['status'])
        if commit:
            profile.save()
        return user
