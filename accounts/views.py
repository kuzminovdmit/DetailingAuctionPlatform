from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from django.utils import timezone
from django.urls import reverse_lazy


from .forms import CarCreationForm, ServiceChoiceForm
from .models import Auction, Car, Company, Order, Service, auction_done



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
            except Car.DoesNotExist:
                context['car_form'] = CarCreationForm()
        else:
            context['login_form'] = AuthenticationForm()
            context['registration_form'] = UserCreationForm()
        
        return context


def car(request):
    try:
        car = request.user.car
    except Car.DoesNotExist:
        return redirect('create_car')
    try:
        auction = Auction.objects.get(car=car)
        if auction.timer_end() < timezone.now():
            auction_done.send(Auction, instance=auction, created=True)
        if auction.is_finished and auction.order_set.count() == 0:
            Order.objects.create(
                auction=auction,
                company=Company.objects.get(id=1),
                cost=3000
            )
    except Auction.DoesNotExist:
        if request.method == 'POST':
            form = ServiceChoiceForm(request.POST)
            if form.is_valid():
                auction = Auction.objects.create(
                    car=car,
                    chosen_service=Service.objects.get(
                        id=form.cleaned_data.get('chosen_service')
                    )
                )
            else:
                auction = None
            return redirect('car')
        else:
            form = ServiceChoiceForm()

        auction = None
    
    return render(request, 'car.html', {
        'repair': Service.objects.filter(category=1),
        'maintenance': Service.objects.filter(category=2),
        'auction': auction,
    })