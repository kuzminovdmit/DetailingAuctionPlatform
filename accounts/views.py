from django.contrib.auth import login, authenticate
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView
from django.urls import reverse_lazy
from django.shortcuts import redirect

from .forms import SignUpForm, CarCreationForm, CompanyCreationForm
from .models import Client, Car, Company, Representative


class SignUpView(CreateView):
    template_name = 'accounts/sign_up.html'
    form_class = SignUpForm
    success_url = reverse_lazy('accounts:choose_account')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user, backend='django.contrib.auth.backends.ModelBackend')

        return redirect(self.success_url)


class SignInView(LoginView):
    template_name = 'accounts/sign_in.html'
    next_page = '/'

    def form_valid(self, form):
        remember_me = form.cleaned_data.get('remember_me')

        if not remember_me:
            self.request.session.set_expiry(0)
            self.request.session.modified = True

        return super(SignInView, self).form_valid(form)


class CarListView(ListView):
    model = Car
    template_name = 'accounts/car_list.html'


class CarDetailView(DetailView):
    model = Car
    template_name = 'accounts/car_detail.html'


class CarCreateView(CreateView):
    model = Car
    form_class = CarCreationForm
    template_name = 'accounts/car_create.html'
    success_url = '/'

    def form_valid(self, form):
        client = Client.objects.create(user=self.request.user)
        form.instance.client = client
        return super(CarCreateView, self).form_valid(form)


class CarUpdateView(UpdateView):
    model = Car
    form_class = CarCreationForm
    template_name = 'accounts/car_update.html'
    success_url = '/'


class CarDeleteView(DeleteView):
    model = Car
    success_url = reverse_lazy('dashboard:main')


class CompanyListView(ListView):
    model = Company
    template_name = 'accounts/company_list.html'


class CompanyDetailView(DetailView):
    model = Company
    template_name = 'accounts/company_detail.html'


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


class CompanyUpdateView(UpdateView):
    model = Company
    form_class = CompanyCreationForm
    template_name = 'accounts/company_update.html'
    success_url = '/'


class CompanyDeleteView(DeleteView):
    model = Company
    success_url = reverse_lazy('dashboard:main')
