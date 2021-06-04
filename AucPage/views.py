from django.shortcuts import render, HttpResponse, redirect
from django.template.loader import render_to_string
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMessage
from django.conf import settings
from Home.models import Client, Registered_Users, Product
from AucPage.models import Auction
import re, os
from datetime import date, datetime


# Create your views here.

def handleEnterForm(request):
    if request.method=="POST":
        error=[]
        today = date.today()
        time = datetime.now()
        time=datetime.time(time)
        #aucFormUname = request.POST['aucFormUname']
        #aucFormEmail = request.POST['aucFormEmail']
        aucFormCode = request.POST['aucFormCode']
        Uname=request.user.username
        try:
            #client_obj = Client.objects.get(Email=aucFormEmail)
            client_obj=Client.objects.get(Uname=Uname)
        except:
            error.append("Invalid Username!")
        try:
            reg_user_obj = Registered_Users.objects.get(User_Name=Uname, PassCode=aucFormCode)
        except:
            error.append("User not Registered!")
        try:
            product_obj = Product.objects.get(id=reg_user_obj.Product_ID, Auction_Passcode=aucFormCode)
            # hours=int(product_obj.Auction_pref_time.strftime('%H'))
            # minutes=int(product_obj.Auction_pref_time.strftime('%M'))
            
            # seconds=int(product_obj.Auction_pref_time.strftime('%S'))
            # time_check1=time.replace(hour=hours, minute=minutes, second=seconds,microsecond=0)
            # if minutes>49:
            #     minutes=(minutes+10)%59
            #     hours=(hours+1)%24
            #     time_check2=time.replace(hour=hours, minute=minutes, second=seconds,microsecond=0)
            # else:
            #     time_check2=time.replace(hour=hours, minute=minutes, second=seconds,microsecond=0)

            # if(product_obj.Auction_pref_date!=today):
            #     error.append("Auction for this product is not today! Check your email for auction details")
            # if(time<time_check1):#Auction ke phele enter nai hone ka check
            #     error.append("Auction is not started yet! Check time for this auction on Mail.")
            # if(time>time_check2):#Auction ke baad enter nai hone ka check
            #     error.append("Auction enter time is passed!")
            if(product_obj.AuctionEnded=='Yes'):
                error.append("Auction has ended!")
        except:
            error.append('Invalid User or Passcode!')
        
        if not error:
            try:
                check=Auction.objects.get(ClientUsername=reg_user_obj.User_Name, ProductID=product_obj.id)
            except:
                auc_obj = Auction(OwnerName=reg_user_obj.Product_Owner, ProductID=product_obj.id, ClientUsername=reg_user_obj.User_Name, ClientID=client_obj.id, ClientInitialBid=product_obj.Starting_Bid)
                auc_obj.save()
                auc_obj=Auction.objects.filter(ProductID=product_obj.id).order_by('-ClientInitialBid')
                return render(request, 'Auction/AucMain.html', {'Client':client_obj,'Product':product_obj,'RegUser':reg_user_obj, 'InAucUser':auc_obj})
            else:
                #filter() will always give you a QuerySet" - it's iterable
                #get() - return single object and it's not iterable
                auc_obj=Auction.objects.filter(ProductID=product_obj.id).order_by('-ClientInitialBid')
                if check.ClientUsername == reg_user_obj.User_Name:
                    return render(request, 'Auction/AucMain.html', {'Client':client_obj,'Product':product_obj,'RegUser':reg_user_obj, 'InAucUser':auc_obj})
        else:
            messages.warning(request, f'Invalid Credentials!.')
            return render(request,'Home/ErrorPage.html',{'Error':error})