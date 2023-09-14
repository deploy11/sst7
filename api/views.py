from django.shortcuts import render,redirect
from .models import *
from .serializers import *
from django.utils import timezone
from rest_framework.generics import *
from django.views.generic import *

class SorovApiView(ListCreateAPIView):
    queryset = Sorov.objects.all()
    serializer_class  = SorovSerializer

def hokimpaneli(request):
    if request.user.username == 'admin':
        hammasi = Sorov.objects.all().count()
        bajargan = Hokimiyat.objects.filter(bajarildi=True).count()
        bajarilmagan = Hokimiyat.objects.filter(bajarildi=False).count()
        muddati_otkan = Hokimiyat.objects.filter(muddat_holati=True).count()
        return render(request,'hokim.html',{
            'hammasi':hammasi,
            'bajargan':bajargan,
            'bajarilmagan':bajarilmagan,
            'muddati_otkan':muddati_otkan
        })
    else:
        return redirect('login')
def hbarchasi(request):
    
    hammasis = Sorov.objects.all()
    return render(request,'barcha.html',{
        'hammasi':hammasis,
    })

def ramat(request):
    return render(request,'rahmat.html')

class CreateBlog(CreateView):
    model = Sorov
    template_name = 'blog_new.html'
    fields = ('__all__')