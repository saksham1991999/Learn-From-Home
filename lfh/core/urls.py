from django.urls import path
from .views import HomeView

from . import views
app_name = 'core'


urlpatterns = [
    path('', HomeView, name='home'),

    path('tutor/profile', views.TutorProfileView, name='tutorprofile'),
    path('tutor/addlisting', views.AddListingView, name='addlisting'),
    path('tutor/viewlistings', views.ViewListingsView, name='addlisting'),
    path('tutor/deletelisting/<listingid>', views.DeleteListingView, name='deletelisting'),
    path('tutor/editlisting/<listingid>', views.EditListingView, name='editlisting'),
    path('tutor/classrequests/', views.TutorClassRequestView, name='studentclassrequests'),

    path('student/profile', views.TutorProfileView, name='studentprofile'),
    path('student/classrequests/', views.StudentClassRequestView, name='studentclassrequests'),
    path('tutor/<id>', views.TutorDetailtView, name='tutordetail'),
]
