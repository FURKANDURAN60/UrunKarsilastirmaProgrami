x = 0
f = 0
urunListesi = []
puanListesi = []
kriterSayisi = 0
kriterListesi = []
katsayiListesi = []

while True:
    print("""
          -----------------------------------------------------------------------[-][O][X]
          |                   KARŞILAŞTIRMA UYGULAMASINA HOŞ GELDİNİZ!!!!               |
          |        ÖĞRENCİ NOTLARINI KARŞILAŞTIRMAK İÇİN -----> 'A' TUŞUNA BASINIZ.     |
          |        ARABALARI KARŞILAŞTIRMAK İÇİN         -----> 'B' TUŞUNA BASINIZ.     |
          |        BİLGİSAYARLARI KARŞILAŞTIRMAK İÇİN    -----> 'C' TUŞUNA BASINIZ.     |
          |        TELEFONLARI KARŞILAŞTIRMAK İÇİN       -----> 'D' TUŞUNA BASINIZ.     |
          |        KENDİ İSTEDİĞİNİZ ÜRÜNLER İÇİN        -----> 'E' TUŞUNA BASINIZ.     |
          -------------------------------------------------------------------------------
           
    """)
    # secenekler=['a','b','c','d','e','A','B','C','D','E']
    secilmis = input('sectiginiz secenek: ')
    if secilmis == 'a' or 'b' or 'c' or 'd' or 'e' or 'A' or 'B' or 'C' or 'D' or 'E':
        if secilmis == 'a' or secilmis == 'A':
            import OgrenciNot
            break

        elif secilmis == 'b' or secilmis == 'B':
            import Arabalar
            break

        elif secilmis == 'c' or secilmis == 'C':
            import Bilgisayarlar
            break

        elif secilmis == 'd' or secilmis == 'D':
            import Telefonlar
            break

        elif secilmis == 'e' or secilmis == 'E':
            urunSayisi = int(input('urun sayisini giriniz: '))

            for a in range(0, urunSayisi):
                urunListesi.append(input('urun ismi giriniz: '))
            kriterSayisi = int(input('kriter sayisini giriniz: '))
            while True:
                for b in range(0, kriterSayisi):
                    print('{}. kriteri giriniz:'.format(b + 1))
                    kriterListesi.append(input())
                for c in range(0, kriterSayisi):
                    print('{} kriterinin katsayisini giriniz:'.format(kriterListesi[c]))
                    katsayiListesi.append(float(input()))
                for d in range(0, urunSayisi):
                    f = 0
                    for e in range(0, kriterSayisi):
                        print('{} urununun {} degerini giriniz: '.format(urunListesi[d], kriterListesi[e]))
                        puan = float(input())
                        f = f+(puan*katsayiListesi[e])
                    puanListesi.append(f)
                break


            tablo = zip(puanListesi, urunListesi)

            siralanmis = sorted(tablo, key=lambda x: x[0], reverse=True)

            for pair in siralanmis:
                print("{} urununun son puani {}".format(pair[1], pair[0]))
    break
