<!DOCTYPE html>
<html lang="en">
<head>
    <title>Delete Task</title>
</head>
<body>
    <h1>Confirm Delete</h1>
    <p>Are you sure you want to delete the task: <strong>{{ task.title }}</strong>?</p>
    <form method="post">
        {% csrf_token %}
        <button type="submit">✅ Yes, Delete</button>
        <a href="{% url 'task_list' %}">❌ Cancel</a>
    </form>
</body>
</html>
