from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register,name='register'),
    path('LogIn/',views.LogIn_view,name='LogIn' ),
    path('add_Event/',views.add_Event,name='add_event'),
    path('Logout/',views.logout_view,name='logout'),
    path('event_list/',views.event_list,name='event_list'),
    path('edit_event/<int:pk>/',views.edit_event,name='edit_event'),
    path('delete_event/<int:pk>/',views.delete_event,name='delete_event'),
    path('search/',views.search,name='search'),
    path('event_detail/<int:pk>/',views.event_detail,name='event_detail'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)