from django.urls import path
from . import views


#http://127.0.0.1:8000/home
#http://127.0.0.1:8000/results
#http://127.0.0.1:8000/user_moredetail
#http://127.0.0.1:8000/



urlpatterns = [
    path("", views.home), #http://127.0.0.1:8000/
    path("home", views.home), #http://127.0.0.1:8000/
    path("results", views.results) #http://127.0.0.1:8000/
   
]