from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from shifts.models import ShiftRequest  # Ensure this import exists



def company_signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.user_type = 'company'  # only if you're using a custom user model
            user.save()
            login(request, user)
            return redirect('company_dashboard')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/company_signup.html', {'form': form})


@login_required
def company_dashboard(request):
    if request.user.user_type != 'company':
        return redirect('login')

    company_shifts = ShiftRequest.objects.filter(company=request.user).order_by('-start_datetime')
    return render(request, 'accounts/company_dashboard.html', {
        'company_shifts': company_shifts
    })


@login_required
def driver_dashboard(request):
    if request.user.user_type != 'driver':
        return redirect('login')  # Redirect unauthorized users

    shifts = ShiftRequest.objects.filter(assigned_driver=request.user).order_by('-start_datetime')
    return render(request, 'accounts/driver_dashboard.html', {'shifts': shifts})


def custom_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if user.user_type == 'company':
                return redirect('company_dashboard')
            elif user.user_type == 'driver':
                return redirect('driver_dashboard')
            elif user.user_type == 'agency':
                return redirect('/admin/')  # or a future agency dashboard
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})
