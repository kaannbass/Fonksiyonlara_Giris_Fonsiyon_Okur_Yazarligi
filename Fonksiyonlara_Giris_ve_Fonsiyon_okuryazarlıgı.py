#Fonksiyonlara Giris ve Fonksiyon Okur YAzarlıgı
3**2

def kare_al(x):
    print(x**2)
    
kare_al(5)

#Bilgi notu ile cikti uretme

def kare_al(x):
    print(x**2)
    


def kare_al(x):
    print("Girilen sayi :" +
          str(x)+
          " Karesi:"+
          str(x**2))
    
    
    kare_al(3)

# IKi Argumanli Fonksiyon Tanimlamak
    
def carpma_yap(x,y):
    print(x*y)
carpma_yap(2, 3)    
    
#On tanimli Arguman ve sıralama
#Argumanı unutursan da x=2,y=4 ile y=4,x=2 yazıp 
# devam edebilirsinin

def carpma_yap(x,y):
    print(x*y)
carpma_yap(2,3)
 
# =============================================================================
# # Ne zaman fonsiyon yazilir ?? 
# programlara dilleri içerisinde  tekrar eden görevleri
#  yerine getirme ve var olan işlemi daha
#  programatik sekilde yerine getirmektedir. 
#sokak lambaları ornek olursa isi,nemi,sarj 
#isi=40 , nem = 25 , sarj = 90 
# =============================================================================

def sokak_lambalari(isi,nem,sarj) : 
    print((isi+nem)/sarj)
    
sokak_lambalari(40, 25, 90)

#Ciktiyi girdi olarak kullanmak 
#return komutu ile kullanilir print komutu tekrar calistirmaz
#return komutu asaya yazma calismaz
def sokak_lambalari(isi,nem,sarj) : 
    return((isi+nem)/sarj)
    
sokak_lambalari(25, 40, 70)

#Local etki alanindan Global etki alani degistirme

x = []

def eleman_ekle(y):
    x.append(y)
    print(str(y)+" ifadesi eklendi")
eleman_ekle(5)

eleman_ekle("ali")

x 

#True-False sorgulama (KArar & kontrol yapıları)
sinir = 5000

sinir == 4000

sinir == 5000

# If yapısı 
#if yapipi true ise koda devam eder

sinir = 5000
gelir = 60000

gelir > sinir

if gelir < sinir: 
    print("Gelir sinirdan kucuk")


#else
sinir = 50000
gelir = 35000

if gelir > sinir: 
    print("Gelir sinirdan buyuk")
else:
    print("Gelir sinirdan kucuk olucak")
    
# Ornek 2 
    
sinir = 50000
gelir = 51000
if gelir == sinir:
     print("Gelir sinira esittir")
else:
    print("Gelir sinira esit degildir.")

#elif
#
sinir = 50000
gelir1 = 60000
gelir2 = 50000
gelir3 = 35000

if gelir1 > sinir : 
    print("Tebrikler")

elif gelir < sinir:
    print("UYARI!!!")
else:
    print("Takibe devam")
    
#Gelir3
    
if gelir3 > sinir : 
    print("Tebrikler")

elif gelir3 < sinir:
    print("UYARI!!!")
else:
    print("Takibe devam")
    
# Gelir2
    
if gelir2 > sinir : 
    print("Tebrikler")

elif gelir2 < sinir:
    print("UYARI!!!")
else:
    print("Takibe devam")
    

#Mini uygulama

sinir = 50000
magaza_adi = input("Magaza Adi Nedir")
gelir = input("Gelirinizi Giriniz:")

if gelir < sinir :
    print("Tebrikler,promosyon kazandınız")
    
elif gelir < sinir : 
    print("UYarı")
    
else :
    print("Takibe Deevam")


#mini uygulama
    
sinir = 50000
magaza_adi = input("Magaza Adi Nedir?: ")
gelir = int(input("Gelir Giriniz: "))

if gelir > sinir:
    print("Tebrikler,promosyon kazandınır!")
elif gelir < sinir:
    print("Uyarı!")
else :
    print("Tekibe Devam")


#mini uygulama2

sinir = 50000
magaza_adi = input("Magaza Adi Nedir?: ")
gelir = int(input("Gelir Giriniz: "))

if gelir > sinir:
    print("Tebrikler:" + magaza_adi +"promosyon kazandınır!")
    
elif gelir < sinir:
    print("Uyarı! Cok dusuk gelir:" + str(gelir))
    
