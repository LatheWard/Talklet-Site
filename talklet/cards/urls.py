from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:cards_id/", views.card_details, name="card_details"),
    path("<int:cards_id/question_text", views.question_text,name="question"),
    path("<int:cards_id/answer_text", views.answer_text,name="answer"),
]