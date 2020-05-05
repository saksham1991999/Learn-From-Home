from rest_framework import serializers
from . import models as coremodels
from django.contrib.auth.models import User

class LanguageSerializer(serializers.ModelSerializer):

    class Meta:
        model = coremodels.languages
        fields = '__all__'


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = coremodels.subjects
        fields = '__all__'


class NotificationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = coremodels.notifications_type
        fields = '__all__'



class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']

class StudentProfileSerializer(serializers.ModelSerializer):
    # student = UserSerializer(many=False)
    # notifications = NotificationsSerializer(many=True)

    class Meta:
        model = coremodels.StudentProfile
        fields = "__all__"


class TutorProfileSerializer(serializers.ModelSerializer):
    # tutor = UserSerializer(many=False)
    # languages_spoken = LanguageSerializer(many=True)

    class Meta:
        model = coremodels.TutorProfile
        fields = "__all__"


class TimeSlotsSerializer(serializers.ModelSerializer):
    class Meta:
        model = coremodels.TimeSlots
        fields = '__all__'


class ListingsSerializer(serializers.ModelSerializer):
    # tutor = TutorProfileSerializer(many=False)
    # subject = SubjectSerializer(many=True)
    # class_slot = TimeSlotsSerializer(many=True)

    class Meta:
        model = coremodels.listings
        fields = "__all__"


class ClassRequestSerializer(serializers.ModelSerializer):
    # student = StudentProfileSerializer(many=False)
    # listing = ListingsSerializer(many=False)
    # time_slot = TimeSlotsSerializer(many=False)

    class Meta:
        model = coremodels.class_request
        fields = "__all__"


class PaymentSerializer(serializers.ModelSerializer):
    # student = StudentProfileSerializer(many=False)
    # listing = ListingsSerializer(many=False)

    class Meta:
        model = coremodels.payment
        fields = "__all__"
