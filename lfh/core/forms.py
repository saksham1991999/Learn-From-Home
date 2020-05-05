from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget
from django.utils.translation import gettext_lazy as _

from core.models import (
    subjects,
    StudentProfile,
    TutorProfile,
    TimeSlots,
    listings,
    payment,
)

class StudentProfileForm(forms.ModelForm):

    class Meta:
        model = StudentProfile
        fields = [
            'profile_pic',
            'name',
            'dob', 
            'gender', 
            'email', 
            'phone_number',
            'skype_id',
            'student_class', 
            'school', 
            'board', 
            'notifications',]

        labels = {
            'name': _("Full Name"),
            'dob': _('Date of Birth'), 
            'gender' : _("Gender"), 
            'email': _('Email ID'), 
            'phone_number': _('Phone Number'),
            'skype_id': _('Skype ID'),
            'profile_pic': _('Profile Pic'), 
            'student_class': _('Class'), 
            'school': _('School'), 
            'board': _('School Board'), 
            'notifications': _('Notidfications Type'),
        }

class TutorProfileForm(forms.ModelForm):

    class Meta:
        model = TutorProfile
        fields = [
            'profile_pic',
            'name',
            'dob', 
            'gender', 
            'email', 
            'phone_number',
            'skype_id',
            'identity_document', 
            'curriculum_vitae', 
            'about', 
            'languages_spoken',
            ]

        labels = {
            'name': _("Full Name"),
            'dob': _('Date of Birth'), 
            'gender' : _("Gender"), 
            'email': _('Email ID'), 
            'phone_number': _('Phone Number'),
            'skype_id': _('Skype ID'),
            'profile_pic': _('Profile Pic'), 
            'identity_document': _('Identity Document'), 
            'curriculum_vitae': _('C.V.'), 
            'about': _('About'), 
            'languages_spoken': _('Languages Spoken'),
        }

class ListingsForm(forms.ModelForm):

    class Meta:
        model = listings
        fields = [
            'title',
            'subject', 
            'student_class', 
            'class_type', 
            'hourly_rate',
            'methodology',
            'details', 
            'class_slot', 
            ]

        labels = {
            'title': _('Title'),
            'subject':_('Subject'), 
            'student_class':_('Class'), 
            'class_type':_('Class Session Type'), 
            'hourly_rate':_('Hourly Rate'),
            'methodology':_('Methodology'),
            'details':_('Details'), 
            'class_slot':_('Class Slot'), 
        }
