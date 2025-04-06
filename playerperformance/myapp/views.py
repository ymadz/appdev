from django.shortcuts import render
from .forms import PlayerPerformanceForm
import pickle
import numpy as np

def predict_player_performance(request):
    prediction = None
    error_message = None

    if request.method == 'POST':
        form = PlayerPerformanceForm(request.POST)
        
        if form.is_valid():
            # Get form data
            pace = form.cleaned_data['pace']
            shooting = form.cleaned_data['shooting']
            passing = form.cleaned_data['passing']
            dribbling = form.cleaned_data['dribbling']
            defending = form.cleaned_data['defending']
            physic = form.cleaned_data['physic']
            
            # Prepare data for prediction
            input_data = np.array([[pace, shooting, passing, dribbling, defending, physic]])
            
            # Load the pre-trained model (replace with your own path)
            try:
                with open('myapp/xgboost_fifa_model.pkl', 'rb') as model_file:
                    model = pickle.load(model_file)
                prediction = model.predict(input_data)[0]  # Assuming a regression model
            except Exception as e:
                error_message = f"Error loading model: {e}"
        else:
            error_message = "Please ensure all fields are filled with valid numbers."
    else:
        form = PlayerPerformanceForm()

    return render(request, 'form.html', {
        'form': form,
        'prediction': prediction,
        'error_message': error_message
    })
