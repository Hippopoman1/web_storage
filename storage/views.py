from django.shortcuts import render,redirect

# Create your views here.

from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm
from .models import User

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])  # Hash password
            user.save()
            return redirect('login')  # Redirect ไปหน้า Login หลังจากสมัครเสร็จ
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            password = form.cleaned_data['password']
            try:
                user = User.objects.get(name=name)
                if user.check_password(password):
                    request.session['user_id'] = user.id  # Save user session
                    return redirect('home')  # Redirect ไปหน้า Home
                else:
                    form.add_error('password', 'Invalid password')
            except User.DoesNotExist:
                form.add_error('name', 'User not found')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def home_view(request):
    user_id = request.session.get('user_id')
    if user_id:
        user = User.objects.get(id=user_id)
        return render(request, 'home.html', {'user': user})
    return redirect('login')


def logout_view(request):
    request.session.flush()  # Clear user session
    return redirect('login')