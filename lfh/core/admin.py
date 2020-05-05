from django.contrib import admin
from .models import (
    languages,
    subjects,
    notifications_type,
    StudentProfile,
    TutorProfile,
    TimeSlots,
    listings,
    class_request,
    payment,
)

class StudentProfileAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'gender',
        'student_class',
    ]
    list_filter = [
        'name',
        'gender',
        'student_class',
        'dob',
        'board',
    ]
    search_fields = [
        'name',
        'gender',
        'student_class',
        'school',
        'board',
        'email',
    ]

class TutorProfileAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'gender',
    ]
    list_filter = [
        'name',
        'gender',
        'dob',
    ]
    search_fields = [
        'name',
        'gender',
        'email',
        'curriculum_vitae',
        'about',
        'skype_id',
    ]

class listingsAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'tutor',
    ]
    list_filter = [
        'tutor',
        'subject',
        'student_class',
        'class_type',
    ]
    search_fields = [
        'tutor',
        'subject',
        'student_class',
        'details',
    ]

class class_requestAdmin(admin.ModelAdmin):
    list_display = [
        'student',
        'listing',
    ]
    list_filter = [
        'student',
        'listing',
        'time_slot',
    ]
    search_fields = [
        'student',
        'listing',
    ]

class paymentAdmin(admin.ModelAdmin):
    list_display = [
        'student',
        'listing',
        'payment_id',
        'amount',
    ]
    list_filter = [
        'student',
        'listing',
    ]
    search_fields = [
        'student',
        'listing',
        'payment_id',
    ]

admin.site.register(languages)
admin.site.register(subjects)
admin.site.register(notifications_type)
admin.site.register(TimeSlots)

admin.site.register(StudentProfile, StudentProfileAdmin)
admin.site.register(TutorProfile, TutorProfileAdmin)
admin.site.register(listings, listingsAdmin)
admin.site.register(class_request, class_requestAdmin)
admin.site.register(payment, paymentAdmin)