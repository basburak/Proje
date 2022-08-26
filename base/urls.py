from django.urls import URLPattern, path
from. import views


urlpatterns=[

    path("",views.home,name="home"),
    path("room/<str:pk>",views.room,name="room")

]