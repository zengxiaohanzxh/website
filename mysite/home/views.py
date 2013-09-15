from django.shortcuts import render_to_response
from django.shortcuts import render, get_object_or_404
from datetime import date

def homepage(request):
    current_date = date.today()
    return render(request, 'home/home.html', {'current_date':current_date})
