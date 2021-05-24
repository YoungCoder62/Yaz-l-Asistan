import time
import os
from datetime import *
from time import *
import random
from random import choice
from datetime import datetime
from playsound import playsound
import webbrowser
        

print("This Assistant Was Made On 27.12.2020 And Is Still In Development.")
print("Bu Asistan 27.12.2020 Tarihinde Yapılmıştır ve Hala Geliştirilmektedir.")
print("Yazılı Asistana Hoş Geldiniz. version: BETA 0.1.0")
print("Komutları öğrenmek için Komutlar yazmanız yeterlidir.")
print("İletişim yazarak discord sunucumuza gidebilirsiniz.İsteklerinizi ve şikayetlerinizi ordan bizlere İletebilirsiniz.")

deyımler = ["Açık kapı bırakmak; Bir olay ve sıkıntı karşısında sıkıntının  bu şekilde devam etmeyeceğini belirtmek.","Ağzında bakla ıslanmamak; Duyduğu bir lafı başkasından saklayamamak, boşboğazlık","Bal dök yala; Her tarafı tertemiz yapmak.","Can kulağı ile dinlemek; Tüm dikkati ile dinlemek.","Cebi delik; Savurgan olan Para biriktiremeyen kişidir.","Çalmadan Oynamak; Eğlenecek bir şey hemen bulan. Teneke sesine daği oynamaya başlayan.","Çam devirmek; Boşboğazlık ederek söylenmemesi gereken lafı söylemek","Çamur atmak; Bir kişiye yalan ithamlarda bulunmak.","Çantada Keklik; Çabucak elde edilmek.Emek harcamadan sahip olmak","Damarına Basmak; Bir kişinin en hassas olduğu konulara değinmek.","Damdan düşer gibi; Birden bire ansızın olan durumlarda kullanılır","Dış kapının dış mandalı; Çok yakın olmadığı halde konuya dahil olana denir.","Dilli Düdük; Geveze kişişlere denir.","Eceline Susamak; Tehlikeli olayların içerisinde yer almak.","Ekmeğine kan doğramak; Büyük acı içerisinde olmak","El Etek Çekmek; Yaptığı işi bırakmak","Fırıldak gibi dönmek; Bencil şekilde davranmak","Fink Atmak; Kafasına göre davranmak,hareket etmek","Göz Gezdirmek; Derinlemesine incelemeden okumak. Bir şeyi, bir yeri pek fazla dikkat etmeden çabucak incelemek.”Raftaki mallara şöyle bir göz gezdirip çıkalım.”","Göz Değmek; Nazar"]

atasozu = ["Aba vakti yaba, yaba vakti aba: Kişinin ihtiyaçlarını mevsiminden, sezonundan, vaktinden önce ucu olduğu zamanda karşılaması.","Bağlandığı yerde otlamak : Yerinde saymak, hiçbir ilerleme göstermemek.","Bahtına küsmek : İşlerin ters gitmesi yüzünden karamsar olmak; şansına küsmek, talihine küsmek.","Balık istifi: Çok sıkışık , üst üste, kalabalık olarak.","Can baş üstüne: İstenilen, arzu edilen şeyin büyük bir memnunlukla yapılacağını anlatır. “Can baş üstüne efendim, kasabaya varınca onu hemen göreceğim.”","Can sıkıntısı: Yapılacak iş ve bir şeyle oyalanma imkânı bulamamaktan duyulan tedirginlik, içine düşülen bunalım. “Bütün gün evde oturuyor, can sıkıntısından ne yapacağımı bilemiyordum.”","Dağa kaldırmak:  Herhangi bir sebepten ötürü birini zorla dağa veya ıssız bir yere götürüp orada alıkoymak. “Eşkıyalar, karakol komutanının oğlunu dağa kaldırmışlar; ne istedikleri henüz belli değil.”","Dalavere çevirmek: Yalan, dolan ve hile ile kötü bir iş yapmak; düzen kurarak gizlice başkasını aldatmak.”Yine bir dalavere çevirmesin bu adam!”","Edebiyat yapmak: Bir işe yaramayan, konuyu açıklamaya yetmeyen, gerçeği yansıtmayan süslü, parlak ve gereksiz sözler söylemek.“Edebiyat yapmaya amma da meraklı bir insanmış.”","Efkâr dağıtmak: Sıkıntıyı gidermek, üzüntüyü yok etmeye çalışmak.“Sahile efkâr dağıtmak için inmiş olmalı.”","El ayak çekilmek: Ortalıkta kimse kalmamak, ıssızlaşıp sessizleşmek.“Bu iş ancak el ayak çekildikten sonra yapılır.”","Madik atmak: Hile, düzen ve oyunla aldatmak; dolap çevirmek. “Ona kolay kolay kimse madik atamaz.”","Nara atmak: Yüksek bir sesle haykırmak, kabadayıca bağırmak. “Birahaneden çıkan sarhoşlar edepsizce nara atmaya başladılar.”"]

