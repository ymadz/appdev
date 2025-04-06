from django import forms

class PlayerPerformanceForm(forms.Form):
    pace = forms.FloatField(
        required=True,
        min_value=0,
        max_value=100,
        label="Pace",
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Pace (0-100)'}),
        error_messages={'required': 'This field is required.'}
    )
    shooting = forms.FloatField(
        required=True,
        min_value=0,
        max_value=100,
        label="Shooting",
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Shooting (0-100)'}),
        error_messages={'required': 'This field is required.'}
    )
    passing = forms.FloatField(
        required=True,
        min_value=0,
        max_value=100,
        label="Passing",
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Passing (0-100)'}),
        error_messages={'required': 'This field is required.'}
    )
    dribbling = forms.FloatField(
        required=True,
        min_value=0,
        max_value=100,
        label="Dribbling",
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Dribbling (0-100)'}),
        error_messages={'required': 'This field is required.'}
    )
    defending = forms.FloatField(
        required=True,
        min_value=0,
        max_value=100,
        label="Defending",
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Defending (0-100)'}),
        error_messages={'required': 'This field is required.'}
    )
    physic = forms.FloatField(
        required=True,
        min_value=0,
        max_value=100,
        label="Physic",
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Physic (0-100)'}),
        error_messages={'required': 'This field is required.'}
    )
