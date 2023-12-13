from django.shortcuts import get_object_or_404, render
from django.http import Http404, HttpResponse, HttpResponseRedirect

from django.template import loader
from django.urls import reverse


from .models import Question, Choice, Vote
from django.contrib.auth.decorators import login_required

# Create your views here.

from .models import Question, Choice

def index(request):
    latest_question_list= Question.objects.order_by('-pub_text')
    context = {'latest_question_list':latest_question_list}
    return render(request, 'polls/home.html', context)

@login_required
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    
    # Check if the user has already voted for this question
    user_has_voted = Vote.objects.filter(user=request.user, question=question).exists()

    context = {'question': question, 'user_has_voted': user_has_voted}
    return render(request, 'polls/detail.html', context)

@login_required
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)

    # Check if the user has already voted for this question
    if Vote.objects.filter(user=request.user, question=question).exists():
        return render(request, 'polls/vote.html', {'question': question, 'error_message': 'You have already voted for this question'})

    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/vote.html', {'question': question, 'error_message': 'You did not select any choice'})
    else:
        selected_choice.votes += 1
        selected_choice.save()

        # Save the vote information to ensure the user can't vote again
        Vote.objects.create(user=request.user, question=question)

        return HttpResponseRedirect(reverse('polls:results', args=(question_id,)))

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question':question})
