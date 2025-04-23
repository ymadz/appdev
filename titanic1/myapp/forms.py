from django import forms

class TitanicForm(forms.Form):
    Pclass = forms.ChoiceField(choices=[(1, '1st'), (2, '2nd'), (3, '3rd')])
    Sex = forms.ChoiceField(choices=[(0, 'Male'), (1, 'Female')])
    Age = forms.FloatField()
    SibSp = forms.IntegerField(label='Siblings/Spouses Aboard')
    Parch = forms.IntegerField(label='Parents/Children Aboard')
    Fare = forms.FloatField()