komutlar = """
    Komutlar:
    1-Nasılsın
    2-Teşekkür Ederim
    3-Bende İyiyim
    4-Adın Ne
    5-Hesap Makinesi
    6-Hava Durumu
    7-Youtube
    8-Çeviri
    9-Komutlar
    10-Temizle
    11-İletişim
    12-Yardım
    13-Youtube'de Ara
    14-Google'de Ara
    15-Saat Kaç
    16-Spotify
    17-Tarih
    18-Deyim
    19-Atasözü
    22-Çıkış
    Yeni komutlar eklenecektir.Komutları Büyük Yada Küçük Harfler ile Yazabilirsiniz.\nParantez içinde yazılan yazılar komut değildir.
"""

while True:


    print("Merhaba Ne Yapmamı İstersiniz?")
    ıstek = input("İstekte Bulunun: ")
    ıstek = ıstek.upper()

    if ıstek == "NASILSIN":
        print("İyiyim Sen Nasılsın? ")

    elif ıstek == "BENDE İYİYİM":
        print("Sevindim.")

    elif ıstek == "TEŞEKKÜR EDERİM":
        print("Rica Ederim.")    

    elif ıstek == "ADIN NE":
        os.system("cls")
        ısım = input("Benim Adım LİLİ senin adın ne? ") 
        print("Tanıştığıma memnun oldum ",ısım)
        
    elif ıstek == "HESAP MAKİNESİ":
        os.system("cls")
        print("Lütfen Bekleyin...")
        os.system("calc")
        
    elif ıstek == "DEYİM":
        os.system("cls")
        rd = deyımler[random.randint(0,len(deyımler)-1)]
        print("Deyim: ",rd)
        asi = input("Atasözü'de söylememi istermisiniz Evet/Hayır: ")
        asi = asi.upper()
        if asi == "EVET":
            ras2 = atasozu[random.randint(0,len(atasozu)-1)]
            print("Atasözü: ",ras2)
        elif asi == "HAYIR":
            print("Tamam :)")
        else:
            print("Lütfen evet yada hayır yazın.")    


    elif ıstek == "ATASÖZÜ":
        os.system("cls")
        ras = atasozu[random.randint(0,len(atasozu)-1)]
        print("Atasözü: ",ras)
        asi2 = input("Deyim'de söylememi istermisiniz Evet/Hayır: ")
        asi2 = asi2.upper()
        if asi2 == "EVET":
            rd2 = deyımler[random.randint(0,len(deyımler)-1)]
            print("Deyim: ",rd2)
        elif asi2 == "HAYIR":
            print("Tamam :)")
        else:
            print("Lütfen evet yada hayır yazın.")        

    elif ıstek == "TEMİZLE":
        os.system("cls")

    elif ıstek == "HAVA DURUMU":
        os.system("cls")
        print("Sadece Chrome/Google için geçerlidir.")
        sehir = input("Hangi Şehir: ")
        os.system("start Chrome https://www.google.com/search?q="+sehir+"+hava+durumu")

    elif ıstek == "YOUTUBE'DE ARA":
        os.system("cls")
        kc = input("Aramak istediğiniz kelime kaç kelime: ")
        if kc == "1":
            klm1 = input("Youtube'de ne aramak istersiniz: ")
            os.system("start Chrome https://www.youtube.com/results?search_query="+klm1)
        
        elif kc == "2":
            os.system("cls")
            klm2 = input("Youtube'de aramak istediğiniz ilk kelimeyi yazınız: ")
            klm3 = input("Youtube'de aramak istediğiniz ikinci kelimeyi yazınız: ")
            os.system("start Chrome https://www.youtube.com/results?search_query="+klm2+"+"+klm3)

        elif kc == "3":
            os.system("cls")
            klm4 = input("Youtube'de aramak istediğiniz ilk kelimeyi yazınız: ")
            klm5 = input("Youtube'de aramak istediğiniz ikinci kelimeyi yazınız: ")
            klm6 = input("Youtube'de aramak istediğiniz üçüncü kelimeyi yazınız: ")
            os.system("start Chrome https://www.youtube.com/results?search_query="+klm4+"+"+klm5+"+"+klm6)

        elif kc == "4":
            os.system("cls")
            klm7 = input("Youtube'de aramak istediğiniz ilk kelimeyi yazınız: ")
            klm8 = input("Youtube'de aramak istediğiniz ikinci kelimeyi yazınız: ")
            klm9 = input("Youtube'de aramak istediğiniz üçüncü kelimeyi yazınız: ")
            klm10 = input("Youtube'de aramak istediğiniz dördüncü kelimeyi yazınız: ")
            os.system("start Chrome https://www.youtube.com/results?search_query="+klm7+"+"+klm8+"+"+klm9+"+"+klm10)

        elif kc == "5":
            os.system("cls")
            klm11 = input("Youtube'de aramak istediğiniz ilk kelimeyi yazınız: ")
            klm12 = input("Youtube'de aramak istediğiniz ikinci kelimeyi yazınız: ")
            klm13 = input("Youtube'de aramak istediğiniz üçüncü kelimeyi yazınız: ")
            klm14 = input("Youtube'de aramak istediğiniz dördüncü kelimeyi yazınız: ")
            klm15 = input("Youtube'de aramak istediğiniz beşinci kelimeyi yazınız: ")
            os.system("start Chrome https://www.youtube.com/results?search_query="+klm11+"+"+klm12+"+"+klm13+"+"+klm14+"+"+klm15)

        else:
            os.system("cls")
            print("en fazla 5 kelimeli arama yapabilirsiniz.") 

    elif ıstek == "GOOGLE'DE ARA":
        os.system("cls")
        print("Şuanda sadece 1 kelime araya bilirsiniz 1 den fazla kelime yazmayınız.")
        word = input("Aramak istediğiniz kelimeyi giriniz: ")  
        os.system("start Chrome https://www.google.com/search?q="+word)       

    elif ıstek == "YOUTUBE":
        os.system("cls")
        tarayici = input("Hangi Tarayıcıyı Kullanıyorsunuz: ")
        soru = input("Youtube.com adresine yönlendiriliyorsunuz.Onaylıyormusunuz Evet/Hayır: ")
        soru = soru.upper()
        if soru == "EVET":
            os.system("start" + " " + tarayici + " " + "www.youtube.com")
        elif soru == "HAYIR":
            print("İşleminiz İptal Edilmiştir.")
        else:
            print("Lütfen Sadece ilk harfi büyük Evet yada Hayır yazın.") 

    elif ıstek == "ÇEVİRİ":
        os.system("cls")
        print("Sadece Chrome/Google için geçerlidir.")
        os.system("start Chrome www.google.com/search?q=ingilizce-türkçe+çeviri&oq=ingi&aqs=chrome.1.69i57j35i39j0j46j0l4.4321j0j7&sourceid=chrome&ie=UTF-8")

    elif ıstek == "İLETİŞİM":
        os.system("cls")
        soru2 = input("Bu Asistanı Yapan Kişinin Discord Sunucusuna Yönlendiriliyorsunuz.Onaylıyormusunuz Evet/Hayır: ")
        soru2 = soru2.upper()
        if soru2 == "EVET":
            os.system("start Chrome https://discord.gg/q4CwcCW")
        elif soru2 == "HAYIR":
            print("İşleminiz İptal Edilmiştir.")
        else:
            print("Lütfen Sadece Evet yada Hayır yazın.")

    elif ıstek == "SPOTİFY":
        print("Spotify açılıyor...")
        os.system("start Chrome https://www.spotify.com/tr/")       

    elif ıstek == "SAAT KAÇ":
        os.system("cls")
        s = strftime('%H:%M:%S')
        print("Şuanda Saat: "+s)      

    elif ıstek == "TARİH":
        ta = strftime('%D')
        print("Bugünün Tarihi: "+ta)

    elif ıstek == "YARDIM":
        os.system("cls")
        print(komutlar, "Tüm komutlar yazıldığı gibidir.")         
        print("İletişim yazarak discord sunucumuza gidebilirsiniz")

    elif ıstek == "TELİF HAKLARI":
        os.system("cls")
        print("Telif Hakları ©2020 Solo Baran'a aittir.Tüm Hakları saklıdır.\nDetaylı Bilgi İçin İletişim yazarak discord sunucumuza gidebilirsiniz.")
        print("Copyright ©2020 Solo Baran.All rights reserved.For detailed information, you can go to our discord server by typing Contact.")    
        print("Bu Asistan 27.12.2020 Tarihinde Yapılmıştır ve Hala Geliştirilmektedir.")
        print("This Assistant Was Made On 27.12.2020 And Is Still In Development.")

    elif ıstek == "KOMUTLAR":
        os.system("cls")
        print(komutlar)     

    elif ıstek == "ÇIKIŞ":
        os.system("cls")
        print("Görüşmek Üzere İyi Günler Dilerim.")
        print("Çıkış Yapılıyor...")
        break

    else:
        os.system("cls")
        print("Ne Dediğinizi Anlamadım.")