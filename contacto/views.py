from django.shortcuts import render, redirect, HttpResponse
from .forms import CreateContact
# from .models import Contact
from django.core.mail import send_mail

# Create your views here.


def contact(request):
    if request.method == 'GET':
        return render(request, 'contact.html', {
            'form': CreateContact()
        })
    else:
        nombre = request.POST['name'] + ' ' + request.POST['last_name']
        numero = request.POST['number']
        email = request.POST['mail']
        mensaje = request.POST['text']
        text = f'Este mensaje fue enviado por {nombre} con el numero {numero} y el mail: {email}\nCon el mensaje de:\n{mensaje}'
        # Contact.objects.create(name=request.POST['name'], last_name=request.POST['last_name'], number=numero, mail=email, text=text) 'prueba con base de datos'
        send_mail(nombre, text, email, ['delfinpalermo@hotmail.com'], fail_silently=False)
        return redirect('success')


def success(request):
    return render(request,'success.html')
