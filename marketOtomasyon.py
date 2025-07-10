
    
class Urun():
    urunList=[]
    urunTamList=[]
    sepet=[]
    def __init__(self,ad,fiyat,adet):
        self.ad=ad
        self.fiyat=fiyat
        self.adet=adet
        self.urunList.append(ad)
        self.urunTamList.append([ad,fiyat,adet])

    def urunYokMu(ad):
        
        if not ad in Urun.urunList:
            
            return True
        else:
            return False
    
    def stokVarMi(ad):
        for x in Urun.urunTamList:    
            if x[0]==ad:
                if int(x[2])==0:
                    print("Stokta hiç ürün kalmadi")
                    return False
                
                else:
                    return True


    @staticmethod
    def urunEkle():
        ad=input("Lütfen eklemek istediğiniz ürün adini giriniz: ")
        if not Urun.urunYokMu(ad):
            print("Bu adda urun ekleyemezsiniz çünkü zaten bu adda ürün var!")
            return
        fiyat=input("Lütfen ürün fiyatini giriniz: ")
        adet=input("Lütfen ürün adedini giriniz: ")
        yeniUrun=Urun(ad,fiyat,adet)
        print(f"{ad} listeye eklendi")

    @staticmethod
    def urunCikar():
        ad=input("Lütfen çikarmak istediğiniz ürün adini giriniz: ")
        if  Urun.urunYokMu(ad) :
            print("Bu adda urun çikaramazsiniz çünkü bu adda ürün yok!")
            return
        Urun.urunList.remove(ad)
        print(f"{ad} listeden çikarildi")
        Urun.stokVarMi(ad)


    def fiyatGüncelle(ad,fiyat):
        
        güncellemeList=Urun.urunTamList
        if Urun.urunYokMu(ad):
            print("Bu adda ürün yok")
            return
        for x in Urun.urunTamList:
            
            if x[0]==ad:
                print(f"{ad} ürününün {x[1]} olan fiyati {fiyat} olarak değiştirildi") 
                x[1]= fiyat
                güncellemeList.remove([x[0],x[1],x[2]])
                Urun.urunTamList.append([x[0],x[1],x[2]])
                return
            
        print("Bu ürün daha önce güncellendiği için güncellenemez")

    def enflasyon(ad,enf):
        Urun.urunYokMu(ad)
        enf=int(enf)
        for x in Urun.urunTamList:
            if x[0]==ad:
                yeniFiyat=int(x[1])*(1+(enf/100))
                print("Enflasyona göre güncellenmiş fiyat: ")
                Urun.fiyatGüncelle(ad,yeniFiyat)

    def stokKontrol(ad):
        if Urun.urunYokMu(ad):
            print("Bu adda ürün yok")
            return
        for x in Urun.urunTamList:
            if ad==x[0]:
                if int(x[2])<5:
                    print("Stokta 5'ten az ürün olduğu için stok güncellenmeli. DÜŞÜK STOK!!!")
                    yeniStok=input("Yeni stok adedini giriniz: ")
                    x[2]=yeniStok

                elif int(x[2])>50:
                    print("Stokta 50'den fazla ürün var. STOK FAZLASI!!!")
    

    @staticmethod
    def calisanEkle(id,isim,yas,bolum):
        calisan=Calisan(id,isim,yas,bolum)
        print(f"ID:{id}   {isim} isimli çalişan eklendi")

    @staticmethod
    def calisancikar(id):
        
        if not id in Calisan.ids:
            print("Bu ID'ye sahip çalişan bulunmamakta")
            return
        else:
            for temp in Calisan.calisanlar:
                if temp[0]==id:
                    print(f"ID:{id}   {temp[1]} isimli çalişan çikarildi")
                    Calisan.calisanlar.remove(temp)
                    Calisan.ids.remove(id)
    
    @staticmethod
    def urunGoster():
        print("---Ürün Listesi---")
        for a in Urun.urunTamList:
            print(f"{a[0]} Adet:{a[2]} Fiyat:{a[1]}")

           
    @staticmethod
    def urunAl(urunAdi,sayi):
        
        for a in Urun.urunTamList:
            if a[0]==urunAdi:
                if sayi<=a[2]:
                    a[2]=int(a[2])-int(sayi)
                    Urun.sepet.append([urunAdi,sayi])
                    print(f"{a[0]} ürününden stokta {a[2]} adet kaldi")
                elif sayi>a[2]:
                    print(f"{a[0]} ürününden stokta {a[2]} adet kaldi. İstenilen sayida ürün bulunmuyor!!!")

    @staticmethod
    def fiyatHesapla():
        toplamFiyat=0
        for fiyatOrj in Urun.urunTamList:
            for x in Urun.sepet:
                if fiyatOrj[0]==x[0]:
                    fiyat=int(x[1])*int(fiyatOrj[1])
                    print(f"{x[0]}: {x[1]} adet X {fiyatOrj[1]} TL = {fiyat} TL")
                    toplamFiyat= toplamFiyat+fiyat 
        return toplamFiyat
    
    @staticmethod
    def sepettenCikar(urun):
        if not urun in Urun.sepet:
            print("İstenilen ürün sepette yok!")
            return
        for x in Urun.sepet:
            if x[0]==urun:  
                Urun.sepet.remove(urun)
                print("Ürün sepetten çikarildi!!!")
                return

    @staticmethod
    def sepetGuncelle():
        if not Urun.sepet:
            print("Sepette ürün yok!")
            return
        Urun.urunGoster()
        urunn=input("Güncellenecek ürün adini giriniz: ")
        for x in Urun.sepet:
            if x[0]==urunn:
                adett=input("Güncellenecek ürünün yeni adedini giriniz: ")
                if adett>=x[1]:
                    Urun.sepet.remove(urunn)
                    print("Sepetteki adetten fazla adet girildiği için ürün sepetten çikarildi!!!")
                elif adett>0 and adett<x[1]:
                    Urun.sepet.remove(urunn)
                    print(f"{x[0]} ürününün adeti {x[1]} adetinden {adett} adetine güncellendi!")
                    x[1]=adett
