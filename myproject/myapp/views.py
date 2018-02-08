from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from django.db import connection
from django import forms
from random import randint

#Importing from forms
from .forms import RegisterForm
from .forms import LoginForm
from .forms import QuizForm
from .forms import PlayQuiz
from .forms import SubmitQuiz
from .forms import SubmitScore

#Importing from models
from .models import Register
from .models import Quiz
from .models import Score

# For registering the form 
def register(request):
   # Checking the type of request 
   if(request.method == "POST"):
      # Create a form instance and get data in it
      form = RegisterForm(request.POST)
      #check the form is valid or not
      if form.is_valid():
         #getting the username 
         name = form.cleaned_data['username']
         request.session['name'] = name
         valid = True
         for person in Register.objects.raw("Select * from myapp_register"):
            if(name == person.username):
               valid = False
               break
            if not valid:
               raise forms.ValidationError("Username is already registered. Try with a different username")
         # saving the form data in the database
         form.save()
         # redirecting 
         return HttpResponseRedirect("/home")
      else:
         # if the form is invalid then redirecting back to register with errors 
         return render(request, 'myapp/register.html', {'form': form})
   else:
      # If the data is not filled that is simply the register file is opened
      Myform = RegisterForm()
      # return render(request, "myapp/register.html", {})
      return render(request, 'myapp/register.html', {'form': Myform})

# For logging in 
def login(request):
   if request.method == "POST":
      login_form = LoginForm(request.POST)
      if login_form.is_valid():
         user = login_form.cleaned_data['user']
         pswd = login_form.cleaned_data['pswd']
         request.session['name'] = user
         valid = False
         for users in Register.objects.raw("Select * from myapp_register"):
            if user == users.username and pswd == users.passw:
               valid = True
               break
         if not valid:
            raise forms.ValidationError("User or password is incorrect")
         return HttpResponseRedirect("/home")
      else:
         return HttpRespnseRedirect('/login')
   else:
      Myloginform = LoginForm()
      return render(request, 'myapp/login.html' , {'login_form' : Myloginform})

# For the home page
def home(request):
   if(request.method == 'POST'):
      request.session['score'] = 0
      request.session['count'] = 0
      request.session['li'] = []
      # request.session['sum_score'] = 0
      if 'Web-Development' in request.POST:
         request.session['category'] = 'Web-Development'
         return redirect('play')
      elif 'Android-Development' in request.POST:
         request.session['category'] = 'Android-Development'
         return redirect('play')
      elif 'Data-Science' in request.POST:
         request.session['category'] = 'Data-Science'
         return redirect('play')
      elif 'Indian-Cinema' in request.POST:
         request.session['category'] = 'Indian-Cinema'
         return redirect('play')
      elif 'Indian-Music' in request.POST:
         request.session['category'] = 'Indian-Music'
         return redirect('play')
      elif 'Indian-Books' in request.POST:
         request.session['category'] = 'Indian-Books'
         return redirect('play')
      else:
         return redirect('home')
   else:
      return render(request , 'myapp/home.html', {})

def play(request):
   # Taking the value of the button from the session variable
   category = request.session['category']
   add = 5
   count = Quiz.objects.filter(category = category).count()
   # Checking the value with the category in the database
   q = ""
   opt_a = ""
   opt_b = ""
   opt_c = ""
   opt_d = ""
   sol = ""
   i = randint(0,count-1)
   for quiz_get in  Quiz.objects.raw('Select * from myapp_quiz where category =  %s', [category]):
      q += quiz_get.question + "<br>"
      opt_a += quiz_get.option_a + "<br>"
      opt_b += quiz_get.option_b + "<br> "
      opt_c += quiz_get.option_c + "<br>"
      opt_d += quiz_get.option_d + "<br>"
      sol += str(quiz_get.solution) + "<br>"
      ques = q.split("<br>")
      optiona = opt_a.split("<br>")
      optionb = opt_b.split("<br>")
      optionc = opt_c.split("<br>")
      optiond = opt_d.split("<br>")
      solution = sol.split("<br>")
      
   context= {
      'category':category,
      'optiona':optiona[i],
      'optionb':optionb[i],
      'optionc':optionc[i],
      'optiond':optiond[i],
      'quest' :ques[i],
      'sol_now':solution[i],
      }
   
   
   if(request.method == 'POST'):
      quiz_play = SubmitQuiz(request.POST)
      # Check if 10 questions completed or not 
      if request.session['count'] < 9:
         # Check if form input vaid or not 
         if quiz_play.is_valid():
            # radio button solution 
            mysol = quiz_play.cleaned_data['question']
            correct = quiz_play.cleaned_data['qsol']
            request.session['count'] += 1 
            # if solution = correct solution
            if mysol == correct:
               # Increase the score if the answer is correct
               request.session['score'] = int(request.session['score']) + int(add)
            else:
               print(request.session['score'])
               # Score remains the same
         else:
            # If the input in invalid 
            print("invalid")
         # if not greater to 10
         return HttpResponseRedirect('/play')
      else:
         return HttpResponseRedirect('/myscore')
   else:
      return render(request, 'myapp/play.html', context)
      
      
def quiz(request):
   if(request.method == "POST"):
      quiz_now = QuizForm(request.POST)
      if quiz_now.is_valid():
         quest = quiz_now.cleaned_data['question']
         valid = True
         for quiz_quest in Quiz.objects.raw("Select * from myapp_quiz"):
            if (quest == quiz_quest.question):
               valid = False
               break
            if not valid:
               raise forms.ValidationError("This Question is alraedy there Kindly Enter a new question")
         quiz_now.save()
         # redirecting 
         return HttpResponseRedirect("/home")
      else:
         # if the form is invalid then redirecting back to register with errors
         return HttpResponseRedirect('/quiz')
      # If the data is not filled that is simply the register file is opened
   else:
      MyQuiz = QuizForm()
      return render(request, 'myapp/quiz.html', {})
   
def myscore(request):
   score = request.session['score']
   category = request.session['category']
   user = request.session['name']
   context= {
      'score':score,
      'category':category,
      'user':user,
      }
   if(request.method == "POST"):
      if 'Send_score' in request.POST:
         score_save = SubmitScore(request.POST)
         if score_save.is_valid():
            score_save.save()
            print("score Saved")
         else:
            print("Error")
         return HttpResponseRedirect('/leaderboard')
      elif 'Dont_send' in request.POST:
         return HttpResponseRedirect('/leaderboard')
   else:
      return render(request,'myapp/myscore.html' , context)
      
def leaderboard(request):
   s = ""
   c = ""
   u = ""
   for score_get in  Score.objects.raw('Select * from myapp_score'):
      s += str(score_get.score)+"<br>"
      c += score_get.category +"<br>"
      u += score_get.user + "<br>"
      sc = s.split("<br>")
      cat = c.split("<br>")
      us = u.split("<br>")
   print(us)
   context = {
      'score':sc,
      'category':cat,
      'user':us,
   }
   return render(request,'myapp/leaderboard.html' , context)