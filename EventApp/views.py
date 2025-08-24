from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate , login, logout
from django.core.paginator import Paginator

from .forms import EventForm
from .models import Event
from .filters import EventFilter

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
    """
    View to display all events with filtering capabilities
    """
    events = Event.objects.all()
    event_filter = EventFilter(request.GET, queryset=events)
    filtered_events = event_filter.qs
    
    # Add pagination
    paginator = Paginator(filtered_events, 12)  # Show 12 events per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'events': page_obj,
        'filter': event_filter,
        'total_events': filtered_events.count(),
        'showing_filtered': bool(request.GET),
    }
    
    return render(request, 'event_list.html', context)

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
