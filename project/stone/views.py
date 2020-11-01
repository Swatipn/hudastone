from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.conf import settings
from django.contrib import messages
from .models import Contact,Posts
from django.core import mail
from django.core.mail.message import EmailMessage

# Create your views here.
def index(request):
    return render(request,'index.html')

def contact(request):
    if request.method=="POST":
        fullname=request.POST.get('fullname')
        email=request.POST.get('email')
        phone=request.POST.get('num')
        description=request.POST.get('desc')
        contact_query=Contact(name=fullname,email=email,number=phone,description=description)
        contact_query.save()
        from_email=settings.EMAIL_HOST_USER
        # email starts here
        # your mail starts here
        connection=mail.get_connection()
        connection.open()
        email_mesge=mail.EmailMessage(f'Website Email from {fullname}',f'Email from : {email}\nUser Query :{description}\nPhone No : {phone}',from_email,['adityaprasad010203@gmail.com','swatinaik20012@gmail.com'],cc=[],connection=connection)
        email_user=mail.EmailMessage('AST STONE PVT. LTD.',f'Hello {fullname}\nThanks fo Contacting Us Will Resolve Your Query Asap\nThank You',from_email,[email],connection=connection)
        connection.send_messages([email_mesge,email_user])
        connection.close()
        messages.info(request,"Thanks for Contacting Us ")
        return redirect('/contact')
    return render(request,'contact.html')


def gallery(request):
    return render(request,'gallery.html')

def about(request):
    return render(request,'about.html')


    


def services(request):
    return render(request,'services.html')

def signup(request):
    if request.method=="POST":
        username=request.POST['username']
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        email=request.POST['email']
        num=request.POST['num']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']
        if pass1 !=pass2:
            messages.error(request,'Password not matching!')
            return redirect('/signup')
        
        try:
            if User.objects.get(username=username):
                messages.error(request,'Username is already taken!')
                return redirect('/signup')
        except Exception as identifier:
            pass        



        myuser=User.objects.create_user(username,email,pass1)
        myuser.firstname=firstname
        myuser.lastname=lastname
        myuser.save()
        messages.success(request,'Signup successful!!')
        return redirect('/')

    return render(request,'auth/signup.html')



def handlelogin(request):
    if request.method=="POST":
        handleusername=request.POST['username']
        handlepassword=request.POST['pass1']
        user=authenticate(username=handleusername,password= handlepassword)
        if user is not None:
            login(request,user)
            return redirect('/')
        else:
            messages.success(request,'Welcome to Hudastone!!')
            return redirect('/')
    
    return render(request,'auth/login.html')


def handlelogout(request):
    logout(request)
    messages.success(request,"Logout Success!!")
    return redirect('/login')

   


def BlockSteps(request):
    if not request.user.is_authenticated:
        messages.error(request,'Please login and Try again!!')
        return redirect('/login')
    posts=Posts.objects.all()
    context={'posts': posts}
    return render(request,'exteriorstoneproducts/BlockSteps.html')

def Cobbles(request):
    if not request.user.is_authenticated:
        messages.error(request,'Please login and Try again!!')
        return redirect('/login')
    posts=Posts.objects.all()
    context={'posts': posts}
    return render(request,'exteriorstoneproducts/Cobbles.html')

def FlagStone(request):
    if not request.user.is_authenticated:
        messages.error(request,'Please login and Try again!!')
        return redirect('/login')
    posts=Posts.objects.all()
    context={'posts': posts}
    return render(request,'exteriorstoneproducts/FlagStone.html')

def KerbStones(request):
    if not request.user.is_authenticated:
        messages.error(request,'Please login and Try again!!')
        return redirect('/login')
    posts=Posts.objects.all()
    context={'posts': posts}
    return render(request,'exteriorstoneproducts/KerbStones.html')

def Palisader(request):
    if not request.user.is_authenticated:
        messages.error(request,'Please login and Try again!!')
        return redirect('/login')
    posts=Posts.objects.all()
    context={'posts': posts}
    return render(request,'exteriorstoneproducts/Palisader.html')

def PierCaps(request):
    if not request.user.is_authenticated:
        messages.error(request,'Please login and Try again!!')
        return redirect('/login')
    posts=Posts.objects.all()
    context={'posts': posts}
    return render(request,'exteriorstoneproducts/PierCaps.html')

