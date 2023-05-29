from unicodedata import name
from django.urls import path
from .import views



urlpatterns = [
    path('', views.home, name='home'),
    path('notes', views.notes, name='notes'),
    path('notes/delet<int:pk>', views.deleteNots, name='deleteNots'),
    path('notes_detail/<int:pk>', views.NotesDetailvew.as_view(),name='notes-detail'),
    
    path('homeWork', views.homeWork, name='homeWork'),
    path('delet-homework/<int:pk>', views.deletehomework, name='deletehomework'),
    path('updatehomework/<int:pk>', views.update_homework, name='update_homework'),
    
    
    path('youtube', views.youtube, name='youtube'),
    
    
    path('todo', views.todo, name='todo'),
    path('updatetodo/<int:pk>', views.update_todo, name='update_todo'),
    path('delettodo/<int:pk>', views.deletTodo, name='deletTodo'),
    
    
    
    path('book', views.book, name='boook'),
    
    
    path('dictionary', views.dictionary, name='dictionary'),
    
    
    path('wikipedia', views.wiki, name='wikipedia'),
    path('conversion', views.conversion, name='conversion'),
    
    # path('register', views.register, name='register')
    
    
    
]