class Calisan():
    calisanlar=[]
    ids=[]
    def __init__(self,id,isim,yas,bolum):
        self.id=id
        self.isim=isim
        self.yas=yas
        self.bolum=bolum
        self.calisanlar.append([id,isim,yas,bolum])
        self.ids.append(id)

deg=True
while deg:
    print("----------Ana Menü----------")
    print("1-Yönetim Menüsü\n2-Müşteri Menüsü\n3-Kapat")
    z=input("Seçim: ")
    deg1=False
    deger=False

    if int(z)==1:
        while True:
            kullaniciAdi="a"
            sifre="a"
            print("Ana menüye dönmek için q tuşlayabilirsiniz.")
            kulAd=input("Kullanici adini giriniz: ")
            if kullaniciAdi==kulAd:
                print("Ana menüye dönmek için q tuşlayabilirsiniz.")
                sif=input("Şifre giriniz: ")
                if sifre==sif:
                    print("Giriş Başarili :)")
                    deg1=True
                    break
                elif sif=="q":
                    break
                else:
                    print("Şifre yanliş. Tekrar deneyiniz")
            elif kulAd=="q":
                break
            else:
                print("Kullanici adi yanliş. Tekrar deneyiniz")

    elif int(z)==2:
        deger=True

    elif int(z)==3:
        deg=False


    while deg1:
        print("----------Yönetim Menüsü----------")
        print("1-Ürün Ekle\n2-Ürün Çikar\n3-Fiyat Güncelle")
        print("4-Enflasyona Göre Otomatik Fiyat Tanimla")
        print("5-Stok Kontrol ve Güncelle")
        print("6-Çalişanlari Göster")
        print("7-Çalişan Ekle veya Çikar")
        print("8-Ana Menüye Dön")
        x=input("Seçim: ")
        if int(x)==1:
            print("----------Ürün Ekle----------")
            Urun.urunEkle()
        elif int(x)==2:
            print("----------Ürün Çikar----------")
            Urun.urunCikar()
        elif int(x)==3:
            print("----------Fiyat Güncelle----------")
            ad=input("Fiyatini güncellemek istediğiniz ürünü giriniz: ")
            if not ad in Urun.urunList :
                print("Bu adda ürün yok!")
                continue
            fiyat=input("Yeni fiyati giriniz: ")
            Urun.fiyatGüncelle(ad,fiyat)

        elif int(x)==4:
            print("----------Enflasyona Göre Otomatik Fiyat Tanimla----------")
            ad=input("Ürün adini giriniz: ")
            enf=input("Ürüne uygulanacak enflasyon oranini giriniz: (%) ")
            Urun.enflasyon(ad,enf)

        elif int(x)==5:
            print("----------Stok Kontrol ve Güncelle----------")
            ad=input("Kontrol edilecek ürünü giriniz: ")
            Urun.stokKontrol(ad)

        elif int(x)==6:
            print("----------Çalişanlari Göster----------")
            if not Calisan.calisanlar:
                print("Hiç Çalişan yok")
                continue
            for a in Calisan.calisanlar:
                print(f"ID: {a[0]} İsim:{a[1]} Yaş:{a[2]} Bölüm:{a[3]} ")
                

        elif int(x)==7:
            deg2=True
            while deg2:
                print("----------Çalişan Ekle veya Çikar----------")
                print("1-Çalişan Ekle\n2-Çalişan Çikar\n3-Yönetim Menüsüne Dön")
                y=input("Seçim: ")
                
                if int(y)==1:
                    print("----------Çalişan Ekle----------")
                    id=input("Eklenecek çalişanin ID'sini giriniz: ")
                    if id in Calisan.ids:
                        print("Bu ID başka çalişan tarafindan kullanilmakta")
                        id=input("Yeni ID seçiniz: ")
                    isim=input("Eklenecek çalişanin adini giriniz: ")
                    yas=input("Çalişanin yaşini giriniz: ")
                    bolum=input("Çalişanin bölümünü giriniz: ")
                    Urun.calisanEkle(id,isim,yas,bolum)

                    
                elif int(y)==2:
                    if not Calisan.ids:
                        print("Hiç çalişan yok!!")
                    print("----------Çalişan Çikar----------")
                    id=input("Silinmek istenen çalişanin ID'sini giriniz: ")
                    Urun.calisancikar(id)

                elif int(y)==3:
                    print("Yönetim menüsüne dönüyor..")
                    deg2=False
                else:
                    print("Lütfen geçerli bir sayi giriniz!!")
                    

        elif int(x)==8:
            print("----------Ana Menüye Dön----------")
            print("Ana menüye dönülüyor..")
            deg1=False


        else:
            print("Lütfen geçerli bir sayi giriniz!!")


    while deger:
        print("----------Müşteri Menüsü----------")
        print("1-Ürün Al\n2-Sepeti Kontrol Et\n3-Sepeti Güncelle")
        print("4-Ürün Çikar\n5-Toplam Tutar\n6-Ana Menüye Dön")
        x=input("Seçim: ")
        
        if int(x)==1:
            print("----------Ürün Al----------")
            Urun.urunGoster()
            urunAdi=input("Lütfen almak istediğiniz ürünün adini yaziniz: ")
            sayi=input("Almak istediğiniz ürün adedini giriniz: ")
            Urun.urunAl(urunAdi,sayi)
          
        elif int(x)==2:
            print("----------Sepeti Kontrol Et----------")
            Urun.fiyatHesapla()
            pass
        elif int(x)==3:
            print("----------Sepeti Güncelle----------")
            print("1-Ürün Ekle\n2-Ürün Çikar\n3-Müşteri Menüsüne Dön")
            y=input("Seçim: ")
            if int(y)==1:
                print("***Ürün Ekle***")
                Urun.sepetGuncelle()

            elif int(y)==2:
                print("***Ürün Çikar***")
                Urun.sepetGuncelle()
            elif int(y)==3:
                print("***Müşteri Menüsüne Dön***")
                print("Müşteri menüsüne dönülüyor..")
                continue
            else:
                print("Lütfen geçerli bir sayi giriniz!!")
            
        elif int(x)==4:
            print("----------Ürün Çikar----------")
            Urun.urunGoster()
            urun=input("Sepetten çikarmak istediğiniz ürünün adini giriniz: ")
            Urun.urunCikar(urun)

        elif int(x)==5:
            print("----------Toplam Tutar----------")
            Urun.fiyatHesapla()
            x= Urun.fiyatHesapla()
            print(f"Toplam Ödenecek Tutar: {x}")

        elif int(x)==6:
            print("Ama menüye dönüyor..")
            deger=False

        else:
            print("Geçerli bir sayi giriniz!!")