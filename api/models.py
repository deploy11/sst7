from django.db import models
from django.utils import timezone
from django.urls import reverse
# Create your models here.
class Sorov(models.Model):
    fish = models.CharField(max_length=500,verbose_name='To`liq ismingizni kiriting?')
    idpassport = models.CharField(max_length=500,verbose_name='pasport seriasini kiriting')
    # Tuman Shaharlar
    GULISTON_SHAHAR = 'Guliston shaxar'
    MIRZAOBOD_TUMANI = 'Mirzaobod tumani'
    YANGEYER_SHAHAR = 'Yangiyer shaxar'
    OQOLTIN_TUMANI = 'Oqoltin tumani'
    SARDOBA_TUMANI = 'Sardoba tumani'
    XOVOS_TUMANI = 'Xovos tumani'
    SIRDARYO_TUMANI = 'Sirdaryo tumani'
    GULISTON_TUMANI = 'Guliston tumani' 
    SAYHUNOBOD_TUMANI = 'Sayhunobod tumani'
    SHIRIN_SHAHR = 'Shirin Shahar'
    BOYOVUT_TUMANI = 'Boyovut tumani'
    Shahar_tumanlar = (
        (GULISTON_SHAHAR,'Guliston shaxar'),
        (MIRZAOBOD_TUMANI,'Mirzaobod tumani'),
        (YANGEYER_SHAHAR,'Yangiyer shaxar'),
        (OQOLTIN_TUMANI ,'Oqoltin tumani'),
        (SARDOBA_TUMANI,'Sardoba tumani'),
        (XOVOS_TUMANI,'Xovos tumani'),
        (SIRDARYO_TUMANI,'Sirdaryo tumani'),
        (GULISTON_TUMANI,'Guliston tumani'),
        (SAYHUNOBOD_TUMANI,'Sayhunobod tumani'),
        (SHIRIN_SHAHR,'Shirin Shahar'),
        (BOYOVUT_TUMANI,'Boyovut tumani'),
    )
    Yashashmanzili = models.CharField(max_length=500)
    
    mfynomi = models.CharField(max_length=500)
    kochanomi = models.CharField(max_length=500)
    telefonraqami = models.CharField(max_length=500)
    rasmvavidio = models.CharField(max_length=500)
    ariza_mazmuni = models.CharField(max_length=500)
    matn = models.TextField()

    def __str__(self) -> str:
        return self.fish
    
    def get_absolute_url(self):
        return reverse('rahmat')
    
class Hokimiyat(models.Model):
    murajat = models.ForeignKey(Sorov,on_delete=models.CASCADE)
    orinbosar = models.CharField(max_length=500)
    tashkilot = models.CharField(max_length=500,default='none',blank=True)
    muddat = models.IntegerField(default=timezone.now()+timezone.timedelta(days=1))
    bajarildi = models.BooleanField(default=False)
    muddat_holati = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.orinbosar
        
    