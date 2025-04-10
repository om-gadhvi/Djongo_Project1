from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
def studentViews(request):
    
    student = {
        'name': 'John Doe',
        'age': 20,
        'major': 'Computer Science'
    }
    return JsonResponse(student)