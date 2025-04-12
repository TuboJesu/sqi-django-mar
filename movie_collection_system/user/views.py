from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

# Create your views here.


def signup(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()

            messages.success(request, 'Account Created Successfully')
            return redirect('user:login')
    
    context = {
        'form':form,
    }

    return render(request, 'user/signup.html', context)