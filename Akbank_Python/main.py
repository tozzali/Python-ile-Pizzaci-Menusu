#Gerekli Kitaplıkları İçe Aktarma
import csv
import datetime

#Pizza üst sınıfı oluşturma
class Pizza:
    def get_description(self):
        return self.__class__.__name__

    def get_cost(self):
        return self.cost

#Pizza alt sınıfı oluşturma
class Margarita(Pizza):
    cost = 60.0
    def __init__(self):
        self.description="Mozeralla , Domates ve Fesleğen"
        print(self.description)

class Klasik(Pizza):
    cost = 70.0
    def __init__(self):
        self.description = "Sucuk , Domates ve  Salam "
        print(self.description)

class TurkPizza(Pizza):
    cost = 80.0
    def __init__(self):
        self.description =  "Sucuk, Pastırma , Dana Sosis ve Domates"
        print(self.description)

class SadePizza(Pizza):
    cost = 65.0
    def __init__(self):
        self.description="Sucuk, Domates , Sosis"
        print(self.description)

#Decorator üst sınıfı oluşturma
class Decorator(Pizza):
    def __init__(self,ekstra):
        self.component = ekstra

    def get_cost(self):
        return self.component.get_cost() + \
        Pizza.get_cost(self)

    def get_description(self):
        return self.component.get_description() + \
        ';' + Pizza.get_description(self)


#Sos sınıflarını oluşturma
class Zeytin(Decorator):
    cost = 7.0
    desc = "Zeytin"
    def __init__(self,ekstra):
        Decorator.__init__(self,ekstra)

class Mantar(Decorator):
    cost = 4.0
    desc = "Mantar"
    def __init__(self, ekstra):
        Decorator.__init__(self, ekstra)


class Peynir(Decorator):
    cost = 7.0
    desc = "Peynir"
    def __init__(self, ekstra):
        Decorator.__init__(self, ekstra)


class Et(Decorator):
    cost = 15.0
    desc = "Et"
    def __init__(self, ekstra):
        Decorator.__init__(self, ekstra)


class Sogan(Decorator):
    cost = 6.0
    desc = "Sogan"
    def __init__(self, ekstra):
        Decorator.__init__(self, ekstra)


class Misir(Decorator):
    cost = 4.0
    desc = "Misir"
    def __init__(self, ekstra):
        Decorator.__init__(self, ekstra)

def main():
        dosya = open("Menu.txt", "r")
        oku = dosya.read()
        print(oku)


#Menüyü yazdırma
print("1-Klasik\n"  "2-Margarita\n"  "3-Türk Pizza\n" "4-Sade Pizza \n" "5-Zeytin\n" "6-Mantar\n" "7-Peynir\n" "8-Et\n" "9-Soğan\n" "10-Mısır")
menu={1: Klasik,
      2: Margarita,
      3: TurkPizza,
      4: SadePizza,
      5: Zeytin,
      6: Mantar,
      7: Peynir,
      8: Et,
      9: Sogan,
      10: Misir
      }


#Pizza seçimi
kontrol = None
while True:
    kontrol = int(input("Pizzanızı seçiniz: "))
    if 0  < kontrol < 5:
        print("Pizzanız seçildi malzeme seçmeye geçebilirsiniz. ")
        break
    else:
        print("Yanlış pizza kodunu girdiniz lütfen 1 ile 4 arasında tekrar deneyiniz.")

order= menu[int(kontrol)]()
ücret = order.get_cost()
slm=[]

#Sosların seçimi
while kontrol != "*":
    kontrol = input("Ekstra malzeme seçiniz (Siparişi Onaylamak İçin '*' Tuşuna Basınız): ")
    if kontrol == "5":
        z=Zeytin(Zeytin)
        slm.append(z)       
    elif kontrol=="6":
        m=Mantar(Mantar)
        slm.append(m)  
    elif kontrol=="7":
        p=Peynir(Peynir)
        slm.append(p)  
    elif kontrol=="8":
        e=Et(Et)
        slm.append(e)  
    elif kontrol=="9":
        s=Sogan(Sogan)
        slm.append(s)  
    elif kontrol=="10":
        mi=Misir(Misir)
        slm.append(mi)      

if kontrol in ["5","6","7","8","9","10"]:
    order = menu[int(kontrol)](order)

#Toplam ücret hesaplama ve Pizzanın malzemelerinin gösterimi 
toplam=0
bilgiler = "İçindekiler: "+ order.description + "Ekstralar: "
for i in slm:
    toplam=i.cost + toplam
    bilgiler = bilgiler + " "  + i.desc 

#Sipariş bilgilerinin alınması ve yazdırılması
print("Sipariş Bilgileri:\n")
isim = input("İsminizi giriniz: ")
ID = input("T.C. kimlik numaranızı giriniz: ")
kk_no = input("Kredi kartı numaranızı giriniz: ")
kk_sifre = input("Kredi kartı şifrenizi giriniz: ")
time = datetime.datetime.now()

#Siparişleri csv dosyasına kaydetme
with open('Orders_Database.csv', 'a') as orders:
    orders = csv.writer(orders, delimiter=',')
    orders.writerow([isim, ID, kk_no, kk_sifre, order.get_description(), ücret + toplam , bilgiler, time])


print("Siparişiniz onaylandı.")


