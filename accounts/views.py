from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.views.generic import CreateView, TemplateView

from .forms import CarCreationForm
from .models import Car


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
    template_name = 'base.html'
    form_class = CarCreationForm
    success_url = 'dashboard'
    
    def get_context_data(self, **kwargs):
        context = super(CarCreateView, self).get_context_data()
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
            except Car.DoesNotExist:
                context['car_form'] = CarCreationForm()
            # context['services'] = Service.objects.all()
            # context['auction_create_form'] = AuctionCreationForm()
        else:
            context['login_form'] = AuthenticationForm()
            context['registration_form'] = UserCreationForm()
        
        return context
