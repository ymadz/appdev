from django.shortcuts import render
from .forms import TitanicForm
import pickle
import numpy as np
import os

model_path = os.path.join('titanic_model.pkl')
with open(model_path, 'rb') as f:
    model = pickle.load(f)

def predict_view(request):
    prediction = None
    if request.method == 'POST':
        form = TitanicForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            input_data = np.array([[
                int(data['Pclass']), int(data['Sex']), float(data['Age']),
                int(data['SibSp']), int(data['Parch']), float(data['Fare'])
            ]])
            prediction = model.predict(input_data)[0]
    else:
        form = TitanicForm()
    return render(request, 'index.html', {'form': form, 'prediction': prediction})
