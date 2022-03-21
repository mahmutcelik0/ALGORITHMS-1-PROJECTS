import math #GÖMÜLÜ MATH FONKSİYONLARINI KULLANMAK İÇİN import kullandım

def main(): #main fonksiyonunu olusturdum
    devam = True #devam ifadesini döngüye girebilmesi için true atadım
    liste = []  #program boyunca kullanacagım listeyi olusturdum
    lisans_no_liste = []    # lisans no yu almak için liste olusturdum
    while devam == True:    # kullanıcının devam etmek istediği sürece donecek bir while dongusu olusturdum
        fake_liste = [] # bilgi almak için gecici liste olusturdum
        fake_ad_soyad = [] # bilgi almak için gecici liste olusturdum
        fake_uluslararasi_dogruluk = [] # bilgi almak için gecici liste olusturdum
        fake_ulusal_dogruluk = [] # bilgi almak için gecici liste olusturdum

        lisans_no_al(fake_liste) # kullanıcıdan lisans no yu almak için fonksiyon olusturdum
        while fake_liste in lisans_no_liste:    # HATA KONTROLU için while döngüsü olusturdum
            print("Lisans no değiştir....") #print fonksiyonu
            fake_liste = [] # bilgi almak için gecici liste olusturdum
            lisans_no_al(fake_liste)    # kullanıcıdan lisans no yu almak için fonksiyon olusturdum
        lisans_no_liste.append(fake_liste) # lisans no listesine

        if fake_liste[0] > 0:   #kullanıcı devam etmek istiyorsa kontrolü
            devam = True    # duruma göre değişecek olan boolean ifade
        else:
            devam = False   # duruma göre değişecek olan boolean ifade

        if devam == True:   # kullanıcı devam etmek istiyorsa tekrar oyuncu girişi yapabilmesini sağlayan kısım
            ad_soyad_al(fake_ad_soyad)  # kullanıcıdan ad soyad alan fonksiyon
            uluslararasi_dogruluk_al(fake_uluslararasi_dogruluk)    # kullanıcıdan ELO yu almayı saglayan fonksiyon
            ulusal_dogruluk_al(fake_ulusal_dogruluk)    #kullanıcıdan UKD yi almayı sağlayan fonksiyon
            liste.append(
                {"puan": 0, "LNo": fake_liste[0], "isim": fake_ad_soyad[0], "ELO": fake_uluslararasi_dogruluk[0],
                 "UKD": fake_ulusal_dogruluk[0], "BSNo": 0, "rakip_oyuncular": [], "bh1": 0, "bh2": 0, "sb": 0, "gs": 0,
                 "s": 0, "b": 0, "-": 0, "renk": "-", "BYE": False, "onceki_iki_renk": ["-", "-"],"sadece_oynanan_rakipler":[]}) #dictionary e gerekli verileri ekleyen kısım
            liste =listeyi_siralama(liste, (("puan",True), ("ELO" ,True), ("UKD",True),("isim",False),("LNo",False)))   # listeyi sıralamaya götüren fonksiyon



    liste = baslangic_no_ekleme(liste)  # listeye başlangıc numarasını ekleyen fonksiyon
    oyunculari_siraya_gore_yazdirma(liste) # oyuncuları istenen sıraya göre yazdıran fonksiyon
    oyuncu_sayisi = len(liste)  # oyuncu sayısı
    masa_sayisi = masa_sayisini_hesapla(oyuncu_sayisi) # masa sayısını hesaplamayı fonksiyonla sağlayan kısım
    fake_tur_sayisi = []    # gecici liste
    tur_sayisini_kullanicidan_al(oyuncu_sayisi, fake_tur_sayisi)    #tur sayısını kullanıcıdan alan fonksiyon
    renk = rengi_kullanicidan_al()  #kullanıcıdan ilk başta renk alan fonksiyon

    ilk_tur_rengi_kullanicilara_dagit(liste, renk)  # renkleri kullanıcılara dağıtan fonksiyon
    tur_sayisi = fake_tur_sayisi[0] # tur sayısı
    for kacinci_tur_oldugu_index in range(tur_sayisi):  #tur sayısı kadar donecek for dongusu olusturdum
        kacinci_tur_oldugu = kacinci_tur_oldugu_index+1 # kacıncı tur oldugunu bulan kısım

        eslestirme_kismi = []   #eslestirmeler için liste olusturdum
        if kacinci_tur_oldugu ==1:  # 1. tur oldugu zaman calısacak if
            ilk_tur_icin_eslestirme(liste,eslestirme_kismi,kacinci_tur_oldugu) # birinci tur için eşleştirme fonksiyonu

        else:   # 1.tur harici calısacak
            genel_icin_eslestirme(liste,eslestirme_kismi,kacinci_tur_oldugu)    # birinci tur harici eslestirme yapacak fonksiyon

        tur_sonuclarini_yazdirma_fonksiyonu(eslestirme_kismi,kacinci_tur_oldugu)    # tur sonuclarını yazdırma fonksiyonu

        for x in range(len(eslestirme_kismi)):  # eslestirme kısmının uzunlugu kadar donecek for dongusu
            if eslestirme_kismi[x][1] != "BYE": # BYE gecmiyorsa
                mac_sonucu =mac_sonucu_alma_fonksiyonu(kacinci_tur_oldugu,x)    # mac sonucunu alacak fonksiyon
                mac_sonuclarini_listeye_isleme_fonksiyonu(mac_sonucu,tur_sayisi,x,eslestirme_kismi) # mac sonuclarını listeye isleyecek kısım

        liste = listeyi_siralama(liste, (("puan", True), ("ELO", True), ("UKD", True), ("isim", False), ("LNo", False))) #listeyi tekrardan sıralama

    listede_tur_sonuclarina_gore_duzenleme_yapan_fonksiyon_1(liste) # tur sonuclarına gore bh1 duzenleyen fonksiyon

    listede_tur_sonuclarina_gore_duzenleme_yapan_fonksiyon_2(liste) # tur sonuclarına gore bh2 duzenleyen fonksiyon

    listede_tur_sonuclarina_gore_duzenleme_yapan_fonksiyon_3(liste) # tur sonuclarına gore sb duzenleyen fonksiyon

    listede_tur_sonuclarina_gore_duzenleme_yapan_fonksiyon_4(liste) # tur sonuclarına gore gs duzenleyen fonsiyon

    liste = listeyi_siralama(liste, (("puan", True), ("bh1",True), ("bh2", True),("sb",True),("gs",True),("ELO",True),("UKD",True),("isim",False),("LNo",False)))   # oyuncuları tekrardan ıstendıgı sekılde sıralayan fonksiyon

    oyunculara_siralama_numarasi_veren_fonksiyon(liste) # oyunculara sıralama numarası veren fonksiyon

    son_siralama_listesini_yazdiran_fonksiyon(liste) # nihai sıralama listesini yazdıran fonksiyon

    capraz_tabloyu_yazdiran_fonksiyon(liste,tur_sayisi) # capraz tabloyu yazdıran fonksiyon




