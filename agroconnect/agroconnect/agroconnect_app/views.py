from django.shortcuts import render
from .forms import SignUpForm

def home(request):
    return render(request, 'agroconnect_app/home.html')

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to a success page or do something else
    else:
        form = SignUpForm()
    return render(request, 'agroconnect_app/signup.html', {'form': form})
