from django.shortcuts import render, redirect
from .models import Team, Question, Round
import random

def home(request):
    rounds = Round.objects.all()
    teams = Team.objects.all()
    return render(request, 'quiz/home.html', {'rounds': rounds, 'teams': teams})


def start_round(request, round_id):
    round_obj = Round.objects.get(id=round_id)
    teams = Team.objects.all()
    selected_team = None
    question = None

    # Handle random team selection
    if 'start_round' in request.POST:
        selected_team = random.choice(teams)
        request.session['selected_team'] = selected_team.name  # Save to session for persistence

    # Handle random question selection
    if 'get_question' in request.POST:
        questions = Question.objects.filter(round=round_obj)
        question = random.choice(questions)
        request.session['current_question'] = question.id  # Save question for display

    # Retrieve session data if available
    selected_team = request.session.get('selected_team', selected_team)
    question_id = request.session.get('current_question')
    if question_id:
        question = Question.objects.get(id=question_id)

    return render(request, 'quiz/start_round.html', {
        'round': round_obj,
        'teams': teams,
        'selected_team': selected_team,
        'question': question,
    })