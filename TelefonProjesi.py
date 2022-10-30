from abc import ABC, abstractmethod
from datetime import datetime
import time
from datetime import date
import re
from typing import IO
import urllib.request


class tel_pyscal(ABC):
    def __init__(self, ekran_olcusu, buton_var):
        self.ekran_olcusu = ekran_olcusu
        self.buton_var = buton_var

    # katlanabilir
    def katlanabilir(self):
        b_katlanabilir = False

    # cebe sigiyormu #abstract = zorunluluk
    @abstractmethod
    def fit_pocket(self):
        fit_pocket = True

    @classmethod
    def add_pen(cls, pen):
        cls.pen = pen

    # batery
    @staticmethod
    def batery():
        batery = True
    #color
    @classmethod
    def color(cls,color):
        cls.color = color
    #ekran suresi
    @staticmethod
    def screentime():
        return True


"""Apple Telefonu"""""


class IosMenu:
    def __init__(self, fotograf, kamera, muzik, hava_durumu):

        self.fotograf = fotograf
        self.kamera = kamera
        self.muzik = muzik
        self.hava_durumu = hava_durumu

    # Fotoğraflar açılır
    yeniliste = []
    liste_uygulama = []

    def foto_ac():
        print("Fotoğraflar açılıyor..")
        time.sleep(1)
        print("Fotoğraf açıldı.")

    # Fotoğraflar kapatılır
    def foto_kapa():
        print("Fotoğraflar kapatılıyor..")
        time.sleep(1)
        print("Fotoğraf kapatıldı")

    # Kamera açılır
    def kamera_ac():
        print("Kamera açılıyor..")
        time.sleep(1)
        print("Kamera Açıldı.")

    # Kamera kapanır
    def kamera_kapa():
        print("Kamera kapatılıyor..")
        time.sleep(1)
        print("Kamera kapatıldı.")

    # Muzik acilir
    def muzik_ac():
        print("Müzik açılıyor..")
        time.sleep(1)
        print("Müzik Açıldı")

    # Muzik Kapanir
    def muzik_kapa():
        print("Müzik kapatılıyor..")
        time.sleep(1)
        print("Müzik Kapandı")

    # Istanbul hava durmunu gosterir
    def hava_durumu():
        url = "https://www.havadurumu15gunluk.net/havadurumu/istanbul-hava-durumu-15-gunluk.html"
        site = urllib.request.urlopen(url).read().decode('utf-8')

        r_gunduz = '<td width="45">&nbsp;&nbsp;(-?\d+)°C</td>'
        r_gece = '<td width="45">&nbsp;(-?\d+)°C</td>'
        r_gun = '<td width="70" nowrap="nowrap">(.*)</td>'
        r_tarih = '<td width="75" nowrap="nowrap">(.*)</td>'
        r_aciklama = '<img src="/havadurumu/images/trans.gif" alt="İstanbul Hava durumu 15 günlük" width="1" height="1" />(.*)</div>'

        comp_gunduz = re.compile(r_gunduz)
        comp_gece = re.compile(r_gece)
        comp_gun = re.compile(r_gun)
        comp_tarih = re.compile(r_tarih)
        comp_aciklama = re.compile(r_aciklama)

        gunduz = []
        gece = []
        gun = []
        tarih = []
        aciklama = []

        for i in re.findall(r_gunduz, site):
            gunduz.append(i)

        for i in re.findall(r_gece, site):
            gece.append(i)

        for i in re.findall(r_gun, site):
            gun.append(i)

        for i in re.findall(r_tarih, site):
            tarih.append(i)

        for i in re.findall(r_aciklama, site):
            aciklama.append(i)

        print("-" * 75)
        print("                         ISTANBUL HAVA DURUMU")
        print("-" * 75)
        for i in range(0, len(gun)):
            print("{} {},\n\t\t\t\t\tgündüz: {} °C\tgece: {} °C\t{}".format(tarih[i], gun[i], gunduz[i], gece[i],
                                                                            aciklama[i]))
            print("-" * 75)

    # Rehbere kayit ekleme
    def kayit_ekle():
        isim = input("isim giriniz: ")
        soyad = input("soyad giriniz: ")
        numara = input("numara giriniz: ")
        IosMenu.yeniliste.append([isim, soyad, numara])
        print(IosMenu.yeniliste)

    # Kayit Listelenir
    def kayit_listele():
        for i, j, k in IosMenu.yeniliste:
            print("isim---> {} soyad---> {}    numara---> {}".format(i, j, k))

    # Kayit Aranir
    def kayıt_ara():
        isim = input(
            "bulmak istediğiniz kişinin adını veya soyadını giriniz: ")
        for i in IosMenu.yeniliste:
            if isim in i:
                print(
                    "isim--> {}  soyad--> {}    numara--> {}".format(i[0], i[1], i[2]))

    # Kayit silinir
    def kayıt_sil():
        for i in IosMenu.yeniliste:
            print(*i)
        isim = input("Silmek istediğiniz kişinin ismini giriniz: ")
        for i in IosMenu.yeniliste:
            if isim in i:
                IosMenu.yeniliste.remove(i)


