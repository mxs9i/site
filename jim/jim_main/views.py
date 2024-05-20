from datetime import datetime
import json
from django.shortcuts import redirect, render
from django.contrib.auth.views import LoginView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib.auth import logout
from .models import *
from .forms import *
import sys
# Create your views here.

def createDt(olddt) :
    newdt = olddt[0] + olddt[1] +olddt[2] + olddt[3] + '-' + olddt[5] + olddt[6] + '-' + olddt[8] + olddt[9] + olddt[10] + olddt[11] + olddt[12] +olddt[13] + olddt[14] + olddt[15]
    return newdt

def index(request) : 
    return render(request, 'main/index.html', {'title':'Главная'})

def createtrening(request) : 
    if request.method == 'POST':
            form = CreateTreningForm(request.POST)
            print(request.POST.get)
            print(request.POST.get("trener"))
            user = User.objects.get(username = request.user)
            trener = Treners.objects.get(id = request.POST.get("trener"))
            hall = Halls.objects.get(id=request.POST.get("hall"))
            print(createDt(request.POST.get("dt")))
            trening = Trenings(trener=trener, hall =hall, user = user, dt = createDt(request.POST.get("dt")))
            trening.save()
            HttpResponseRedirect('/home')
    else:
        form = CreateTreningForm()

    return render(request, 'main/createtrening.html', {'title':'Записаться на тренировку', 'form': form}) 

class TreningUpdate(UpdateView):
    model = Trenings
    template_name = 'main/createtrening.html'
    form_class = CreateTreningForm
    success_url = '/mypage'


class TreningDelete(DeleteView):
    model = Trenings
    template_name = 'main/deleteTrening.html'
    success_url = '/mypage'

def halls(request) :
    halls = Halls.objects.all()
    return render(request, 'main/halls.html', {'title':'Наши залы','halls' : halls})

def ourcomand(request) :
    treners = Treners.objects.all() 
    return render(request, 'main/ourcomand.html', {'title':'Наша команда','treners' : treners, 'count': len(treners)})

def abonements(request) : 
    return render(request, 'main/abonements.html', {'title':'Абонементы'})

def mypage(request) : 
    trenings = Trenings.objects.all()
    return render(request, 'main/mypage.html', {'title': 'Моя страница', 'trenings' : trenings})


def loveJim(request) : 
    import http.cookies
    http.cookies._is_legal_key = lambda _: True
    if request.COOKIES.get('lovingJim') is not None:
        value = request.COOKIES.get('lovingJim')
        html = render(request, 'main/loveJim.html', {'title': 'Любимый зал', 'value': value})
        # html = HttpResponse(
        #     "<center style = 'padding-top:20%;' ><h1> Your loving Jim is <br>{0}</h1></center>".format(value))
        html.set_cookie('your loving Jim is ', value + 'again')
        return html
    else : 
        return redirect('/home')


    
def delete_coockie(request):
    if request.COOKIES.get('lovingJim'):
        response = HttpResponse("<h1><br>Cookie deleted</h1>")
        response.delete_cookie("lovingJim")
    else:
        response = HttpResponse(
            "<h1></h1>Need to create cookie before deleting")
    return response    


class LoginUser(LoginView):
    form_class = LogInForm
    template_name = 'signIn/signIn.html'

    def get_default_redirect_url(self, **kwargs):
        url = super().get_success_url(**kwargs)
        return url

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get_success_url(self):
        return reverse_lazy('home')


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'signIn/signUp.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get_success_url(self):
        return reverse_lazy('home')


def logout_user(request):
    logout(request)
    return HttpResponseRedirect('signIn')


def lovingJimJson(request) : 
    treningssql = Trenings.objects.all().filter(user_id = request.user)
    if request.method == 'GET':
        response_data = {}
        loveJims = {}
        for i in treningssql:
            if i.hall_id in loveJims :
                loveJims[i.hall_id] = loveJims[i.hall_id] + 1
            else :
                loveJims[i.hall_id] = 1
        print(loveJims)
        max = 0
        for j in loveJims :
            if loveJims[j] > max :
                max = j
        lovingJim = Halls.objects.get(id = max)
        jim = {}
        jim['adres'] = lovingJim.Adres
        jim['title'] = lovingJim.title
        jim['area'] = lovingJim.area
        response_data['lovingJim'] = jim
        print(response_data)
        return HttpResponse(json.dumps(response_data), content_type="application/json")
    else:
        return HttpResponse(json.dumps([]), content_type="application/json")