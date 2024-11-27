Creating a Django-based web app for your floor quiz with image support involves the following steps:

Features

	1.	Admin Panel:
	•	Manage teams, questions, and rounds (including image upload for questions).
	2.	Quiz Interface:
	•	Randomly select teams and questions.
	•	Display questions with or without images.
	•	Include a countdown timer.
	3.	Score Tracking:
	•	Update and display team scores dynamically.
	4.	Frontend:
	•	User-friendly interface using Django templates and CSS.

Implementation

1. Set Up Django Project

	1.	Install Django:

pip install django


	2.	Create a project:

django-admin startproject floor_quiz
cd floor_quiz
python manage.py startapp quiz


	3.	Add the app (quiz) to INSTALLED_APPS in settings.py.
	4.	Set up a SQLite database:

python manage.py migrate

2. Define Models

In quiz/models.py:

from django.db import models

class Team(models.Model):
    name = models.CharField(max_length=100, unique=True)
    score = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Round(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Question(models.Model):
    round = models.ForeignKey(Round, on_delete=models.CASCADE)
    question_text = models.TextField()
    image = models.ImageField(upload_to='question_images/', blank=True, null=True)
    answer = models.CharField(max_length=255)

    def __str__(self):
        return self.question_text

Run migrations:

python manage.py makemigrations
python manage.py migrate

3. Admin Panel for Management

In quiz/admin.py:

from django.contrib import admin
from .models import Team, Round, Question

admin.site.register(Team)
admin.site.register(Round)
admin.site.register(Question)

Create a superuser:

python manage.py createsuperuser

4. Views and Logic

In quiz/views.py:

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

5. URLs

In quiz/urls.py:

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('start-quiz/<int:round_id>/', views.start_quiz, name='start_quiz'),
]

In floor_quiz/urls.py:

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('quiz.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

6. Templates

	•	templates/quiz/home.html:

<!DOCTYPE html>
<html>
<head>
    <title>Floor Quiz</title>
</head>
<body>
    <h1>Floor Quiz</h1>
    <h2>Teams:</h2>
    <ul>
        {% for team in teams %}
        <li>{{ team.name }} - Score: {{ team.score }}</li>
        {% endfor %}
    </ul>
    <h2>Select Round:</h2>
    <ul>
        {% for round in round_list %}
        <li><a href="{% url 'start_quiz' round.id %}">{{ round.name }}</a></li>
        {% endfor %}
    </ul>
</body>
</html>

	•	templates/quiz/quiz.html:

<!DOCTYPE html>
<html>
<head>
    <title>Quiz Round</title>
</head>
<body>
    <h1>Round: {{ round.name }}</h1>
    <h2>Question:</h2>
    <p>{{ question.question_text }}</p>
    {% if question.image %}
    <img src="{{ question.image.url }}" alt="Question Image">
    {% endif %}
    <form method="POST">
        {% csrf_token %}
        <label for="team">Select Team:</label>
        <select name="team">
            {% for team in teams %}
            <option value="{{ team.id }}">{{ team.name }}</option>
            {% endfor %}
        </select>
        <button type="submit">Submit Answer</button>
    </form>
</body>
</html>

7. Configure Static and Media Files

In settings.py:

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

8. Run the App

Start the server:

python manage.py runserver

Visit http://127.0.0.1:8000/ to access the quiz.

Next Steps

	1.	Styling: Use Bootstrap or Tailwind CSS for a modern interface.
	2.	Timer: Add JavaScript to handle countdown timers.
	3.	Leaderboard: Create a page to display team scores dynamically.
	4.	Deployment: Use Heroku or Django’s deployment tools to host the app.

Let me know if you’d like any specific feature or enhancement!