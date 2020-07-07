from django.shortcuts import render
from django.http import HttpResponse
from .forms import RegistrationForm
from django.http import HttpResponseRedirect
# Create your views here.
def index(request):
    # response = HttpResponse()
    # response.writelines('<h1>Hello</h1>')
    # response.write("App cua tui")
    # return response
    return render(request, "pages/home.html")

def contact(request):
    # response = HttpResponse()
    # response.writelines('<h1>Hello</h1>')
    # response.write("App cua tui")
    # return response
    return render(request, "pages/contact.html")

def register(request):
    form = RegistrationForm
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.clean_save()
            return HttpResponseRedirect('/')
    return render(request, 'pages/register.html', {'form' : form})

def error(request, exception):
    return render(request, 'pages/error.html', {'message' : exception})