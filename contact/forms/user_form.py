from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django import forms

class RegisterForm (UserCreationForm):
    first_name= forms.CharField(
        required= True,
        min_length= 3,
        error_messages= {
            'required' : 'Campo Obrigatório'
        } 
    )
    last_name= forms.CharField(
        required= True,
        min_length= 3
    )
    email= forms.EmailField(
        required= True,
    )
    
    class Meta:
        model= User
        fields= (
           'first_name', 'last_name', 'email',
           'username', 'password1', 'password2', 
        )
    def clean_email(self):
        email= self.cleaned_data.get('email')


        if User.objects.filter(email=email).exists():
            self.add_error(
                'email',
                ValidationError(
                'Email ja cadastrado',
                code= 'invalid',
                )

            )
        return email
