from django.shortcuts import render
from .models import *
from django.http import JsonResponse
import json

# Create your views here.
def store(request):

    if request.user.is_authenticated:
        customer= request.user.customer # taking details of child items, user.customer
        order,created=Order.objects.get_or_create(customer=customer,complete=False) # fetching orders of related customer
        items = order.orderitem_set.all() # fetching all items
        cartItems = order.get_cart_items
    else: # for not logged in user
        items=[]     
        order={'get_cart_total':0,'get_cart_items':0,'shipping':False}
        cartItems = order['get_cart_items']

    print("Clicked on store...")
    print("Getting all Product details from Store....")
    products = Product.objects.all()
    context={'products': products,'cartItems':cartItems}

    print("Here are all the products we have....")
    print(context)
    
    return render(request,'store/store.html',context)

def cart(request):

    if request.user.is_authenticated:
        customer= request.user.customer # taking details of child items, user.customer
        order,created=Order.objects.get_or_create(customer=customer,complete=False) # fetching orders of related customer
        items = order.orderitem_set.all() # fetching all items
        cartItems = order.get_cart_items
   
    else: # for not logged in user
        items=[]     
        order={'get_cart_total':0,'get_cart_items':0,'shipping':False}
        cartItems = order['get_cart_items']

    
    context={'items':items,'order':order,'cartItems':cartItems}
    return render(request,'store/cart.html',context)

def checkout(request):
    if request.user.is_authenticated:
        customer= request.user.customer
        order,created=Order.objects.get_or_create(customer=customer,complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
     
    else: # for not logged in user
        items=[]     
        order={'get_cart_total':0,'get_cart_items':0,'shipping':False}
        cartItems = order['get_cart_items']

    context={'items':items,'order':order,'cartItems':cartItems}
    return render(request,'store/checkout.html',context)

def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']


    customer = request.user.customer # getting logged in customer
    product = Product.objects.get(id=productId) # getting product with the productId sent through JSON
    order,created=Order.objects.get_or_create(customer=customer,complete=False) # getting order that is attacehd to customer
    orderItem,created = OrderItem.objects.get_or_create(order=order,product=product) # getting order items if available, 
    orderItem.save()

    if action=='add':
        orderItem.quantity = (orderItem.quantity+1)

    elif action=='remove':
        orderItem.quantity = (orderItem.quantity-1)
    
    orderItem.save()

    if orderItem.quantity <=0:
        orderItem.delete()
   


    return JsonResponse("Item was added", safe=False) # safe=False, if we don't want to confirm anything