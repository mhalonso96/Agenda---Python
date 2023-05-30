from django.shortcuts import render, get_object_or_404,redirect
from django.db.models import Q ### para utilizar o operador logico OR
from django.urls import reverse 
from contact.forms import ContactForm
from contact.models import Contact
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required(login_url='contact:login')
def delete(request, contact_id):
    contact = get_object_or_404(
        Contact, 
        pk=contact_id, 
        show=True,
        owner=request.user
        )
    
    confirmation = request.POST.get('confirmation', 'no')
    print('confirmation: ', confirmation)

    if confirmation == 'yes':
        contact.delete()
        messages.success(request, 'Contato deletado com sucesso')
        return redirect('contact:index')
    
    return render(
        request, 'contact/contact.html',
        {
            'contact':contact,
            'confirmation': confirmation,
        }
    )