def lisans_no_al(fake_liste, ): # lisans no almayı sağlayan fonksiyon
    dogruluk = False    # kontrol için boolean ifade
    while dogruluk == False:    # dogruluk ifadesi false oldukca donecek while dongusu
        try:    # try except kontrol kısmı
            lisans_no = int(input("Oyuncunun lisans numarasını giriniz (bitirmek için 0 ya da negatif giriniz):"))  # oyuncudan lisans no alan input
            dogruluk = True # kontrol için boolean ifade
            fake_liste.append(lisans_no)    # listeye eklemek için append kısmı
        except: # programda hata verdirebilecek bir veri girildiğinde calısır
            print("Tam sayı giriniz...")    #kullanıcıyı uyarır
            dogruluk = False    # kontrol için boolean ifade

def ad_soyad_al(fake_ad_soyad): # ad soyad alan fonksiyon
    ad_soyad = input("Oyuncunun adını-soyadını giriniz:")   # kullanıcıdan ad soyad alan input
    yeni_ad_soyad = ad_soyad.replace("i", "İ")  # i gördüğünde İ yapacak kısım
    yeni_ad_soyad = yeni_ad_soyad.upper()   # oyuncu ad soyadını büyük harflere dönüştürecek kısım
    fake_ad_soyad.append(yeni_ad_soyad) # listeye eklemek için append kısmı

def uluslararasi_dogruluk_al(fake_uluslararasi_dogruluk):   # ELO yu kullanıcıdan alan fonksiyon
    uluslararasi_dogruluk = False   # kontrol için boolean ifade
    while uluslararasi_dogruluk == False:    # dogruluk ifadesi false oldukca donecek while dongusu
        try:     # try except kontrol kısmı
            uluslararasi_kuvvet_puani = int(input("Oyuncunun ELO'sunu giriniz (en az 1000, yoksa 0):")) # ELO yu kullanıcıdan alan input
            while uluslararasi_kuvvet_puani < 0 or uluslararasi_kuvvet_puani in range(1, 1000): # belirtilen aralığın dısında oldugu zaman calısacak dongu
                print("Lütfen doğru veri girişi yapınız...")    #kullanıcıyı uyaran print
                uluslararasi_kuvvet_puani = int(input("Oyuncunun ELO'sunu giriniz (en az 1000, yoksa 0):")) # ELO yu kullanıcıdan alan input
            uluslararasi_dogruluk = True    # kontrol için boolean ifade
            fake_uluslararasi_dogruluk.append(uluslararasi_kuvvet_puani)    #listeye eklemek için append kısmı
        except: # programda hata verdirebilecek bir veri girildiğinde calısır
            print("Tam sayı giriniz...")    #kullanıcıyı uyaran kısım
            uluslararasi_dogruluk = False   # kontrol için boolean ifade

def ulusal_dogruluk_al(fake_ulusal_dogruluk):   # UKD yi kullanıcıdan alan fonksiyon
    ulusal_dogruluk = False # kontrol için boolean ifade
    while ulusal_dogruluk == False:  # dogruluk ifadesi false oldukca donecek while dongusu
        try:     # try except kontrol kısmı
            ulusal_kuvvet_puani = int(input("Oyuncunun UKD'sini giriniz (en az 1000, yoksa 0):"))   # UKD yi kullanıcıdan alan input
            while ulusal_kuvvet_puani < 0 or ulusal_kuvvet_puani in range(1, 1000): # belirtilen aralığın dısında oldugu zaman calısacak dongu
                print("Lütfen doğru veri girişi yapınız...")    #kullanıcıyı uyaran kısım
                ulusal_kuvvet_puani = int(input("Oyuncunun UKD'sini giriniz (en az 1000, yoksa 0)"))     # UKD yi kullanıcıdan alan input
            ulusal_dogruluk = True  # kontrol için boolean ifade
            fake_ulusal_dogruluk.append(ulusal_kuvvet_puani)    #listeye eklemek için append kısmı
        except: # programda hata verdirebilecek bir veri girildiğinde calısır
            print("Tam sayı giriniz...")    #kullanıcıyı uyaran kısım
            ulusal_dogruluk = False # kontrol için boolean ifade

def karakterlerin_turkce_dizilim(oyuncu): # turkce dizilim fonksiyonu
    ALFABE = "ABCÇDEFGĞHIİJKLMNOÖPRSŞTUÜVYZ"    # türkçe alfabe harf sırası
    sonuc = ""  # SONUC ICIN
    for harf in oyuncu["isim"]: # for döngüsü
        if harf in ALFABE:  # harf kontrolü
            sonuc+= str(ALFABE.find(harf))+ "," # sonuca ekleme yapan kısım
        else:
            sonuc+= harf + ","  # sonuca ekleme yapan kısım
    return  sonuc   # sonucu geri gonderen kısım

def listeyi_siralama(liste, istenen_kriterler): #listeyi sıralayan
    for key, reverse in reversed(istenen_kriterler):    # sıralama için for dongusu
        if key == "isim":  # gelen key isim ise calısacak kısım
            liste.sort(key=karakterlerin_turkce_dizilim, reverse=reverse)   # listeyi turkceye gore sıralayan kısım

        else:
            liste.sort(key = lambda m:m[key], reverse = reverse)    # gelen eleman isim olmadığı zaman sıralama

    return liste    # listeyi geri gonderen kısım

def baslangic_no_ekleme(liste): # baslangıc no ekleyen fonksiyon
    for listeden_gelen in range(len(liste)):    # liste uzunlugu kadar donecek for dongusu
        liste[listeden_gelen]["BSNo"] = listeden_gelen+1    # listeye baslangıs sıra numarası ekleyen kısım
    return liste    # listeyi geri gonderen kısım

def oyunculari_siraya_gore_yazdirma(liste): #oyuncuları sıraya gore yazdıran fonksiyon
    print("\n")
    print("BSNo \t LNo \t Ad-Soyad \t\tELO\t\tUKD") # TABLO OLUSTURMA
    print("---- \t ---\t ------------\t----\t----")

    for m in liste: # listedeki elemanlar sırasıyla gelecek ve listedeki elemanlar bitesiye kadar donecek for dongusu
        print(format(m["BSNo"]).rjust(4), end="")   #SIRASIYLA İSTENEN VERİLERİN YAZDIRILMASI
        print(format(m["LNo"]).rjust(8), end="     ")
        print(format(m["isim"]), end="")
        print(format(m["ELO"]).rjust(19 - len(m["isim"])), end="")
        print(format(m["UKD"]).rjust(8), end="\n")

