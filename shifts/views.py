from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import ShiftRequest
from .forms import ShiftRequestForm
from .models import DriverHoliday
from .forms import DriverHolidayForm


@login_required
def shift_create(request):
    if request.user.user_type != 'company':
        return redirect('company_dashboard')

    form = ShiftRequestForm(request.POST or None)
    company_shifts = ShiftRequest.objects.filter(company=request.user).order_by('-start_datetime')

    if request.method == 'POST' and form.is_valid():
        shift = form.save(commit=False)
        shift.company = request.user
        shift.save()

        if 'save_and_new' in request.POST:
            return redirect('shift_create')
        return redirect('company_dashboard')

    return render(request, 'shifts/shift_form.html', {
        'form': form,
        'company_shifts': company_shifts,
    })


@login_required
def shift_view(request, pk):
    shift = get_object_or_404(ShiftRequest, pk=pk, company=request.user)
    return render(request, 'shifts/shift_view.html', {'shift': shift})

@login_required
def shift_edit(request, pk):
    shift = get_object_or_404(ShiftRequest, pk=pk, company=request.user)
    form = ShiftRequestForm(request.POST or None, instance=shift)

    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('shift_create')  # Or 'company_dashboard' if you prefer

    company_shifts = ShiftRequest.objects.filter(company=request.user).order_by('-start_datetime')
    return render(request, 'shifts/shift_form.html', {
        'form': form,
        'company_shifts': company_shifts,
    })


@login_required
def shift_delete(request, pk):
    shift = get_object_or_404(ShiftRequest, pk=pk, company=request.user)
    if request.method == 'POST':
        shift.delete()
        return redirect('shift_create')  # or 'company_dashboard'
    
    # Optional: confirm deletion
    return render(request, 'shifts/shift_confirm_delete.html', {'shift': shift})


@login_required
def holiday_request(request):
    if request.user.user_type != 'driver':
        return redirect('login')

    form = DriverHolidayForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        holiday = form.save(commit=False)
        holiday.driver = request.user
        holiday.save()
        return redirect('driver_dashboard')

    driver_holidays = DriverHoliday.objects.filter(driver=request.user).order_by('-start_date')

    return render(request, 'shifts/holiday_request.html', {
        'form': form,
        'driver_holidays': driver_holidays
    })