from django.shortcuts import render, redirect
from .models import User
from .forms import UserForm
# Create your views here.
# def users(request):
#     return render(
#         request,
#         'users/users.html'
        
#     )

def users(request):
    users = User.objects.all()
    context = { 
        'usuarios': users
    }
    return render(request, 'users/users.html', context)


def new_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users')   
    else:
        form = UserForm()
    context = {'form': form}    
    return render(request, 'users/new_user.html', context)        

    
    