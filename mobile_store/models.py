from django.db import models
from django.conf import settings

# Create your models here.

ram_choices = (("4GB","4GB"),("6GB","6GB"),("8GB","8GB"))
rom_choices = (("64GB","64GB"),("128GB","128GB"),("256GB","256GB"))
front_cam_choices = (("8px","8px"),("16px","16px"))
back_cam_choices = (("16px","16px"),("32px","32px"),("64px","64px"),("108px","108px"))
network_choices = (("4G","4G"),("5G","5G"))
class Mobile(models.Model):
    name = models.CharField(max_length=100,default=None)
    price = models.IntegerField(default=None)
    description =models.TextField(max_length=500,default=None)
    previewImage = models.ImageField(upload_to="mobile_images/",default=None)
    discountPrice = models.IntegerField(default=None)
    Process = models.CharField(max_length=100,default=None)
    def __str__ (self):
        return f"{self.id}-{self.name}"
    

class Ram(models.Model):
    ram = models.CharField(max_length=100,choices=ram_choices,default=None)
    mobile = models.ForeignKey(Mobile, on_delete=models.CASCADE, related_name="ram")
    def __str__ (self):
        return f"{self.mobile.name}-{self.ram}"
    

class Rom(models.Model):
    rom = models.CharField(max_length=100,choices = rom_choices,default=None)
    mobile = models.ForeignKey(Mobile, on_delete=models.CASCADE, related_name="rom")
    def __str__ (self):
        return f"{self.mobile.name}-{self.rom}"
    

class Front_cam(models.Model):
    front_cam = models.CharField(max_length=100,choices = front_cam_choices,default=None)
    mobile = models.ForeignKey(Mobile, on_delete=models.CASCADE, related_name="front_cam")
    def __str__ (self):
        return f"{self.mobile.name}-{self.front_cam}"
    

class back_cam(models.Model):
    back_cam = models.CharField(max_length=100,choices = back_cam_choices,default=None)
    mobile = models.ForeignKey(Mobile, on_delete=models.CASCADE, related_name="back_cam")
    def __str__ (self):
        return f"{self.mobile.name}-{self.back_cam}"
    

class mobileImage(models.Model):
    image = models.ImageField(upload_to="mobile_images/")
    mobile = models.ForeignKey(Mobile, on_delete=models.CASCADE, related_name="images")
    def __str__ (self):
        return f"{self.mobile.name}-{self.image}"
    

class Network(models.Model):
    mobile_network = models.CharField(max_length=10,choices=network_choices,default=None)
    mobile = models.ForeignKey(Mobile, on_delete=models.CASCADE, related_name="mobile_network")
    def __str__ (self):
        return f"{self.mobile.name}-{self.mobile_network}"
    


class wishlist(models.Model):
    mobile = models.ForeignKey(Mobile, on_delete=models.CASCADE, related_name="wishlist")
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="wishlist",
        default=None,
    )

    def __str__(self):
        return f"{self.mobile.name} - {self.user.username}"
    

class Cart(models.Model):
    mobile = models.ForeignKey(Mobile, on_delete=models.CASCADE, related_name="cart")
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="cart",
        default=None,
    )
    quantity = models.IntegerField(default=1)
    price = models.IntegerField(null=True, blank=True)


    def __str__(self):
        return f"{self.mobile.name}-{self.mobile.id}"

class Checkout(models.Model):
    mobile = models.ForeignKey(Mobile,on_delete=models.CASCADE, related_name="checkout")
    

    def __str__(self):
        return f"{self.mobile.name}-{self.mobile.id}"

    
class address(models.Model):
    first_name = models.CharField(default=None)
    mobile_number = models.CharField(default=None)
    email = models.CharField(default=None)
    village = models.CharField(default=None)
    state = models.CharField(default=None)
    city = models.CharField(default=None)
    colony = models.CharField(default=None)
    pin_code = models.CharField(default=None)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="address",
        default=None,
    )

    def __str__(self):
 
        return self.user.username

    
class cart_orders(models.Model):

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="orders",
        default=None,
    )
    
    #order = models.ForeignKey(Cart,on_delete=models.CASCADE, related_name="order")
    #address = models.ForeignKey(address,on_delete=models.CASCADE, related_name="address")
    
    mobile_name = models.CharField(default="N/A")
    quantity = models.CharField(default="N/A")
    price = models.CharField(default="N/A")
    address = models.CharField(default="N/A")
    


    def __str__(self):
        return self.user.username
        