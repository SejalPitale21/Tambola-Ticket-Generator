# tickets/urls.py
from django.urls import path
from ticketGenerator.views import generate_ticket_api, get_tickets_data

urlpatterns = [
    path('generate-ticket/', generate_ticket_api, name='generate_ticket_api'),
    path('get_tickets_data/', get_tickets_data, name='get_tickets_data')
]
