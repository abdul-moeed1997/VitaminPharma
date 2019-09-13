from django.core.paginator import Paginator
import json
from django.shortcuts import render
from .models import Product, Order, OrderUpdate, Contact
from django.http import HttpResponse
# Create your views here.
def index(request):
    #products=[]
    temp_products= Product.objects.filter(old_price= 0)
   # for i in range(0,6):
    #    if temp_products[i]:
     #       products.append(temp_products[i])
    return render(request,'index.html',{'products': temp_products})

def about(request):
    return render(request,'about.html')

def products(request):
    brands = []
    brand_count = []
    catagery = []
    cat_count = []

    products=Product.objects.all()

    for product in products:
        if product.brand not in brands:
            brand = Product.objects.filter(brand=product.brand)
            brands.append(brand[0].brand)
            brand_count.append(brand.count)
        if product.catagory not in catagery:
            cat = Product.objects.filter(catagory=product.catagory)
            catagery.append(cat[0].catagory)
            cat_count.append(cat.count)
    p_paginator = Paginator(products, 9)
    page = request.GET.get('page')
    products = p_paginator.get_page(page)

    return render(request,'products.html',{'products': products, 'brands': brands, 'brand_count': brand_count, 'catagery': catagery, 'cat_count':cat_count})

def product_details(request, myid):
    product = Product.objects.filter(id=myid)
    return render(request,'productdetails.html', {'product': product[0]})

def searchResult(query, item):
    query = query.lower()
    if query in item.name.lower() or query in item.desc.lower() or query in item.catagory.lower() or query in item.sub_catagory.lower() or query in item.gender_catagory.lower() or query in item.brand.lower():
        return True
    else:
       return False

def search(request):
    brands = []
    brand_count = []
    catagery = []
    cat_count = []
    query = request.GET.get('search',"")
    temp_products = Product.objects.all()
    products = [item for item in temp_products if searchResult(query, item)]
    if len(products) != 0:
        for product in temp_products:
            if product.brand not in brands:
                brand = Product.objects.filter(brand=product.brand)
                brands.append(brand[0].brand)
                brand_count.append(brand.count)
            if product.catagory not in catagery:
                cat = Product.objects.filter(catagory=product.catagory)
                catagery.append(cat[0].catagory)
                cat_count.append(cat.count)
        p_paginator = Paginator(products, 9)
        page = request.GET.get('page')
        products = p_paginator.get_page(page)
        return render(request, 'products.html',
                  {'products': products, 'brands': brands, 'brand_count': brand_count, 'catagery': catagery,
                   'cat_count': cat_count})
    else:
        return render(request, '404.html')

def checkout(request):
    id = -1
    if request.method == "POST":
        itemJson = request.POST.get('itemJson', '')
        fname = request.POST.get('fname', '')
        lname = request.POST.get('lname', '')
        email = request.POST.get('email', '')
        adress = request.POST.get('address1', '') + "...." + request.POST.get('address2', '')
        city = request.POST.get('state', '')
        state = request.POST.get('state', '')
        zip_code = request.POST.get('postcode', '')
        phone = request.POST.get('phone', '')
        ordernotes = request.POST.get('ordernotes', '')
        thank = True
        order = Order(order=itemJson, first_name=fname, last_name=lname, email=email, address=adress, city=city,
                      state=state,postcode=zip_code, phone=phone, ordernotes=ordernotes )
        order.save()
        update = OrderUpdate(order_id=order.id, update_desc="The order has been placed")
        update.save()
        id = order.id
        return render(request, 'shop/thankyou.html', {'id': id})

    else:
        return render(request,'checkout.html')

def cart(request):
    return render(request,'cart.html')

def tracker(request):
    if request.method == "POST":
        orderId = request.POST.get('orderId', '')
        email = request.POST.get('email', '')
        try:
            order = Order.objects.filter(id=orderId, email=email)
            if len(order) > 0:
                update = OrderUpdate.objects.filter(id=orderId)
                updates = []
                for item in update:
                    updates.append({'text': item.update_desc, 'time': item.timestamp})
                    response = json.dumps([updates, order[0].order], default=str)
                return HttpResponse(response)
            else:
                return HttpResponse('{}')
        except Exception as e:
            return HttpResponse('{}')

    return render(request, 'shop/tracker.html')

def contact(request):
    thank = False
    if request.method == "POST":
        m_name = request.POST.get('name', '')
        m_email = request.POST.get('email', '')
        m_comment = request.POST.get('comment', '')
        contact1 = Contact(name=m_name, email=m_email, comment=m_comment)
        contact1.save()
        thank = True
        return render(request, 'shop/contact.html', {'Thank': thank})
    return render(request, 'shop/contact.html', {'Thank': thank})

def brand(request):
    brandname = request.GET.get('brand','')
    brands = []
    brand_count = []
    catagery = []
    cat_count = []
    query = request.GET.get('search', "")
    temp_products = Product.objects.all()
    products = Product.objects.filter(brand=brandname)
    if len(products) != 0:
        for product in temp_products:
            if product.brand not in brands:
                brand = Product.objects.filter(brand=product.brand)
                brands.append(brand[0].brand)
                brand_count.append(brand.count)
            if product.catagory not in catagery:
                cat = Product.objects.filter(catagory=product.catagory)
                catagery.append(cat[0].catagory)
                cat_count.append(cat.count)
        p_paginator = Paginator(products, 9)
        page = request.GET.get('page')
        products = p_paginator.get_page(page)
        return render(request, 'products.html',
                      {'products': products, 'brands': brands, 'brand_count': brand_count, 'catagery': catagery,
                       'cat_count': cat_count})
    else:
        return render(request, '404.html')

def category(request):
    cat = request.GET.get('cat','')
    brands = []
    brand_count = []
    catagery = []
    cat_count = []
    query = request.GET.get('search', "")
    temp_products = Product.objects.all()
    products = Product.objects.filter(catagory=cat)
    if len(products) != 0:
        for product in temp_products:
            if product.brand not in brands:
                brand = Product.objects.filter(brand=product.brand)
                brands.append(brand[0].brand)
                brand_count.append(brand.count)
            if product.catagory not in catagery:
                cat = Product.objects.filter(catagory=product.catagory)
                catagery.append(cat[0].catagory)
                cat_count.append(cat.count)
        p_paginator = Paginator(products, 9)
        page = request.GET.get('page')
        products = p_paginator.get_page(page)
        return render(request, 'products.html',
                      {'products': products, 'brands': brands, 'brand_count': brand_count, 'catagery': catagery,
                       'cat_count': cat_count})
    else:
        return render(request, '404.html')