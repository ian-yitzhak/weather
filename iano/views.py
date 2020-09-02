from django.shortcuts import render




from . models import Contact ,Post

from django.http import HttpResponse




def home(request):

    posts = Post.objects.all()




    if request.method =="POST":

        contact = Contact()
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        subject = request.POST.get('subject')
        contact.name=name
        contact.email=email
        contact.phone=phone
        contact.subject=subject
        contact.save()

        return render( request , 'iano/contact.html')

    return render( request , 'iano/home.html'  , {'post' : posts})


def contact(request):


    return render( request , 'iano/contact.html')




def fb(request):


    return render( request , 'iano/home.html')