def masa_sayisini_hesapla(oyuncu_sayisi):   # masa sayısını hesaplayan fonksiyon
    masa_sayisi = math.ceil(oyuncu_sayisi / 2)  # masa sayısını hesaplayan kısım
    return masa_sayisi  # masa sayısını geri gonderen kısım

def tur_sayisini_kullanicidan_al(oyuncu_sayisi, fake_tur_sayisi):   # tur sayısını kullanıcıdan alan fonksiyon
    dogruluk = False    # kontrol için boolean ifade
    alt_sinir = int(math.log(oyuncu_sayisi, 2)) +1 # alt sınırı math fonksiyonu kullanarak hesaplayan kısım
    ust_sinir = oyuncu_sayisi - 1   # ust sınırı hesaplayan kısım
    while dogruluk == False:    # boolean ifade False oldugu surece donecek döngü
        try:     # try except kontrol kısmı
            tur_sayisi = int(input("Turnuvadaki Tur Sayısını Giriniz ({} - {}): ".format(alt_sinir,ust_sinir))) # tur sayısını kullanıcıdan alan input
            while (tur_sayisi > ust_sinir) or (tur_sayisi < alt_sinir): # tur sayısı sınırlar dısında oldukca donecek while dongusu
                print("TEKRARDAN GİRİNİZ...")   # kullanıcıyı uyaran print kısmı
                tur_sayisi = int(input("Turnuvadaki Tur Sayısını Giriniz ({} - {}): ".format(alt_sinir,ust_sinir))) # tur sayısını kullanıcıdan alan input
            dogruluk = True # kontrol için boolean ifade
            fake_tur_sayisi.append(tur_sayisi)  # listeye eklemek için append kullandım
        except: # programda hata verdirebilecek bir veri girildiğinde calısır
            print("Tam sayı GİRİNİZ...")    #kullanıcıyı uyaran kısım
            dogruluk = False    # kontrol için boolean ifade

def rengi_kullanicidan_al():    # rengi kullanıcıdan alan fonksiyon
    renk = input("RENGİ GİR:")  # rengi kullanıcıdan alan input
    muhtemel_renkler =["b","s"]
    while renk not in muhtemel_renkler:   # renk kontrolunu sağlamadığı surece donecek while dongusu
        print("Devam etmek için b veya s girmelisiniz...") # kullanıcıyı uyaran print
        renk = input("RENGİ GİR:")  # rengi kullanıcıdan alan input
    return renk # rengi geri gonderen kısım

def ilk_tur_rengi_kullanicilara_dagit(liste, renk): # ilk turda renkleri oyunculara dagıtan kısım
    for liste_index in range(len(liste)): # liste uzunlugu kadar donecek for dongusu
        if (liste_index+1) %2 ==1:  #oyuncunun sırasına gore if else kısmı
            liste[liste_index]["renk"] = renk
            son_renk_durumu = ""  # tanımlı olması ve str oldugunun belirli  olması ıcın tanımladım
            if renk == "b":  # renk beyaz ise
                son_renk_durumu = "b"
            elif renk == "s":  # renk siyah ise
                son_renk_durumu = "s"
            liste[liste_index][son_renk_durumu] += 1  # rengin oyuncudaki değerini 1 arttırma kısmı
            liste[liste_index]["onceki_iki_renk"][0] = renk  # onceki iki renk düzenlenmesi
            liste[liste_index]["onceki_iki_renk"][1] = liste[liste_index]["onceki_iki_renk"][
                0]  # onceki iki renk düzenlenmesi
        else:
            diger_renk = rengin_zittini_bulma_fonksiyonu(renk)
            liste[liste_index]["renk"] = diger_renk
            son_renk_durumu = ""  # tanımlı olması ve str oldugunun belirli  olması ıcın tanımladım
            if diger_renk == "b":  # renk beyaz ise
                son_renk_durumu = "b"
            elif diger_renk == "s":  # renk siyah ise
                son_renk_durumu = "s"
            liste[liste_index][son_renk_durumu] += 1  # rengin oyuncudaki değerini 1 arttırma kısmı
            liste[liste_index]["onceki_iki_renk"][0] = diger_renk  # onceki iki renk düzenlenmesi
            liste[liste_index]["onceki_iki_renk"][1] = liste[liste_index]["onceki_iki_renk"][
                0]  # onceki iki renk düzenlenmesi


def rengin_zittini_bulma_fonksiyonu(renk):  # rengin zıttını bulmayı sağlayan fonksiyon
    if renk =="b":  # renk beyazsa siyah olarak geri donus olacaktır
        return "s"

    elif renk =="s": #renk siyahsa beyaz olarak geri donus olacaktır
        return "b"


def ilk_tur_icin_eslestirme(liste,eslestirme_kismi,kacinci_tur_oldugu): # ilk tur için eslestirme yapan fonksiyon
    for m in range(0,len(liste),2): # listenin uzunluğunu 2ser atlayarak donecek for dongusu
        try:    # try except hata kontrolu
            oyunculari_eslestirme_fonksiyonu(liste[m],liste[m+1],eslestirme_kismi)  # oyuncuları eslestirmeyi sağlayan fonksiyona geçiş
        except: # except verdiğinde son elemana gelindiğini tekli oyuncularda anlaşılır
            bu_tur_bye_gececek_oyuncu = bye_bulma_fonksiyonu(liste,kacinci_tur_oldugu)  # bye bulma fonksiyonu sayesinde bye gececek oyuncu bulunur
            bu_tur_bye_gececek_oyuncu["onceki_iki_renk"][0] ="-"    # dictteki elemanda düzenleme
            bu_tur_bye_gececek_oyuncu["b"] = 0   # dictteki elemanda düzenleme
            bu_tur_bye_gececek_oyuncu["s"] = 0   # dictteki elemanda düzenleme
            eslestirme_kismi.append([bu_tur_bye_gececek_oyuncu,"BYE"])  # masaya bye yi yerleştirme



