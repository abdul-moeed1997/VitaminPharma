from django.db import models

class Product (models.Model):
    male = 'male'
    female = 'female'
    both = 'both'
    catagory_based_on_gender=[
        (male, 'male'),
        (female,'female'),
        (both,'both')
    ]

    name = models.CharField(max_length=100)
    desc = models.TextField()
    gender_catagory = models.CharField(max_length=6, choices=catagory_based_on_gender, default=female)
    catagory = models.CharField(max_length=50)
    sub_catagory = models.CharField(max_length=50)
    price = models.IntegerField(default="0")
    old_price = models.IntegerField(default="0")
    code = models.CharField(max_length=30)
    expire_date = models.DateField()
    quantity = models.IntegerField(default="1")
    brand = models.CharField(max_length=50, default="")
    image = models.ImageField(upload_to="shop/images")
    size = models.CharField(max_length=20, default="")
    dosage =models.CharField(max_length=20, default="")

    def __str__(self):
        return self.name



class Order (models.Model):
    order = models.TextField()
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    postcode = models.CharField(max_length=10)
    phone = models.CharField(max_length=15)
    ordernotes = models.TextField(default="")
    yes = 'yes'
    no = 'no'
    delivery_report =[
        (yes,'yes'),
        (no, 'no')
    ]
    delivered = models.CharField(max_length=3,choices=delivery_report,default=no)

class OrderUpdate(models.Model):
    order_id = models.IntegerField(default="")
    update_desc = models.CharField(max_length=5000)
    timestamp = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.update_desc[0:7] + "..."

class Contact (models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    comment = models.CharField(max_length=5000)

    def __str__(self):
        return self.name