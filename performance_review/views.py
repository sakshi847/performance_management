from django.shortcuts import render, redirect, get_object_or_404
from .forms import PerformanceReviewForm
from .models import PerformanceReview
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.http import Http404
from performance_review.models import PerformanceReview
from .forms import ReviewForm


def dashboard(request):
    reviews = PerformanceReview.objects.all()
    return render(request, 'admin_dashboard.html', {'reviews': reviews})


def add_review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_dashboard')  
    else:
        form = ReviewForm()
    return render(request, 'add_review.html', {'form': form})

def review_list(request):
    reviews = PerformanceReview.objects.all()  
    return render(request, 'review_list.html', {'reviews': reviews})


def edit_review(request, review_id):
    review = get_object_or_404(PerformanceReview, review_id=review_id)
    
    if request.method == "POST":
        form = PerformanceReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            return redirect('performance_review:review_list')
    else:
        form = PerformanceReviewForm(instance=review)

    return render(request, 'edit_review.html', {'form': form, 'review': review})

def admin_dashboard(request):
    reviews = PerformanceReview.objects.all()
    return render(request, 'admin_dashboard.html', {'reviews': reviews})



