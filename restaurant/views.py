from django.shortcuts import render
import random, time

prices = {
    'sinigang': ('Sinigang', 22.00),
    'tinola': ('Tinola', 20.00),
    'adobo': ('Adobo', 22.00),
    'nilaga': ('Nilaga', 20.00),
    'mango': ('Mango Shake', 6.5),
    'flan': ('Leche Flan', 5.00),
}

def main(request):
    '''Show the form to the user'''
    template_name = 'restaurant/main.html'
    return render(request, template_name)

def order(request):
    '''Show the form to the user'''
    template_name = 'restaurant/order.html'
    return render(request, template_name)

def confirmation(request):
    '''Show the form to the user'''
    template_name = 'restaurant/confirmation.html'
    
    if request.POST: # if it exists
        ordered = []
        total = 0.0

        for x, (name, price) in prices.items():
            if x in request.POST:
                ordered.append({name, price})
                total += price
            
        name = request.POST.get('name','')
        phone = request.POST.get('phone','')
        email = request.POST.get('email','')
        instructions = request.POST.get('instructions','')

        time_later = random.randint(30, 60) * 60
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