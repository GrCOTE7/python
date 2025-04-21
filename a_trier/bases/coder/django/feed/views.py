from datetime import datetime
from django.shortcuts import render


# Create your views here.
def index(request):
    context = {
        "messages": [
            {"content": "Hello World 1", "username": "GC7.1", "created_at": datetime.now()},
            {"content": "Hello World 2", "username": "GC7.2", "created_at": datetime.now()},
            {"content": "Hello World 3", "username": "GC7.2", "created_at": datetime.now()},
        ]
    }
    return render(request, "index.html", context=context)
