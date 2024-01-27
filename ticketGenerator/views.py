from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
import sys
from ticketGenerator.TicketGeneratorFile import ticket_generator
from ticketGenerator.models import Tambola
from ticketGenerator.errorClass import wrong_sets_input

@api_view(['POST'])
def generate_ticket_api(request):
    try:
        sets = request.data['sets']
        if isinstance(sets, int):
            ticket = ticket_generator().tambola_ticket_generator(sets)
            return Response({'ticket': ticket})
        else:
            raise wrong_sets_input("Wrong sets number")
    except Exception as e:
        print ("In generate_ticket_api")
        print (e)
        print ('Error on line {}'.format(sys.exc_info()[-1].tb_lineno))

@api_view(['GET'])
def get_tickets_data(request):
    try:
        all_data = Tambola.objects.all()
        page_number = int(request.GET.get('page'))
        items_per_page = 3
        start_index = (page_number - 1) * items_per_page
        end_index = start_index + items_per_page
        data_page = all_data[start_index:end_index]
        ticket_data = [{'Ticket': item.id, 'Data': item.json_data} for item in data_page]

        return JsonResponse({'data': ticket_data})
    except Exception as e:
        print ("In get_tickets_data")
        print (e)
        print ('Error on line {}'.format(sys.exc_info()[-1].tb_lineno))
    
