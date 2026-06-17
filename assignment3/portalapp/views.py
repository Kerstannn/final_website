from django.shortcuts import render
from .forms import RegistrationForm

def home(request):
    return render(request, 'portal/home.html')

def about(request):
    return render(request, 'portal/about.html')

def register(request):
    
    message = ""

    if request.method == "POST":
        form = RegistrationForm(request.POST)

        if form.is_valid():
            form.save()
            message = "Registration submitted successfully!"
            form = RegistrationForm()

    else:
        form = RegistrationForm()

    return render(request,
                  'portal/form.html',
                  {'form': form,
                   'message': message})