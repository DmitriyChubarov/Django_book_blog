from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.forms import UserCreationForm

class SignUpView(generic.CreateView):
    success_url = reverse_lazy('login')
    form_class = UserCreationForm
    template_name ="signup.html"
