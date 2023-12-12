from django.shortcuts import render
from django.http import HttpResponse

from django.template import loader
# Create your views here.

from .models import Question

def index(request):
    latest_question_list= Question.objects.order_by('-pub_text')
    context = {'latest_question_list':latest_question_list}
    return render(request, 'polls/home.html', context)

def detail(request, question_id):
    return render(request, 'polls/detail.html')

def results(request, question_id):
    return render(request, 'polls/results.html')

def vote(request, question_id):
    return render(request, 'polls/vote.html')