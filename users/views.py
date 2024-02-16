from email import message
from django.shortcuts import redirect, render
from .models import Profil
from django.contrib.auth import authenticate, login, logout
from .forms import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator


# Create your views here.

def profiles(request):
    profile = request.GET.get('q')
    users = Profil.objects.all()

    if profile:
        users = users.filter(name__icontains=profile)

    page_number = request.GET.get('page')
    paginator = Paginator(users, 1)
    users_page = paginator.get_page(page_number)

    max_pages = paginator.num_pages
    current_page = users_page.number
    start_page = max(current_page - 5, 1)
    end_page = min(current_page + 4, max_pages)
    page_numbers = range(start_page, end_page + 1)

    context = {
        "users_page": users_page,
        "page_numbers": page_numbers,
        "max_pages": max_pages,
        "current_page": current_page,
    }
    return render(request, 'users/profiles.html', context)


def profile(request, id):
    user = Profil.objects.get(id=id)
    context = {
        "user": user
    }
    return render(request, 'users/profile.html', context)


def login_user(request):
    if request.user.is_authenticated:
        return redirect('profiles')

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Tizimga hush kelibsiz")
            return redirect('profiles')
        else:
            messages.error(request, 'Bunday login va parol mavjud emas')

    return render(request, "users/login.html")


def logout_user(request):
    logout(request)
    messages.info(request, 'Tizimdan chiqdingiz')
    return redirect('login')


def register_user(request):
    form = CustomUserCreationForm()
    for f in form:
        if f.label == "Password":
            f.label = "Parol"
        elif f.label == "Password confirmation":
            f.label = "Parolni tasdiqlash"

    context = {
        "form": form
    }

    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()

            login(request, user)

            messages.success(request, "Foydalnuvchi ro'yxatdan o'tdi")
            return redirect('profiles')
        else:
            messages.error(request, "Foydalnuvchi ro'yxatdan o'tmadi")

    return render(request, "users/register.html", context)


@login_required(login_url='login')
def account(request):
    profil = request.user.profil
    context = {
        "profil": profil
    }
    return render(request, "users/account.html", context)


@login_required(login_url='login')
def account_edit(request):
    profil = request.user.profil
    form = CustomProfilCreationForm(instance=profil)
    if request.method == "POST":
        form = CustomProfilCreationForm(request.POST, request.FILES, instance=profil)
        if form.is_valid():
            form.save()
            return redirect('account')

    context = {
        "form": form
    }
    return render(request, "users/account_edit.html", context)