def PoolCaping(request):
    if not request.user.is_authenticated:
        messages.error(request,'Please login and Try again!!')
        return redirect('/login')
    posts=Posts.objects.all()
    context={'posts': posts}
    return render(request,'exteriorstoneproducts/PoolCoping.html')

def RoofingTiles(request):
    if not request.user.is_authenticated:
        messages.error(request,'Please login and Try again!!')
        return redirect('/login')
    posts=Posts.objects.all()
    context={'posts': posts}
    return render(request,'exteriorstoneproducts/RoofingTiles.html')

def StonePaving(request):
    if not request.user.is_authenticated:
        messages.error(request,'Please login and Try again!!')
        return redirect('/login')
    posts=Posts.objects.all()
    context={'posts': posts}
    return render(request,'exteriorstoneproducts/StonePaving.html')

def StoneQuoins(request):
    if not request.user.is_authenticated:
        messages.error(request,'Please login and Try again!!')
        return redirect('/login')
    posts=Posts.objects.all()
    context={'posts': posts}
    return render(request,'exteriorstoneproducts/StoneQuoins.html')

def kadapablack(request):
    if not request.user.is_authenticated:
        messages.error(request,'Please login and Try again!!')
        return redirect('/login')
    posts=Posts.objects.all()
    context={'posts': posts}
    return render(request,'naturalstones/kadapablack.html')

def KarnoolGray(request):
    if not request.user.is_authenticated:
        messages.error(request,'Please login and Try again!!')
        return redirect('/login')
    posts=Posts.objects.all()
    context={'posts': posts}
    return render(request,'naturalstones/KarnoolGray.html')

def LimeStones(request):
    if not request.user.is_authenticated:
        messages.error(request,'Please login and Try again!!')
        return redirect('/login')
    posts=Posts.objects.all()
    context={'posts': posts}
    return render(request,'naturalstones/LimeStones.html')

def TandurBlue(request):
    if not request.user.is_authenticated:
        messages.error(request,'Please login and Try again!!')
        return redirect('/login')
    posts=Posts.objects.all()
    context={'posts': posts}
    return render(request,'naturalstones/TandurBlue.html')

def TandurYellow(request):
    if not request.user.is_authenticated:
        messages.error(request,'Please login and Try again!!')
        return redirect('/login')
    posts=Posts.objects.all()
    context={'posts': posts}
    return render(request,'naturalstones/TandurYellow.html')

def MosaicTiles(request):
    if not request.user.is_authenticated:
        messages.error(request,'Please login and Try again!!')
        return redirect('/login')
    posts=Posts.objects.all()
    context={'posts': posts}
    return render(request,'interiorstoneproducts/MosaicTiles.html')

def StonePebbles(request):
    if not request.user.is_authenticated:
        messages.error(request,'Please login and Try again!!')
        return redirect('/login')
    posts=Posts.objects.all()
    context={'posts': posts}
    return render(request,'interiorstoneproducts/StonePebbles.html')

def WindowSills(request):
    if not request.user.is_authenticated:
        messages.error(request,'Please login and Try again!!')
        return redirect('/login')
    posts=Posts.objects.all()
    context={'posts': posts}
    return render(request,'interiorstoneproducts/WindowSills.html')

def StoneVenus(request):
    if not request.user.is_authenticated:
        messages.error(request,'Please login and Try again!!')
        return redirect('/login')
    posts=Posts.objects.all()
    context={'posts': posts}
    return render(request,'interiorstoneproducts/StoneVenus.html')

def PoolCoping(request):
    if not request.user.is_authenticated:
        messages.error(request,'Please login and Try again!!')
        return redirect('/login')
    posts=Posts.objects.all()
    context={'posts': posts}
    return render(request,'exteriorstoneproducts/PoolCoping.html')



def search(request):
    query=request.GET['search']
    if len(query)>75:
        allPosts=Posts.objects.none()
    else:
        allPostsTitle=Posts.objects.filter(title__icontains=query)
        allPostsContent=Posts.objects.filter(content__icontains=query)
        allPosts=allPostsTitle.union(allPostsContent)   
    if allPosts.count()==0:#if no query matchs
        messages.warning(request,"No Search Results")

    params={'allPosts':allPosts,'query':query}         
    
    return render(request,'search.html',params)    

