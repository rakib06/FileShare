from django.shortcuts import render, redirect
from .models import Team, Question, Round
import random

def home(request):
    teams = Team.objects.all()
    return render(request, 'quiz/home.html', {'teams': teams})

def start_quiz(request, round_id):
    round_obj = Round.objects.get(id=round_id)
    questions = Question.objects.filter(round=round_obj)
    random_question = random.choice(questions)

    if request.method == 'POST':
        team_id = request.POST['team']
        team = Team.objects.get(id=team_id)
        team.score += 1  # Update score for correct answer
        team.save()
        return redirect('home')

    return render(request, 'quiz/quiz.html', {
        'question': random_question,
        'teams': Team.objects.all(),
        'round': round_obj,
    })