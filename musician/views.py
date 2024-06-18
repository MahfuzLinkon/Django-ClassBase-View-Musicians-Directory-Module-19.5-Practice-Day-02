from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView
from . import forms
from django.urls import reverse_lazy
from django.contrib import messages
from . import models
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

# Create your views here.
@method_decorator(login_required, name="dispatch")
class MusicianCreateView(CreateView):
    model = models.Musician
    template_name = 'musician_form.html'
    form_class = forms.MusicianForm
    success_url = reverse_lazy('musician_create')
    
    def form_valid(self, form):
        messages.success(self.request, "Musician Created Successfully!")
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = 'Create'
        return context
    
@method_decorator(login_required, name="dispatch")
class MusicianEditView(UpdateView):
    model = models.Musician
    template_name = 'musician_form.html'
    form_class = forms.MusicianForm
    success_url = reverse_lazy('home')
    pk_url_kwarg = 'id'
    
    def form_valid(self, form):
        messages.success(self.request, "Musician Updated Successfully!")
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = 'Update'
        return context