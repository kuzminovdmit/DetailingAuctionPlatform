from django.contrib.auth.views import LoginView
from django.views.generic import CreateView, ListView, TemplateView, DetailView
from django.urls import reverse_lazy

from .forms import SignUpForm, CarCreationForm
from .models import Car


class DashboardView(TemplateView):
    template_name = 'accounts/dashboard.html'


class SignUpView(CreateView):
    template_name = 'accounts/sign_up.html'
    form_class = SignUpForm
    success_url = reverse_lazy('accounts:sign_in')
  

class SignInView(LoginView):
    template_name = 'accounts/sign_in.html'
    next_page = '/'

    def form_valid(self, form):
        remember_me = form.cleaned_data.get('remember_me')

        if not remember_me:
            self.request.session.set_expiry(0)
            self.request.session.modified = True

        return super(SignInView, self).form_valid(form)


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
