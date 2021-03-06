from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import ContactForm
from products.models import Product
from django.core.mail import EmailMessage

# Create your views here.

def contact(request):
    contact_form = ContactForm()
    products = Product.objects.all()

    if request.method == "POST":
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            content = request.POST.get('content', '')

            #Enviamos correo
            email =EmailMessage(
                "Bágah: Nuevo mensaje de contacto",
                "De {} <{}>\n\nEscribió:\n\n{}".format(name, email, content),
                "no-contestar@inbox.mailtrap.io",
                ["victorm.brioness@gmail.com"],
                reply_to=[email]
            )
            try:
                email.send()
                #todo ha ido bien
                return redirect(reverse("contact")+"?ok")
            except:
                #algo no ha ido bien..
                return redirect(reverse('contact')+"?fail")

    return render(request, "contact/mail.html", {'products':products,'form':contact_form})