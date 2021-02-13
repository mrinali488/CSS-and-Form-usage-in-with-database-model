from django.urls import path
from .views import AddPostView

urlpatterns = [
            path('', AddPostView.as_view(), name="home"),


    ]