# Ayarlar Classı oluşturulur
class IosAyarlar(ABC):
    def __init__(self, parlaklik=50):
        self.parlaklik = parlaklik

    def parlaklik_ayari(self):
        while True:
            secim = input("Azaltmak için '-' Artırmak İçin '+' basın.. ")
            if (secim == "-"):
                if (self.parlaklik != 50):
                    self.parlaklik -= 10
                    print("Parlaklik:", self.parlaklik)
            elif (secim == "+"):
                if (self.parlaklik != 100):
                    self.parlaklik += 10
                    print("Parlaklik:", self.parlaklik)
            else:
                print("Parlaklik Güncellendi:", self.parlaklik)
                break


# IOS Sensor Classı oluşturulur
class IosTelefonSensorleri(ABC):
    def __init__(self, telefon_parola=123456):
        self.telefon_parola = telefon_parola
    def ac():
        print("Telefon açılıyor..")
        time.sleep(1)
        print("Telefon açıldı")
    def kapa():
        print("Telefon kapanıyor..")
        time.sleep(1)
        print("Telefon Kapandı")
    def parola_yazma():
        tparola = input("Parolayı giriniz: ")
        if not tparola == "123456":
            print("Telefon parolası yanlıştır..")
        elif (tparola == "123456"):
            print("Parola doğrudur. Başarıyla giriş yapıldı..")


# UygulamaIos sınıfı IosMenu classından miras alır
class UygulamaIos(IosMenu):
    def __init__(self, fotograf, kamera, muzik, takvim, uygulamalar=[]):
        super.__init__(fotograf, kamera, muzik)
        self.takvim = takvim
        self.uygulamalar = uygulamalar

    # Takvimi yazdırır
    def takvimYazdir():
        # bugun = date.self.takvim()
        # print("Bu gün", self.takvim)
        today = date.today()
        print("Today's date:", today)

    # Uygulama eklemek icin kullanilir
    def ios():
        uygulama = input("Eklemek istediginzi uygulamayi arayin: ")
        x = IosMenu.liste_uygulama
        x.append(uygulama)
        print(x)


"""________________________________________________________Samsung _________________________________________________________"""