def genel_icin_eslestirme(liste,eslestirme_kismi,kacinci_tur_oldugu):   # genel için eslestirme yapan fonksiyon
    onceki_turlarda_eslestirilmis_oyuncular = []    # onceki turlarda eslestirilmiş oyuncuları yerleştirmek için boş liste olusturdum
    oyuncu_sayisi = len(liste)  # oyuncu saysını buldum
    if len(liste )%2 ==1:   # liste uzunlugu tek sayı ise
        bu_tur_bye_gececek_oyuncu =bye_bulma_fonksiyonu(liste,kacinci_tur_oldugu)   #bye gecen olacagı için bye bulma fonksiyonu yardımıyla hangi oyuncu bye onu buldum
        onceki_turlarda_eslestirilmis_oyuncular.append(bu_tur_bye_gececek_oyuncu["BSNo"])   # BSNo ya ekleme yapan kısım


    for eslestirilecek_oyuncu_1 in liste:   # oyuncu 1 in listeden alınması
        if eslestirilecek_oyuncu_1["BSNo"] not in onceki_turlarda_eslestirilmis_oyuncular:  # önceki masalarda eşleştirilmiş oyuncular içinde değilse
            ayni_puan = eslestirilecek_oyuncu_1["puan"] # puan değeri belirlenmesi
            kontrol_ifadesi =False  # kontrol boolean ifadesi
            while not kontrol_ifadesi and ayni_puan >=0:    # kontrol ifadesi doğru olmadığında ve puan 0dan büyük olduğunda dönecek while dongüsü
                kontrol_sayisi_1 = 1    # kontrol sayısı 1 while dondukce 1 artar
                while kontrol_sayisi_1 <=3 and not kontrol_ifadesi: # while döngüsü
                    kontrol_sayisi_2 = liste.index(eslestirilecek_oyuncu_1)+1   # kontrol sayısı 2.yi liste index kullanarak olusturdum

                    while kontrol_sayisi_2 < len(liste) and not kontrol_ifadesi:    # kontrol sayisi 2 liste uzunludugundan kücük oldugunda ve kontrol ifadesi True olmadığında dönecek while döngüsü
                        eslestirilecek_oyuncu_2 = liste[kontrol_sayisi_2]   # ikinci oyuncunun belirlenmesi
                        bos_liste = []
                        oyuncu_1_icin_kontrol = bos_liste   # EKLEME YAPILABİLECEK KISIM

                        if eslestirilecek_oyuncu_2["puan"] ==ayni_puan and eslestirilecek_oyuncu_2["BSNo"] not in onceki_turlarda_eslestirilmis_oyuncular and eslestirilecek_oyuncu_2["BSNo"] not in oyuncu_1_icin_kontrol and eslestirilecek_oyuncu_2["LNo"] not in eslestirilecek_oyuncu_1["sadece_oynanan_rakipler"]:    # istenen kosulları sağladıgında calısacak if kısmı
                            if (kontrol_sayisi_1 ==1) and (birinci_durum_eslestirme_fonksiyonu(eslestirilecek_oyuncu_1,eslestirilecek_oyuncu_2,eslestirme_kismi)):  # 1.Kural için if kısmı
                                onceki_turlarda_eslestirilmis_oyuncular.extend([eslestirilecek_oyuncu_1["BSNo"],eslestirilecek_oyuncu_2["BSNo"]])   #calışırsa onceki tur eşleşmiş oyunculara extend yardımıyla ekleme yapar
                                kontrol_ifadesi =True   # kontrol ifadei True ya dönüşür

                            elif (kontrol_sayisi_1 ==2) and (ikinci_durum_eslestirme_fonksiyonu(eslestirilecek_oyuncu_1,eslestirilecek_oyuncu_2,eslestirme_kismi)): # 2.Kural için if kısmı
                                onceki_turlarda_eslestirilmis_oyuncular.extend([eslestirilecek_oyuncu_1["BSNo"],eslestirilecek_oyuncu_2["BSNo"]])   #calışırsa onceki tur eşleşmiş oyunculara extend yardımıyla ekleme yapar
                                kontrol_ifadesi =True   # kontrol ifadei True ya dönüşür

                            elif (kontrol_sayisi_1 ==3) and (ucuncu_durum_eslestirme_fonksiyonu(eslestirilecek_oyuncu_1,eslestirilecek_oyuncu_2,eslestirme_kismi)): # 3.Kural için if kısmı
                                onceki_turlarda_eslestirilmis_oyuncular.extend([eslestirilecek_oyuncu_1["BSNo"],eslestirilecek_oyuncu_2["BSNo"]])   #calışırsa onceki tur eşleşmiş oyunculara extend yardımıyla ekleme yapar
                                kontrol_ifadesi =True   # kontrol ifadei True ya dönüşür

                        kontrol_sayisi_2 +=1    # kontrol sayisi 2 1 artar
                    kontrol_sayisi_1 +=1    #kontrol sayisi 1 1artar
                ayni_puan -=0.50 # SIRASIYLA PUAN DEĞERLERİ İNCELENMEK İSTEDİĞİ İÇİN YARIM PUAN DÜŞECEK ŞEKİLDE YAZDIM ÇÜNKÜ İKİ PUAN ARASI FARK 0.50 OLABİLİR
    if oyuncu_sayisi %2 ==1:    # oyuncu sayısı tek oldugunda calısacak if kısmı
        eslestirme_kismi.append([bu_tur_bye_gececek_oyuncu,"BYE"])  # son masaya bye gececek oyuncuyu yerleştirir



def bye_bulma_fonksiyonu(liste,kacinci_tur_oldugu): # bye bulmak için kullandığım fonksiyon
    for listedeki_oyuncu in reversed(liste):    # sıralanmıs listede dönecek for döngüsü
        if listedeki_oyuncu["BYE"] !=True:
            listedeki_oyuncu["BYE"] = True  # BYE dict elemanını True ya çevirir
            listedeki_oyuncu["rakip_oyuncular"].append([{"BSNo": "-","puan":listedeki_oyuncu["puan"]+ ((kacinci_tur_oldugu - len(listedeki_oyuncu["rakip_oyuncular"])-1)*0.5)},"-","1"])    # dict e ekleme yapar
            return  listedeki_oyuncu    # listedeki oyuncuyu geri gönderir



