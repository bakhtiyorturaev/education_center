from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import Profil, Skill


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password1', 'password2']
        labels = {
            'first_name': "Ism",
            'last_name': "Familiya",
            'email': "Elektron manzil",
            'username': "Login"
        }

    def __init__(self, *args, **kwargs):
        super(ModelForm, self).__init__(*args, **kwargs)

        for key, field in self.fields.items():
            field.widget.attrs.update({"class": "input input--text"})


class CustomProfilCreationForm(ModelForm):
    class Meta:
        model = Profil
        fields = ['name', 'email', 'info', 'location', 'bio', 'social_github', 'social_linkedin', 'social_youtube',
                  'social_instagram', 'social_telegram', 'image']

    def __init__(self, *args, **kwargs):
        super(ModelForm, self).__init__(*args, **kwargs)

        for key, field in self.fields.items():
            field.widget.attrs.update({"class": "input input--text"})


class SkillCreationForm(ModelForm):
    class Meta:
        model = Skill
        fields = ['name', 'description']
        labels = {
            'name': 'Malaka nomi',
            'description': 'Tavsif'
        }
