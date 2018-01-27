from django.shortcuts import render, redirect
#from django.contrib.auth.forms import UserCreationForm
from accounts.forms import(
    RegistrationForm,
    EditProfileForm,
)
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.urls import reverse

#@login_required


# def home(request):
#     numbers = [1, 2, 3, 4, 5]
#     name = 'Max Goodridge'

#     context = {
#         'myName': name,
#         'numbers': numbers
#     }

#     return render(request, 'accounts/home.html', context)


def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect(reverse('accounts:login'))

    else:
        form = RegistrationForm()
        context = {
            'form': form
        }
        return render(request, 'accounts/reg_form.html', context)


#@login_required
def view_profile(request, pk=None):
    if pk:
        user = User.objects.get(pk=pk)
    else:
        user = request.user
    args = {
        'user': user
    }
    return render(request, 'accounts/profile.html', args)


#@login_required
def edit_profile(request):
    if request.method == "POST":
        form = EditProfileForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect(reverse('accounts:view_profile'))

    else:
        form = EditProfileForm(instance=request.user)
        context = {
            'form': form
        }
        return render(request, 'accounts/edit_profile.html', context)


#@login_required
def change_password(request):
    if request.method == "POST":
        form = PasswordChangeForm(data=request.POST, user=request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect(reverse('accounts:view_profile'))
        else:
            return redirect(reverse('accounts:change_password'))

    else:
        form = PasswordChangeForm(user=request.user)

        args = {
            'form': form
        }

        return render(request, 'accounts/change_password.html', args)


def ch_ps(request):
    if request.method == "GET":
        form = PasswordChangeForm(user=request.user)

        args = {
            'form': form
        }

        return render(request, 'accounts/change_password.html', args)