def birinci_durum_eslestirme_fonksiyonu(eslestirilecek_oyuncu_1,eslestirilecek_oyuncu_2,eslestirme_kismi):  # 1.durum için eşleştirme fonksiyonu
    eslestirilecek_oyuncu_1in_rengi,eslestirilecek_oyuncu_2nin_rengi =oyuncularin_renklerini_bulma(eslestirilecek_oyuncu_1,eslestirilecek_oyuncu_2) # oyuncu renklerini bulmak için fonksiyona yolladım
    if ((eslestirilecek_oyuncu_2nin_rengi == eslestirilecek_oyuncu_2["renk"] or eslestirilecek_oyuncu_2["onceki_iki_renk"] ==["-","-"]) and eslestirilecek_oyuncu_2 not in [m[0] for m in eslestirilecek_oyuncu_1["rakip_oyuncular"]]):

        ikinci_oyuncu_icin_renk_farki_hesabi, birinci_oyuncu_icin_renk_farki_hesabi = renk_farki_hesaplamasi(
            eslestirilecek_oyuncu_1, eslestirilecek_oyuncu_2, eslestirilecek_oyuncu_1in_rengi,
            eslestirilecek_oyuncu_2nin_rengi)   # renk farklarının hesaplanması için fonksiyona yolladım

        if birinci_oyuncu_icin_renk_farki_hesabi<=2 and (eslestirilecek_oyuncu_1["onceki_iki_renk"] != [eslestirilecek_oyuncu_2nin_rengi]*2):   # aradaki renk farklarına gore ve istenen kosullara gore calısacak if kısmı
            if ikinci_oyuncu_icin_renk_farki_hesabi <=2 and (eslestirilecek_oyuncu_2["onceki_iki_renk"] != [eslestirilecek_oyuncu_1in_rengi]*2):     # aradaki renk farklarına gore ve istenen kosullara gore calısacak if kısmı
                eslestirilecek_oyuncu_1["renk"] = eslestirilecek_oyuncu_2nin_rengi              # oyuncuların renkleriyle ilgili düzenlemeler
                eslestirilecek_oyuncu_1["onceki_iki_renk"][1] = eslestirilecek_oyuncu_1["onceki_iki_renk"][0]
                eslestirilecek_oyuncu_1["onceki_iki_renk"][0] = eslestirilecek_oyuncu_2nin_rengi
                eslestirilecek_oyuncu_1[eslestirilecek_oyuncu_2nin_rengi] += 1
                eslestirilecek_oyuncu_2["renk"] = eslestirilecek_oyuncu_1in_rengi
                eslestirilecek_oyuncu_2["onceki_iki_renk"][1] = eslestirilecek_oyuncu_2["onceki_iki_renk"][0]
                eslestirilecek_oyuncu_2["onceki_iki_renk"][0] = eslestirilecek_oyuncu_1in_rengi
                eslestirilecek_oyuncu_2[eslestirilecek_oyuncu_1in_rengi] += 1


                oyunculari_eslestirme_fonksiyonu(eslestirilecek_oyuncu_1, eslestirilecek_oyuncu_2, eslestirme_kismi)    # eslesen oyuncuları fonksiyona yolladım
                return True #kosulları sağladıgında True gonderecek
    return False    #kosulları sağladıgında False gonderecek



def ikinci_durum_eslestirme_fonksiyonu(eslestirilecek_oyuncu_1,eslestirilecek_oyuncu_2,eslestirme_kismi):     # 2.durum için eşleştirme fonksiyonu
    eslestirilecek_oyuncu_1in_rengi,eslestirilecek_oyuncu_2nin_rengi =oyuncularin_renklerini_bulma(eslestirilecek_oyuncu_1,eslestirilecek_oyuncu_2) # oyuncu renklerini bulmak için fonksiyona yolladım

    if eslestirilecek_oyuncu_1in_rengi == eslestirilecek_oyuncu_2["renk"]:
        if eslestirilecek_oyuncu_2 not in [onceki_rakipler[0] for onceki_rakipler in eslestirilecek_oyuncu_1["rakip_oyuncular"]]:
            ikinci_oyuncu_icin_renk_farki_hesabi,birinci_oyuncu_icin_renk_farki_hesabi = renk_farki_hesaplamasi(eslestirilecek_oyuncu_1,eslestirilecek_oyuncu_2,eslestirilecek_oyuncu_1in_rengi,eslestirilecek_oyuncu_2nin_rengi)

            if birinci_oyuncu_icin_renk_farki_hesabi<=2 and eslestirilecek_oyuncu_1["onceki_iki_renk"] != ([eslestirilecek_oyuncu_2nin_rengi] *2):   # aradaki renk farklarına gore ve istenen kosullara gore calısacak if kısmı
                if ikinci_oyuncu_icin_renk_farki_hesabi<=2 and eslestirilecek_oyuncu_2["onceki_iki_renk"] != ([eslestirilecek_oyuncu_1in_rengi] *2):     # aradaki renk farklarına gore ve istenen kosullara gore calısacak if kısmı
                    eslestirilecek_oyuncu_1["renk"] = eslestirilecek_oyuncu_2nin_rengi              # oyuncuların renkleriyle ilgili düzenlemeler
                    eslestirilecek_oyuncu_1["onceki_iki_renk"][1] = eslestirilecek_oyuncu_1["onceki_iki_renk"][0]
                    eslestirilecek_oyuncu_1["onceki_iki_renk"][0] = eslestirilecek_oyuncu_2nin_rengi
                    eslestirilecek_oyuncu_1[eslestirilecek_oyuncu_2nin_rengi] += 1
                    eslestirilecek_oyuncu_2["renk"] = eslestirilecek_oyuncu_1in_rengi
                    eslestirilecek_oyuncu_2["onceki_iki_renk"][1] = eslestirilecek_oyuncu_2["onceki_iki_renk"][0]
                    eslestirilecek_oyuncu_2["onceki_iki_renk"][0] = eslestirilecek_oyuncu_1in_rengi
                    eslestirilecek_oyuncu_2[eslestirilecek_oyuncu_1in_rengi] += 1


                    oyunculari_eslestirme_fonksiyonu(eslestirilecek_oyuncu_1,eslestirilecek_oyuncu_2,eslestirme_kismi)  # eslesen oyuncuları fonksiyona yolladım
                    return True #kosulları sağladıgında True gonderecek
    return False    #kosulları sağladıgında False gonderecek

