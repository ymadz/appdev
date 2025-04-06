from django.shortcuts import render
import pickle
import numpy as np
from .models import PlayerInput
import os

# Load model once
MODEL_PATH = os.path.join(os.path.dirname(__file__), 'xgboost_fifa_model.pkl')
with open(MODEL_PATH, 'rb') as f:
    model = pickle.load(f)

def predict(request):
    prediction = None

    if request.method == 'POST':
        try:
            pace = float(request.POST.get('pace'))
            shooting = float(request.POST.get('shooting'))
            passing = float(request.POST.get('passing'))
            dribbling = float(request.POST.get('dribbling'))
            defending = float(request.POST.get('defending'))
            physic = float(request.POST.get('physic'))

            input_data = np.array([[pace, shooting, passing, dribbling, defending, physic]])
            prediction = round(model.predict(input_data)[0], 2)

            # Save to MySQL DB
            PlayerInput.objects.create(
                pace=pace,
                shooting=shooting,
                passing=passing,
                dribbling=dribbling,
                defending=defending,
                physic=physic,
                prediction=prediction
            )

        except Exception as e:
            prediction = f"Error: {str(e)}"

    return render(request, 'form.html', {'prediction': prediction})
