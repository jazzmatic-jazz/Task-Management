from django.urls import path
from .views.auth import login_page, register_page
from .views.index import index, create_task_view, update_task_view, delete_task_view

urlpatterns = [
    path('register', register_page, name='register'),
    path('login', login_page, name='login'),
    path('', index, name='home'),
    path('create', create_task_view, name='create'),
    path('<int:pk>/update', update_task_view, name='update'),
    path('<int:pk>/delete', delete_task_view, name='delete'),
]