def ucuncu_durum_eslestirme_fonksiyonu(eslestirilecek_oyuncu_1,eslestirilecek_oyuncu_2,eslestirme_kismi):     # 3.durum için eşleştirme fonksiyonu
    eslestirilecek_oyuncu_1in_rengi, eslestirilecek_oyuncu_2nin_rengi = oyuncularin_renklerini_bulma(
        eslestirilecek_oyuncu_1, eslestirilecek_oyuncu_2)   # oyuncu renklerini bulmak için fonksiyona yolladım
    if eslestirilecek_oyuncu_1in_rengi == eslestirilecek_oyuncu_2["renk"]:
        if eslestirilecek_oyuncu_2 not in [m[0] for m in eslestirilecek_oyuncu_1["rakip_oyuncular"]]:
            ikinci_oyuncu_icin_renk_farki_hesabi, birinci_oyuncu_icin_renk_farki_hesabi = renk_farki_hesaplamasi(
                eslestirilecek_oyuncu_1, eslestirilecek_oyuncu_2, eslestirilecek_oyuncu_1in_rengi,
                eslestirilecek_oyuncu_2nin_rengi)
            if birinci_oyuncu_icin_renk_farki_hesabi<=2 and (eslestirilecek_oyuncu_1["onceki_iki_renk"]!= [eslestirilecek_oyuncu_1in_rengi]*2):  # aradaki renk farklarına gore ve istenen kosullara gore calısacak if kısmı
                if ikinci_oyuncu_icin_renk_farki_hesabi<=2 and (eslestirilecek_oyuncu_2["onceki_iki_renk"]!= [eslestirilecek_oyuncu_2nin_rengi]*2):  # aradaki renk farklarına gore ve istenen kosullara gore calısacak if kısmı
                    eslestirilecek_oyuncu_1["renk"] = eslestirilecek_oyuncu_2nin_rengi                  # oyuncuların renkleriyle ilgili düzenlemeler
                    eslestirilecek_oyuncu_1["onceki_iki_renk"][1] = eslestirilecek_oyuncu_1["onceki_iki_renk"][0]
                    eslestirilecek_oyuncu_1["onceki_iki_renk"][0] = eslestirilecek_oyuncu_2nin_rengi
                    eslestirilecek_oyuncu_1[eslestirilecek_oyuncu_2nin_rengi] +=1
                    eslestirilecek_oyuncu_2["renk"] = eslestirilecek_oyuncu_1in_rengi
                    eslestirilecek_oyuncu_2["onceki_iki_renk"][1] = eslestirilecek_oyuncu_2["onceki_iki_renk"][0]
                    eslestirilecek_oyuncu_2["onceki_iki_renk"][0] = eslestirilecek_oyuncu_1in_rengi
                    eslestirilecek_oyuncu_2[eslestirilecek_oyuncu_1in_rengi]+=1

                    oyunculari_eslestirme_fonksiyonu(eslestirilecek_oyuncu_1, eslestirilecek_oyuncu_2, eslestirme_kismi)    # eslesen oyuncuları fonksiyona yolladım
                    return True #kosulları sağladıgında True gonderecek
    return False    #kosulları sağladıgında False gonderecek





def oyuncularin_renklerini_bulma(eslestirilecek_oyuncu_1,eslestirilecek_oyuncu_2):  # oyuncuların renklerini bulma fonksiyonu
    eslestirilecek_oyuncu_1in_rengi = eslestirilecek_oyuncu_1["renk"]   # oyuncu 1in rengini bulma
    eslestirilecek_oyuncu_2nin_rengi = rengin_zittini_bulma_fonksiyonu(eslestirilecek_oyuncu_1in_rengi) # zıt renk olması gerektiği için zıt renk bulma fonksiyonuna yolladım
    return eslestirilecek_oyuncu_1in_rengi,eslestirilecek_oyuncu_2nin_rengi # renkleri geri yolladım

def renk_farki_hesaplamasi(eslestirilecek_oyuncu_1,eslestirilecek_oyuncu_2,eslestirilecek_oyuncu_1in_rengi,eslestirilecek_oyuncu_2nin_rengi):   # aradaki renk farklarının hesaplanması
    ikinci_oyuncu_icin_renk_farki_hesabi = eslestirilecek_oyuncu_2[eslestirilecek_oyuncu_1in_rengi] - eslestirilecek_oyuncu_2[eslestirilecek_oyuncu_2nin_rengi] # ikinci oyuncu için renk farkının hesaplanması
    birinci_oyuncu_icin_renk_farki_hesabi = eslestirilecek_oyuncu_1[eslestirilecek_oyuncu_2nin_rengi] - eslestirilecek_oyuncu_1[eslestirilecek_oyuncu_1in_rengi]    # birinci oyuncu için rnek farkının hesaplanması
    return ikinci_oyuncu_icin_renk_farki_hesabi,birinci_oyuncu_icin_renk_farki_hesabi   # renk farklarının geri gönderilmesi

def oyunculari_eslestirme_fonksiyonu(eslestirilecek_oyuncu_1,eslestirilecek_oyuncu_2,eslestirme_kismi): # oyuncuları eslestirme fonksiyonu
    eslestirme_kismi.append(sorted([eslestirilecek_oyuncu_1,eslestirilecek_oyuncu_2], key=lambda  x: x["renk"]))    #eslestirme kısmına 2 oyuncuyu renk sırasına göre sıralayıp ekler


def tur_sonuclarini_yazdirma_fonksiyonu(eslestirme_kismi,kacinci_tur_oldugu):   # TUR SONUCLARINI YAZDIRMA FONKSİYONU

    print("{}. Tur Eşleştirme LİSTESİ:".format(kacinci_tur_oldugu))
    print(format("Beyazlar").rjust(20), end="")
    print(format("Siyahlar").rjust(20))
    print("MNo\tBSNo\tLNo\t Puan\t-\tPuan\t\tLNo\t BSNo")
    print("--- ----    ---  ----   -   ----        ---  ----")
    for masa in range(len(eslestirme_kismi)):
        print(format(masa+1).rjust(3),end="")
        print(format(eslestirme_kismi[masa][0]["BSNo"]).rjust(5),end=" ")
        print(format(eslestirme_kismi[masa][0]["LNo"]).rjust(6),end=" ")
        print(format(eslestirme_kismi[masa][0]["puan"],"5.2f"),end=" ")


        if eslestirme_kismi[masa][1] == "BYE":
            print(format("BYE").rjust(10))
            eslestirme_kismi[masa][0]["puan"]+=1
        else:
            print(format(eslestirme_kismi[masa][1]["puan"],".2f").rjust(10),end=" ")
            print(format(eslestirme_kismi[masa][1]["LNo"]).rjust(10),end=" ")
            print(format(eslestirme_kismi[masa][1]["BSNo"]).rjust(5))




def mac_sonucu_alma_fonksiyonu(kacinci_tur_oldugu,x):   # mac sonuclarını kullanıcıdan alan fonksiyon
    mac_sonucu = int(input("{}. Turda {} masada oynanan maçın sonucunu GİRİNİZ:".format(kacinci_tur_oldugu,x+1)))   # input kısmı
    mac_sonucu_ihtimalleri= [0,1,2,3,4,5]   # olabilecek mac sonuc ihtimalleri
    while mac_sonucu not in mac_sonucu_ihtimalleri: # kullanıcı farklı değer girdiğinde oyuncuyu uyaracak while dongusu
        print("0,1,2,3,4,5 seçenekleri arasından bir maç sonucu GİRİNİZ...")    # kullanıcıyı uyaran print
        mac_sonucu = int(input("{}. Turda {} masada oynanan maçın sonucunu GİRİNİZ:".format(kacinci_tur_oldugu, x + 1)))     # input kısmı
    return mac_sonucu   # mac sonucunu geri gonderen kısım


