from django.shortcuts import render, HttpResponse 

# Create your views here.
def index(request):
    context = {
        'variable': "Sent OK"
    }
    return render(request, "index.html", context)
    # return HttpResponse("Homepage")

def about(request):
    return HttpResponse("About")

def services(request):
    return HttpResponse("Services")

def contact(request):
    return HttpResponse("Contact")