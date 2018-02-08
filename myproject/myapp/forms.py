from django import forms
#Importing from models
from .models import Register
from .models import Quiz
from .models import Score

# taking values from models. 
class RegisterForm(forms.ModelForm):
    class Meta:
        model = Register
        fields = ('fname', 'username', 'email' , 'passw')
        
class LoginForm(forms.Form):
    user = forms.CharField(max_length = 100)
    pswd = forms.CharField(widget = forms.PasswordInput())
    
 # Creating a Quiz  
class QuizForm(forms.ModelForm):
    class Meta:
        model = Quiz
        fields = ('category', 'question' , 'option_a', 'option_b' , 'option_c' , 'option_d' , 'solution')
# playing a quiz 
class PlayQuiz(forms.Form):
    category = forms.CharField(max_length  = 100)
   # Submitting the answers of a quiz  
class SubmitQuiz(forms.Form):
    question = forms.CharField(max_length = 10)
    qsol = forms.CharField(max_length = 10)

# Submitting the score
class SubmitScore(forms.ModelForm):
    class Meta:
        model = Score
        fields = ('category' , 'user' , 'score')
    