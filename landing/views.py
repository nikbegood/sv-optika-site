from django.shortcuts import render
from .forms import SubscriberForm
from products.models import *


def landing(request):

    return render(request, 'landing/landing.html', locals())


def home(request):
    products_images = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True)
    products_images_new = products_images.filter(product__category__id=5)
    products_images_sun = products_images.filter(product__category__id=6)
    products_images_gotmetall = products_images.filter(product__category__id=7)
    products_images_gotplastik = products_images.filter(product__category__id=8)
    products_images_vfutlyare = products_images.filter(product__category__id=9)
    products_images_gotdetplastik = products_images.filter(product__category__id=10)
    products_images_odetmetall = products_images.filter(product__category__id=11)
    products_images_odetplastik = products_images.filter(product__category__id=12)
    products_images_antifari = products_images.filter(product__category__id=13)
    products_images_bezopr= products_images.filter(product__category__id=14)
    products_images_taktik = products_images.filter(product__category__id=15)
    products_images_trenag = products_images.filter(product__category__id=16)
    products_images_komp = products_images.filter(product__category__id=17)
    products_images_izum = products_images.filter(product__category__id=18)
    products_images_lektor = products_images.filter(product__category__id=19)
    products_images_linzy = products_images.filter(product__category__id=20)
    products_images_futlar = products_images.filter(product__category__id=21)
    return render(request, 'landing/home.html', locals())

def contacts(request):
    return render(request, 'landing/contacts.html', locals())

def novinky(request):
    products_images = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True)
    products_images_new = products_images.filter(product__category__id=5)
    return render(request, 'landing/novinky.html', locals())

def sunglasses(request):
    products_images = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True)
    products_images_sun = products_images.filter(product__category__id=6)
    return render(request, 'landing/sunglasses.html', locals())

def gotmetall(request):
    products_images = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True)
    products_images_gotmetall= products_images.filter(product__category__id=7)
    return render(request, 'landing/gotmetall.html', locals())

def gotplastik(request):
    products_images = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True)
    products_images_gotplastik= products_images.filter(product__category__id=8)
    return render(request, 'landing/gotplastik.html', locals())

def vfutlyare(request):
    products_images = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True)
    products_images_vfutlyare= products_images.filter(product__category__id=9)
    return render(request, 'landing/vfutlyare.html', locals())

def gotdetplastik(request):
    products_images = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True)
    products_images_gotdetplastik= products_images.filter(product__category__id=10)
    return render(request, 'landing/gotdetplastik.html', locals())

def antifari(request):
    products_images = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True)
    products_images_antifari= products_images.filter(product__category__id=13)
    return render(request, 'landing/antifari.html', locals())

def bezopr(request):
    products_images = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True)
    products_images_bezopr= products_images.filter(product__category__id=14)
    return render(request, 'landing/bezopr.html', locals())

def taktik(request):
    products_images = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True)
    products_images_taktik= products_images.filter(product__category__id=15)
    return render(request, 'landing/taktik.html', locals())

def trenag(request):
    products_images = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True)
    products_images_trenag= products_images.filter(product__category__id=16)
    return render(request, 'landing/trenag.html', locals())

def komp(request):
    products_images = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True)
    products_images_komp= products_images.filter(product__category__id=17)
    return render(request, 'landing/komp.html', locals())

def izum(request):
    products_images = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True)
    products_images_izum= products_images.filter(product__category__id=18)
    return render(request, 'landing/izum.html', locals())

def lektor(request):
    products_images = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True)
    products_images_lektor= products_images.filter(product__category__id=19)
    return render(request, 'landing/lektor.html', locals())

def linzy(request):
    products_images = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True)
    products_images_linzy= products_images.filter(product__category__id=20)
    return render(request, 'landing/linzy.html', locals())

def futlar(request):
    products_images = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True)
    products_images_futlar= products_images.filter(product__category__id=21)
    return render(request, 'landing/futlar.html', locals())

def metall(request):
    products_images = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True)
    products_images_metall= products_images.filter(product__category__id=22)
    return render(request, 'landing/metall.html', locals())

def plastik(request):
    products_images = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True)
    products_images_plastik= products_images.filter(product__category__id=23)
    return render(request, 'landing/plastik.html', locals())

def odetmetall(request):
    products_images = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True)
    products_images_odetmetall = products_images.filter(product__category__id=11)
    return render(request, 'landing/odetmetall.html', locals())