from django.shortcuts import render
from django.http import HttpResponse

from blog.models import Entry
# Create your views here.

def index(request):
    entries = Entry.objects.order_by('-date')
    
    return render(request, 'blog/index.html', locals())