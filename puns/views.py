from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Pun, Rating
from .forms import PunForm, RatingForm
from django.db.models import Count, Avg
from django.contrib.auth.models import User

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'puns/register.html', {'form': form})


@login_required
def submit_pun(request):
    if request.method == 'POST':
        form = PunForm(request.POST)
        if form.is_valid():
            pun = form.save(commit=False)
            pun.author = request.user
            pun.save()
            return redirect('puns_list')
    else:
        form = PunForm()
    return render(request, 'puns/submit_pun.html', {'form': form})

@login_required
def rate_pun(request, pun_id):
    pun = Pun.objects.get(id=pun_id)
    if request.method == 'POST':
        form = RatingForm(request.POST)
        if form.is_valid():
            rating = form.save(commit=False)
            rating.pun = pun
            rating.user = request.user
            rating.save()
            return redirect('puns_list')
    else:
        form = RatingForm()
    return render(request, 'puns/rate_pun.html', {'form': form, 'pun': pun})

@login_required
def puns_list(request):
    puns = Pun.objects.all()
    return render(request, 'puns/pun_list.html', {'puns': puns})

@login_required
def leaderboard(request):
    # Top punsters by the number of puns submitted
    top_punsters_by_count = User.objects.annotate(num_puns=Count('pun')).order_by('-num_puns')[:10]

    # Top punsters by average rating of their puns
    top_punsters_by_rating = User.objects.annotate(avg_rating=Avg('pun__rating__rating')).order_by('-avg_rating')[:10]

    context = {
        'top_punsters_by_count': top_punsters_by_count,
        'top_punsters_by_rating': top_punsters_by_rating,
    }

    return render(request, 'puns/leaderboard.html', context)