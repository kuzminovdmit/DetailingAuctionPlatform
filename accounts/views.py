from django.contrib.auth import login, authenticate
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView, ListView, DetailView
from django.urls import reverse_lazy

from .forms import SignUpForm, CarCreationForm, CompanyCreationForm
from .models import Car, Company, Representative


class SignUpView(CreateView):
    template_name = 'accounts/sign_up.html'
    form_class = SignUpForm
    success_url = reverse_lazy('accounts:choose_account')

    def form_valid(self, form):
        authenticate(
            email=form.cleaned_data.get('email'),
            password=form.cleaned_data.get('password1')
        )
        login(self.request, form.save())
        return super(SignUpView, self).form_valid(form)


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
    success_url = '/'

    def form_valid(self, form):
        form.instance.client = self.request.user.client
        return super(CarCreateView, self).form_valid(form)


class CarDetailView(DetailView):
    model = Car
    template_name = 'accounts/car_detail.html'


class CarListView(ListView):
    model = Car
    template_name = 'accounts/car_list.html'


class CompanyCreateView(CreateView):
    model = Company
    form_class = CompanyCreationForm
    template_name = 'accounts/company_create.html'

    def get_success_url(self):
        Representative.objects.create(
            user=self.request.user,
            company=self.object
        )
        return reverse_lazy('dashboard:main')
