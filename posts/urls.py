from django.urls import path
from . import views

urlpatterns = [
  path('', views.list_posts),
  path('new/', views.create_post, name='create_post'),
  path('delete_post/<int:post_id>/', views.delete_post, name='delete_post'),
  path('update_post/<int:post_id>/', views.update_post, name='update_post'),
]
