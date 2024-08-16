# -*- coding: utf-8 -*-
import random

def tas_kagit_makas():

    # Bilgilendirme ve açılış
    print("Hoşgeldiniz! ")
    print("***Bilgilendirme***")
    print("Bu oyun taş kağıt ve makas olmak üzere üç durumda taşın makası, makasın kağıdı, kâğıdın da taşı yendiği şekilde oynanır.\n")
    print("Oyunumuz üç turdan oluşmakta, yukarıda belirtilen kurala göre puan alınmaktadır.\nBaşarılar!")

    bilgisayar = 0
    kullanıcı = 0
    round = 3

    # Bilgisayardan veri alınması
    oyun = ["tas", "kagıt", "makas"]

    while round!=0:
        x = random.randint(0, 2)
        bilgisayar_hamle = oyun[x]
        hamle = input("Tas, kagıt, makas birini giriniz:\n").lower()

        if hamle not in oyun:
            print("Geçersiz! Lütfen tas, kagıt ya da makas giriniz.")
            continue

        print("Gelen hamle: ", bilgisayar_hamle)

        if bilgisayar_hamle == hamle:
            print("Berabere!")
        elif hamle == "tas":
            if bilgisayar_hamle == "kagıt":
                bilgisayar += 1
            else:
                kullanıcı += 1
        elif hamle == "makas":
            if bilgisayar_hamle == "tas":
                bilgisayar += 1
            else:
                kullanıcı += 1
        elif hamle == "kagıt":
            if bilgisayar_hamle == "makas":
                bilgisayar += 1
            else:
                kullanıcı += 1

        print(f"Bilgisayar: {bilgisayar} | Kullanıcı: {kullanıcı}")
        round -= 1
        print(f"Kalan Round: {round}\n")

    print("Oyun Bitti!!!")
    
    if kullanıcı > bilgisayar:
       print("Kazandınız, tebrikler!!!")
    elif kullanıcı == bilgisayar:
         print("Berabere!")
    else:
        print("Kaybettiniz, şans bu sefer benden yana :)")

    # Tekrar oynama isteği
    while True:
          tekrar = input("Tekrar oynamak ister misiniz? (e/h): ").lower()
          if tekrar == 'e':
             tas_kagit_makas()
             break
          elif tekrar == 'h':
               print("Teşekkürler, görüşmek üzere!")
               break
          else:
              print("Geçersiz giriş. Lütfen 'e' ya da 'h' giriniz.")
    
   
# Oyun fonksiyonunu başlat
tas_kagit_makas()