else :
    print("Tekibe Devam")


#For komutu Donguler
    
ogr = ["ali","veli","isik","berk"]

for i in ogr:
    print(i)

# for devam örnek 

maaslar = [1000,2000,3000,4000,5000]
maaslar[0]

for a in maaslar:
    print(a)

# dongu ve fonsiyonlar birlikte kullanmak 

def kare_al(x):
    print(x**2)

kare_al(2)

maaslar = [1000,2000,3000,4000,5000]

# =============================================================================
# #maaslara yüzde 20 zam olucak kodları yaz
# #1. yol
# for a in maaslar:
#     print(((a*20)/100)+int(a))
# 
# =============================================================================
##2. yol
def yeni_maas(x):
    print((x*20)/100 + x)

for i in maaslar:
    yeni_maas(i)

#if,for ve fonsiyonlari birlikte kullanmak 
#3000tl buyuk ½ 10 az olan .%20
    
maaslar = [1000,2000,3000,4000,5000]

def maas_ust(x):
    print(x*10/100 + x)
    
def maas_alt(x):
    print(x*20/100 + x)
    
for i in maaslar:
    if i >= 3000:
        maas_ust(i)
    else :
        maas_alt(i)
   
#Break & continue 

maaslar = [8000,5000,2000,1000,3000,7000,1000]

dir(maaslar)

maaslar.sort()

maaslar

for i in maaslar:
    if i == 3000:
        print("kesildi")
        break
    print(i)



for i in maaslar:
    if i == 3000:
        continue
    print(i)
    
#while - bu sart saglandigi surece
#2 den +1 şeklinde 10 kadar yazılma

sayi = 1
while sayi < 9:
    sayi += 1
    print(sayi)






def islem(x):
    if (x>10):
        return "YES"
    else:
        return x*5
 
islem(4)



sayilar = [10,20,30]
 
for i in sayilar:
    if i > 20:
        print(i/2)



for i in ["a",11]:
    print(i)



A = "*A*"
if type(A) == str:
    A = A.strip("*")
    print(A)



A = 12
 
if type(A) == str:
    A = A.strip("*")
    print(A)
else:
    A = "*" + str(A) + "*"
    print(A.strip())







A = []
B = []
 
 
for i in [1,"a",12,"b"]:
    if type(i) == int:
        B.append(i)
    else:
        A.append(i)
 
A[1]





def islem(x,y):
    A = [x,y]
    return A[0] + A[1]
 
islem(1,3)


# =============================================================================
# 
# =============================================================================
#Sınıf Özellikleri(class attributes) :
class VeriBilimci():
    bolum = ''
    sql = "Evet"
    deneyim_yili = 0
    bildigi_diller = []

#Yukarıda tanımladık asagida gösteriyor..
VeriBilimci.bolum
VeriBilimci.sql
VeriBilimci.bildigi_diller = ""
VeriBilimci.bildigi_diller 

#Sınıf Orneklendirme  (instanyiation)

ali = VeriBilimci()

ali.sql
ali.deneyim_yili
ali.bolum
#append yapmaya calistim str özellik hatası dedi böyle yaptım oldu :)) 
#append fonk deger herseyi etkiler ama asagidaki gibi olunca tek kisigi etkiler.

ali.bildigi_diller = "Python"

ali.bildigi_diller

Veli = VeriBilimci()

Veli.sql
Veli.bildigi_diller

#Ornek ozellikler:
#self örneklemleri temsil eder.(Temsilci)
class VeriBilimci():
    bildigi_diller = ["R","Python"]
    bolum = ''
    sql = "Evet"
    deneyim_yili = 0
    def __init__(self):
        self.bildigi_diller = []
        self.bolum = ""

ali = VeriBilimci()
ali.bildigi_diller

ali.bildigi_diller.append("Python")
ali.bildigi_diller
#Fazla yazdim bir tane sildim.
# =============================================================================
# ali.bildigi_diller.remove("Python")
# =============================================================================
ali.bildigi_diller

Veli = VeriBilimci()
Veli.bildigi_diller.append("R")

Veli.bildigi_diller

VeriBilimci.bildigi_diller

ali.bolum

VeriBilimci.bolum

ali.bolum = "istatistik"

VeriBilimci.bolum

Veli.bolum = "end_muh"

ali.bolum
Veli.bolum
VeriBilimci.bolum

