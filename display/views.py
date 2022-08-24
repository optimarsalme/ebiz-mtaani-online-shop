from django.shortcuts import render
from .models import Fashion, Electronics, Mainview
from django.core.mail import send_mail
# Create your views here.
def home(request):
    mainview                = Mainview.objects.all()
    fashion                 = Fashion.objects.order_by('rating')[0:8]
    smartphones             = Electronics.objects.filter(category="smartphone")[0:8]
    tv                      = Electronics.objects.filter(category="TV") [0:8]
    
    context                 = {
        'MAINVIEW':         mainview,
        'FASHION':          fashion,
        'TELEVISION':       tv,
        'SMARTPHONE':       smartphones,
        
    }       
    return render(request, "index.html",context)

# views for all electronics tv's, smartphones etc
def electronics(request):
    smartphone              = Electronics.objects.filter(category="smartphone")
    tv                      = Electronics.objects.filter(category="tv")
    context                 = {
        'SMARTPHONE'          : smartphone,
        'TV'                  : tv,
    }
    return render(request, 'shop_electronics.html', context)
def fashion(request):
    shirt                   = Fashion.objects.filter(category="shirt")
    jean                    = Fashion.objects.filter(category="jean")
    tshirt                  = Fashion.objects.filter(category="tshirt")
    print(jean)
    context                 = {
        'SHIRT'             : shirt,
        'JEAN'              : jean,
        'TSHIRT'            : tshirt,
    }
    return render(request, 'shop_fashion.html', context)
def contact(request):
    return render(request, 'contact.html')

def login(request):
    return render(request, 'login.html')