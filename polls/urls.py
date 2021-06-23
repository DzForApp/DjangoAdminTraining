from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^(?P<question_id>[0-9]+)/$',  views.detail, name="detail"),
    #localhost:8080/polls/1
    url(r'^(?P<question_id>[0-9]+)/results$',  views.results, name="results"),
    #localhost:8080/polls/1/results
    url(r'^(?P<question_id>[0-9]+)/vote$',  views.vote, name="vote"),
    #localhost:8080/polls/1/vote
]