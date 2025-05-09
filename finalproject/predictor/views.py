from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from django.shortcuts import render
from io import BytesIO
from django.http import HttpResponse
import base64
import pickle
import io


with open('xgboost_fifa_model.pkl', 'rb') as file:
    model = pickle.load(file)

def home(request):
    if not request.session.get('has_visited'):
        request.session['has_visited'] = True
        return render(request, 'predictor/welcome.html')
    
    if request.user.is_authenticated:
        return redirect('dashboard')
    else:
        return redirect('login')


def plot_to_base64(fig):
    buf = BytesIO()
    fig.savefig(buf, format='png', bbox_inches='tight')
    buf.seek(0)
    return base64.b64encode(buf.getvalue()).decode('utf-8')

def get_graph():
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png', bbox_inches='tight')
    buffer.seek(0)
    image_png = buffer.getvalue()
    buffer.close()
    graph = base64.b64encode(image_png).decode('utf-8')
    return graph

@login_required
def dashboard(request):
    # Load FIFA data
    df = pd.read_csv('players_21.csv')

    # Drop rows with missing values in important columns
    df = df.dropna(subset=['short_name', 'age', 'height_cm', 'weight_kg', 'nationality', 'club_name', 'overall', 'potential', 'preferred_foot'])

    # Select key columns for display
    df_stats = df[['short_name', 'age', 'height_cm', 'weight_kg', 'nationality', 'club_name', 'overall', 'potential', 'preferred_foot']]

    # Compute summary statistics
    stats = {
        'Total Players': len(df_stats),
        'Average Overall': round(df_stats['overall'].mean(), 2),
        'Average Potential': round(df_stats['potential'].mean(), 2),
        'Average Age': round(df_stats['age'].mean(), 2),
    }

    # Top 10 players by overall rating
    top_players = df_stats.sort_values(by='overall', ascending=False).head(10)

    # Average overall by nationality (top 10)
    top_nationalities = (
        df_stats.groupby('nationality')['overall']
        .mean()
        .sort_values(ascending=False)
        .head(10)
        .reset_index()
    )

    ### Visualization 1: Distribution of Overall Ratings ###
    plt.figure(figsize=(6, 4))
    sns.histplot(df_stats['overall'], kde=True, color='skyblue', bins=30)
    plt.title('Distribution of Overall Ratings')
    img1 = get_graph()
    plt.clf()

    ### Visualization 2: Correlation Heatmap ###
    corr = df_stats[['age', 'height_cm', 'weight_kg', 'overall', 'potential']].corr()
    plt.figure(figsize=(6, 4))
    sns.heatmap(corr, annot=True, cmap='coolwarm', fmt='.2f')
    plt.title('Correlation Heatmap')
    img2 = get_graph()
    plt.clf()

    ### Visualization 3: Average Overall by Preferred Foot ###
    plt.figure(figsize=(6, 4))
    sns.barplot(data=df_stats, x='preferred_foot', y='overall', palette='viridis', errorbar=None)
    plt.title('Average Overall by Preferred Foot')
    img3 = get_graph()
    plt.clf()

    context = {
        'stats': stats,
        'top_players': top_players.to_dict(orient='records'),
        'top_nationalities': top_nationalities.to_dict(orient='records'),
        'img1': img1,
        'img2': img2,
        'img3': img3,
    }

    return render(request, 'predictor/dashboard.html', context)


def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = UserCreationForm()
    return render(request, 'predictor/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'predictor/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')
from .forms import PlayerInputForm

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
import pandas as pd
import pickle

# Load your trained model (do this once, globally ideally)
with open("xgboost_fifa_model.pkl", "rb") as f:
    model = pickle.load(f)

@login_required
def predict_overall(request):
    prediction = None
    error = None

    if request.method == 'POST':
        form = PlayerInputForm(request.POST)
        if form.is_valid():
            try:
                data = form.cleaned_data

                # Encode categorical features to match training-time column names
                preferred_foot_enc = 1 if data['preferred_foot'] == 'Right' else 0
                work_rate_enc = hash(data['work_rate']) % 1000
                position_group_enc = hash(data['player_positions']) % 1000

                # Construct feature DataFrame in exact order
                features = pd.DataFrame([{
                    'age': data['age'],
                    'height_cm': data['height_cm'],
                    'weight_kg': data['weight_kg'],
                    'pace': data['pace'],
                    'shooting': data['shooting'],
                    'passing': data['passing'],
                    'dribbling': data['dribbling'],
                    'defending': data['defending'],
                    'physic': data['physic'],
                    'preferred_foot_enc': preferred_foot_enc,
                    'work_rate_enc': work_rate_enc,
                    'position_group_enc': position_group_enc
                }])

                # Make prediction
                prediction = model.predict(features)[0]
                prediction = round(prediction, 2)

            except Exception as e:
                error = f"Error making prediction: {str(e)}"
        else:
            error = "Please correct the errors below."
    else:
        form = PlayerInputForm()

    return render(request, 'predictor/predict.html', {
        'form': form,
        'prediction': prediction,
        'error': error
    })
