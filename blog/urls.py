from django.urls import path
from . import views

# TEMPLATE TAGGING
app_name = 'blog'

urlpatterns = [
	path('post/<int:post_id>/', views.post, name='post'),
	path('register/', views.register, name='register'),
	path('user_login/', views.user_login, name='login'),
	path('create_post/', views.create_post, name='create_post'),
	path('profile/', views.profile, name='profile'),
]
