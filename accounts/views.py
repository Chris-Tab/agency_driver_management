from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from shifts.models import ShiftRequest
from datetime import timedelta, date
from django.utils import timezone
import calendar



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



def custom_login(request):
    form = AuthenticationForm(request, data=request.POST or None)

    if request.method == 'POST':
        print("Form Submitted")
        print("Form Valid:", form.is_valid())
        print("Errors:", form.errors)

        if form.is_valid():
            user = form.get_user()
            print("User Found:", user)

            login(request, user)

            # ✅ Check user_type attribute
            if hasattr(user, 'user_type'):
                print("User Type:", user.user_type)
                if user.user_type == 'company':
                    return redirect('company_dashboard')
                elif user.user_type == 'driver':
                    return redirect('driver_dashboard')

            # Optional: Redirect superuser/admins
            if user.is_superuser:
                return redirect('/admin/')

            # Fallback if no user_type is set
            return redirect('login')

    return render(request, 'accounts/login.html', {'form': form})



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
        return redirect('login')
    return render(request, 'accounts/driver_dashboard.html')

def custom_logout(request):
    if request.method == "POST" or request.method == "GET":
        logout(request)
        return redirect('login')

def terms_of_use(request):
    return render(request, 'accounts/terms_of_use.html')


def get_week_range(today):
    start = today - timedelta(days=today.weekday())  # Monday
    return [start + timedelta(days=i) for i in range(7)]

def driver_dashboard(request):
    today = timezone.now().date()
    week = get_week_range(today)


    week_days = []
    for day in week:
        week_days.append({
            'date': day,
            'weekday': calendar.day_name[day.weekday()],
            'availability': False,  # Replace with actual logic
            'is_today': day == today
        })

    return render(request, 'accounts/driver_dashboard.html', {
        'week_days': week_days
    })

