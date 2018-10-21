from django.shortcuts import render, get_object_or_404, redirect
from threading import Thread
from django.core.mail import send_mail
from django.views.decorators.http import require_POST
from .models import *
from .forms import CheaperForm
import os
import logging

logging.basicConfig(filename=os.path.join("/home/ubuntu-admin/mebli-virtualenv/MebliProj/", 'log.txt'), level=logging.DEBUG)
logger = logging.getLogger(__name__)
user_email = "mebelFest5@gmail.com"


def all_categories():
    all_categories = ProductCategory.objects.all()
    return all_categories

def index(request):
    sale_products = Product.objects.filter(sale_price__isnull=False).order_by("pub_date")[:5]
    return render(request, 'MebliShop/base.html', {"all_categories": all_categories(), "sale_products": sale_products})


def sub_category_view(request, sub_cat_id):
    sub_category = get_object_or_404(SubCategory, pk=sub_cat_id)
    return render(request, "MebliShop/sub_category.html", {"sub_category": sub_category, "all_categories": all_categories()})


def product_view(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    if request.method == "POST":
        logger.debug("My log: {}".format(request.POST))
        phone_number = request.POST.get("phone_number")
        if phone_number:
            tr = run_separate_thread(send_mail_with_phone)
            tr(phone_number, product.product_name, product.price)
            return redirect("MebliShop:thanks_view", product_id=product_id)
    return render(request, "MebliShop/product.html", {"product": product, "all_categories": all_categories()})


def thanks_view(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, "MebliShop/thanks.html", {"product": product, "all_categories": all_categories()})

def cheaper_view(request):
    form = CheaperForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            model = form.cleaned_data["model"]
            where = form.cleaned_data["where"]
            price = form.cleaned_data["price"]
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            phone = form.cleaned_data["phone"]
            comment = form.cleaned_data["comment"]
            subject = "Found cheaper model {}".format(model)
            message = "Клиент {} нашел товар {} дешевле.\nГде: {}\nЦена: {}\nПочта клиента: {}\nНомер клиента: {}\nКомментарий: {}".\
                format(name, model, where, price, email, phone, comment)
            func = lambda: send_mail(subject, message, user_email, [user_email])
            thread = run_separate_thread(func)
            thread()
            try:
                product_id = Product.objects.get(product_name=model).id
                return redirect("MebliShop:thanks_view", product_id=product_id)
            except:
                return redirect("MebliShop:main")
    return render(request, "MebliShop/cheaper.html", {"form": form, "all_categories": all_categories()})


def send_mail_with_phone(phone, product_name, price):
    subject = 'Order {}'.format(product_name)
    message = "Product {} with price {} was ordered by phone number {}".format(product_name, price, phone)
    send_mail(subject, message, user_email, [user_email, ])


def run_separate_thread(func):
    logger.debug("Get tread for mail")
    def thread(*args, **kwargs):
        t = Thread(target=func, args=args, kwargs=kwargs)
        t.daemon = True
        t.start()
    return thread


def map_view(request):
    return render(request, "MebliShop/address_shop.html", {"all_categories": all_categories()})
