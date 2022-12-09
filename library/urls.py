from django.urls import path
from .views import IndexView, CategoryCreateView

urlpatterns = [
    path('', IndexView.as_view()),
    path('add-category', CategoryCreateView.as_view()),
]
