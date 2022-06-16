from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView

from .forms import CarCreationForm
from .models import Car, Service


class SignUpView(CreateView):
    template_name = 'base.html'
    form_class = UserCreationForm
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
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
        context = super().get_context_data(**kwargs)
        context.pop('form')
        context['login_form'] = self.get_form()
        return context


class CarCreate(CreateView):
    template_name = 'base.html'
    form_class = CarCreationForm
    success_url = 'dashboard'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.pop('form')
        context['car_form'] = self.get_form()
        return context


class DashboardView(TemplateView):
    template_name = 'base.html'
    
    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)
    
    def get_context_data(self, **kwargs):
        context = super(DashboardView, self).get_context_data(**kwargs)
        user = self.request.user
        
        if user.is_authenticated:
            try:
                context['car'] = user.car
                context['orders_in_progress'] = user.car.get_orders(
                    is_completed=False)
                context['completed_orders'] = user.car.get_orders(
                    is_completed=True)
            except Car.DoesNotExist:
                context['car_form'] = CarCreationForm()
            context['services'] = Service.objects.all()
        else:
            context['login_form'] = AuthenticationForm()
            context['registration_form'] = UserCreationForm()
        
        return context
