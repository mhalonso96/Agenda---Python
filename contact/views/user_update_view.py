from django.shortcuts import render, redirect
from contact.forms import RegisterUpdateForm
from django.contrib.auth.decorators import login_required


@login_required(login_url='contact:login')
def user_update(request):
    form = RegisterUpdateForm(instance=request.user)

    if request.method != 'POST':

        return render(
            request,
            'contact/register_update.html',
            {
                'form': form
            }    
        )
    form = RegisterUpdateForm(data=request.POST, instance= request.user)

    if not form.is_valid():
        return render(
            request,
            'contact/register_update.html',
            {
                'form': form
            }    
        )
    form.save()
    return redirect('contact:login')