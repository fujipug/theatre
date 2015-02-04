from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse
from django.shortcuts import render
from polls.models import Performance, Movie

def home(request):
    #dictionary to be passed into the tepmlate render object.
    Performance_array = Performance.objects.all()
    Movie_array = Movie.objects.all()
    Performance_dictionary = {'performance': Performance_array[0].date}
    random_dictionary = {'testing': Movie_array[0].name}
    #gets template from Template folder
    template = get_template('home.html')
    #fills in template tags with corresponing text from dicitonary
    html = template.render(Context(random_dictionary))
    return HttpResponse(html)

def merch(request):
    return render(request, 'merch.html')

def tickets(request):
    return render(request, 'tickets.html')

def upcoming_performances(request):
    Performance_array = Performance.objects.all()
    Performance_dictionary = {'performance': Performance_array[0].date}
    template = get_template('upcoming_performances.html')
    html = template.render(Context(Performance_dictionary))
    return HttpResponse(html)

def home_nontest_v(request):
    return render(request, 'home_nontest_v.html')    
    


#how to add entry to database:
    #1. from CMD "python manage.py shell"
    #2. from polls.models import Performance, Movie (or whatever table you want to work on)
    #3. new_addition = Performance(name="balh", date="12/12/1212", etc for all the fields)
    #4. new_addition.save() grats you added an entry to the database

#how to remove entry from the database:
    #1. from CMD "python manage.py shell"
    #2. from polls.models import Performance, Movie (or whatever table you want to work on)
    #3. new_array = Performance.objects.all()
    #4. new_array (this will list out all the elements in the array, find the one you want to delete)
    #5. new_array[3].delete() (this assumes you want to delete the fourth entry in the Performance)

#how to add table to the database:
    #1. Open polls\models.py
    #2. Create a new model (each model acts as a table)
    #3. from CMD "python manage.py check"
    #4. STOP if you have any errrors
    #5. "python manage.py migrate"
