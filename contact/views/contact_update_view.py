from django.shortcuts import render, get_object_or_404,redirect
from django.db.models import Q ### para utilizar o operador logico OR
from django.urls import reverse 
from contact.forms import ContactForm
from contact.models import Contact
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required(login_url='contact:login')
def update(request, contact_id):
    contact = get_object_or_404(
        Contact, 
        pk=contact_id, 
        show=True,
        owner=request.user)
    form_action = reverse('contact:update', args= (contact_id,))

    if request.method == 'POST':
        form = ContactForm(
            request.POST,
            request.FILES,
            instance=contact) # formulario postado
        context ={
            'form': form,
            'form_action': form_action,
        }
        if form.is_valid():
            contact = form.save()
            messages.success(request, 'Contato atualizado com sucesso')
            return redirect('contact:update',contact_id=contact.id)
        
        return render(
            request,
            'contact/create.html',
            context,
        )
    context ={
            'form': ContactForm(instance=contact),
            'form_action': form_action,
        }
    return render(
        request,
        'contact/create.html',
        context,   
    )

