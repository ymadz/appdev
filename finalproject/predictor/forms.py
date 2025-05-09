from django import forms

class PlayerInputForm(forms.Form):
    age = forms.IntegerField(min_value=15, max_value=50, label='Age')
    height_cm = forms.IntegerField(min_value=100, max_value=250, label='Height (cm)')
    weight_kg = forms.IntegerField(min_value=40, max_value=150, label='Weight (kg)')
    pace = forms.FloatField(min_value=0, max_value=99, label='Pace')
    shooting = forms.FloatField(min_value=0, max_value=99, label='Shooting')
    passing = forms.FloatField(min_value=0, max_value=99, label='Passing')
    dribbling = forms.FloatField(min_value=0, max_value=99, label='Dribbling')
    defending = forms.FloatField(min_value=0, max_value=99, label='Defending')
    physic = forms.FloatField(min_value=0, max_value=99, label='Physic')

    PREFERRED_FOOT_CHOICES = [
        ('Left', 'Left'),
        ('Right', 'Right'),
    ]
    WORK_RATE_CHOICES = [
        ('Low/Low', 'Low/Low'),
        ('Low/Medium', 'Low/Medium'),
        ('Low/High', 'Low/High'),
        ('Medium/Low', 'Medium/Low'),
        ('Medium/Medium', 'Medium/Medium'),
        ('Medium/High', 'Medium/High'),
        ('High/Low', 'High/Low'),
        ('High/Medium', 'High/Medium'),
        ('High/High', 'High/High'),
    ]

    PLAYER_POSITION_CHOICES = [
        ('ST', 'ST'), ('LW', 'LW'), ('RW', 'RW'), ('CAM', 'CAM'), ('CM', 'CM'),
        ('CDM', 'CDM'), ('LM', 'LM'), ('RM', 'RM'), ('CB', 'CB'), ('LB', 'LB'),
        ('RB', 'RB'), ('LWB', 'LWB'), ('RWB', 'RWB'), ('CF', 'CF'), ('LF', 'LF'), ('RF', 'RF')
    ]

    preferred_foot = forms.ChoiceField(choices=PREFERRED_FOOT_CHOICES, label="Preferred Foot")
    work_rate = forms.ChoiceField(choices=WORK_RATE_CHOICES, label="Work Rate")
    player_positions = forms.ChoiceField(choices=PLAYER_POSITION_CHOICES, label="Primary Position")
