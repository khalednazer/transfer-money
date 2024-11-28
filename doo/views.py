from django.shortcuts import get_object_or_404, redirect, render
from .form import Form, Ac
from django.contrib.auth import authenticate
from django.contrib import messages
from .models import Pay, Transfers
from .auth import NewAuth
from .email import send_email
from django.contrib.auth.decorators import login_required

# Create your views here.

def form(request):
    fo = Form()
    getus = NewAuth()
    if request.method =='POST':
        # nameW = request.POST['name']
        data = Form(request.POST)
        cred = request.POST['credit_No']
        ttes = getus.testUser(request, credit_No = str(cred))
        print(ttes)
        print(type(cred))
        if ttes is None :
            print(ttes)
            if data.is_valid:
                data.save()
                request.session['cname']= request.POST['name']
                return redirect('/create')
        else : 
            messages.success(request, 'this number allready used ')
    return render(request, 'payForm.html',{'form':fo})


def succ(request):
    user = Pay.objects.all()
    
    amo = request.session.pop('amount', None) # amount data
    one = request.session.pop('data', None) # sender data 
    reec = request.session.pop('rec', None) # recever data
    if one and reec:
        dat = get_object_or_404(Pay, id = one)
        Rv = get_object_or_404(Pay, id = reec)
        return render(request, 'success.html', {'message': amo, 'tt':dat, 'rec':Rv})
    else:
        return render(request, 'success.html', {'Err': 'No transaction has been sent.'})

    # return redirect(reversed('success', args=[amount]))


def create(request):
    toCreate = request.session.pop('cname', None)
    return render(request, 'created.html',{'name':toCreate})


def tem(request):
    return render(request, 'tem.html',{})

def trans(request):
    att = NewAuth()
    AllTrans = Transfers()
    if request.method =='POST':
        card = request.POST['card']
        password = request.POST['password']
        him = request.POST['him']
        amount = request.POST['amount']

        relat = authenticate(request, credit_No = card , crPass= password)
        print( 'sender',relat)
        if relat is not None:
            transFrom = Pay.objects.get(credit_No = card) # sender 
            recever = att.receve(request, credit_No=int(him)) # recever
            if transFrom.cash > int(amount) :
                transFrom.cash -= int(amount)
                transFrom.save()
                request.session['amount'] = amount
                request.session['data'] = transFrom.id
                
                if recever is not None:
                    request.session['rec'] = recever.id
                    rec = Pay.objects.get(name = recever)
                    rec.cash += int(amount)
                    rec.save()
                    AllTrans.frome = card
                    AllTrans.to = him
                    AllTrans.status = 'done'
                    AllTrans.amount = amount
                    AllTrans.save()
                    return redirect('/seucces/')
                else:
                    AllTrans.frome = card
                    AllTrans.to = him
                    AllTrans.status = 'Erorr'
                    AllTrans.amount = amount
                    AllTrans.save()
            else:
                messages.success(request, 'you dont have enough mony!')
        else:
            AllTrans.frome = card
            AllTrans.to = him
            AllTrans.status = 'Erorr'
            AllTrans.amount = amount
            AllTrans.save()
    return render(request, 'transfer.html',{})

@login_required(login_url='main')
def data(request):
    allPay = Pay.objects.all()
    foruser = Transfers.objects.all()
    return render(request, 'data.html', {'all' : allPay, 'tr':foruser})


def account(request):
    if request.method =='POST':
        crr = request.POST['cre']
        pas = request.POST['passs']
        founded= authenticate(request, credit_No = crr , crPass = pas)
        if founded is not None:
            return redirect( "acc/"+str(founded.id))
        else :
            messages.success(request, 'invalid data')
    return render(request, 'formMyAccount.html', {})


def Acc(request, pk):
    owner = Pay.objects.get(id = pk)
    foruser = Transfers.objects.all() # wain for filter data
    userdata = foruser.filter(frome = owner.credit_No)
    rec = foruser.filter(to = owner.credit_No)

    return render(request, 'MYAcc.html', {'ow':owner, 'userTr':userdata, 'recev':rec})
