#from django.views.generic.list import ListView
#from django.views.generic.detail import DetailView
#from django.views.generic.edit import CreateView, UpdateView, DeleteView
#from django.contrib.admin.views.decorators import staff_member_required
#from django.utils.decorators import method_decorator
#from django.urls import reverse, reverse_lazy
from django.shortcuts import render, get_object_or_404
from .models import Page
#from .forms import PageForm

def page(request, page_id, page_slug):
    page = get_object_or_404(Page, id=page_id)
    return render(request, 'pages/privacy.html', {'page':page})