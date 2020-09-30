from . import views
from django.urls import path
from django.conf.urls import url
from search.views import VideoList,Start

urlpatterns = [
    #path('upload/<int:claim_id>/<str:phone>/', views.upload_form, name='upload_form'),
    path('video/', VideoList.as_view()),
     path('register/', Start.as_view()),
]
