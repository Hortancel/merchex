from django.shortcuts import render,redirect
from django.http import HttpResponse
from listings.models import Band
from listings.forms import ConctactUsForm, BandForm
from django.core.mail import send_mail


def band_delete(request, id):
    band = Band.objects.get(id=id)
    if request.method == 'POST':
        band.delete()
        return redirect('band-list')
    return render(request, 'listings/band_delete.html', {'band': band})

def band_update(request,id):
    band = Band.objects.get(id=id)
    if request.method =='POST':
        form = BandForm(request.POST, instance = band)
        if form.is_valid():
            form.save()
            return redirect('band-detail',band.id)
    else:
        
        form=BandForm(instance=band)
    
    return render(request,'listings/band_update.html',{'form' : form})


def band_create(request):
    if request.method == 'POST':
        form = BandForm(request.POST)
        if form.is_valid():
            band = form.save()
            return redirect('band-detail', band.id)
    else:
        form = BandForm()
    
    return  render(request, 'listings/band_create.html', {'form': form})

    
    

def contact(request):
    
    if request.method =='POST':
        form = ConctactUsForm(request.POST)
        if form.is_valid():
            send_mail(
                subject=f'Message from {form.cleaned_data["name"] or "anonyme"} via MerchEx Contact Us form',
                message=form.cleaned_data['message'],
                from_email=form.cleaned_data['email'],
                recipient_list=['admin@merchex.xyz'],
            )
                 
    else:
        form = ConctactUsForm()
    
    return redirect('email-sent')



def band_detail(request,id):
    band = Band.objects.get(id=id)
    return render(request,'listings/band_detail.html',{'band':band})
 

def band_list(request):
    bands = Band.objects.all()
    return render(request ,'listings/band_list.html',{'bands':bands})


def about(request):
    return HttpResponse('<h1> A Propos de nous </h1> <p>Nous Adherons merch!</p>')
