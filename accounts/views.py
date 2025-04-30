from shifts.models import ShiftRequest
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import CompanySignUpForm
from django.contrib.auth.decorators import login_required

def company_signup(request):
    if request.method == 'POST':
        form = CompanySignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # automatically log in after signup
            return redirect('company_dashboard')
    else:
        form = CompanySignUpForm()
    return render(request, 'accounts/company_signup.html', {'form': form})

@login_required
def company_dashboard(request):
    if request.user.user_type != 'company':
        return redirect('login')  # or show error
    return render(request, 'accounts/company_dashboard.html')

@login_required
def driver_dashboard(request):
    if request.user.user_type != 'driver':
        return redirect('login')  # only drivers allowed

    shifts = ShiftRequest.objects.filter(assigned_driver=request.user).order_by('-start_datetime')
    return render(request, 'accounts/driver_dashboard.html', {'shifts': shifts})