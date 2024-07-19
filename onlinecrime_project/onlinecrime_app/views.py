from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from .models import CrimeReport
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .forms import CustomUserCreationForm
from django.contrib.auth import logout
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import CrimeReport
from .forms import NewComplaintForm
from .forms import ComplaintForm
from .models import Complaint

def report_complaint(request):
    if request.method == 'POST':
        form = ComplaintForm(request.POST)
        if form.is_valid():
            form.save()  # Save the form data to the database
            return redirect('success')  # Redirect to a success page
    else:
        form = ComplaintForm()
    
    return render(request, 'report_complaint.html', {'form': form})

def success_page(request):
    return render(request, 'success.html')


def dashboard(request):
    reports = CrimeReport.objects.all().order_by('-date_reported')
    context = {
        'reports': reports,
    }
    return render(request, 'dashboard.html', context)

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

def all_complaints(request):
    complaints = CrimeReport.objects.all().order_by('-date_reported')
    context = {
        'complaints': complaints
    }
    return render(request, 'all_complaints.html', context)

def complaints_detail(request, complaint_id):
    complaint = get_object_or_404(CrimeReport, pk=complaint_id)
    context = {
        'complaint': complaint
    }
    return render(request, 'complaints_detail.html', context)

@login_required
def new_complaint(request):
    if request.method == 'POST':
        form = NewComplaintForm(request.POST)
        if form.is_valid():
            complaint = form.save(commit=False)
            complaint.user = request.user
            complaint.save()
            return redirect('complaints_detail', complaint_id=complaint.id)
    else:
        form = NewComplaintForm()
    
    context = {
        'form': form
    }
    return render(request, 'new_complaint.html', context)

def home(request):
    return render(request, 'home.html')





