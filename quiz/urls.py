from django.urls import re_path
import quiz.views as quiz_views

urlpatterns = [
	re_path(r'^$', quiz_views.qpage),
]
