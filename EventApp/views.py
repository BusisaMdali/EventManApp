from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate , login, logout

from .forms import EventForm
from .models import Event

# Create your views here.

def home(request):
    return render(request,'home.html')

def register(request):
    if request.method == 'POST' :
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('LogIn')
    else:
        form = UserCreationForm()
    return render(request,'register.html', {'form':form})

def LogIn_view(request):
    if request.method == 'POST' :
        form = AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            userName = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request,username=userName,password=password)
            if user is not None :
                login(request, user)
                print('Log In Successfull')
                return redirect ('home')
            else:
                print('User not found')
        else:
            print(f'Form not valid {form.errors}')
    else:
        form = AuthenticationForm()
    return render(request,'login.html', {'form':form})

def add_Event(request):
    if request.method == 'POST':
        form = EventForm(request.POST,request.FILES)
        if form.is_valid():
            event = form.save(commit=False)
            event.organizer = request.user
            event.save()
            return redirect('event_list')
        else:
            print("Event is not valid")
    else:
        form = EventForm()
    return render(request, 'add_event.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('LogIn')

def event_list(request):
    event_list = Event.objects.all()
    return render(request,'event_list.html' ,{'events' : event_list} )

def edit_event(request,pk):
    event = get_object_or_404(Event,pk=pk)
    if request.method =='POST':
        form = EventForm(request.POST,request.FILES,instance=event)
        if form.is_valid():
            event = form.save()
            return redirect('event_list')
    else:
        event_form = EventForm(instance=event)
    return render(request,'add_event.html', {'form': event_form})

def delete_event(request,pk):
    event = get_object_or_404(Event,pk=pk)
    event.delete()
    return redirect('event_list')
        
def search(request):
    query = request.GET.get('query', '')
    print(query)
    events = Event.objects.filter(title=query.strip())
 
    print(f"about to print events: {events}")
    for event in events:
        print(event.title)
    
    return render(request,'event_list.html', {'events': events})

def event_detail(request, pk):
    event = get_object_or_404(Event, pk=pk)
    return render(request, 'event_detail.html', {'event': event})
