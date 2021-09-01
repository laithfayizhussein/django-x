
from django.urls.base import reverse_lazy
from django.views.generic import ListView , DetailView , CreateView , DeleteView ,UpdateView
from django.urls import reverse_lazy
from .models import Myapp
# Create your views here.

class MyappListView (ListView):
    template_name = 'myapp/Myapp-list.html'
    model = Myapp
    
class MyappDetailView (DetailView):
    template_name = 'myapp/Myapp-detail.html'
    model = Myapp
    
class MyappCreateView (CreateView):
    template_name = 'myapp/Myapp-create.html'
    model = Myapp
    fields = ['name','description','purchaser']
    
class MyappUpdateView (UpdateView):
    template_name = 'myapp/Myapp-update.html'
    model = Myapp
    fields = ['name ','description','purchaser']

    
class MyappDeleteView (DeleteView):
    template_name = 'myapp/Myapp-delete.html'
    model = Myapp
    success_url =reverse_lazy("myapp_list")
    
    
