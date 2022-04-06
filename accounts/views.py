import imp
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from .forms import CustomeUserCreationForm
# Create your views here.

class SignUpView(generic.CreateView):
    form_class = CustomeUserCreationForm #UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
