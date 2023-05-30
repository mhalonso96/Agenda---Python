from django.shortcuts import render, get_object_or_404, redirect
from contact.forms import RegisterForm
from django.contrib import messages

from django.contrib.auth.decorators import login_required
def register (request):
    form = RegisterForm()
    #messages.info(request, 'Texto de info') #messages.success(request, 'Texto de sucess') #messages.error(request, 'Texto de erro') #messages.warning(request, 'Texto de warning')

    if request.method == 'POST':
        form = RegisterForm(
            request.POST,
        )
        if form.is_valid():
            form.save()
            messages.success(request, 'Usuario registrado com sucesso')
            return redirect('contact:index')
            
    return render(
        request,
        'contact/register.html',
        {
            'form':form
        },
    )