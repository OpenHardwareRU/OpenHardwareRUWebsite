
# Create your views here.

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .models import Choice, Question

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'homepage/index.html', context)

def about(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'homepage/about.html', context)

def shop(request):
    return render(request, 'homepage/shop.html')

def privacy(request):
    return render(request, 'homepage/privacy.html')

def terms(request):
    return render(request, 'homepage/terms.html')