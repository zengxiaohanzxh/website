from django.shortcuts import render_to_response
from django.shortcuts import render, get_object_or_404

def view_wedding(request):
    return render(request, 'wedding.html',
                  {})
