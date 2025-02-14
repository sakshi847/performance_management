from django.urls import path
from . import views

app_name = 'performance_review'

urlpatterns = [
    path('add/', views.add_review, name='add_review'),
    path('list/', views.review_list, name='review_list'),
    path('edit/<int:review_id>/', views.edit_review, name='edit_review'),
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
]