# Takvim menu classindan miras alir
class AndroidMenu(ABC):
    def __init__(self, fotograf, kamera, muzik, hava_durumu):
        self.fotograf = fotograf
        self.kamera = kamera
        self.muzik = muzik
        self.hava_durumu = hava_durumu

    yeni_liste = []
    # Fotoğraflar açılır
    def foto_ac():
        print("Fotoğraflar açılıyor..")
        time.sleep(1)
        print("Fotoğraf açıldı.")

    # Fotoğraflar kapatılır
    def foto_kapa():
        print("Fotoğraflar kapatılıyor..")
        time.sleep(1)
        print("Fotoğraf kapatıldı")

    # Kamera açılır
    def kamera_ac():
        print("Kamera açılıyor..")
        time.sleep(1)
        print("Kamera açıldı.")

    # Kamera kapanır
    def kamera_kapa():
        print("Kamera kapatılıyor..")
        time.sleep(1)
        print("Kamera kapatıldı.")

    def muzik_ac():
        print("Müzik açılıyor..")
        time.sleep(1)
        print("Müzik açıldı.")

    def muzik_kapa():
        print("Müzik kapatılıyor..")
        time.sleep(1)
        print("Müzik kapatıldı.")

    def hava_durumu():
        url = "https://www.havadurumu15gunluk.net/havadurumu/istanbul-hava-durumu-15-gunluk.html"
        site = urllib.request.urlopen(url).read().decode('utf-8')

        r_gunduz = '<td width="45">&nbsp;&nbsp;(-?\d+)°C</td>'
        r_gece = '<td width="45">&nbsp;(-?\d+)°C</td>'
        r_gun = '<td width="70" nowrap="nowrap">(.*)</td>'
        r_tarih = '<td width="75" nowrap="nowrap">(.*)</td>'
        r_aciklama = '<img src="/havadurumu/images/trans.gif" alt="İstanbul Hava durumu 15 günlük" width="1" height="1" />(.*)</div>'

        comp_gunduz = re.compile(r_gunduz)
        comp_gece = re.compile(r_gece)
        comp_gun = re.compile(r_gun)
        comp_tarih = re.compile(r_tarih)
        comp_aciklama = re.compile(r_aciklama)

        gunduz = []
        gece = []
        gun = []
        tarih = []
        aciklama = []

        for i in re.findall(r_gunduz, site):
            gunduz.append(i)

        for i in re.findall(r_gece, site):
            gece.append(i)

        for i in re.findall(r_gun, site):
            gun.append(i)

        for i in re.findall(r_tarih, site):
            tarih.append(i)

        for i in re.findall(r_aciklama, site):
            aciklama.append(i)

        print("-" * 75)
        print("                         ISTANBUL HAVA DURUMU")
        print("-" * 75)
        for i in range(0, len(gun)):
            print("{} {},\n\t\t\t\t\tgündüz: {} °C\tgece: {} °C\t{}".format(tarih[i], gun[i], gunduz[i], gece[i],
                                                                            aciklama[i]))
            print("-" * 75)

    # Rehbere kayit ekleme
    def kayit_ekle():
        isim = input("isim giriniz: ")
        soyad = input("soyad giriniz: ")
        numara = input("numara giriniz: ")
        AndroidMenu.yeni_liste.append([isim, soyad, numara])
        print(AndroidMenu.yeni_liste)

    # Kayit Listelenir
    def kayit_listele():
        for i, j, k in AndroidMenu.yeni_liste:
            print("isim---> {} soyad---> {}    numara---> {}".format(i, j, k))

    # Kayit Aranir
    def kayıt_ara():
        isim = input(
            "bulmak istediğiniz kişinin adını veya soyadını giriniz: ")
        for i in AndroidMenu.yeni_liste:
            if isim in i:
                print(
                    "isim--> {}  soyad--> {}    numara--> {}".format(i[0], i[1], i[2]))

    # Kayit silinir
    def kayıt_sil():
        for i in AndroidMenu.yeni_liste:
            print(*i)
        isim = input("Silmek istediğiniz kişinin ismini giriniz: ")
        for i in AndroidMenu.yeni_liste:
            if isim in i:
                AndroidMenu.yeni_liste.remove(i)


