
from datetime import datetime, timedelta

def start_round(request, round_id):
    round_obj = Round.objects.get(id=round_id)
    timer_duration = round_obj.timer_duration  # Timer duration in seconds

    # Set start time in session when round starts
    if 'start_round' in request.POST:
        request.session['round_start_time'] = datetime.now().strftime('%Y-%m-%dT%H:%M:%S')  # Save as ISO format string

    # Check if time is up
    if 'finish' in request.POST:
        start_time_str = request.session.get('round_start_time')
        if start_time_str:
            # Parse the stored time string into a datetime object
            start_time = datetime.strptime(start_time_str, '%Y-%m-%dT%H:%M:%S')
            time_elapsed = (datetime.now() - start_time).total_seconds()

            if time_elapsed > timer_duration:
                message = "Time's Up! You can't finish now."
                return render(request, 'quiz/start_round.html', {
                    'round': round_obj,
                    'message': message,
                })

    # Existing logic...
    return render(request, 'quiz/start_round.html', {
        'round': round_obj,
        'timer_duration': timer_duration,
        # other context data
    })


from datetime import datetime, timedelta

def start_round(request, round_id):
    round_obj = Round.objects.get(id=round_id)
    timer_duration = round_obj.timer_duration  # Timer duration in seconds

    # Set start time in session when round starts
    if 'start_round' in request.POST:
        request.session['round_start_time'] = datetime.now().isoformat()

    # Check if time is up
    if 'finish' in request.POST:
        start_time = datetime.fromisoformat(request.session.get('round_start_time'))
        time_elapsed = (datetime.now() - start_time).total_seconds()

        if time_elapsed > timer_duration:
            message = "Time's Up! You can't finish now."
            return render(request, 'quiz/start_round.html', {
                'round': round_obj,
                'message': message,
            })

    # Existing logic...


from django.shortcuts import render, redirect
from .models import Team, Question, Round
import random

def start_round(request, round_id):
    round_obj = Round.objects.get(id=round_id)
    teams = Team.objects.all()
    selected_team = None
    question = None

    # Clear selected team and question on page refresh
    if request.method == "GET":
        request.session.pop('selected_team', None)
        request.session.pop('current_question', None)

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