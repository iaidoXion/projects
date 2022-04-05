from django.urls import path
from . import index

app_name = 'xion'

urlpatterns = [
    path('list/', index.list, name='list'),
    path('detail/<int:question_id>/', index.detail, name='detail'),
    path('answer/create/<int:question_id>/', index.answerCreate, name='answerCreate'),
    path('question/create/', index.questionCreate, name='questionCreate'),
    path('question/modify/<int:question_id>/', index.questionModify, name='questionModify'),
    path('question/delete/<int:question_id>/', index.questionDelete, name='questionDelete'),
    path('answer/modify/<int:answer_id>/', index.answerModify, name='answerModify'),
    path('answer/delete/<int:answer_id>/', index.answerDelete, name='answerDelete'),
    path('comment/create/question/<int:question_id>/', index.comment_create_question, name='comment_create_question'),
    path('comment/modify/question/<int:comment_id>/', index.comment_modify_question, name='comment_modify_question'),
    path('comment/delete/question/<int:comment_id>/', index.comment_delete_question, name='comment_delete_question'),
    path('comment/create/answer/<int:answer_id>/', index.comment_create_answer, name='comment_create_answer'),
    path('comment/modify/answer/<int:comment_id>/', index.comment_modify_answer, name='comment_modify_answer'),
    path('comment/delete/answer/<int:comment_id>/', index.comment_delete_answer, name='comment_delete_answer'),
]