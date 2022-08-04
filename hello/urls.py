from django.urls import path
from . import views
urlpatterns =[
	path("",views.index, name="index"),
	path("khushi", views.khushi, name="khushi"),
	path("<str:name>", views.greet, name="greet")
]