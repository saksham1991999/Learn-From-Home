from django.db import models
from django_countries.fields import CountryField
from phone_field import PhoneField
from django.conf import settings

gender_choices = (
    ('M', 'Male'),
    ('F', 'Female'),
    ('O', 'Other'),
)

class_choices = (
    ('6', 'Class 6'),
    ('7', 'Class 7'),
    ('8', 'Class 8'),
    ('9', 'Class 9'),
    ('10', 'Class 10'),
    ('11', 'Class 11'),
    ('12', 'Class 12'),
)

class_type_choices = (
    ('1-1', 'One-to-One Class'),
    ('1-n', 'One-to-Many Class'),
)

class languages(models.Model):
    language = models.CharField(max_length = 50)

    def __str__(self):
        return self.language

    class Meta:
        verbose_name_plural = 'Languages Spoken'

class subjects(models.Model):
    subject_name = models.CharField(max_length = 50)
    sub_detail = models.CharField(max_length = 500, blank = True, null = True)

    def __str__(self):
        return self.subject_name

    class Meta:
        verbose_name_plural = 'Subjects'
   
class notifications_type(models.Model):
    notifications_title = models.CharField(max_length = 20)

    def __str__(self):
        return self.notifications_title

    class Meta:
        verbose_name_plural = 'Notification Types'

class StudentProfile(models.Model):
    student = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default = 1)
    name = models.CharField(max_length = 100)
    dob = models.DateField(blank = True, null = True)
    gender = models.CharField(max_length = 1, choices = gender_choices)
    email = models.EmailField()
    phone_number = PhoneField(blank = True, null = True)
    skype_id = models.CharField(max_length = 15, blank = True, null = True)
    profile_pic = models.ImageField(blank = True, null = True)
    active = models.BooleanField(default=1)
    student_class = models.CharField(max_length = 5, choices = class_choices)
    school = models.CharField(max_length = 100, blank = True, null = True)
    board = models.CharField(max_length = 50, blank = True, null = True)
    notifications = models.ManyToManyField(notifications_type, blank = True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Students'

#name, dob, gender email phone_number skype_id profile_pic acctive class school board

class TutorProfile(models.Model):
    tutor = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default = 1)
    name = models.CharField(max_length = 100)
    dob = models.DateField(blank = True, null = True)
    gender = models.CharField(max_length = 1, choices = gender_choices)
    email = models.EmailField()
    phone_number = PhoneField()
    skype_id = models.CharField(max_length = 15)
    profile_pic = models.ImageField()
    active = models.BooleanField(default=1)
    identity_document = models.FileField()
    curriculum_vitae = models.TextField()
    about = models.TextField()
    languages_spoken = models.ManyToManyField(languages)
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Tutors'

class TimeSlots(models.Model):
    start_time = models.CharField(max_length = 10)
    end_time = models.CharField(max_length = 10)

    def __str__(self):
        slot = str(self.start_time) + ' - ' + str(self.end_time)
        return slot

    class Meta:
        verbose_name_plural = 'Time Slots'

class listings(models.Model):
    title = models.CharField(max_length = 100)
    tutor = models.ForeignKey(TutorProfile, on_delete=models.CASCADE)
    subject = models.ManyToManyField(subjects)
    student_class = models.CharField(max_length = 2, choices = class_choices)
    class_type = models.CharField(max_length = 5, choices = class_type_choices)
    hourly_rate = models.IntegerField()
    methodology = models.TextField(blank= True, null = True)
    details = models.TextField(blank= True, null = True)
    class_slot = models.ManyToManyField(TimeSlots)

    def __str__(self):
        return self.tutor.name

    class Meta:
        verbose_name_plural = 'Class Listings'

class class_request(models.Model):
    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE)
    listing = models.ForeignKey(listings, on_delete=models.CASCADE)
    time_slot = models.ForeignKey(TimeSlots, on_delete=models.CASCADE)
    date_time = models.DateTimeField()
    accepted_status = models.BooleanField(default=0)

    def __str__(self):
        lsiting_name = self.student.name + ' - ' + str(self.listing)
        return lsiting_name
    
    class Meta:
        verbose_name_plural = 'Class Requests'

class payment(models.Model):
    student = models.ForeignKey(StudentProfile, on_delete=models.SET_NULL, blank= True, null = True)
    listing = models.ForeignKey(listings, on_delete=models.SET_NULL, blank= True, null = True)
    date_time = models.DateTimeField()
    payment_id = models.CharField(max_length = 20)
    amount = models.IntegerField()

    def __str__(self):
        return self.student.name
    
    class Meta:
        verbose_name_plural = 'Payments'