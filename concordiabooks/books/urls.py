from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing_page, name='landing'),
    path('search/<str:course_code>/', views.search_results, name='search_results'),
]
