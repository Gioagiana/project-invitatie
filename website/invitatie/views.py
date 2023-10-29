from django.http import HttpResponse
from django.template import loader
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from .forms import ContactForm
import datetime

def home(request):
    template = loader.get_template('home.html')
    return HttpResponse(template.render())

# Create your views here.
# views.py




def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            # Salvați mesajul în baza de date
            contact_message = ContactMessage(name=name, email=email, message=message)
            contact_message.save()

            # Trimiteți emailul
            subject = 'Mesaj de contact de la {}'.format(name)
            message = 'De la: {}\nEmail: {}\nMesaj: {}'.format(name, email, message)
            from_email = 'babiciugiorgiana@gmail.com'  # Adresa de email de la care se trimite
            recipient_list = ['babiciugiorgiana@gmail.com']  # Adresa de email a destinatarului
            send_mail(subject, message, from_email, recipient_list)

            return redirect('success_page')  # Redirecționați către o pagină de succes
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})


