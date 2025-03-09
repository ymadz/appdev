# Task Manager

This is the midterm project for CC105, a simple task management system built using Django.

## Project Setup

### 1. Create MySQL Database
Create a MySQL database named `taskdb`:
```sql
CREATE DATABASE taskdb;
```

### 2. Set Up Virtual Environment
Navigate to your project directory and activate the virtual environment:
```sh
venv\Scripts\activate  # Windows
source venv/bin/activate  # Mac/Linux
```

### 3. Migrate the Models
Run the following command to apply database migrations:
```sh
python manage.py migrate
```

### 4. Start the Django Project
Run the following command to start the Django server and click the link on the terminal to open the application:
```sh
python manage.py runserver
```
