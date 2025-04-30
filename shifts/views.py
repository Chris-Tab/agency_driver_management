from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ShiftRequestForm

@login_required
def shift_create(request):
    if request.user.user_type != 'company':
        return redirect('company_dashboard')  # Only companies can submit shift requests

    if request.method == 'POST':
        form = ShiftRequestForm(request.POST)
        if form.is_valid():
            shift = form.save(commit=False)
            shift.company = request.user
            shift.save()
            if 'save_and_new' in request.POST:
                return redirect('shift_create')  # Save and New
            else:
                return redirect('company_dashboard')  # Normal Save
    else:
        form = ShiftRequestForm()

    return render(request, 'shifts/shift_form.html', {'form': form})
