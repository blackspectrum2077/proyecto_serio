from django.urls import path
from .views import BlogListView

app_name="blog"
urlspatterns = [
    path('', BlogListView.as_view(), name="home")
    
]