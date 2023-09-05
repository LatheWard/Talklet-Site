from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("Hello world! This is Emily's idea")

def card_details(request, cards_id):
    return HttpResponse(cards_id)

def question_text(request, cards_id):
    return HttpResponse(cards_id + 'Question')

def answer_text(request, cards_id):
    return HttpResponse(cards_id + 'Answer')