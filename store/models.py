from django.db import models
from django.contrib.auth.models import User

class Customer(models.Model):
    user =models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    '''
    OneToOneField implies that a User can have only one Customer and Customer can have only one User 
    on_delete=models.CASCADE if the User is deleted, this item will also be deleted
    blank: determines whether the field should be validated as required or not in forms. False means the form will generate an error if not provided, while True means empty values are allowed.
    null: determines whether the field should be set as NULL or NOT NULL at the DB level. This has nothing to do with form validation.
    '''

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=200, null=True)
    price = models.DecimalField(max_digits=7,decimal_places=2)
    digital = models.BooleanField(default=False,null=True,blank=False)
    image= models.ImageField(null=True,blank=True)

    def __str__(self):
        return self.name
    
    # if an image is not present, we'll get an error
    # as we fetching image with url.
    # to prevent that, this function is created.
    # using @property decorator, a function can be used as an attribute
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url=''
        
        return url

class Order(models.Model):
    customer= models.ForeignKey(Customer,on_delete=models.SET_NULL,null=True, blank=True)
    data_ordered=models.DateTimeField(auto_now_add=True) # will set current date time
    complete = models.BooleanField(default=False,null=True, blank=False)
    transaction_id=models.CharField(max_length=200,null=True)    

    '''
    ForeignKey implies that a Customer can have multiple Orders but one Order can be associated with one Customer only
    on_delete=models.SET_NULL means if the owner of an existing object got deleted set this field for existing object to null.

    '''

    def __str__(self):
        return str(self.id)
    
    @property
    def shipping(self):
        shipping = False
        orderitem=self.orderitem_set.all()
        for i in orderitem:
            if i.product.digital == False:

                 shipping = True
            print(f'shipping : ',shipping)
        return shipping
    
    @property
    def get_cart_total(self):
        orderitem=self.orderitem_set.all()
        total= sum([item.get_total for item in orderitem])
        return total
    
    @property
    def get_cart_items(self):
        orderitem=self.orderitem_set.all()
        total= sum([item.quantity for item in orderitem])
        return total


    

class OrderItem(models.Model):
    product=models.ForeignKey(Product,on_delete=models.SET_NULL,null=True, blank=True)
    order = models.ForeignKey(Order,on_delete=models.SET_NULL,null=True, blank=True)
    quantity=models.IntegerField(default=0,null=True,blank=True)
    date_added=models.DateTimeField(auto_now_add=True)

    @property
    def get_total(self):
        total=self.product.price*self.quantity
        return total


class ShippingAddress(models.Model):
    customer= models.ForeignKey(Customer,on_delete=models.SET_NULL,null=True, blank=True)
    order = models.ForeignKey(Order,on_delete=models.SET_NULL,null=True, blank=True)
    address = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=200, null=True)
    state = models.CharField(max_length=200, null=True)
    zipcode = models.CharField(max_length=200, null=True)
    date_added=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address