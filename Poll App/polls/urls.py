from django.conf.urls import url
from . import views

app_name = 'polls'
urlpatterns = [
    #example /polls/
    url(r'^$', views.IndexView.as_view(), name='index'),
    #example /polls/1/
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    #example /polls/1/results/
    url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
    #example /polls/1/vote/
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]