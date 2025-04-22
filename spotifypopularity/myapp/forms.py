from django import forms

class SongInputForm(forms.Form):
    duration_ms = forms.FloatField()
    explicit = forms.ChoiceField(choices=[(0, 'No'), (1, 'Yes')], widget=forms.RadioSelect)
    danceability = forms.FloatField()
    energy = forms.FloatField()
    key = forms.IntegerField()
    loudness = forms.FloatField()
    mode = forms.ChoiceField(choices=[(0, 'Minor'), (1, 'Major')], widget=forms.RadioSelect)
    speechiness = forms.FloatField()
    acousticness = forms.FloatField()
    instrumentalness = forms.FloatField()
    liveness = forms.FloatField()
    valence = forms.FloatField()
    tempo = forms.FloatField()
    time_signature = forms.IntegerField()
