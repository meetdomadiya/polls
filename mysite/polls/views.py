from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from .models import Question
# Create your views here.

def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {"latest_question_list": latest_question_list,}
    return render(request, "polls/index.html", context)

def about(request):
    #this is a simplest view possible in django. to call this view we need to configure url
    return HttpResponse("Hello world! My name is Meet!")

def detail(request,question_id):
    question = get_object_or_404(Question, pk = question_id)
    return render(request, "polls/detail.html", {"question":question})


def results(request, question_id):
    response = "You're looking at the result of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
