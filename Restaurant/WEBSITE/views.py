from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.contrib import messages
from .forms import SignUpForm, Reservetableform, UpdateUserForm, CustomerFeedbackForm
from .models import *
from django.contrib.auth.models import User

# Create your views here.

def home(request):
    products = Product.objects.all()
    return render(request, 'home.html',{'products':products})

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, ('Hi welcome!'))
            return redirect('home')
        else:
            messages.success(request, ('Invalid username or password! Please try again.'))
            return redirect('login')
    else:
        return render(request, 'login.html',{})
    
def logout_user(request):
    logout(request)
    messages.success(request, ('Thank you for stopping by!See yah!'))
    return redirect('home')

def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ('Registration succcess! You are now logged in.'))
            return redirect('home')
        else:
            messages.success(request, ('Something is wrong with your registration, Please try again!'))
            return redirect('register')
    else:
        form=SignUpForm()
        return render(request, 'register.html', {'form': form})
    
def about(request):
    return render(request, 'about.html',{})


def reservation(request):
    
    if request.method == 'POST':
        form = Reservetableform(request.POST)
        if form.is_valid():
            reserve = form.save(commit=False)
            reserve.created_by = request.user
            reserve.save()
            reserved_table = Reservation.objects.all()
            messages.success(request, ('We will contact you shortly!'))
            return render(request,'schedule.html', {'form': form, 'reserved_table': reserved_table})
        else: 
            return redirect('profile')
    else:
        form = Reservetableform()
    return render(request, 'reservations.html', {'form': form}) 

def contact(request):
    if request.method == 'POST':
        form = CustomerFeedbackForm(request.POST)
        if form.is_valid():
            feedback_msg = form.save(commit=False)
            feedback_msg.save()
            messages.success(request, ('Thank you for the feedback, we are making sure that our customer\' feedback will be heard!'))
            return render(request,'contactus.html', {'form': form})
        else:
            messages.success(request, ('Invalid format please try again.'))
            return redirect('contactpage')
    return render(request, 'contactus.html',{}) 



def user_profile(request):
    if request.user.is_authenticated:
        reserved_table = Reservation.objects.all()
        return render(request, 'profile.html', {'reserved_table': reserved_table})
    else:
        return redirect('home')

def update_user(request):
    if request.user.is_authenticated:
        current_user = User.objects.get(id=request.user.id)
        update_form = UpdateUserForm(request.POST or None, instance = current_user)
        if update_form.is_valid():
            update_form.save()
            login(request, current_user)
            messages.success(request,("You have updated your profile!"))
            return redirect('profile')
        return render(request, 'update_user.html', {'update_form': update_form})
    else:
        messages.success(request,("You must be logged in first!"))
        return redirect('home')

def delete_user(request, pk):
    if request.user.is_authenticated:
        delete_user = User.objects.get(id=pk)
        delete_user.delete()
        messages.success(request, "Record is deleted successfully.")
        return redirect('home')
    else:
        messages.success(request, "You must be logged in to delete the record!")
        return redirect('home')
    
def delete_reserve(request, pk):
    if request.user.is_authenticated:
            delete_reserve = Reservation.objects.get(random_number=pk)
            delete_reserve.delete()
            messages.success(request, "Reservation ticket is deleted successfully.")
            return redirect('profile')
    else:
        messages.success(request, "You must login first!")
        return redirect('profile')

