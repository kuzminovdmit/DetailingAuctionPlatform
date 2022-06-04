from django.utils import timezone
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required


from .forms import CarCreationForm, ServiceChoiceForm
from .models import Auction, Car, Company, Order, Service, auction_done


def index(request):
    if request.method == 'POST':
        if request.POST.get('button-name') == 'login':
            login_form = UserCreationForm(request.POST)
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return HttpResponseRedirect(reverse('car'))
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
                    login(request, user)
                    return HttpResponseRedirect(reverse('create_car'))
    else:
        registration_form = UserCreationForm()
        login_form = AuthenticationForm()

    context = {
        'login_form': login_form,
        'registration_form': registration_form
    }

    return render(request, 'index.html', context)


@login_required
def create_car(request):
    if request.method == 'POST':
        form = CarCreationForm(request.POST)
        if form.is_valid():
            Car.objects.create(
                client=request.user,
                brand=form.cleaned_data.get('brand'),
                color=form.cleaned_data.get('color'),
                release_year=form.cleaned_data.get('release_year'),
                model=form.cleaned_data.get('model')
            )
            return HttpResponseRedirect(reverse('car'))
    else:
        form = CarCreationForm()
    
    return render(request, 'car_create.html', {'form': form})


@login_required
def car(request):
    try:
        car = Car.objects.get(client__pk=request.user.pk)
    except Car.DoesNotExist:
        return HttpResponseRedirect(reverse('create_car'))
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
                auction = Auction.objects.create(car=car,
                    chosen_service=Service.objects.get(id=form.cleaned_data.get('chosen_service'))
                )
            else:
                auction = None
            return HttpResponseRedirect(reverse('car'))
        else:
            form = ServiceChoiceForm()

        auction = None
    return render(request, 'car.html', {
        'user': request.user,
        'car': car,
        'repair': Service.objects.filter(category=1),
        'maintenance': Service.objects.filter(category=2),
        'auction': auction,
    })