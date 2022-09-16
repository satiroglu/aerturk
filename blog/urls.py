from . import views
from django.urls import path, include

urlpatterns = [
    path('blog/', views.PostList.as_view(), name='blog'),
    path('blog/<slug:slug>/', views.SinglePost.as_view(), name='singlePost'),
]