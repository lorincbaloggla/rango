from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def index(request):
    # Construct a dictionary to pass to the template engine as its context.
    # Note the key boldmessage is the same as {{ boldmessage }} in the template!
    context_dict = {'boldmessage': "Crunchy, creamy, cookie, candy, cupcake!"}
    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.
    return render(request, 'rango/index.html', context=context_dict)
    #response = HttpResponse("Rango says hey there partner!")
    #response.write("<br/> <a href='/rango/about/'>About</a>")
    #return response
    #return HttpResponse("Rango says hey there partner!")

def about(request):
    context_dict = {'boldmessage': "We don't really need this..."}
    return render(request, 'rango/about.html', context=context_dict)
    #response = HttpResponse("Rango says here is the about page.")
    #response.write("<br/> <a href='/rango/'>Index</a>")
    #return response
    #return HttpResponse("Rango says here is the about page.")
