from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from .models import Question, Answer

# Create your views here.
def index(request):
	questions = Question.objects.all()
	answers = []
	for q in questions:
		answer = Answer.objects.filter(question = q).order_by('-upvotes')[:1]
		answers.append(answer)
	context = {'answers': answers}
	return render(request, 'Poll_R_Bear/index.html', context)

def question(request, question_id):
	question = Question.objects.get(id=question_id)
	answers = Answer.objects.filter(question=question)
	context = {'question': question,
				'answers': answers }
	return render(request, 'Poll_R_Bear/question.html', context)

@csrf_exempt #TODO ask Shilad what to do about this problem 
def add_question(request):
	if (request.POST and request.POST['question']):
		question = request.POST['question']
		q = Question(text=question)
		q.save()
		return HttpResponse('success')
	else: 
		return HttpResponse('failure')

@csrf_exempt #TODO ask Shilad what to do about this problem 
def add_answer(request):
	if (request.POST and request.POST['question_id'] and request.POST['answer']):
		question_id = request.POST['question_id']
		answer_text = request.POST['answer']
		q = Question.objects.filter(id = question_id)[0]
		a = Answer(text=answer_text, question=q)
		a.save()
		return HttpResponse('success')
	else: 
		return HttpResponse('failure')

#Useful link: http://django.cowhite.com/blog/working-with-url-get-post-parameters-in-django/