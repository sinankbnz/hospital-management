from django.urls import path
from . import views
urlpatterns=[
    path('',views.index,name='index'),
    path('index/',views.index,name='index'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('booking/',views.booking,name='booking'),
    path('departments/',views.departments,name='departments'),
    path('doctors/',views.doctors,name='doctors'),
]