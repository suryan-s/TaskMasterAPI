from django.urls import path, include
from .views import HomeView, AddToDo, CompleteToDoItem

urlpatterns = [
    path('', HomeView.as_view()),
    path('add/', AddToDo.as_view()),
    path('complete/', CompleteToDoItem.as_view()),
]
