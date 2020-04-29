#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Copyright 2020 Selçuk Sinan KIRAT

English Text
<Python program of data mining association rulse>
    Copyright (C) <2020>  <Selçuk Sinan KIRAT>

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.

---------------------------------------------------------

Türkçe Metin
<Veri Madenciliği Birliktelik Kuralları Python Programı>

    Copyright (C) <2020> <Selçuk Sinan KIRAT>

    Bu program özgür yazılımdır: Özgür Yazılım Vakfı tarafından yayımlanan GNU Genel Kamu Lisansı’nın sürüm 3 ya da 
    (isteğinize bağlı olarak) daha sonraki sürümlerinin hükümleri altında yeniden dağıtabilir ve/veya değiştirebilirsiniz.

    Bu program, yararlı olması umuduyla dağıtılmış olup, programın BİR TEMİNATI YOKTUR; TİCARETİNİN YAPILABİLİRLİĞİNE VE 
    ÖZEL BİR AMAÇ İÇİN UYGUNLUĞUNA dair bir teminat da vermez. Ayrıntılar için GNU Genel Kamu Lisansı’na göz atınız.

    Bu programla birlikte GNU Genel Kamu Lisansı’nın bir kopyasını elde etmiş olmanız gerekir. 
    Eğer elinize ulaşmadıysa <http://www.gnu.org/licenses/> adresine bakınız.
    
    Tükrçe çeviri: http://ozgurlisanslar.org.tr/gpl/gpl-v3/

    Selçuk Sinan KIRAT (Bilgisayar Öğretmeni)
    http://www.selcuksinankirat.com

