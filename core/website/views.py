from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import ListView,FormView,CreateView,TemplateView

# Create your views here.


class IndexView(TemplateView):
    template_name = 'website/index.html'
    