# Android Ayarlar Classı oluşturulur
class AndroidAyarlar(ABC):
    def __init__(self, parlaklik=70):
        self.parlaklik = parlaklik
    def parlaklik_ayari(self):
        while True:
            secim = input("Azaltmak için '-' Artırmak İçin '+' basın.. ")
            if (secim == "-"):
                if (self.parlaklik != 70):
                    self.parlaklik -= 10
                    print("Parlaklik:", self.parlaklik)
            elif (secim == "+"):
                if (self.parlaklik != 100):
                    self.parlaklik += 10
                    print("Parlaklik:", self.parlaklik)
            else:
                print("Parlaklik Güncellendi:", self.parlaklik)
                break


class AndroidTelefonSensorleri(ABC):
    def __init__(self, telefon_parola = 123456):
        self.telefon_parola = telefon_parola

    def ac():
        print("Telefon açılıyor..")
        time.sleep(1)
        print("Telefon açıldı")

    def kapa():
        print("Telefon kapanıyor..")
        time.sleep(1)
        print("Telefon kapandı.")

    def parola_yazma():
        tparola = input("Parolayı giriniz: ")
        if not tparola == "1234321":
            print("Telefon parolası yanlıştır..")
        elif (tparola == "1234321"):
            print("Parola doğrudur. Başarıyla giriş yapıldı..")


class UygulamaAndroid(AndroidMenu):
    def __init__(self, fotograf, kamera, muzik, hava_durumu, takvim, uygulamalar=[]):
        super.__init__(fotograf, kamera, muzik, hava_durumu)
        self.takvim = takvim
        self.uygulamalar = uygulamalar
    #Takvim Yazdirir
    def takvimYazdir():
        # bugun = date.self.takvim()
        # print("Bu gün", self.takvim)
        today = date.today()
        print("Today's date:", today)
    #Uygulama eklemek icin fonksiyon olustururlur
    def android():
        uygulama = input("Eklemek istediginzi uygulamayi arayin: ")
        x = IosMenu.liste_uygulama
        x.append(uygulama)
        print(x)


class InfoAndroid(AndroidAyarlar):
    def __init__(self, parlaklik, pil,seri_no = "AXGAD16531S"):
        super.__init__(parlaklik, pil)
        self.surum = "11"
        self.__seri_no = seri_no

    # Seri No yazdirir (Kapsulleme)
    def get_Serino(self):
        return self.__seri_no