"""

class Birliktelik():
    def __init__(self, dosya, destekEsik, guvenEsik):
        self.dosya = dosya
             
        try:
            self.guven = float(guvenEsik)
            self.destek = float(destekEsik)
            if((self.destek > 1.0 or self.destek < 0.0) or (self.guven > 1.0 or self.guven < 0.0)):
                print("Destek ve güven değerleri 0 ile 1 aralığında ondalık sayı türünde olmalıdır.")
            else:
                self.verileriAl()
        except:
            print("Destek ve güven değerleri 0 ile 1 aralığında ondalık sayı türünde olmalıdır.")
        
    def verileriAl(self):
        """
        txt dosyası içerisindeki verileri alır.
        bilgiler'i geri döndürür. bilgiler, sözlük türünde veridir
        """
        try:
            with open(self.dosya) as veri:
                satirSayisi = len(veri.readlines())
                veri.seek(0)
                degerler = []
                satirlar=[]
                
                for i in range(satirSayisi):
                    satir = veri.readline().strip().split(",")
                    satirlar.append(satir)
                    for j in range(len(satir)):
                        if (degerler.count(satir[j]) == 0):
                            degerler.append(satir[j])
                            
            degerler.sort()
       
            bilgiler = {"Değerler":degerler,
                      "Değer Sayısı":len(degerler),
                      "Kayıtlar":satirlar,
                      "Kayıt Sayısı":len(satirlar)}
            del degerler
            del satirlar
            return bilgiler
        
        except:
            print("Dosya bulunamadı")
        
    
    def verileriYaz(self):
        # txt dosyasındaki verileri ekrana basar
        
        gelen = self.verileriAl()
        print("DEĞERLER", gelen["Değerler"], sep="\n")
        print()
        print("KAYITLAR", *gelen["Kayıtlar"], sep="\n")
        
    def degerSayilari(self):
        """
        her bir seçimin toplamda kaç kez seçildiğini (frekansını) hesaplar
        sayilar listesinde bu frekansları geri döndürür
        """
        veriler = self.verileriAl()
    
        sayilar = []
        for i in range(veriler["Değer Sayısı"]):
            sayac = 0
            for j in range(veriler["Kayıt Sayısı"]):
                
                taranan = veriler["Kayıtlar"][j]
                aranan = veriler["Değerler"][i]
                
                if (taranan.count(aranan)!=0):
                    sayac += 1
                    
            sayilar.append(sayac)
        return sayilar
    
    def tekliVeriSec(self):
        """
        verilerin frekans tablosunu oluşturur. Tabloda destek eşik değerinden
        büyük olan veriler bulunur. Bu veriler sözlük tipindeki 'tablo' ismiyle
        ile geri döndürülür
        """
        veriler = self.verileriAl()
        frList = self.degerSayilari()    # Frekans Listesi
        tablo = {}
        for i in range(len(frList)):
            if (frList[i]/veriler["Kayıt Sayısı"] >= self.destek):
                tablo[veriler["Değerler"][i]] = frList[i]
        return tablo
    
    def ikiliVeriSec(self):
        """
        tekliVeriSec() methodundan gelen tablodaki verilerin ikili kombinasyonları
        içerisinde destek eşik değerini geçenlerle yeni bir tablo oluşturur. Oluşturulan
        tabloyu sözlük tipindeki 'ikililer' ismiyle geri döndürür.
        """
        tekliler = self.tekliVeriSec()
        tekliDegerler = list(tekliler.keys())
        
        tklDgrSy = len(tekliDegerler)
        dongu = (tklDgrSy * (tklDgrSy - 1)) / 2
        
        veriler = self.verileriAl()
        
        ikililer = {}
        
        m = sayac = 0
        n = 1
        for i in range(int(dongu)):
            for j in range(veriler["Kayıt Sayısı"]):
                if (n >= tklDgrSy): break
                taranan = veriler["Kayıtlar"][j]
                aranan1 = tekliDegerler[m]
                aranan2 = tekliDegerler[n]
                if ((taranan.count(aranan1) != 0) and (taranan.count(aranan2) != 0)):
                    sayac += 1
                if (sayac/veriler["Kayıt Sayısı"] > self.destek):
                    ikililer[aranan1 + "," + aranan2] = sayac
                #n += 1
            n += 1    
            if (n >= tklDgrSy): 
                m += 1
                n = m + 1
            sayac = 0
        return ikililer
    
    def ucluVeriSec (self):
        """
        ikiliVeriSec() methodundan gelen tablodaki verilerin üçlü kombinasyonları
        içerisinde destek eşik değerini geçenlerle yeni bir tablo oluşturur. Oluşturulan
        tabloyu sözlük tipindeki 'ucluler' ismiyle geri döndürür.
        """
        vrlr = self.verileriAl()    # Veriler
        kyt = vrlr["Kayıtlar"]           # Kayıtlar
        kytSys = vrlr["Kayıt Sayısı"]    # Kayıt Sayısı
        ikililer = self.ikiliVeriSec()
        ikiliDegerler = list(ikililer.keys())
        kD = [] # kullanılacak değerler
        
        for i in range(len(ikiliDegerler)):
            deger = ikiliDegerler[i].split(",")
            for j in range(2):
                if (kD.count(deger[j])==0):
                    kD.append(deger[j])
          
        uzunluk = len(kD)
        ucluler = {}
        sayac = 0
        for m in range(uzunluk-2):
            for n in range(m+1, uzunluk-1):            
                for o in range(n+1,uzunluk):                
                    for k in range(len(kyt)):
                        if ((kyt[k].count(kD[m]) != 0) and (kyt[k].count(kD[n]) != 0) and (kyt[k].count(kD[o]) != 0)):
                            sayac += 1
                            sonuc = sayac/kytSys
                            if (sonuc > self.destek):
                                ucluler[kD[m]+","+kD[n]+","+kD[o]]=sayac
                    sayac = 0
        return ucluler 
    
    def ikiliKurallar (self):
        """
        destek eşik değerlerinin üzerindeki tekliVeriSec() ve ikiliVeriSec() methotlarından
        gelen verilerle güven eşik değerinin üzerinde oluşabilecek A => B ve B => A şeklindeki
        kuralları oluşturup ekrana basar
        """
        tekliler = self.tekliVeriSec()
        ikililer = self.ikiliVeriSec()
        ikiliAnahtar = list(ikililer.keys())
        altIkiliAnht = []
        kurallar = {}
        #kontrol = 1
        for i in range(len(ikiliAnahtar)):
            altIkiliAnht = ikiliAnahtar[i].split(",")
            for j in range(2):
                if (j == 0):
                    if (ikililer[ikiliAnahtar[i]] / tekliler[altIkiliAnht[1]] > self.guven):
                        kurallar[altIkiliAnht[1]+" => "+altIkiliAnht[0]] = round(ikililer[ikiliAnahtar[i]] / tekliler[altIkiliAnht[1]],2)
                else:
                    if (ikililer[ikiliAnahtar[i]] / tekliler[altIkiliAnht[0]] > self.guven):
                        kurallar[altIkiliAnht[0]+" => "+altIkiliAnht[1]] = round(ikililer[ikiliAnahtar[i]] / tekliler[altIkiliAnht[0]],2)
        print("\n____________________________İKİLİ KURALLAR____________________________")
        for anahtar, deger in kurallar.items():
            print("{} \t\t|  Güven Değeri: {}".format(anahtar, deger))
        print("______________________________________________________________________\n")
        
    def ucluKurallar (self):
        """
        destek eşik değerlerinin üzerindeki tekliVeriSec(), ikiliVeriSec() ve ucluVeriSec()
        methotlarından gelen verilerle güven eşik değerinin üzerinde oluşabilecek 
        A,B => C ya da A => B,C kombinasyonlarındaki kuralları oluşturup ekrana basar
        """
        tekliler = self.tekliVeriSec()
        ikililer = self.ikiliVeriSec()
        ucluler = self.ucluVeriSec()      #Destek eşik değerinin üzerindeki üçlüler
        
        anahtar = list(ucluler.keys())    # Sözlükteki veri etiketleri liste olarak alındı
        kurallar = {}
        altAnahtar = []
        
        for i in range(len(anahtar)):
            for j in range(3):
                altAnahtar = anahtar[i].split(",")
                if ((ucluler[anahtar[i]] / tekliler[altAnahtar[j]]) > self.guven):
                    if (j == 0):
                        kurallar[altAnahtar[j]+" => "+altAnahtar[j+1]+","+altAnahtar[j+2]] = round(ucluler[anahtar[i]] / tekliler[altAnahtar[j]],2)
                    elif (j == 1):
                        kurallar[altAnahtar[j]+" => "+altAnahtar[j-1]+","+altAnahtar[j+1]] = round(ucluler[anahtar[i]] / tekliler[altAnahtar[j]],2)
                    else:
                        kurallar[altAnahtar[j]+" => "+altAnahtar[j-2]+","+altAnahtar[j-1]] = round(ucluler[anahtar[i]] / tekliler[altAnahtar[j]],2)
        m = 0
        n = 1
        ikiliAnahtar = ""
        ikiliAnahtar2 = ""
        for i in range(len(anahtar)):
            for j in range(3):
                altAnahtar = anahtar[i].split(",")
                ikiliAnahtar = altAnahtar[m]+","+altAnahtar[n]
                if (ikililer.get(ikiliAnahtar,0) != 0 and ucluler[anahtar[i]] / ikililer[ikiliAnahtar] > self.guven):  # ikililer[ikiliAnahtar] / kytSys > self.guven):
                    if (m == 0 and n == 1):
                        kurallar[ikiliAnahtar+" => "+altAnahtar[2]] = round(ucluler[anahtar[i]] / ikililer[ikiliAnahtar],2)  # ikililer[ikiliAnahtar] / kytSys
                    elif (m == 0 and n == 2):
                        kurallar[ikiliAnahtar+" => "+altAnahtar[1]] = round(ucluler[anahtar[i]] / ikililer[ikiliAnahtar],2)
                    else:
                        kurallar[ikiliAnahtar+" => "+altAnahtar[0]] = round(ucluler[anahtar[i]] / ikililer[ikiliAnahtar],2)
                elif (ikililer.get(ikiliAnahtar2,0) != 0 and ucluler[anahtar[i]] / ikililer[ikiliAnahtar2] > self.guven):   # ikililer[ikiliAnahtar2] / kytSys > self.guven):
                    if (m == 0 and n == 1):
                        kurallar[ikiliAnahtar2+" => "+altAnahtar[2]] = round(ucluler[anahtar[i]] / ikililer[ikiliAnahtar],2)
                    elif (m == 0 and n == 2):
                        kurallar[ikiliAnahtar2+" => "+altAnahtar[1]] = round(ucluler[anahtar[i]] / ikililer[ikiliAnahtar],2)
                    else:
                        kurallar[ikiliAnahtar2+" => "+altAnahtar[0]] = round(ucluler[anahtar[i]] / ikililer[ikiliAnahtar],2)
                if (n != 2 and m != 1):
                    n += 1
                elif (n == 2 and m == 0):
                    m += 1
                else:
                    m = 0
                    n = 1
        print("\n____________________________ÜÇLÜ KURALLAR____________________________\n")
        for anahtar, deger in kurallar.items():
            print("{} \t|\tGüven Değeri: {}".format(anahtar, deger))
        print("____________________________________________________________________")
