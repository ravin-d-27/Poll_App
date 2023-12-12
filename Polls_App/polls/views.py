from django.shortcuts import get_object_or_404, render
from django.http import Http404, HttpResponse

from django.template import loader
# Create your views here.

from .models import Question

def index(request):
    latest_question_list= Question.objects.order_by('-pub_text')
    context = {'latest_question_list':latest_question_list}
    return render(request, 'polls/home.html', context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question':question})

def vote(request, question_id):
    return render(request, 'polls/vote.html')

def results(request, question_id):
    return render(request, 'polls/results.html')