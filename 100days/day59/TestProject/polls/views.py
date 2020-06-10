from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from polls.models import Question, Choice
from django.utils import timezone

def index(request):
    return HttpResponse('你好，这是一个投票页面。')

# 定义视图方法
def add(request):
    question = Question(question_text='双十一你在哪个平台剁手？', pub_date = timezone.now())
    question.save()
    return HttpResponse("新增投票成功！")

def query(request):
    # 通过objects这个模型管理器的all()获得所有数据行，相当于SQL中的SELECT * FROM question
    questionList = Question.objects.all()
    # 获取单条数据
    question1 = Question.objects.get(id = 1)
    # 相当于 where id = 1
    question2 = Question.objects.filter(id = 1)
    # 按ID排序
    question3 = Question.objects.order_by('id')

    res = ""

    for q in questionList:
        res += str(q.id) + "." + q.question_text + "<br/>"
    return HttpResponse("查询所有选项：<br/>" + res)


def update(request):
    question1 = Question.objects.get(id = 2)
    question1.question_text = '天猫和京东你会选哪个？'
    question1.save()
    return HttpResponse('更新id=2:'+question1.question_text)


def delete(request):
    question1 = Question.objects.get(id = 2)
    question1.delete()
    return HttpResponse('删除id=2:'+question1.question_text)