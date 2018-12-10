from django.contrib.auth.models import Group, User, Permission
from django.template.loader import get_template
from django.shortcuts import render_to_response
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render_to_response('index.html')

