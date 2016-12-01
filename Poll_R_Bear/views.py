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

def question(request, question_id):
	question = Question.objects.get(id=question_id)
	answers = Answer.objects.filter(question=question)
	context = {'question': question,
				'answers': answer }
    return render(request, 'Poll_R_Bear/question.html', context)


#def addQuestion(request):

#Useful link: http://django.cowhite.com/blog/working-with-url-get-post-parameters-in-django/