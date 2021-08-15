from django.forms import forms
from vocapp.models import word
from django.http.response import HttpResponse
from django.shortcuts import render,redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView,FormView
from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.contrib.auth import login

from django.contrib.auth.views import LoginView

from django.urls import reverse_lazy
from .models import word



class CustomLoginView(LoginView):
    template_name = "vocapp/login.html"
    fields = "__all__"
    redirect_authenticated_user = True
    
    def get_success_url(self):
        return reverse_lazy("words")
    
class RegisterPage(FormView):
    template_name = "vocapp/register.html"
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('words')
    
    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)
    
    def get(self, *arg, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('words')
        return super(RegisterPage, self).get(*arg, **kwargs)
    
    

class WordList(LoginRequiredMixin,ListView):
    model = word
    template_name = "vocapp/words_list.html"
    context_object_name = "words"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['words'] = context['words'].filter(user=self.request.user)
        context['count'] = context['words'].filter(mastered=False).count()
        
        search_input = self.request.GET.get('search_area') or ''
        if search_input:
            context['words'] = context['words'].filter(
                wordname__startswith=search_input
            )
            context['search_input'] = search_input
        return context
    
    
class WordDetail(LoginRequiredMixin,DetailView):
    model = word
    template_name = "vocapp/word.html"
    context_object_name = "word"
    
    
class WordCreate(LoginRequiredMixin,CreateView):
    model = word
    fields = ('wordname', 'synonyme', 'category', 'sense', 'mastered')
    success_url = reverse_lazy('words')
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(WordCreate, self).form_valid(form)
    
class WordUpdate(LoginRequiredMixin,UpdateView):
    model = word
    fields = ('wordname', 'synonyme', 'category', 'sense', 'mastered')    
    success_url = reverse_lazy('words')
    

class WordDelete(LoginRequiredMixin,DeleteView):
    model = word
    context_object_name = "word"
    success_url = reverse_lazy('words')