from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.views.generic import CreateView, ListView, TemplateView

from .forms import CarCreationForm, AuctionCreationForm
from .models import Car, Service, Auction, Order


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


class AuctionCreateView(CreateView):
    template_name = 'car_service.html'
    form_class = AuctionCreationForm
    success_url = 'auction_list'

    def form_valid(self, form):
        form.instance.car = self.request.user.car
        return super(AuctionCreateView, self).form_valid(form)


class AuctionListView(ListView):
    model = Auction
    context_object_name = 'auctions'
    template_name = 'auction_list.html'
    queryset = Auction.objects.filter(is_company_chosen=False)


class OrderListView(ListView):
    model = Order
    context_object_name = 'orders'
    template_name = 'order_list.html'

    def get_queryset(self):
        status = self.kwargs.get('status')
        is_completed = False

        if status == 'in_progress':
            is_completed = False
        elif status == 'completed':
            is_completed = True

        return super(OrderListView, self).get_queryset().filter(
            auction__car=self.request.user.car,
            is_completed=is_completed
        )

    def get_context_data(self, **kwargs):
        context = super(OrderListView, self).get_context_data()
        context['is_completed'] = self.kwargs.get('is_completed', False)
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
            context['services'] = Service.objects.all()
            context['auction_create_form'] = AuctionCreationForm()
        else:
            context['login_form'] = AuthenticationForm()
            context['registration_form'] = UserCreationForm()
        
        return context
