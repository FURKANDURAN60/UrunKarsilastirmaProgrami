x = 0
urunSayisi = int(input('karşılaştırılacak telefon sayisini giriniz: '))
telefonListesi = []
puanListesi = []
kriterSayisi = 5
kriterListesi = ['batarya','hafiza','ram','fiyat','kamera']
katsayiListesi = [0.003,0.3,0.5,-0.001,0.05]
for a in range(0, urunSayisi):
    telefonListesi.append(input('{}. telefonun markasını giriniz: '.format(a+1)))
while True:
    for d in range(0, urunSayisi):
        f = 0
        for e in range(0, kriterSayisi):
            print('{} telefonunun {} degerini giriniz: '.format(telefonListesi[d], kriterListesi[e]))
            puan = float(input())
            f = f+(puan*katsayiListesi[e])
        puanListesi.append(f)
    break

tablo = zip(puanListesi, telefonListesi)

siralanmis = sorted(tablo, key=lambda x: x[0], reverse=True)

for pair in siralanmis:
    print("{} telefonunun son puani {}".format(pair[1], pair[0]))
