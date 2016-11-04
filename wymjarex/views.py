from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.utils import timezone
from .models import Wpis
from .forms import WpisForm
from django.contrib.auth.decorators import login_required
from datetime import datetime, timedelta
#import matplotlib.pyplot as plt

# Create your views here.
@login_required
def wpiss_list(request):
    wpisy = Wpis.objects.filter(author= request.user,created_date__lte=timezone.now()).order_by('-created_date')
    return render(request, 'wymjarex/wpiss_list.html', {'wpisy' : wpisy})

@login_required
def wpis_new(request):
    if request.method == "POST":
        form = WpisForm(request.POST)
        if form.is_valid():
            wpis = form.save(commit=False)
            wpis.author = request.user
            # wpis.created_date = timezone.now()
            wpis.save()
            return redirect('wpiss_list')
    else:
        form = WpisForm(initial={"created_date": "YYYY-MM-DD"})
    return render(request, 'wymjarex/wpis_new.html', {'form': form})

@login_required
def last(request, pk):    
    start_date = datetime.now()-timedelta(days = int(pk))
    end_date = datetime.now()
    wpisy = Wpis.objects.filter(author= request.user, created_date__gte=start_date, created_date__lte=end_date).order_by('-created_date')
    return render(request, 'wymjarex/wpiss_list.html', {'wpisy' : wpisy})

@login_required
def wpis_edit(request, pk):
    wpis = get_object_or_404(Wpis.objects.filter(author= request.user), pk=pk)
    if request.method == "POST":
        form = WpisForm(request.POST, instance=wpis)
        if form.is_valid():
            wpis = form.save(commit=False)
            wpis.author = request.user
            
            wpis.save()
            return redirect('wpiss_list')
    else:
        form = WpisForm(instance=wpis)
    return render(request, 'wymjarex/wpis_edit.html', {'form': form})
