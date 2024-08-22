x = 0
urunSayisi = int(input('karşılaştırılacak araba sayisini giriniz: '))
arabaListesi = []
puanListesi = []
kriterSayisi = 5
kriterListesi = ['depo hacmi', 'hiz', 'konfor', 'fiyat', 'beygir gucu']
katsayiListesi = [10, 4, 7, -0.0005, 5]
for a in range(0, urunSayisi):
    arabaListesi.append(input('{}. arabanın markasını giriniz: '.format(a+1)))
while True:
    for d in range(0, urunSayisi):
        f = 0
        for e in range(0, kriterSayisi):
            print("{} arabasinin {} degerini giriniz: ".format(arabaListesi[d], kriterListesi[e]))
            puan = float(input())
            f = f+(puan*katsayiListesi[e])
        puanListesi.append(f)
    break

tablo = zip(puanListesi, arabaListesi)

siralanmis = sorted(tablo, key=lambda x: x[0], reverse=True)

for pair in siralanmis:
    print("{} arabasinin son puani {}".format(pair[1], pair[0]))
