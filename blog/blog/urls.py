from django.urls import path

from . import views

urlpatterns = [
    path('', views.BlogListView.as_view(), name='home'),
    path('blog/<int:pk>/', views.BlogDetailView.as_view(), name='blog_detail'),
    path('blog/new/', views.BlogCreateView.as_view(), name='blog_new'),
    path('blog/edit/<int:pk>', views.BlogUpdateView.as_view(), name='blog_edit'),
    path('blog/delete/<int:pk>', views.BlogDeleteView.as_view(), name='blog_delete'),
]
