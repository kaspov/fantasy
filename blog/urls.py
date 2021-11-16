from django.urls import path, include

from blog.views import ( BlogListView, BlogDetailView, BlogCreateView,
BlogUpdateView)

urlpatterns = [
    path('blog/', BlogListView.as_view() , name='blog-list'), 
    path('blog/<int:pk>', BlogDetailView.as_view(), name='blog-detail'), 
    path('blog/create/', BlogCreateView.as_view(), name='blog-create'),
    path('blog/update/<int:pk>', BlogUpdateView.as_view(),name='blog-update'), 
]
