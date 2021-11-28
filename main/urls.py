from django.urls import path 
from . import views 

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
   
    path('projects/', views.ProjectListView.as_view(), name='projects'),      
    path('proj1/<int:pk>/', views.ProjectDetailView.as_view(), name='proj1'),  
    
    path('blog/', views.blog, name='blog'),
    path('singlepost/<int:pk>/', views.singlepost, name='singlepost'),

    path('contact/', views.contact, name='contact'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
]

