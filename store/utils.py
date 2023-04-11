from django.shortcuts import render
from .models import *
from django.http import JsonResponse
import json
import datetime

def cookieCart(request):
    
    try:
        cart = json.loads(request.COOKIES['cart']) # getting cookies from request and parsing into python dict
        
    except:
        cart = {}

    print('cart: ', cart)
    items=[]     
    order={'get_cart_total':0,'get_cart_items':0,'shipping':False}
    cartItems = order['get_cart_items']
    for i in cart:
        try:
            cartItems+= cart[i]['quantity']

            product = Product.objects.get(id=i)
            total = product.price*cart[i]['quantity']

            order['get_cart_total']+=total
            order['get_cart_items']+=cart[i]['quantity']

            item={
                'product':{
                'id':product.id,
                'name': product.name,
                'price':product.price,
                'imageURL': product.imageURL,           
                },
                'quantity': cart[i]['quantity'],
                'get_total': total
            }

            items.append(item)

            if product.digital==False:
                order['shipping'] = True
        except:
            pass
    
    return {'cartItems':cartItems, 'order':order, 'items':items}


def cartData(request):
    if request.user.is_authenticated:
        customer= request.user.customer # taking details of child items, user.customer
        order,created=Order.objects.get_or_create(customer=customer,complete=False) # fetching orders of related customer
        items = order.orderitem_set.all() # fetching all items
        cartItems = order.get_cart_items
   
    else: # for not logged in user
        cookieData = cookieCart(request) # see utills.py
        items = cookieData['items']
        order = cookieData['order']
        cartItems = cookieData['cartItems']

       # items=[]     
       # order={'get_cart_total':0,'get_cart_items':0,'shipping':False}
       # cartItems = order['get_cart_items']
    
    return {'cartItems':cartItems, 'order':order, 'items':items} 

def guestOrder(request,data):
    print('user not authenticated')
    print("Cookies:", request.COOKIES)
    name = data['form']['name']
    email = data['form']['email']

    cookieData = cookieCart(request)
    items = cookieData['items']


    customer, created = Customer.objects.get_or_create(email=email) # taking on email attribute 
    customer.name = name
    customer.save() # saving unauthenticated customer

    order = Order.objects.create(customer=customer, complete=False)

    for item in items:
        product = Product.objects.get(id=item['product']['id'])
        orderItem = OrderItem.objects.create(product=product, order=order, quantity=item['quantity'])


    return customer,order

