# Player Performance Prediction Using XGBoost

This project aims to predict the overall rating of a player based on various attributes such as Pace, Shooting, Passing, Dribbling, Defending, and Physic. The project uses **XGBoost** to train a model and then serves the prediction through a **Django web application**.

## Features

- **Player Performance Prediction**: Predicts the overall performance rating of a player based on key attributes using XGBoost.
- **Django Web Interface**: Provides an intuitive UI for inputting player attributes and viewing predicted ratings.
- **Form Validation**: Ensures that all input fields are correctly filled and provides feedback to users if any fields are left empty.
- **Model Serialization**: The trained model is serialized using **Pickle** and loaded in the backend for prediction.

## Prerequisites

Before running the application, make sure you have the following installed:

- Python 3.x
- MySQL (for database storage)
- Django 3.x+
- XGBoost
- scikit-learn
- pandas
- numpy
- matplotlib (optional for visualizations)
- Bootstrap 5.x (for UI styling)

## Installation

1. **Clone the repository**:

   ```bash
   git clone [https://github.com/yourusername/player-performance-prediction.git](https://github.com/ymadz/appdev)
   ```

2. **Set up a virtual environment**:

   ```bash
   python3 -m venv venv
   source venv/bin/activate   # For Linux/Mac
   venv\Scripts\activate      # For Windows
   ```

3. **Install dependencies**:

   Use terminal to install the listed dependencies on top.

4. **Set up the database**:

   - Create a MySQL database (playerperformancedb) and configure your settings in `settings.py`.
   - Run Django migrations to set up the database:

   ```bash
   python manage.py migrate
   ```

5. **Train the model (optional)**:

   The XGBoost model can be trained using the provided script. Run the following to train and pickle the model:

   ```bash
   python train_model.py
   ```

   The model will be saved as `xgboost_fifa_model.pkl`.

6. **Run the development server**:

   ```bash
   python manage.py runserver
   ```

   The application should now be running at `http://127.0.0.1:8000/`.

## Usage

1. **Input Player Attributes**: Use the form to input the following attributes:
   - Pace
   - Shooting
   - Passing
   - Dribbling
   - Defending
   - Physic

2. **Get the Prediction**: After filling the form and submitting it, the model will predict the player's overall rating, which will be displayed below the form.

3. **Reset the Form**: Use the **Reset** button to clear the form and start over.

## Model Details

- **Model Type**: XGBoost
- **Input Features**: Pace, Shooting, Passing, Dribbling, Defending, Physic
- **Prediction Output**: Player's Overall Rating
