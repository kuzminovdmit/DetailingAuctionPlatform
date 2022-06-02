from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .forms import AccountCreationForm
from .models import Account


def index(request):
    if request.method == 'POST':
      if request.POST.get('button-name') == 'login':
          login_form = UserCreationForm(request.POST)
          username = request.POST.get('username')
          password = request.POST.get('password')
          user = authenticate(username=username, password=password)
          if user:
                login(request,user)
                return HttpResponseRedirect(reverse('account'))
          else:
              return HttpResponse("Invalid login details given")

      else:
          registration_form = UserCreationForm(request.POST)
          if registration_form.is_valid():
            registration_form.save()
            username = registration_form.cleaned_data.get('username')
            password = request.POST.get('password1')
            user = authenticate(username=username, password=password)
            if user:
                login(request,user)
                return HttpResponseRedirect(reverse('create_account'))
    else:
        registration_form = UserCreationForm()
        login_form = AuthenticationForm()

    context = {
        'login_form': login_form,
        'registration_form': registration_form
    }

    return render(request, 'index.html', context)


@login_required
def create_account(request):
    if request.method == 'POST':
        form = AccountCreationForm(request.POST)
        if form.is_valid():
            Account.objects.create(
                user=request.user,
                auto=form.cleaned_data.get('auto'),
                color=form.cleaned_data.get('color'),
                release_year=form.cleaned_data.get('release_year'),
                model=form.cleaned_data.get('model')
            )
            return HttpResponseRedirect(reverse('account'))
    else:
        form = AccountCreationForm()
    
    return render(request, 'create_account.html', {'form': form})


@login_required
def account(request):
    return render(request, 'account.html', {
        'user': request.user,
        'account': Account.objects.get(user__pk=request.user.pk)
    })