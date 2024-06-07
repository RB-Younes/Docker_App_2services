from django.urls import path
from . import views


urlpatterns = [
  path('',views.home,name='home'),
  path('add_task/' , views.add_task, name='add_task'),
  path('update_task_status/' , views.update_task_status, name='update_task_status'),
  path('delete_task/' , views.delete_task, name='delete_task'),
]