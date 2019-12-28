from django.shortcuts import render, get_object_or_404, redirect
from django.core.mail import send_mail
from django.core.paginator import Paginator
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from datetime import date

from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.db.models import Count
from django.urls import reverse

from . import models, forms

def HomeView(request):
    all_classes = models.class_choices
    all_subjects = models.subjects.objects.all()
    all_tutors = models.TutorProfile.objects.all()
    all_listing = models.listings.objects.all()

    search_term = ''
    
    if 'subject' in request.GET:
        selected_subject = request.GET.get('subject')
        all_listing = all_listing.filter(subject = selected_subject)

    if 'class' in request.GET:
        selected_class = request.GET.get('class')
        all_listing = all_listing.filter(student_class = selected_class)
    
    if 'search' in request.GET:
        search_term = request.GET['search']
        all_listing = all_listing.filter(subject__icontains = search_term, class__icontains = search_term)

    paginator = Paginator(all_listing, 10)

    page = request.GET.get('page')
    all_listing = paginator.get_page(page)

    get_dict_copy = request.GET.copy()
    params = get_dict_copy.pop('page', True) and get_dict_copy.urlencode()
    context = {
        'subjects': all_subjects,
        'classes': all_classes,
        'listings': all_listing,
        'params': params, 
        'search_term': search_term
    }
    return render(request, 'index.html', context)

def TutorsView(request, tutorid):
    tutors = models.TutorProfile.objectsall()
    context = {
        'tutors': tutors,
    }
    return render(request, 'index.html', context)

def TutorDetailView(request, tutorid):
    tutor = get_object_or_404(models.TutorProfile, id = tutorid)
    context = {
        'tutor': tutor,
    }
    return render(request, 'tutordetails.html', context)

def ListingDetailView(request, listingid):
    listing = get_object_or_404( models.listings, id = listingid )
    context = {
        'listing': listing,
    }
    return render(request, 'listingdetail.html', context)

@login_required
def StudentProfileView(request):
    currentstudentprofile = models.StudentProfile.objects.filter(student = request.user).first()
    if request.method == "POST":
        form = forms.StudentProfileForm(request.POST, instance=currentstudentprofile)
        if form.is_valid():
            form.student = request.user
            form.save()
            messages.success(
                request,
                'Details Saved Successfully',
                extra_tags='alert alert-success alert-dismissible fade show'
                )
            return redirect('core:studentprofile')
    else:
        form = forms.StudentProfileForm(instance = currentstudentprofile)
        context = {
            'form': form,
        }
        return render(request, 'student/studentprofile.html', context)

@login_required
def TutorProfileView(request):
    currenttutorprofile = models.TutorProfile.objects.filter(tutor = request.user).first()
    if request.method == "POST":
        form = forms.TutorProfileForm(request.POST, instance=currenttutorprofile)
        if form.is_valid():
            form.tutor = request.user
            form.save()
            messages.success(
                request,
                'Details Saved Successfully',
                extra_tags='alert alert-success alert-dismissible fade show'
                )
            return redirect('core:tutorprofile')
    else:
        form = forms.TutorProfileForm(instance = currenttutorprofile)
        context = {
            'form': form,
        }
        return render(request, 'tutor/tutorprofile.html', context)

@login_required
def AddListingView(request):
    if request.method == "POST":
        form = forms.ListingsForm(request.POST)
        if form.is_valid():
            new_listing = form(commit = False)
            tutorprofile = get_object_or_404(models.TutorProfile, tutor=request.user)
            new_listing.tutor = tutorprofile
            new_listing.save()
            messages.success(
                request,
                'Listing Added Successfully',
                extra_tags='alert alert-success alert-dismissible fade show'
                )
            return redirect('core:addlisting')
    else:
        form = forms.ListingsForm()
        context = {
            'form': form,
        }
        return render(request, 'tutor/tutoraddlisting.html', context)

@login_required
def ViewListingsView(request):
    tutorprofile = get_object_or_404(models.TutorProfile, tutor = request.user)
    listings = models.listings.objects.filter(tutor = tutorprofile)
    context = {
        'listings': listings,
    }
    return render(request, 'tutor/tutorlistings.html', context)

@login_required
def EditListingView(request, listingid):
    listing = get_object_or_404(models.listings, id=listingid)
    if request.user != listing.tutor:
        return redirect('/')

    if request.method == "POST":
        form = forms.ListingsForm(request.POST, instance = listing)
        if form.is_valid():
            form.save()
            messages.success(
                            request,
                            'Listing Editted Successfully',
                            extra_tags='alert alert-success alert-dismissible fade show'
                            )
            return redirect('core:home')
    else:
        form = forms.ListingsForm(instance=listing)

    context = {
        'form': form,
    }
    return render(request, 'edit_listing.html', context)

@login_required
def DeleteListingView(request, listingid):
    listing = get_object_or_404(models.listings, id = listingid)
    if request.user != listing.tutor:
        return redirect('/')

    if request.method == 'POST':
        listing.delete()
        messages.success(
                request,
                'Poll Deleted Successfully',
                extra_tags='alert alert-success alert-dismissible fade show'
                )
        return redirect('polls:home')

    context = {
        'listing': listing,
    }
    return render(request, 'delete_listing.html', context)

@login_required
def StudentClassRequestView(request):
    studentuser = get_object_or_404(models.StudentProfile, student = request.user)
    studentrequests = models.class_request.objects.filter(student = studentuser)
    context = {
        'studentrequests':studentrequests,
    }
    return render(request, 'index.html', context)

@login_required
def TutorClassRequestView(request):
    tutoruser = get_object_or_404(models.TutorProfile, student = request.user)
    listings = models.listings.objects.filter(tutor = tutoruser)
    classrequests = models.class_request.objects.all(listingset__in = listings)
    context = {
        'classrequests':classrequests,
    }
    return render(request, 'index.html', context)

