# Task Manager

This is the midterm project for CC105, a simple task management system built using Django.

## Project Setup

### 1. Create MySQL Database
Create a MySQL database named `taskdb`:
```sql
CREATE DATABASE taskdb;
```

### 2. Set Up Virtual Environment
Navigate to the project directory (taskmanager) and activate the virtual environment:
```sh
venv\Scripts\activate  # Windows
source venv/bin/activate  # Mac/Linux
```

### 3. Install Django and MySQL Client
If Django and MySQL client are not installed, install them using:
```sh
pip install django mysqlclient
```

### 4. Migrate the Models
Run the following command to apply database migrations:
```sh
python manage.py migrate
```

### 5. Start the Django Project
Run the following command to start the Django server:
```sh
python manage.py runserver
```
