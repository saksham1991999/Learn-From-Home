from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views as tokenviews
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from core import views


router = DefaultRouter()
router.register('users' , views.UsersAPIViewSet, basename='user')
router.register('languages' , views.LanguagesAPIViewSet, basename='language')
router.register('subjects' , views.SubjectsAPIViewSet, basename='subject')
router.register('notifications' , views.NotificationsAPIViewSet, basename='notification')
router.register('student-profiles' , views.StudentProfileAPIViewSet, basename='student-profile')
router.register('tutors-profiles' , views.TutorProfileAPIViewSet, basename='tutors-profile')
router.register('time-slots' , views.TimeslotsAPIViewSet, basename='time-slot')
router.register('listings' , views.ListingAPIViewSet, basename='listing')
router.register('class-requests' , views.ClassRequestsAPIViewSet, basename='class-request')
router.register('payments' , views.PaymentsAPIViewSet, basename='payment')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls', namespace = 'core')),
    path('api/', include(router.urls), name='api'),
    path('api-auth/', include('rest_framework.urls')),
    path('api-token-auth/', tokenviews.obtain_auth_token),
    path('accounts/', include('allauth.urls')),
]

urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)