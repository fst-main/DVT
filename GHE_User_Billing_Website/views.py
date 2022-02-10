from unicodedata import name
from django.shortcuts import render, redirect
from DVT_api.models import EventApp
from django.http import HttpResponseRedirect
from .forms import UserForm

def update_user(request, user_id):
    user = EventApp.objects.get(pk=user_id)
    form = UserForm(request.POST or None, instance = user)
    if form.is_valid():
        form.save()
        return redirect('list-users')
    else:
        render(request,
        'update_user.html',
                    {'user' : user, 'form' : form})



def search_user(request):
    if request.method == "POST":
        searched = request.POST['searched']
        users = EventApp.objects.filter(name__contains=searched)

        return render(request,
        'search_user.html',
                    {'searched' : searched, 'users' : users})
    else:
        return render(request,
        'search_user.html',
                    {})
        
def show_user(request, user_id):
    user = EventApp.objects.get(pk = user_id)
    return render(request, 'show_user.html',
                    {'user' : user})

def add_users_manually(request):
    submitted = False
    if request.method =="POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add-users?submitted=True')
    else:
        form = UserForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'add_users_manually.html',  
                    {'form' : form, 'submitted' : submitted})

def all_users(request):
    user_list = EventApp.objects.all()
    return render(request, 'user_list.html',
                    {'user_list' : user_list})

def home(request):
    return render(request, 'home.html', {})