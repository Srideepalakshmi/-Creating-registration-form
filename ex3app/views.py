from django.shortcuts import render
from django import forms

# Create the registration form
class RegistrationForm(forms.Form):
    username = forms.CharField(label='Username', max_length=100)
    email = forms.EmailField(label='Email')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

def signup(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            return render(request, 'ex3app/success.html', {'username': username})
    else:
        form = RegistrationForm()

    return render(request, 'ex3app/signup.html', {'form': form})
