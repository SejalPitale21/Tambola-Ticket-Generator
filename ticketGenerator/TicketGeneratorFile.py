import pandas as pd
import numpy as np
import sys
from ticketGenerator.models import Tambola
from datetime import datetime, timezone
from django.db import IntegrityError
from django.http import JsonResponse


class ticket_generator():
    def __init__(self):
        pass
    
    def lists_match(self,dict_obj, key1, key2):
        """
        Check if two lists are equal, element-wise.

        Parameters:
            dict_obj (dict): The dictionary to search in.
            key1 (str): The first key to search for.
            key2 (str): The second key to search for.

        Returns:
            bool: Whether the two lists match, element-wise.
        """
        
        try:
            if key1 in dict_obj and key2 in dict_obj:
                list1 = dict_obj[key1]
                list2 = dict_obj[key2]

                # Check if lists match element-wise
                return all(x == y for x, y in zip(list1, list2))
            else:
                return False
            
        except Exception as e:
            print ("In lists_match")
            print (e)
            print ('Error on line {}'.format(sys.exc_info()[-1].tb_lineno))
            
    
    def tambola_ticket_generator(self, sets):
        """
        This function generates a json object with the given parameters.

        Parameters:
        sets (int): The number of sets to generate.

        Returns:
        data_json (dict): The generated json object.

        """
        try:
            start = [0,1,11,21,31,41,51,61,71,81,91]
            end = [0,9,19,29,39,49,59,69,79,89,99]
            data_json = {}
            for k in range(1, sets+1):
                for i in range(1,6 + 1):
                    self.generate_json(i, k, start, end,data_json)
            
            return data_json
        
        except IntegrityError as e:
            print ("In generate_json")
            print (e)
            print ('Error on line {}'.format(sys.exc_info()[-1].tb_lineno))
            return {'error': 'Duplicate key violation', "status":400}
        
        except Exception as e:
            print ("In tambola_ticket_generator")
            print (e)
            print ('Error on line {}'.format(sys.exc_info()[-1].tb_lineno))
            
    
    def generate_json(self, i, k, start, end,data_json):
        """
        This function generates a json object with the given parameters.

        Parameters:
        i (int): The set number.
        k (int): The ticket number.
        start (list): The starting numbers for each set.
        end (list): The ending numbers for each set.
        data_json (dict): The existing json object.

        Returns:
        None: This function does not return any values.

        """
        try:
            df = pd.DataFrame(columns = [1,2,3,4,5,6,7,8,9])
            
            st = str(k) + str(i)
            index_numebr = list(np.random.choice(range(1, 9 + 1), size=5, replace=False))
            
            for j in index_numebr:
                df[j] = np.sort(list(np.random.choice(range(start[j], end[j] + 1), size=3, replace=False)))
                
            df = df.fillna(0)
            
            if i>=2:
                match=self.lists_match(data_json,str(k) + str(i-1), st)
                if match:
                    self.generate_json(i,k, data_json, start, end)
                    
            data_json[st] = df.to_numpy().tolist()
            current_time = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S')
            
            Tambola.objects.create(id = st, created_at = current_time,json_data = df.to_numpy().tolist())
        
        except IntegrityError as e:
            print ("In generate_json")
            print (e)
            print ('Error on line {}'.format(sys.exc_info()[-1].tb_lineno))
            raise #return JsonResponse({'error': 'Duplicate key violation'}, status=400)
            
        except Exception as e:
            print ("In generate_json")
            print (e)
            print ('Error on line {}'.format(sys.exc_info()[-1].tb_lineno))
        
    