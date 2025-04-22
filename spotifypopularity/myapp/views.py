import pickle
import numpy as np
from django.shortcuts import render
from .forms import SongInputForm

# Load model, scaler, and feature names once
with open('model.pkl', 'rb') as f:
    model, scaler, feature_names = pickle.load(f)

def predict_popularity(request):
    prediction = None

    if request.method == 'POST':
        form = SongInputForm(request.POST)
        if form.is_valid():
            # Get values in the order of feature_names
            input_data = [form.cleaned_data[feature] for feature in feature_names]
            input_scaled = scaler.transform([input_data])
            prediction = model.predict(input_scaled)[0]
            prediction = "Popular 🎉" if prediction == 1 else "Not Popular 😢"
    else:
        form = SongInputForm()

    return render(request, 'index.html', {'form': form, 'prediction': prediction})
