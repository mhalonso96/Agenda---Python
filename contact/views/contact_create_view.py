from django.shortcuts import render, get_object_or_404,redirect
from django.db.models import Q ### para utilizar o operador logico OR
from django.urls import reverse 
from contact.forms import ContactForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required(login_url='contact:login')
def create(request):
    form_action = reverse('contact:create')
    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES) # formulario postado
        context = {
            'form': form,
            'form_action': form_action,
        }
        if form.is_valid():
            contact = form.save(commit=False)
            contact.owner = request.user
            contact.save()
            messages.success(request, 'Contato criado com sucesso')
            return redirect('contact:update',contact_id=contact.id)
        
        return render(
            request,
            'contact/create.html',
            context,
        )
    context ={
            'form': ContactForm(),
            'form_action': form_action,
        }
    return render(
        request,
        'contact/create.html',
        context,   
    )