def mac_sonuclarini_listeye_isleme_fonksiyonu(mac_sonucu,kacinci_tur_oldugu,x,eslestirme_kismi):    # alınan mac sonuclarını listeye işleyen fonksiyonn
    hangi_masa_oldugu = eslestirme_kismi[x] # hangi masa oldugunun gosterilmesi
    istenen_carpim_sayisi = 0.5 # dokumanda verilen çarpım sayısı
    if mac_sonucu ==0:  # mac sonucu 0 sa dökümanda verilen bilgilere göre dictte yapılan işlemler
        hangi_masa_oldugu[0]["puan"] += 0.5
        hangi_masa_oldugu[1]["puan"] +=0.5
        hangi_masa_oldugu[0]["rakip_oyuncular"].append([hangi_masa_oldugu[1],hangi_masa_oldugu[0]["renk"],"½"])
        hangi_masa_oldugu[1]["rakip_oyuncular"].append([hangi_masa_oldugu[0],hangi_masa_oldugu[1]["renk"],"½"])
        hangi_masa_oldugu[0]["sadece_oynanan_rakipler"].append(hangi_masa_oldugu[1]["LNo"])
        hangi_masa_oldugu[1]["sadece_oynanan_rakipler"].append(hangi_masa_oldugu[0]["LNo"])


    elif mac_sonucu ==1:    # mac sonucu 1 sa dökümanda verilen bilgilere göre dictte yapılan işlemler
        hangi_masa_oldugu[0]["puan"]+=1
        hangi_masa_oldugu[0]["rakip_oyuncular"].append([hangi_masa_oldugu[1],hangi_masa_oldugu[0]["renk"],"1"])
        hangi_masa_oldugu[1]["rakip_oyuncular"].append([hangi_masa_oldugu[0],hangi_masa_oldugu[1]["renk"],"0"])
        hangi_masa_oldugu[0]["sadece_oynanan_rakipler"].append(hangi_masa_oldugu[1]["LNo"])
        hangi_masa_oldugu[1]["sadece_oynanan_rakipler"].append(hangi_masa_oldugu[0]["LNo"])

    elif mac_sonucu ==2:    # mac sonucu 2 sa dökümanda verilen bilgilere göre dictte yapılan işlemler
        hangi_masa_oldugu[1]["puan"] +=1
        hangi_masa_oldugu[0]["rakip_oyuncular"].append([hangi_masa_oldugu[1],hangi_masa_oldugu[0]["renk"],"0"])
        hangi_masa_oldugu[1]["rakip_oyuncular"].append([hangi_masa_oldugu[0],hangi_masa_oldugu[1]["renk"],"1"])
        hangi_masa_oldugu[0]["sadece_oynanan_rakipler"].append(hangi_masa_oldugu[1]["LNo"])
        hangi_masa_oldugu[1]["sadece_oynanan_rakipler"].append(hangi_masa_oldugu[0]["LNo"])

    elif mac_sonucu==3: # mac sonucu 3 sa dökümanda verilen bilgilere göre dictte yapılan işlemler
        hangi_masa_oldugu[0]["puan"]+=1
        hangi_masa_oldugu[0]["BYE"] =True
        hangi_masa_oldugu[0]["rakip_oyuncular"].append([{"BSNo": hangi_masa_oldugu[1]["BSNo"],"puan": hangi_masa_oldugu[0]["puan"]+ ((kacinci_tur_oldugu-len(hangi_masa_oldugu[0]["rakip_oyuncular"])-1)*istenen_carpim_sayisi)},hangi_masa_oldugu[0]["renk"],"+"])
        hangi_masa_oldugu[1]["rakip_oyuncular"].append([{"BSNo": hangi_masa_oldugu[0]["BSNo"],"puan": hangi_masa_oldugu[1]["puan"]+ ((kacinci_tur_oldugu-len(hangi_masa_oldugu[1]["rakip_oyuncular"])-1)*istenen_carpim_sayisi)},hangi_masa_oldugu[1]["renk"],"-"])
        hangi_masa_oldugu[0]["sadece_oynanan_rakipler"].append(hangi_masa_oldugu[1]["LNo"])
        hangi_masa_oldugu[1]["sadece_oynanan_rakipler"].append(hangi_masa_oldugu[0]["LNo"])



    elif mac_sonucu ==4:    # mac sonucu 4sa dökümanda verilen bilgilere göre dictte yapılan işlemler
        hangi_masa_oldugu[1]["puan"]+=1
        hangi_masa_oldugu[1]["BYE"] = True
        hangi_masa_oldugu[0]["rakip_oyuncular"].append([{"BSNo": hangi_masa_oldugu[1]["BSNo"],"puan": hangi_masa_oldugu[0]["puan"]+ ((kacinci_tur_oldugu-len(hangi_masa_oldugu[0]["rakip_oyuncular"])-1)*istenen_carpim_sayisi)},hangi_masa_oldugu[0]["renk"],"-"])
        hangi_masa_oldugu[1]["rakip_oyuncular"].append([{"BSNo": hangi_masa_oldugu[0]["BSNo"],"puan": hangi_masa_oldugu[1]["puan"]+ ((kacinci_tur_oldugu-len(hangi_masa_oldugu[1]["rakip_oyuncular"])-1)*istenen_carpim_sayisi)},hangi_masa_oldugu[1]["renk"],"+"])
        hangi_masa_oldugu[0]["sadece_oynanan_rakipler"].append(hangi_masa_oldugu[1]["LNo"])
        hangi_masa_oldugu[1]["sadece_oynanan_rakipler"].append(hangi_masa_oldugu[0]["LNo"])


    else:   # mac sonucu 5sa dökümanda verilen bilgilere göre dictte yapılan işlemler
        hangi_masa_oldugu[0]["rakip_oyuncular"].append([{"BSNo": hangi_masa_oldugu[1]["BSNo"],"puan": hangi_masa_oldugu[0]["puan"]+ ((kacinci_tur_oldugu-len(hangi_masa_oldugu[0]["rakip_oyuncular"])-1)*istenen_carpim_sayisi)},hangi_masa_oldugu[0]["renk"],"-"])
        hangi_masa_oldugu[1]["rakip_oyuncular"].append([{"BSNo": hangi_masa_oldugu[0]["BSNo"],"puan": hangi_masa_oldugu[1]["puan"]+ ((kacinci_tur_oldugu-len(hangi_masa_oldugu[1]["rakip_oyuncular"])-1)*istenen_carpim_sayisi)},hangi_masa_oldugu[1]["renk"],"-"])
        hangi_masa_oldugu[0]["sadece_oynanan_rakipler"].append(hangi_masa_oldugu[1]["LNo"])
        hangi_masa_oldugu[1]["sadece_oynanan_rakipler"].append(hangi_masa_oldugu[0]["LNo"])


