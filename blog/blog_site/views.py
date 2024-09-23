from django.shortcuts import render,get_object_or_404,redirect
from api.models import BlogModel
from .forms import BlogForm,UserRegistrationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
# Create your views here.
def home(request):
    blogs=BlogModel.objects.all().order_by('-created_at')
    return render(request,'index.html',{'blogs':blogs})


@login_required
def blog_create(request):
    if request.method == "POST":
        form = BlogForm(request.POST,request.FILES)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.user=request.user
            blog.save()
            return redirect('homepage')
    else:
        form = BlogForm()
    return render(request,'blog_form.html',{'form':form})

@login_required
def blog_edit(request,blog_id):
    blog = get_object_or_404(BlogModel,pk=blog_id,user = request.user)
    if request.method == "POST":
        form = BlogForm(request.POST,request.FILES,instance=blog)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.user=request.user
            blog.save()
            return redirect('homepage')    
    else:
        form = BlogForm(instance=blog)
    return render(request,'blog_form.html',{'form':form})

@login_required
def blog_delete(request,blog_id):
    blog=get_object_or_404(BlogModel,pk=blog_id,user=request.user)
    if request.method == "POST":
        blog.delete()
        return redirect('homepage')
    
    return render(request,'blog_confirm_delete.html',{'blog':blog})   

def register(request):
    if request.method == "POST":
        form=UserRegistrationForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            login(request,user)
            return redirect('homepage')
    else:
        form=UserRegistrationForm()
    return render(request,'registration/register.html',{'form':form})