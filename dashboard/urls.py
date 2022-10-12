from django.urls import path
from . import views
from django.views.generic import TemplateView
from django.views.static import serve
from django.conf.urls import url
from django.conf import settings
urlpatterns = [
    path('', views.home, name='home'),
    path('notes', views.notes, name='notes'),
    path('homework', views.homework, name='homework'),
    path('conversion', views.conversion, name='conversion'),
    path('todo', views.todo, name='todo'),
    path('wiki', views.wiki, name='wiki'),
    path('youtube', views.youtube, name='youtube'),
    path('dictionary', views.dictionary, name='dictionary'),
    path('books', views.books, name='books'),

    path('notes_detail/<int:pk>',
         views.NotesDetailView.as_view(), name="notes_detail"),
    path('delete_homework/<int:pk>', views.delete_homework, name='delete-homework'),
    path('delete_note/<int:pk>', views.delete_note, name='delete-note'),
    path('delete_todo/<int:pk>', views.delete_todo, name='delete-todo'),
    path('update_todo/<int:pk>', views.update_todo, name='update-todo'),
    path('update_homework/<int:pk>', views.update_homework, name='update-homework'),
    url(r'^media/(?P<path>.*)$', serve,{'document_root':       settings.MEDIA_ROOT}), 
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}), 
]
