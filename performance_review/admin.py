from django.contrib import admin
from .models import PerformanceReview, Employee

class PerformanceReviewAdmin(admin.ModelAdmin):
    list_display = ['review_title', 'employee', 'review_date', 'rating', 'reviewed_by']
    search_fields = ['employee__name', 'review_title']
    
admin.site.register(PerformanceReview, PerformanceReviewAdmin)
admin.site.register(Employee)

