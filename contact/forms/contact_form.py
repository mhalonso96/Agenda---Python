from django import forms
from contact.models import Contact
from django.core.exceptions import ValidationError



class ContactForm(forms.ModelForm):
    first_name = forms.CharField(
        widget= forms.TextInput(
            attrs={
                'placeholder' : 'Digite aqui seu nome' #mesma função, escolher melhor jeito, fazem a mesma coisa
            }
        ),
        help_text= 'Digite o seu primeiro nome',
    )
    last_name = forms.CharField(
        widget= forms.TextInput(
            attrs={
                'placeholder' : 'Digite aqui seu sobrenome' #mesma função, escolher melhor jeito, fazem a mesma coisa
            }
        ),
        help_text= 'Digite o seu sobrenome',
    )
    phone = forms.CharField(
        widget= forms.TextInput(
            attrs={
                'placeholder' : 'Digite aqui seu Telefone' #mesma função, escolher melhor jeito, fazem a mesma coisa
            }
        ),
        help_text= 'Digite o seu telefone EX:111111111',
    )
    picture = forms.ImageField(
        widget= forms.FileInput(
            attrs={
                'accept':'image/*',
                
            }
        ),
        required= False,
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
      #  self.fields['first_name'].widget.attrs.update({
       #     'placeholder' : 'Digite aqui seu primeiro nome' #mesma função, escolher melhor jeito, fazem a mesma coisa
        #})
               
    class Meta:
        model = Contact
        fields = (
            'first_name', 'last_name', 'phone', 'email', 'description', 'category', 'picture',
        )
        #widgets = {
         #   'phone' : forms.TextInput(
          #      attrs= {
            #        'placeholder' : 'Digite seu numero de telefone' #mesma função, escolher melhor jeito, fazem a mesma coisa
           #     }
            #)
        #}
    def clean(self):
        #cleaned_data = self.changed_data

        #self.add_error(
         #   'first_name', ValidationError(
          #      'Mensagem de erro',
           #     code= 'invalid'))
    
        return super().clean()
    
    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')
        
                
        if first_name.isdigit():
            self.add_error(
                'first_name', ValidationError(
                'Verifique o seu nome',
                code= 'invalid'))
        return first_name

    def clean_last_name(self):

        last_name = self.cleaned_data.get('last_name')
        
                
        if last_name.isdigit():
            self.add_error(
                'last_name', ValidationError(
                'Verifique o seu sobrenome',
                code= 'invalid'))
        return last_name    
    
  
    
