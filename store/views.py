from django.shortcuts import render
from .models import *
from django.http import JsonResponse
import json
import datetime
from .utils import cookieCart, cartData, guestOrder

# Create your views here.
def store(request):
    data = cartData(request) # see utills.py
    cartItems = data['cartItems'] 
    products = Product.objects.all()
    context={'products': products,'cartItems':cartItems}

    print("Here are all the products we have....")
    print(context)
    
    return render(request,'store/store.html',context)

def cart(request):

    data = cartData(request) # see utills.py
    items = data['items']
    order = data['order']
    cartItems = data['cartItems']

    
    context={'items':items,'order':order,'cartItems':cartItems}
    return render(request,'store/cart.html',context)

#from django.views.decorators.csrf import csrf_exempt # csrf token required for any request to backend, being done to exempt the csrf token
#@csrf_exempt
def checkout(request):
    data = cartData(request) # see utills.py
    items = data['items']
    order = data['order']
    cartItems = data['cartItems']

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

from django.views.decorators.csrf import csrf_exempt # csrf token required for any request to backend, being done to exempt the csrf token
@csrf_exempt
def processOrder(request):
    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)

    if request.user.is_authenticated:
        customer = request.user.customer
        order,created=Order.objects.get_or_create(customer=customer,complete=False) # getting order that is attacehd to customer

    else: # guest user
        customer,order = guestOrder(request,data) # see utils.py
        
    
    total = float(data['form']['total'])
    order.transaction_id = transaction_id

    if total == order.get_cart_total:
        order.complete = True
    order.save()

    if order.shipping==True:
        ShippingAddress.objects.create(
            customer=customer,
            order=order,
            address=data['shipping']['address'],
            city=data['shipping']['city'],
            state=data['shipping']['state'],
            zipcode=data['shipping']['zipcode']
        )

    return JsonResponse("Payment was completed", safe=False)