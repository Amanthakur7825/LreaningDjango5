from django.shortcuts import render
from datetime import datetime


class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age


def home(request):
    context = {
        "name": "Aman",
        "age": 23,
        "skill": ["java", "python", "django"],
        "user": User("kumar", 30),
        "blog": {
            "title": "Django Template Intro",
            "contact": "<b>this is bold</b>",
            "content": "<b>this is bold</b>",
            "created_at": datetime(2026, 10, 11, 10, 30),
        },
        "empty_value": None,
    }
    return render(request, 'blog/home.html', context)