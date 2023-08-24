from django.shortcuts import redirect, render
from evoting.models import userName,party
from django.contrib import messages



# Create your views here.


def index(request):
    return render(request , "index.html")



def about(request):
    return render(request  , "about.html")


re="false"
def registration(request):
    if request.method == 'POST':
        save = userName()
        save.fname = request.POST.get('fname')
        save.lname = request.POST.get('lname')
        save.password = request.POST.get('pass')
        save.cpassword = request.POST.get('cpass')
        save.address = request.POST.get('add')
        a = request.POST.get('pnumber')
        save.email = request.POST.get('email')
        save.panNumber = request.POST.get('pannumber')
        save.aadharNumber = request.POST.get('anumber')
        

        if(save.fname =="" or save.lname =="" or save.password == "" or save.cpassword == "" or save.address =="" or a == "" or save.email == "" or save.panNumber == "" or save.aadharNumber == "" ):
            global re
            if re != "false":
                re ="false"
                messages.add_message(request, messages.SUCCESS , "INVALID INPUT!")
            else :
                messages.add_message(request, messages.SUCCESS , "INVALID INPUT!")                
        else:
            lo = userName.objects.filter(number = a ).all()
            lo1=userName.objects.filter(aadharNumber = save.aadharNumber).all()
            lo2=userName.objects.filter(panNumber =save.panNumber).all()
            v=""
            b=""
            n=""
            for i in lo:
                v=i.number
            for i in lo1:
                b=i.aadharNumber
            for i in lo2:
                n=i.panNumber
            print(v)
            print(b)
            print(n)
            if v=="" and b=="" and n=="":
                save.number=a
                save.save()
                messages.add_message(request, messages.SUCCESS , "RESITRATION!")
                
                re="true"
    #    messages.info(request,"created user info")
    #    messages.warning(request,"created user war")   
    #    messages.error(request,"created user err")
                return render(request  , "registration.html",{'msg':re})
            else:
                re="sddd"
                messages.add_message(request, messages.SUCCESS , "YOU HAVE ALREDAY REGISTER!")
                return render(request  , "registration.html")
    return render(request  , "registration.html",{'msg':re})

def login(request):
    if request.method == 'POST':
        pass1 = request.POST['password']
        cpass = request.POST['cpassword']
        number = request.POST['number']
        aadhar = request.POST['aadhar']
        a=""
        b=""
        c=""
        d=""
        if number == '':
            messages.add_message(request, messages.SUCCESS , "INVALID INPUT!")
        else:
            lo = userName.objects.filter(aadharNumber = aadhar,password = pass1 , cpassword = cpass , number = number).all()
        
            for i in lo :
                a=i.aadharNumber
                b=i.number
                c=i.cpassword
                d=i.password
                print(id)
            # print(a)
            # print(b)
            # print(c)
            # print(d)
        if a=='' or b =="" or c == "" or d =="":
            messages.add_message(request, messages.SUCCESS , "INVALID INPUT!")
            return render(request,'login.html')
            
        else:
            for i in lo :
                request.session['sid'] = i.id
                request.session['sfname'] = i.fname
                request.session['slname'] = i.lname
                # print(request.session.get('sid'))
            return redirect('party.html') 
    return render(request  , "login.html")
    


def contect(request):
    return render(request  , "contect.html")



def logout(request):
    userId=request.session.get('sid')
    if userId is None:
        return render(request,"login.html")
    else:
        del request.session['sid']
        del request.session['sfname']
        del request.session['slname']
        #print(request.session.get('sid'))
    return render(request  , "index.html")


def vote(request):
    userId=request.session.get('sid')
    if userId is None:
        return render(request,"login.html")
    else:
        ab  = party.objects.all()
        b=fname(request)
    return render(request,'vote.html',{'party':ab,'b':b})




def result(request):
    userId=request.session.get('sid')
    if userId is None:
        return render(request,"login.html")
    else:
        ab  = party.objects.all()
        b=fname(request)
    return render(request,'result.html',{'party':ab,'b':b})



x=""
def profile(request):
    userId=request.session.get('sid')
    if userId is None:
        return render(request,"login.html")
    else:
        userId=request.session.get('sid')
        ab= userName.objects.filter(id=userId)
        for i in ab:
            id=i.id
            fname=i.fname
            lname=i.lname
            password=i.password
            cpassword=i.cpassword
            address=i.address
            number=i.number
            email=i.email
            panNumber=i.panNumber
            aadhar=i.aadharNumber
            vote=i.vote
        global x
        if x=="true":
            messages.add_message(request, messages.SUCCESS , "PROFILE UPDATED SUCCESSFULLY..!")
            x=""
        else:
            pass
        
    return render(request,'profile.html',{'a':id,'b':fname,'c':lname,'d':password,'e':cpassword,'f':address,'g':number,'h':email,'j':panNumber,'k':aadhar,'m':vote,'msg1':x})



def edit_profile(request):
    userId=request.session.get('sid')
    if userId is None:
        return render(request,"login.html")
    else:
        userId=request.session.get('sid')
        ab= userName.objects.filter(id=userId)
        for i in ab:
            id=i.id
            fname=i.fname
            lname=i.lname
            password=i.password
            cpassword=i.cpassword
            address=i.address
            number=i.number
            email=i.email
            panNumber=i.panNumber
            aadhar=i.aadharNumber
            vote=i.vote

        if request.method == 'POST':
            save = userName.objects.get(id=userId)
            print(save)
            save.fname= request.POST['fname']
            save.lname = request.POST['lname']
            save.password = request.POST['pass']
            save.cpassword = request.POST['cpass']
            save.address = request.POST['add']
            save.email = request.POST['email']
            save.save()  
            global x
            x = "true"
            return redirect("profile.html")
    return render(request,'edit_profile.html',{'a':id,'b':fname,'c':lname,'d':password,'e':cpassword,'f':address,'g':number,'h':email,'j':panNumber,'k':aadhar,'m':vote,})



def fname(request):
    userId=request.session.get('sid')
    ab= userName.objects.filter(id=userId)
    for i in ab:
        fname=i.fname
    return fname



def update_vote(request):
    userId=request.session.get('sid')
    if userId is None:
        return render(request,"login.html")
    else:
        save = userName.objects.filter(id=userId)
        for i in save:
            flag = i.vote
        y=""
        if flag == True :
            messages.add_message(request, messages.SUCCESS , "YOU HAVE ALREDAY VOTED!")
            global vote1
            vote1="error"
            return redirect('party.html') 
        else:
            save = userName.objects.get(id=userId)
            save.vote = True
            save.save()

            party_id=request.GET['id']
            # print(party_id)
   
            vo = party.objects.filter(pid=party_id)
            # print(vo)
            for i in vo:
                vote = i.total
                vote = vote + 1

            #print(vote)
                vo = party.objects.get(pid=party_id)
            vo.total=vote
            vo.save()
            if vote1=="error" or vote1=="":
                messages.add_message(request, messages.SUCCESS , "THANKS FOR VOTING!")
                vote1="success"
            #return redirect("vote.html",{'pa':y})
            return redirect('party.html')
        #print(messages.error)
    return render(request,"vote.html")
vote1=""
def party1(request):
    userId=request.session.get('sid')
    if userId is None:
        return render(request,"login.html")
    else:
        ab  = party.objects.all()   
        if ab is None:
            ab=party.objects.all()
        b=fname(request)
    return render(request,'party.html',{'party':ab,'b':b,'pa':vote1})

def feedback(request):
    return render(request,"feedback.html")