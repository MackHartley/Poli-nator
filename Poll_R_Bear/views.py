from django.shortcuts import render
from django.http import HttpResponse

from .models import Question, Answer

# Create your views here.
def index(request):
	questions = Question.objects.all()
	res = ""
	for q in questions:
		answers = Answer.objects.filter(question = q)
		res += str(q)
		res = res + '\n\t' + ', '.join([str(a) for a in answers])
	return HttpResponse(res) 

#def addQuestion(request):

#Useful link: http://django.cowhite.com/blog/working-with-url-get-post-parameters-in-django/