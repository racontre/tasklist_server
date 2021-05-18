from django.urls import path
from .views import todo_list,todo_retrieve

app_name = 'todos'

urlpatterns = [
    path('', todo_list),
    path('<id>/', todo_retrieve)
]