from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from .models import Question
from django.http import Http404

def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5];
    #template = loader.get_template("index.html")
    context = {'latest_question_list' : latest_question_list}
    #output = ",".join([q.question_text for q in latest_question_list])
    #return HttpResponse(template.render(context, request))
    return render(request, "index.html", context)

# Create your views here.

def details(request, question_id):
    #try:
    #    question = Question.objects.get(pk=question_id)
    #except Question.DoesNotExist:
    #    raise Http404("Question does not exist")
    #return render(request, 'detail.html', {'question': question})
    #MAS LIMPIO:
    question = get_object_or_404(Question, pk = question_id)
    return render(request, "detail.html", {"question" : question, })

def results(request, question_id):
    response = "Resultts %s"
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("vote %s" % question_id)
