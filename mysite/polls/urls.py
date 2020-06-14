from django.urls import path

from . import views

urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),

    path('add/question/', views.addQuestion, name='addQuestion'),
    path('delete/question/<int:question_id>/', views.deleteQuestion, name='deleteQuestion'),
    path('edit/question/<int:question_id>/', views.editQuestion, name='editQuestion'),

    # ex: /polls/5/
    path('<int:question_id>/', views.detail, name='detail'),

    # ex: /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),

    path('download/<int:question_id>/', views.download, name='download'),
]