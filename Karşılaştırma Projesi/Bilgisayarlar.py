x = 0
urunSayisi = int(input('karşılaştırılacak bilgisayar sayisini giriniz: '))
bilgisayarListesi = []
puanListesi = []
kriterSayisi = 4
kriterListesi = ['batarya', 'hafiza', 'ram', 'fiyat',]
katsayiListesi = [0.0007, 0.4, 0.4, -0.0003]
for a in range(0, urunSayisi):
    bilgisayarListesi.append(input('{}. bilgisayarın ismini giriniz: '.format(a+1)))
while True:
    for d in range(0, urunSayisi):
        f = 0
        for e in range(0, kriterSayisi):
            print('{} bilgisayarinin {} degerini giriniz: '.format(bilgisayarListesi[d], kriterListesi[e]))
            puan = float(input())
            f = f+(puan*katsayiListesi[e])
        puanListesi.append(f)
    break

tablo = zip(puanListesi, bilgisayarListesi)

siralanmis = sorted(tablo, key=lambda x: x[0], reverse=True)

for pair in siralanmis:
    print("{} bilgisayarinin son puani {}".format(pair[1], pair[0]))