def listede_tur_sonuclarina_gore_duzenleme_yapan_fonksiyon_1(liste):    # eşitlik bozmak için istenen kurallara gore düzenleme yapan fonksiyon 1
    for degistirilecek_oyuncu in liste: # dictteki elemanları sırayla donecek for dongusu
        for onceden_oynadiklarinin_renk_sonuclari in sorted(degistirilecek_oyuncu["rakip_oyuncular"], key=lambda m: m[0]["puan"],reverse=True)[:-1]:
            degistirilecek_oyuncu["bh1"] += onceden_oynadiklarinin_renk_sonuclari[0]["puan"]

def listede_tur_sonuclarina_gore_duzenleme_yapan_fonksiyon_2(liste):    # eşitlik bozmak için istenen kurallara gore düzenleme yapan fonksiyon  2
    for degistirilecek_oyuncu in liste: # dictteki elemanları sırayla donecek for dongusu
        for onceden_oynadiklarinin_renk_sonuclari in sorted(degistirilecek_oyuncu["rakip_oyuncular"], key=lambda m: m[0]["puan"],reverse=True)[:-2]:
            degistirilecek_oyuncu["bh2"] += onceden_oynadiklarinin_renk_sonuclari[0]["puan"]

def listede_tur_sonuclarina_gore_duzenleme_yapan_fonksiyon_3(liste):    # eşitlik bozmak için istenen kurallara gore düzenleme yapan fonksiyon  3
    for degistirilecek_oyuncu in liste: # dictteki elemanları sırayla donecek for dongusu
        for onceden_oynadiklarinin_renk_sonuclari in degistirilecek_oyuncu["rakip_oyuncular"]:
            if (onceden_oynadiklarinin_renk_sonuclari[1] != "-") and (onceden_oynadiklarinin_renk_sonuclari[2] =="1" or onceden_oynadiklarinin_renk_sonuclari[2] =="+"):
                degistirilecek_oyuncu["gs"]+=1

def listede_tur_sonuclarina_gore_duzenleme_yapan_fonksiyon_4(liste):    # eşitlik bozmak için istenen kurallara gore düzenleme yapan fonksiyon  4
    for degistirilecek_oyuncu in liste: # dictteki elemanları sırayla donecek for dongusu
        for onceden_oynadiklarinin_renk_sonuclari in degistirilecek_oyuncu["rakip_oyuncular"]:
            if onceden_oynadiklarinin_renk_sonuclari[2] in ["+","1"]:
                degistirilecek_oyuncu["sb"] += onceden_oynadiklarinin_renk_sonuclari[0]["puan"]
            elif onceden_oynadiklarinin_renk_sonuclari[2] =="½":
                degistirilecek_oyuncu["sb"] += onceden_oynadiklarinin_renk_sonuclari[0]["puan"] /2



def oyunculara_siralama_numarasi_veren_fonksiyon(liste):    # oyunculara sıralama numarası veren kısım
    for oyuncu in range(len(liste)):
        liste[oyuncu]["SNo"] = oyuncu+1

def son_siralama_listesini_yazdiran_fonksiyon(liste):   # NİHAİ TABLO PRINT KISMI
    print("NİHAİ SIRALAMA LİSTESİ")
    print("SNo BSNo    LNo Ad-Soyad       ELO     UKD     Puan    BH1     BH2    SB   GS")
    print("--- ----    --- ------------   ----    ----    ----    -----   ----   ----  --")
    for yazilacak_oyuncu in liste:
        print(format(yazilacak_oyuncu["SNo"]).rjust(3),end="")
        print(format(yazilacak_oyuncu["BSNo"]).rjust(5), end="")
        print(format(yazilacak_oyuncu["LNo"]).rjust(7), end=" ")
        print(format(yazilacak_oyuncu["isim"]), end="")
        print(format(yazilacak_oyuncu["ELO"]).rjust(19 - len(yazilacak_oyuncu["isim"])), end="")
        print(format(yazilacak_oyuncu["UKD"]).rjust(8), end="")
        print(format(yazilacak_oyuncu["puan"],".2f").rjust(9), end="")
        print(format(yazilacak_oyuncu["bh1"],".2f").rjust(8), end="")
        print(format(yazilacak_oyuncu["bh2"],".2f").rjust(7), end="")
        print(format(yazilacak_oyuncu["sb"]).rjust(7), end="")
        print(format(yazilacak_oyuncu["gs"]).rjust(4))

def capraz_tabloyu_yazdiran_fonksiyon(liste,tur_sayisi):    # CAPRAZ TABLO PRINT KISMI
    print("ÇAPRAZ TABLO")
    print("BSNo SNo   LNo  Ad-Soyad      ELO   UKD",end="    ")
    for kacinci_tur in range(tur_sayisi):
        print("{}.Tur".format(kacinci_tur+1),end="  ")
    print("Puan   BH1   BH2     SB    GS")
    print("---- ---   ---  -----------   ----  ----",end="   ")
    for kacinci_tur_1 in range(tur_sayisi):
        print("-----",end="  ")
    print("----   ----  ----    ----  ---")
    for yazilacak_oyuncu in sorted(liste, key=lambda m:m["BSNo"]):
        print(format(yazilacak_oyuncu["BSNo"]).rjust(4),end="")
        print(format(yazilacak_oyuncu["SNo"]).rjust(4),end="")
        print(format(yazilacak_oyuncu["LNo"]).rjust(6), end="  ")
        print(format(yazilacak_oyuncu["isim"]), end="")
        print(format(yazilacak_oyuncu["ELO"]).rjust(18 - len(yazilacak_oyuncu["isim"])), end="")
        print(format(yazilacak_oyuncu["UKD"]).rjust(6), end=" ")
        for kacinci_tur_2 in range(tur_sayisi):
            print(format(yazilacak_oyuncu["rakip_oyuncular"][kacinci_tur_2][0]["BSNo"]).rjust(3),end=" ")
            print(format(yazilacak_oyuncu["rakip_oyuncular"][kacinci_tur_2][1]).rjust(1),end=" ")
            print(format(yazilacak_oyuncu["rakip_oyuncular"][kacinci_tur_2][2]).rjust(1),end="")
            pass
        print(format(yazilacak_oyuncu["puan"],".2f").rjust(6), end="")
        print(format(yazilacak_oyuncu["bh1"]).rjust(7), end="")
        print(format(yazilacak_oyuncu["bh2"]).rjust(6), end="")
        print(format(yazilacak_oyuncu["sb"]).rjust(8), end="")
        print(format(yazilacak_oyuncu["gs"]).rjust(5))

main()
