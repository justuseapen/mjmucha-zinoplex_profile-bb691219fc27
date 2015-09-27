from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required
from json import dumps
from django.db.models import Q
from display.models import Profile, PPI_scorecard
# Create your views here.


#---- API code

@login_required()
def autocomplete(request, query):
    suggestions = Profile.objects.filter(Q(first_name__contains=query) | Q(last_name__contains=query))[:30]
    suggestions = [{'value' : suggestion.name()} for suggestion in suggestions]
    return HttpResponse(dumps(suggestions), content_type='application/json')

### Model serialization example
# def tasks_json(request):
#     tasks = Model.objects.all()
#     data = serializers.serialize("json", tasks)
#     return HttpResponse(data, content_type='application/json')