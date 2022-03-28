#from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Question, Answer

def index(request):
    #return HttpResponse("안녕하세요 xion에 오신것을 환영합니다.")
    """ 목록 출력 """
    question_list = Question.objects.order_by('-create_date')
    context = {'list': question_list}
    return render(request, 'xion/list.html', context)

def detail(request, question_id):
    """ 내용 출력 """
    question = Question.objects.get(id=question_id)
    context = {'question': question}
    return render(request, 'xion/detail.html', context)

def answer_create(request, question_id):
    """ pybo 답변등록 """
    question = get_object_or_404(Question, pk=question_id)
    answer = Answer(question=question, content=request.POST.get('content'), create_date=timezone.now())
    answer.save()
    #question.answer_set.create(content=request.POST.get('content'), create_date=timezone.now())
    return redirect('xion:detail', question_id=question.id)