from django.shortcuts import render, redirect, render_to_response, HttpResponse, Http404
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.db.models import Q
# Create your views here.
from .models import Profile, WorkExperience, PPI_scorecard


@login_required()
def home(request):
    context = {'pagetitle' : 'Zinoplex Dashboard'}
    return render(request, 'display/index.html', context)

@login_required()
def profile_e(request): # with no id given - own profile, if exists
    try:
        p = Profile.objects.get(user_account=request.user.pk)
        return profile(request, p.pk)
    except:
        return profile(request, None)

@login_required()
def profile_s(request,query): # with name given
    try:
        q = query.split(' ')
        p = Profile.objects.get(Q(first_name__contains=q[0]) & Q(last_name__contains=q[1]))
        return profile(request, p.pk)
    except:
        return profile(request, None)

@login_required()
def profile(request, profile_id):
    try:
        p = Profile.objects.get(pk = profile_id)
        experiences = WorkExperience.objects.filter(user_profile=profile_id)
        try:
            ppi = PPI_scorecard.objects.get(user_profile=p)
        except:
            ppi={}
        context = {'pagetitle' : 'Profile',
                   'profile' : {
                            'name' : p.name(),
                            'email' : p.email,
                            'picture_url' : p.picture_url,
                            'work_experience' : experiences,
                            'sc' : ppi
                        }
                   }
    except Exception as e:
        context = {'pagetitle' : 'Profile',
               'profile' : {
                        'name' : e,
                        'email' : 'jb@zee.de'
                    }
               }

    return render(request, 'display/profile.html', context)
