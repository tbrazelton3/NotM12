from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.http import HttpResponse
#import matplotlib as pl
#pl.use('Agg')



def live(request):
#    tasks.keepPlotting()
    return render(request, 'graphs/livegraph.html')


    

#@background(schedule = 10)
#def keepPlotting():
#    stockList = ['MSFT', 'SPY', 'AAPL', 'NVDA']
#    while True:
#        Plot(random.sample(stockList, 2))

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/signup/success')
    else:
        form = UserCreationForm()
    return render(request, 'signup/signup.html', {'form': form})

def success(request):
    return render(request, 'signup/success.html')