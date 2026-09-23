# File: views.py
# Author: Gab Alingog (galingog@bu.edu), 09/22/2026
# Description: Stores the menu data and the functions for each of the web pages

from django.shortcuts import render
import random, time

# Main menu data
prices = {
    'sinigang': ('Sinigang', 22.00),
    'added': ('Extra Soup', 2.00),
    'tinola': ('Tinola', 20.00),
    'adobo': ('Adobo', 22.00),
    'nilaga': ('Nilaga', 20.00),
}

# Specials menu data
specials = {
    'mango': ('Mango Shake', 6.50),
    'flan': ('Leche Flan', 5.00),
    'sorbae': ('Sorbae', 3.50),
}

def main(request):
    '''Show the restaurant welcome page to the user'''
    template_name = 'restaurant/main.html'
    return render(request, template_name)

def order(request):
    '''Show the menu order form that will be submitted'''
    template_name = 'restaurant/order.html'

    # Randomized specials by indexing
    key1 = random.choice(list(specials.keys()))
    special1, price1 = specials[key1]

    context = {
        'key1': key1,
        'special1': special1,
        'price1': price1,
    }
    return render(request, template_name, context)

def confirmation(request):
    '''Show the confirmation receipt of a submitted order form'''
    template_name = 'restaurant/confirmation.html'
    
    # Only if the order form was submitted
    if request.POST:
        ordered = []
        total = 0.0

        # Iterates through the name and price of each item in the menu, alongside the input
        for x, (name, price) in prices.items():
            # If a valid menu item
            if x in request.POST:
                # Add the name and price to the list of what the user ordered
                ordered.append((name, price))
                # Add to the total price
                total += price

        # Another loop with same structure to account for specials
        for x, (name, price) in specials.items():
            if x in request.POST:
                ordered.append((name, price))
                total += price
        
        # Fetch the customer information
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        instructions = request.POST.get('instructions')

        # Random order time between 30 to 60 minutes converted to seconds
        time_later = random.randint(30, 60) * 60
        # Current time + the random computed time
        time_ready = time.ctime(time.time() + time_later)

        context = {
            'ordered': ordered,
            'total': total,
            'name': name,
            'phone': phone,
            'email': email,
            'instructions': instructions,
            'time_ready': time_ready,
        }

        return render(request, template_name, context)
    return render(request, 'restaurant/order.html')