import django_filters
from django import forms
from django.contrib.auth.models import User
from .models import Event

class EventFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(
        lookup_expr='icontains',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Search by title...'
        })
    )
    
    description = django_filters.CharFilter(
        lookup_expr='icontains',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Search in description...'
        })
    )
    
    location = django_filters.CharFilter(
        lookup_expr='icontains',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Search by location...'
        })
    )
    
    date = django_filters.DateFromToRangeFilter(
        widget=django_filters.widgets.RangeWidget(attrs={
            'class': 'form-control',
            'type': 'date'
        })
    )
    
    organizer = django_filters.ModelChoiceFilter(
        queryset=User.objects.all(),
        widget=forms.Select(attrs={
            'class': 'form-control'
        })
    )
    
    created = django_filters.DateFromToRangeFilter(
        widget=django_filters.widgets.RangeWidget(attrs={
            'class': 'form-control',
            'type': 'date'
        })
    )
    
    # Custom filter for events happening today
    happening_today = django_filters.BooleanFilter(
        method='filter_happening_today',
        widget=forms.CheckboxInput(attrs={
            'class': 'form-check-input'
        })
    )
    
    # Custom filter for upcoming events
    upcoming_events = django_filters.BooleanFilter(
        method='filter_upcoming_events',
        widget=forms.CheckboxInput(attrs={
            'class': 'form-check-input'
        })
    )

    class Meta:
        model = Event
        fields = ['title', 'description', 'location', 'date', 'organizer', 'created']

    def filter_happening_today(self, queryset, name, value):
        from django.utils import timezone
        if value:
            today = timezone.now().date()
            return queryset.filter(date=today)
        return queryset

    def filter_upcoming_events(self, queryset, name, value):
        from django.utils import timezone
        if value:
            today = timezone.now().date()
            return queryset.filter(date__gte=today)
        return queryset