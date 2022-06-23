from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.views.generic import CreateView, ListView, TemplateView, DetailView

from .forms import CarCreationForm
from .models import Car


class DashboardView(TemplateView):
    template_name = 'accounts/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super(DashboardView, self).get_context_data(**kwargs)

        if not self.request.user.is_authenticated:
            context['login_form'] = AuthenticationForm()
            context['registration_form'] = UserCreationForm()

        return context


class SignUpView(CreateView):
    template_name = 'base.html'
    form_class = UserCreationForm
    
    def get_context_data(self, **kwargs):
        context = super(SignUpView, self).get_context_data(**kwargs)
        context.pop('form')
        context['registration_form'] = self.get_form()
        return context

    def form_valid(self, form):
        form.save()
        login(self.request, authenticate(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password1']
        ))
        return redirect('dashboard')
  

class SignInView(LoginView):
    template_name = 'base.html'
    next_page = '/'
    
    def get_context_data(self, **kwargs):
        context = super(SignInView, self).get_context_data(**kwargs)
        context.pop('form')
        context['login_form'] = self.get_form()
        return context


class CarCreateView(CreateView):
    model = Car
    form_class = CarCreationForm
    template_name = 'accounts/car_create.html'
    success_url = 'dashboard'


class CarDetailView(DetailView):
    model = Car
    template_name = 'accounts/car_detail.html'


class CarListView(ListView):
    model = Car
    template_name = 'accounts/car_list.html'