def main():
    telPyscal = tel_pyscal
    iMenu = IosMenu
    iAyarlar = IosAyarlar
    iTelSensorleri = IosTelefonSensorleri
    iUygulama = UygulamaIos
    aMenu = AndroidMenu
    aAyarlar = AndroidAyarlar
    aTelSensorleri = AndroidTelefonSensorleri
    aUygulama = UygulamaAndroid
    loop = True
    while loop:
        print("""
        1.Iphone
        2.Samsung
        3.Çıkış
        """)

        giris = input("Lütfen seçeceğiniz telefonu giriniz: ")
        if giris == "3":
            print("Çıkış yapılıyor..")
            time.sleep(1)
            print("Başarıyla çıkış yapıldı.")
        sub_loop = True
        while sub_loop:
            if giris == "1":
                print("""
            1.Ana Menu
            2.Telefon
            3.Uygulamalar
            4.Ayarlar
            5.Çıkış  
            """)
                iphone_giris = input("Lütfen seçeneklerden birini seçin: ")
                if iphone_giris == "5":
                    sub_loop = False
                    print("Çıkış yapılıyor..")
                    time.sleep(1)
                    print("Başarıyla çıkış yapıldı.")

                if iphone_giris == "1":
                    iphoneloop = True
                    while iphoneloop:
                        print(""""
                    1. Fotoğraf
                    2. Kamera
                    3. Müzik
                    4. Hava Durumu
                    5. Rehber
                    6. Çıkış
                    """)
                        secim = input("Lütfen seçeneklerden birini seçin: ")
                        if secim == "6":
                            iphoneloop = False
                            print("Çıkış yapılıyor..")
                            time.sleep(1)
                            print("Başarıyla çıkış yapıldı.")
                            break
                        fotoloop = True
                        while fotoloop:
                            if secim == "1":
                                print("""
                            1.Foto Ac
                            2.Foto Kapa
                            3.Çıkş
                            """)
                                fsecim = input("Lütfen seçenek seçiniz")
                                if fsecim == "3":
                                    fotoloop = False
                                    print("Çıkış yapılıyor..")
                                    time.sleep(1)
                                    print("Başarıyla çıkış yapıldı.")
                                    break
                                if fsecim == "1":
                                    iMenu.foto_ac()
                                elif fsecim == "2":
                                    iMenu.foto_kapa()
                                else:
                                    print("Lütfen doğru seçim yapınız!")
                            elif secim == "2":
                                kameraloop = True
                                while kameraloop:
                                    if secim == "2":
                                        print("""
                                    1.Kamera Ac
                                    2.Kamera Kapa
                                    3.Çıkş
                                    """)
                                        ksecim = input(
                                            "Lütfen seçenek seçiniz: ")
                                        if ksecim == "3":
                                            kameraloop = False
                                            fotoloop = False
                                            print("Çıkış yapılıyor..")
                                            time.sleep(1)
                                            print("Başarıyla çıkış yapıldı.")
                                            break
                                        if ksecim == "1":
                                            iMenu.kamera_ac()
                                        elif ksecim == "2":
                                            iMenu.kamera_kapa()
                                        else:
                                            print("Lütfen doğru seçim yapınız!")
                            elif secim == "3":
                                muzikloop = True
                                while muzikloop:
                                    print("""
                                    1.Müzik aç
                                    2.Müzik kapa
                                    3.Çıkış""")
                                    msecim = input("Lütfen seçim yapınız: ")
                                    if msecim == "3":
                                        muzikloop = False
                                        fotoloop = False
                                        print("Çıkış yapılıyor..")
                                        time.sleep(1)
                                        print("Başarıyla çıkış yapıldı.")
                                        break
                                    if msecim == "1":
                                        iMenu.muzik_ac()
                                    elif msecim == "2":
                                        iMenu.muzik_kapa()
                                    else:
                                        print("Lütfen doğru seçim yapınız !")

                            elif secim == "4":
                                print("İstanbul hava durumu görüntüleniyor..")
                                time.sleep(1)
                                print("İstanbul Hava Durumu:")
                                iMenu.hava_durumu()
                                break
                            elif secim == "5":
                                print("""
                                    1.Kayıt Ekle
                                    2.Kayıt Listele
                                    3.Kayıt Ara
                                    4.Kayıt Sil
                                    5.Çıkış""")
                                kayit_secim = input(
                                    "Lütfen seçenek seçiniz: ")
                                if kayit_secim == "5":
                                    print("Çıkış yapılıyor..")
                                    time.sleep(1)
                                    print("Başarıyla çıkış yapıldı.")
                                    break
                                if kayit_secim == "1":
                                    iMenu.kayit_ekle()
                                elif kayit_secim == "2":
                                    iMenu.kayit_listele()
                                elif kayit_secim == "3":
                                    iMenu.kayıt_ara()
                                elif kayit_secim == "4":
                                    iMenu.kayıt_sil()
                elif iphone_giris == "2":
                    print("""
                    1.Telefon Parola
                    2.Telefon Aç
                    3.Telefon Kapat
                    4.Çıkış
                    """)
                    tsecim = input("Lütfen seçim yapınız: ")
                    tloop = True
                    while tloop:
                        if tsecim == "4":
                            tloop = False
                            print("Çıkış yapılıyor..")
                            time.sleep(1)
                            print("Başarıyla çıkış yapıldı.")
                            break
                        if tsecim == "1":
                            iTelSensorleri.parola_yazma()
                            tloop = False
                        elif tsecim == "2":
                            iTelSensorleri.ac()
                            break
                        elif tsecim == "3":
                            iTelSensorleri.kapa()
                            tloop = False
                            loop = False

                elif iphone_giris == "3":
                    print("""
                    1.Takvim
                    2.AppStore
                    3.Çıkış
                    """)
                    usecim = input("Lütfen seçim yapınız: ")
                    uloop = True
                    while uloop:
                        if usecim == "3":
                            uloop = False
                            print("Çıkış yapılıyor..")
                            time.sleep(1)
                            print("Başarıyla çıkış yapıldı.")
                            break
                        elif usecim == "1":
                            iUygulama.takvimYazdir()
                            uloop = False
                        elif usecim == "2":
                            iUygulama.ios()
                            uloop = False
                elif iphone_giris == "4":
                    print("""
                    1.Parlaklik
                    2.Info
                    3.Çıkış 
                    """)
                    asecim = input("Lütfen seçim yapınız: ")
                    aloop = True
                    while aloop:
                        if asecim == "3":
                            aloop = False
                            print("Çıkış yapılıyor..")
                            time.sleep(1)
                            print("Başarıyla çıkış yapıldı.")
                            break
                        if asecim == "1":
                            ayarlar = IosAyarlar()
                            iAyarlar.parlaklik_ayari(ayarlar)
                            aloop = False
                        elif asecim == "2":
                            ios_info = {"Uretici": "Apple", "Model": 11, "Versiyon": "IOS13"}
                            print(ios_info)
                            aloop = False

            elif giris == "2":
                print("""
                    1.Ana Menu
                    2.Telefon
                    3.Uygulamalar
                    4.Ayarlar
                    5.Çıkış  
                    """)
                android_giris = input("Lütfen seçeneklerden birini seçin: ")
                if android_giris == "5":
                    sub_loop = False
                    print("Çıkış yapılıyor..")
                    time.sleep(1)
                    print("Başarıyla çıkış yapıldı.")

                if android_giris == "1":
                    androidloop = True
                    while androidloop:
                        print(""""
                    1. Fotoğraf
                    2. Kamera
                    3. Müzik
                    4. Hava Durumu
                    5. Rehber
                    6. Çıkış
                    """)
                        secim = input("Lütfen seçeneklerden birini seçin: ")
                        if secim == "6":
                            androidloop = False
                            print("Çıkış yapılıyor..")
                            time.sleep(1)
                            print("Başarıyla çıkış yapıldı.")
                            break
                        fotoloop = True
                        while fotoloop:
                            if secim == "1":
                                print("""
                            1.Foto Ac
                            2.Foto Kapa
                            3.Çıkş
                            """)
                                fsecim = input("Lütfen seçenek seçiniz")
                                if fsecim == "3":
                                    fotoloop = False
                                    print("Çıkış yapılıyor..")
                                    time.sleep(1)
                                    print("Başarıyla çıkış yapıldı.")
                                    break
                                if fsecim == "1":
                                    aMenu.foto_ac()
                                elif fsecim == "2":
                                    aMenu.foto_kapa()
                                else:
                                    print("Lütfen doğru seçim yapınız!")
                            elif secim == "2":
                                kameraloop = True
                                while kameraloop:
                                    if secim == "2":
                                        print("""
                                    1.Kamera Ac
                                    2.Kamera Kapa
                                    3.Çıkş
                                    """)
                                        ksecim = input(
                                            "Lütfen seçenek seçiniz: ")
                                        if ksecim == "3":
                                            kameraloop = False
                                            fotoloop = False
                                            print("Çıkış yapılıyor..")
                                            time.sleep(1)
                                            print("Başarıyla çıkış yapıldı.")
                                            break
                                        if ksecim == "1":
                                            aMenu.kamera_ac()
                                        elif ksecim == "2":
                                            aMenu.kamera_kapa()
                                        else:
                                            print("Lütfen doğru seçim yapınız!")
                            elif secim == "3":
                                muzikloop = True
                                while muzikloop:
                                    print("""
                                    1.Müzik aç
                                    2.Müzik kapa
                                    3.Çıkış""")
                                    msecim = input("Lütfen seçim yapınız: ")
                                    if msecim == "3":
                                        muzikloop = False
                                        fotoloop = False
                                        print("Çıkış yapılıyor..")
                                        time.sleep(1)
                                        print("Başarıyla çıkış yapıldı.")
                                        break
                                    if msecim == "1":
                                        aMenu.muzik_ac()
                                    elif msecim == "2":
                                        aMenu.muzik_kapa()
                                    else:
                                        print("Lütfen doğru seçim yapınız !")

                            elif secim == "4":
                                print("İstanbul hava durumu görüntüleniyor..")
                                time.sleep(1)
                                print("İstanbul Hava Durumu:")
                                aMenu.hava_durumu()
                                break
                            elif secim == "5":
                                print("""
                                    1.Kayıt Ekle
                                    2.Kayıt Listele
                                    3.Kayıt Ara
                                    4.Kayıt Sil
                                    5.Çıkış""")
                                kayit_secim = input(
                                    "Lütfen seçenek seçiniz: ")
                                if kayit_secim == "5":
                                    print("Çıkış yapılıyor..")
                                    time.sleep(1)
                                    print("Başarıyla çıkış yapıldı.")
                                    break
                                if kayit_secim == "1":
                                    aMenu.kayit_ekle()
                                elif kayit_secim == "2":
                                    aMenu.kayit_listele()
                                elif kayit_secim == "3":
                                    aMenu.kayıt_ara()
                                elif kayit_secim == "4":
                                    aMenu.kayıt_sil()
                elif android_giris == "2":
                    print("""
                    1.Telefon Parola
                    2.Telefon Aç
                    3.Telefon Kapat
                    4.Çıkış
                    """)
                    tsecim = input("Lütfen seçim yapınız: ")
                    tloop = True
                    while tloop:
                        if tsecim == "5":
                            tloop = False
                            print("Çıkış yapılıyor..")
                            time.sleep(1)
                            print("Başarıyla çıkış yapıldı.")
                            break
                        if tsecim == "1":
                            aTelSensorleri.parola_yazma()
                            tloop = False
                        elif tsecim == "2":
                            aTelSensorleri.ac()
                            break
                        elif tsecim == "3":
                            aTelSensorleri.kapa()
                            tloop = False
                            loop = False

                elif android_giris == "3":
                    print("""
                    1.Takvim
                    2.Play Store
                    3.Çıkış
                    """)
                    usecim = input("Lütfen seçim yapınız: ")
                    uloop = True
                    while uloop:
                        if usecim == "3":
                            uloop = False
                            print("Çıkış yapılıyor..")
                            time.sleep(1)
                            print("Başarıyla çıkış yapıldı.")
                            break
                        elif usecim == "1":
                            aUygulama.takvimYazdir()
                            uloop = False
                        elif usecim == "2":
                            aUygulama.android()
                            uloop = False
                elif android_giris == "4":
                    print("""
                    1.Parlaklik
                    2.Info
                    3.Çıkış 
                    """)
                    asecim = input("Lütfen seçim yapınız: ")
                    aloop = True
                    while aloop:
                        if asecim == "3":
                            aloop = False
                            print("Çıkış yapılıyor..")
                            time.sleep(1)
                            print("Başarıyla çıkış yapıldı.")
                            break
                        if asecim == "1":
                            ayarlar = AndroidAyarlar()
                            aAyarlar.parlaklik_ayari(ayarlar)
                            aloop = False
                        elif asecim == "2":
                            android_info = {"Uretici": "Samsung", "Model": "Note 20", "Versiyon": "Android12"}
                            print(android_info)
                            aloop = False


main()



