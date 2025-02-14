from django import forms
from .models import PerformanceReview, Employee
from django.contrib.auth.models import User

class PerformanceReviewForm(forms.ModelForm):
    class Meta:
        model = PerformanceReview
        fields = ['review_title', 'review_date', 'employee', 'reviewed_by', 'review_period', 'rating', 'comments']

    def __init__(self, *args, **kwargs):
        user = kwargs.get('user')
        super().__init__(*args, **kwargs)
        self.fields['employee'].queryset = Employee.objects.filter(reporting_manager=user)
        self.fields['reviewed_by'].initial = user

    def clean_rating(self):
        rating = self.cleaned_data['rating']
        if rating < 1 or rating > 10:
            raise forms.ValidationError('Rating must be between 1 and 10.')
        return rating


class ReviewForm(forms.ModelForm):
    class Meta:
        model = PerformanceReview  
        fields = ['review_title', 'review_date', 'employee', 'reviewed_by', 'review_period', 'rating', 'comments']
