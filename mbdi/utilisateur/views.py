from django.shortcuts import render , get_object_or_404 ,redirect
from .form import UserForm, ProfileForm
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponse 
from .models import *


#TOUT SE QUI EST RELATIF AU LOGIN/LOGOUT/REGISTER CI DESSOUS
def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = ProfileForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user 
            profile.save()
            registered = True
            return HttpResponseRedirect('/')
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = ProfileForm()
    content = {
        'registered': registered,
        'form1':user_form,
        'form2':profile_form,
    }
    return render(request, 'utilisateur/register.html', content)

def user_login(request):
    if request.method =='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/')
            else:
               return HttpResponse("UTILISATEUR DESACTIVER")
        else:
            return HttpResponse('MOT DE PASSE OU NOM UTILISATEUR INCCORECT')

    else:
        return render(request, 'utilisateur/login.html')


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')

# FIN DU LOGIN/LOGOUT/REGISTER 



def Viewdata(request):
    obj = Attente.objects.all()
    if request.method == 'POST':
        name = request.POST['name']
        num = request.POST['num']
        lati = request.POST['lati']
        longi = request.POST['longi']
        fait_par = request.POST['fait_par']
        donnees = Fini(name=name, num=num, lati=lati, longi=longi ,fait_par=fait_par, fini=True)
        donnees.save()
        
        return redirect('https://www.google.com/maps/dir/?api=1&origin=Lille&destination='+ lati + '%2C' + longi )
    return render(request, 'utilisateur/index.html',{'obj':obj})

def getdata(request):
    profiles = Attente.objects.all()
    return JsonResponse({"profiles":list(profiles.values())})
    
def getdatabis(request):
    profiles = Fini.objects.all()
    return JsonResponse({"profiles":list(profiles.values())})

def create(request):
    if request.method == 'POST':
        name = request.POST['name']
        num = request.POST['num']
        lati = request.POST['lati']
        longi = request.POST['longi']
        donnees = Attente(name=name, num=num, lati=lati, longi=longi)
        donnees.save()
        return HttpResponse("VOS INFORMATIONS ONT ETE TRANSMISE A NOS EQUIPES , VOUS SEREZ BIENTOT RECONTACTER")
    return render(request, 'utilisateur/form.html')




def ViewdataBis(request):
    obj = Fini.objects.all()
    return render(request, 'utilisateur/active.html',{'obj':obj})

def deleteUser(request, my_id):
    obj = get_object_or_404(Attente, id=my_id)
    name = obj.name
    if request.method == 'POST':
        obj.delete()
        return redirect('home')
    return render(request, 'utilisateur/delete.html',{"name":name})
    
def deleteUseract(request, my_id):
    obj = get_object_or_404(Fini, id=my_id)  
    name = obj.name
    if request.method == 'POST':
        obj.delete()
        return redirect('active')
    return render(request, 'utilisateur/deletact.html',{"name":name})

def deletecurent(request, my_id):
    obj = get_object_or_404(Attente, id=my_id)  
    if request.method == 'POST':
        obj.delete()
        return HttpResponseRedirect('')
   