#Ornek Metodları 
#self(örnekleri temsil eder,onları 
#yapalar islem uygulamamızı saglar )
class VeriBilimci():
    calisanlar =[]
    def __init__(self):
        self.bildigi_diller = []
        self.bolum = ""
    def dil_ekle(self, yeni_dil):
        self.bildigi_diller.append(yeni_dil)
        
ali = VeriBilimci()

veli = VeriBilimci()

dir(VeriBilimci)

ali.bildigi_diller
veli.bildigi_diller

ali.dil_ekle("R")
ali.bildigi_diller

veli.dil_ekle("Python")
veli.bildigi_diller

#Miras yapilari(inheritance)
# =============================================================================
# class Employees():
#      def __init__(self,FirstName,LastName,Address):
#         self.FirstName = FirstName
#         self.LastName = LastName
#         self.Address = Address
# asagıya tanımlandıgında 
#ali = Employees("a","b","c")
# ali.FirstName
#output = a 
# Ve böylece devam edecektir ic ice koyarak 
#belli basli seyleri yapabilirim.
# =============================================================================

class Employees():
     def __init__(self):
        self.FirstName = ""
        self.LastName = ""
        self.Address = ""
        
class DataScience(Employees):
     def __init__(self):
        self.Programming = ""

veribilimci1 = DataScience

class Marketing(Employees):
     def __init__(self):
        self.StoryTelling = ""
        
mar1 = Marketing

#Fonksiyonel Programlama 
#Fonksiyonlar dilin bastacidir. 
#(Birinci sinif neslelerdir.)
#Yan etkisiz fonsiyonlar. (stateless,girdi-cikti)
#Yuksek seviye fonksiyonlar 
#Vektorel operasyonlar.

#Yan etkisiz Fonksiyonlar (Pure Functions)

#Ornek1 : Yan Etki Bagimsizlik

A = 9

def impure_sum(b):
    return b+A


def pure_sum(a,b):
    return a+b

impure_sum(6)

pure_sum(3, 4)


#Ornek 2 : Olumcul yan etkiler 

#ISIMSIZ fonksiyonlar(Anonymous Functions)

def old_sum(a,b):
    return a+b

old_sum(4,5)

new_sum = lambda a,b : a+b
new_sum(4, 5)

sirasiz_liste = [("b",3),("a",8),("d",12),("c",1)]
sirasiz_liste

sorted(sirasiz_liste, key = lambda x: x[1])

# Vektorel Operasyonlar ( Vectorel Operations )
#işlerimizi daha kolay hale getirr.
#OOP (nesle yonelimli)


a = [1,2,3,4]
b = [2,3,4,5]

ab = []

range(0, len(a))

for i in range(0, len(a)):
    ab.append(a[i]*b[i])

ab

#FP
import numpy as np

a = np.array([1,2,3,4])
b = np.array([2,3,4,5])

ab

#map & filter & reduce (lambda ile birlikte kullanilir)
#vektörel işlem yapiyorlar.
#map = verilen bir vektorun icerisinde belirli bir fonksiyonu calistirmaya imkan verir ama isimsizdir.

liste = [1,2,3,4,5]

for i in liste: 
    print(i+ 10)

list(map(lambda x: x*10, liste))

#filter = benzer sekilde bir fonk ve iteratif nesne alarak calisir 
#bir itaratif nesne alir bu nesne uzerinde baska bir nesne olusturur 
#ve itaretif nesne icinde aradıgı sartın saglandıgı tum elemanlar filtrelenir.

liste = [1,2,3,4,5,6,7,8,9,10]

list(filter(lambda x: x % 2 == 0 , liste))

#reduce = indirgeme islemi yapar 

from functools import reduce 
liste = [1,2,3,4]
reduce (lambda a,b: a+b , liste)

#Modul olusturmak 

import HesapModulu

HesapModulu.yeni_maas(1000)

import HesapModulu as hm 

hm.yeni_maas(1000)

#Kolaylık ayni yukaridaki gibi 

from HesapModulu import yeni_maas

yeni_maas(4000)
yeni_maas(1000)

## liste eklendi 

import HesapModulu as hm 
hm.maaslar

# Istisnalar / Hatalar(exceptions)
# try / except
#Görmezden gelir kod akisini bozmaz 
a = 10 
b = 0

try:
    print(a/b)
except ZeroDivisionError:
    print("Payda da sifir olmaz")

#tip hatasi
    
    
a = 10 
b = 5

a / b 

try:
    print(a/b)
except TypeError:
    print("Sayi ve String problemi")



















































