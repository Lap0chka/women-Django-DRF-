from audioop import reverse

from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import UpdateView

from account.forms import UserUpdateForm, UserRegisterForm, LoginUserForm
from women.forms import WomenForm
from women.models import Women
from django_email_verification import send_email


class SingInView(LoginView):
    template_name = 'account/registration/login.html'
    form_class = LoginUserForm

    def get_success_url(self):
        return reverse_lazy('account:dashboard')


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
            messages.success(request, f'Account created for {username}')
            return redirect('account:login')
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


@method_decorator(login_required, name='dispatch')
class UpdatePostView(UpdateView):
    model = Women
    form_class = WomenForm
    template_name = 'account/dashboard/update_my_post.html'

    def form_valid(self, form):
        instance = form.save(commit=False)
        categories = form.cleaned_data.pop('cat', None)
        instance.save()
        if categories:
            instance.cat.add(categories)
        messages.success(self.request, 'Your post will be added.')
        return super().form_valid(form)
