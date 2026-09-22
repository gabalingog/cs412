from django.shortcuts import render
import random, time

# Create your views here.
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
    return render(request, template_name)