from audioop import reverse

from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy

from account.forms import UserUpdateForm, UserRegisterForm
from women.models import Women
from django_email_verification import send_email


class SingInView(LoginView):
    template_name = 'account/registration/login.html'

    def get_success_url(self):
        return reverse_lazy('women:index')


def log_out(request):
    logout(request)
    return redirect(reverse_lazy('women:index'))


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password1']
            user = User.objects.create(username=username, email=email, password=password, is_active=False)
            # send_email(user)
            # return redirect('/account/email-verification-sent/')
    else:
        form = UserRegisterForm()
    return render(request, 'account/registration/register.html', {'form': form})


@login_required
def dashboard(request):
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('account:dashboard')
    else:
        form = UserUpdateForm(instance=request.user)

    return render(request, 'account/dashboard/profile.html', {'form': form})


@login_required
def profile_posts(request):
    posts = Women.published.filter(user=request.user)
    return render(request, 'account/dashboard/posts.html', {'posts': posts})
