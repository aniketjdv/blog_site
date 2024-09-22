from django.shortcuts import render,get_object_or_404
from api.models import BlogModel
from .forms import BlogForm

# Create your views here.
def home(request):
    blogs=BlogModel.objects.all().order_by('-created_at')
    return render(request,'index.html',{'blogs':blogs})

def create(request):
    pass