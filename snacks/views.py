from typing import List
from django.views.generic import ListView, DetailView
from .models import Snack

# Create your views here.

class SnackListPageView(ListView): 
  template_name = 'snack_list.html'
  model = Snack

class SnackDetailPageView(DetailView): 
  template_name = 'snack_detail.html'
  model = Snack