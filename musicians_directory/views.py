from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, ListView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.models import User
from . import forms
from django.contrib import messages
from django.urls import reverse_lazy
from album.models import Album
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


class HomeView(ListView):
    template_name = 'home.html'
    queryset = Album.objects.all()
    
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     album = Album.objects.all()
    #     print(album)
    #     context['albums'] = Album.objects.all()
    #     return context
    
class UserRegisterView(CreateView):
    template_name = 'auth.html'
    model = User
    form_class = forms.UserRegistrationForm
    success_url = reverse_lazy('register')
    
    def form_valid(self, form):
        messages.success(self.request, 'Account Created Successfully!')
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = 'Register'
        return context
    

class UserLoginView(LoginView):
    template_name = 'auth.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = 'Login'
        return context
    
    def form_valid(self, form):
        messages.success(self.request, 'Logged in Successfully!')
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.warning(self.request, 'Invalid Username Or Password!')
        return super().form_invalid(form)
    
    def get_success_url(self):
        return reverse_lazy("home")
    
@method_decorator(login_required, name="dispatch")
class UserProfileView(TemplateView):
    template_name = "profile.html"