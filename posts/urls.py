from django.urls import path
from .import views

urlpatterns = [
    path("",views.index, name = 'index'),
    path("login",views.login, name="login"),
    path("register",views.register, name = 'register'),
    path('logout',views.logout,name= 'logout'),
    path('post1/<str:pk>',views.post1,name='post1'),

]