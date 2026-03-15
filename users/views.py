#from django.contrib.auth import authenticate, login
from django.shortcuts import render,redirect
#from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.views.generic import CreateView, TemplateView, UpdateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import CustomUserCreationForm,CustomUserChangeForm
from .models import CustomUser

def home_view(request):
    return render(request, template_name='home.html')

class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'protectedContent.html'


class RegisterView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'signin.html'
    success_url = reverse_lazy('dashboard')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)  # Авто-вход после регистрации
        return super().form_valid(form)


class ProfileView(LoginRequiredMixin, UpdateView):
    model = CustomUser
    form_class = CustomUserChangeForm
    template_name = 'profile.html'
    success_url = reverse_lazy('dashboard')

    def get_object(self):
        return self.request.user  # Редактируем только текущего пользователя