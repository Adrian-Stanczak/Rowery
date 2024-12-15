import json, smtplib, os
from datetime import datetime



def rent_bike(customer_name:str, rental_duration:float):
    pass

def calculate_cost(rental_duration:float):
    
    rental_duration = float(input('Enter duration of your rental: '))

    if rental_duration > 0 and rental_duration <= 1:
        rental_duration = 10
    elif rental_duration > 1:
        rental_duration = 10 + (rental_duration - 1)* 5
    else:
        print('Define your rental duration correctly!')

calculate_cost()

def save_rental(rental):
    pass