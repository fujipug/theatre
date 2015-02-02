from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    #dictionary to be passed into the tepmlate render object.
    random_dictionary = {'testing': "this is a template test..."}
    #gets template from Template folder
    template = get_template('home.html')
    #fills in template tags with corresponing text from dicitonary
    html = template.render(Context(random_dictionary))
    return HttpResponse(html)