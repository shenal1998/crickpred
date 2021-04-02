from django import forms
from django.contrib.auth.models import User
from .models import Profile
from .models import runs
from .models import wickets
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm



class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

#UserProfile form
class ProfileForm(ModelForm):
        class Meta:
            model = Profile
            fields = [  'profile_picture',
                        'address',
                        'city',
                        'zipcode',
                        'bio',
                        'contact_number',

                        ]

# Batsman Data Input Form
class RunsForm(ModelForm):
        class Meta:
            model = runs
            fields = [
                        'match_number',
                        'runs',
                        'balls_face',
                        'strikerate',
                        'sixers',
                        'fours',
                        'opposite_team',
                        'ground'

                        ]
            labels = {
               'match_number':'Match ID',
               'runs':'Runs Scored',
               'balls_face':'Balls Faced',
               'strikerate':'Strike Rate',
               'sixers':'Sixers Hit in the Innings',
               'fours':'Fours Hit in the Innings',
               'opposite_team':'Opposite Team',
               'ground':'Ground'

            }


# Batsman Data Input Form
class WicketsForm(ModelForm):
        class Meta:
            model = wickets
            fields = [
                        'match_number',
                        'overs',
                        'runs',
                        'maidens',
                        'wickets',
                        'econ',
                        'average',
                        'opposite_team',
                        'ground'

                        ]
            labels = {
               'match_number':'Match ID',
               'overs':'Number of Overs',
               'runs':'Runs Scored',
               'maidens':'Maidens',
               'wickets':'Wickets',
               'econ':'Economy',
               'average':'Average',
               'opposite_team':'Opposite Team',
               'ground':'Ground'

            }
