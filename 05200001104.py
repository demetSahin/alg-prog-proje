from math import log, ceil
from operator import itemgetter


def is_input_unique(lno, oyuncu_bilgileri):  # girilen lisans numarasının tekil olduğunu kontrol eden metot
    if lno != 0:
        for b in range(len(oyuncu_bilgileri)):
            if oyuncu_bilgileri[b][0] == lno:
                return False
    return True


def is_input_valid(desc, err):  # girilen değerin sayı karakteri olduğunu ve ondalık olmadığını kontrol eden metot
    valid_input = input(desc)
    while not valid_input.isdigit() or "," in valid_input or "." in valid_input:
        valid_input = input(err)  # girilen değer yukarıdaki ölçütlere uymuyorsa uyan bir giriş yapılana kadar dön
    return valid_input


def harf_donustur():
    ad = input("Oyuncunun adını-soyadını giriniz : ")

    while ad.find("i") != -1:  # girilen adı büyük harfe çevirmeden önce tüm 'i' karakterlerini 'İ'ye dönüştür
        ad = ad.replace("i", "İ")

    while ad.find("ı") != -1:  # girilen adı büyük harfe çevirmeden önce tüm 'ı' karakterlerini 'I'ya dönüştür
        ad = ad.replace("ı", "I")

    ad = ad.upper()

    return ad


def oyuncu_bilgilerini_al(oyuncu_bilgileri):
    lno = is_input_valid("Oyuncunun lisans numarasını giriniz (bitirmek için 0 ya da negatif giriniz) : ",
                         "Lisans numarası tamsayı ve tekil olmalıdır. Lütfen yeniden deneyiniz. (bitirmek için 0 ya da negatif giriniz) : ")
    while int(lno) > 0:
        ad = harf_donustur()
        elo = is_input_valid("Oyuncunun ELO’sunu giriniz (en az 1000, yoksa 0) : ", "Hatalı veri girdiniz. Oyuncunun ELO’su en az 1000 olmalıdır, yoksa 0 giriniz) : ")
        while int(elo) < 1000 and int(elo) != 0:
            elo = is_input_valid("Hatalı veri girdiniz. Oyuncunun ELO’su en az 1000 olmalıdır, yoksa 0 giriniz) : ",
                                 "Oyuncunun ELO’sunu giriniz (en az 1000, yoksa 0) : ")
        ukd = is_input_valid("Oyuncunun UKD’sini giriniz (en az 1000, yoksa 0) : ",
                             "Hatalı veri girdiniz. Oyuncunun UKD’si en az 1000 olmalıdır, yoksa 0 giriniz) : ")
        while int(ukd) < 1000 and int(ukd) != 0:
            ukd = is_input_valid("Hatalı veri girdiniz. Oyuncunun UKD’si en az 1000 olmalıdır, yoksa 0 giriniz) : ",
                                 "Oyuncunun UKD’sini giriniz (en az 1000, yoksa 0) : ")
        oyuncu_bilgileri.append([int(lno), ad, elo, ukd])
        lno = is_input_valid("Oyuncunun lisans numarasını giriniz (bitirmek için 0 ya da negatif giriniz) : ",
                             "Lisans numarası tamsayı ve tekil olmalıdır. Lütfen yeniden deneyiniz. (bitirmek için 0 ya da negatif giriniz) : ")
        while not is_input_unique(int(lno), oyuncu_bilgileri):
            lno = is_input_valid("Lisans numarası tamsayı ve tekil olmalıdır. Lütfen yeniden deneyiniz. (bitirmek için 0 ya da negatif giriniz) : ",
                                 "Oyuncunun lisans numarasını giriniz (bitirmek için 0 ya da negatif giriniz) : "
                                 )
    oyuncu_bilgileri.sort(key=itemgetter(0))  # burada, ilk turda puanlara bakılmadığı için, puanlar girilmeden önce, sondan başa (en az öncelikliden en çok öncelikliye) sıralama yapılmaktadır.
    oyuncu_bilgileri.sort(key=itemgetter(1))
    oyuncu_bilgileri.sort(key=itemgetter(3), reverse=True)
    oyuncu_bilgileri.sort(key=itemgetter(2), reverse=True)

    for i in range(len(oyuncu_bilgileri)):  # her bir oyuncu listesine BSNo eklenmesi. Sözlükte BSNo anahtar olarak kullanılacak.
        oyuncu_bilgileri[i] = [i + 1] + oyuncu_bilgileri[i]


def oyuncu_bilgilerini_yazdir(oyuncu_bilgileri):  # oyuncu bilgilerini istenen formatta yazdıran metot
    print("\nBaşlangıç Sıralama Listesi : ")
    print(format("BSNo", '4'), end="   ")
    print(format("LNo", '4'), end=" ")
    print(format("Ad-Soyad", '12'), end="   ")
    print(format("ELO", '4'), end="  ")
    print(format("UKD", '4'))
    print(format("----", '4'), end="  ")
    print(format("----", '4'), end="  ")
    print(format("------------", '12'), end="  ")
    print(format("----", '4'), end="  ")
    print(format("----", '4'))
    for i in range(len(oyuncu_bilgileri)):
        for j in range(len(oyuncu_bilgileri[i])):
            if j == 2:
                print('{:<12}'.format(oyuncu_bilgileri[i][j]), end="  ")
            else:
                print('{:>4}'.format(oyuncu_bilgileri[i][j]), end="  ")
        print()


def carpraz_tabloyu_yazdir(oyuncu_bilgileri):  # çarpraz tabloyu istenen formatta yazdıran metot
    for i in range(len(oyuncu_bilgileri)):
        oyuncu_bilgileri[i] = [i + 1] + oyuncu_bilgileri[i]

    oyuncu_bilgileri.sort(key=itemgetter(1))

    for i in range(len(oyuncu_bilgileri)):
        ikinci = oyuncu_bilgileri[i][1]
        oyuncu_bilgileri[i].pop(1)
        oyuncu_bilgileri[i] = [ikinci] + oyuncu_bilgileri[i]

    print("\n\nÇapraz Tablo : ")
    print(format("BSNo", '4'), end="  ")
    print(format("SNo", '3'), end="   ")
    print(format("LNo", '4'), end=" ")
    print(format("Ad-Soyad", '12'), end="   ")
    print(format("ELO", '4'), end="  ")
    print(format("UKD", '4'), end=" ")
    for i in range(len(oyuncu_bilgileri[0][6])):  # buradaki 6 sayısı tur sayısını göstermemektedir. tur bilgilerinin 6. indiste yer aldığını bildiğim için kullanılmıştır. hardcoded değildir.
        print("{0}. Tur".format(i+1, '4'), end="  ")
    print(format(" Puan", '5'), end="   ")
    print(format("BH-1", '5'), end="  ")
    print(format("BH-2", '5'), end="    ")
    print(format("SB", '3'), end=" ")
    print(format("GS", '2'))
    print(format("----", '4'), end="  ")
    print(format("---", '3'), end="  ")
    print(format("----", '4'), end="  ")
    print(format("------------", '12'), end="  ")
    print(format("----", '4'), end="  ")
    print(format("----", '4'), end="  ")
    for j in range(len(oyuncu_bilgileri[0][6])):
        print(format("------", '6'), end="  ")
    print(format(" ----", '4'), end="  ")
    print(format("-----", '5'), end="  ")
    print(format("-----", '5'), end="  ")
    print(format("-----", '5'), end="  ")
    print(format("--", '2'))
    for k in range(len(oyuncu_bilgileri)):
        for m in range(len(oyuncu_bilgileri[k])):
            if m == 12:
                pass
            elif m == 11:
                print('{:>3}'.format(str(oyuncu_bilgileri[k][m])))
            elif m == 10:
                print('{:>5.2f}'.format(oyuncu_bilgileri[k][m]), end=" ")
            elif m in [8, 9]:
                print('{:>5.2f}'.format(oyuncu_bilgileri[k][m]), end="  ")
            elif m == 7:
                print('{:>3.2f}'.format(oyuncu_bilgileri[k][m]), end="  ")
            elif m == 6:
                for n in range(len(oyuncu_bilgileri[k][m])):
                    for o in range(len(oyuncu_bilgileri[k][m][n])):
                        print('{:>1}'.format(oyuncu_bilgileri[k][m][n][o]), end=" ")
                    print(" ", end=" ")
            elif m in [0, 2, 4]:
                print('{:>4}'.format(oyuncu_bilgileri[k][m]), end="  ")
            elif m == 5:
                print('{:>4}'.format(oyuncu_bilgileri[k][m]), end="   ")
            elif m == 3:
                print('{:<12}'.format(oyuncu_bilgileri[k][m]), end="  ")
            elif m == 1:
                print('{:>3}'.format(oyuncu_bilgileri[k][m]), end="  ")


def nihai_siralamayi_yazdir(oyuncu_bilgileri):  # nihai sıralamayı istenen formatta yazdıran metot

    oyuncu_bilgileri.sort(key=itemgetter(10), reverse=True)
    oyuncu_bilgileri.sort(key=itemgetter(9), reverse=True)
    oyuncu_bilgileri.sort(key=itemgetter(8), reverse=True)
    oyuncu_bilgileri.sort(key=itemgetter(7), reverse=True)
    oyuncu_bilgileri.sort(key=itemgetter(6), reverse=True)

    print("\n\nNihai Sıralama Listesi : ")
    print(format("SNo", '3'), end="  ")
    print(format("BSNo", '4'), end="   ")
    print(format("LNo", '4'), end=" ")
    print(format("Ad-Soyad", '12'), end="   ")
    print(format("ELO", '4'), end="  ")
    print(format("UKD", '4'), end=" ")
    print(format("Puan", '4'), end="   ")
    print(format("BH-1", '5'), end="  ")
    print(format("BH-2", '5'), end="    ")
    print(format("SB", '4'), end="")
    print(format("GS", '2'))
    print(format("---", '3'), end="  ")
    print(format("----", '4'), end="  ")
    print(format("----", '4'), end="  ")
    print(format("------------", '12'), end="  ")
    print(format("----", '4'), end="  ")
    print(format("----", '4'), end="  ")
    print(format("----", '4'), end="  ")
    print(format("-----", '5'), end="  ")
    print(format("-----", '5'), end="  ")
    print(format("-----", '5'), end="  ")
    print(format("--", '2'))
    for i in range(len(oyuncu_bilgileri)):
        print('{:>3}'.format(i + 1), end="  ")
        for j in range(len(oyuncu_bilgileri[i])):
            if j == 2:
                print('{:<12}'.format(oyuncu_bilgileri[i][j]), end="  ")
                # format(matches[i][1][j], '.2f')
            elif j == 5 or j == 11:
                pass
            elif j == 6 or j == 7 or j == 8 or j == 9:
                print('{:>5.2f}'.format(oyuncu_bilgileri[i][j]), end="  ")
            elif j == 4:
                print('{:>4}'.format(oyuncu_bilgileri[i][j]), end=" ")
            elif j == 10:
                print('{:>2}'.format(oyuncu_bilgileri[i][j]))
            else:
                print('{:>4}'.format(str(oyuncu_bilgileri[i][j])), end="  ")


def eslestirmeleri_yazdir(matches, n):  # eşleştirme sonucunu istenen formatta yazdırmaya yarayan metot
    print("\n\n{0}. Tur Eşleştirme Listesi : ".format(n))
    print("       Beyazlar               Siyahlar")
    print(format("MNo", '3'), end="  ")
    print(format("BSNo", '4'), end="  ")
    print(format("LNo", '4'), end="  ")
    print(format("Puan", '4'), end="  ")
    print(format("-", '1'), end="  ")
    print(format("Puan", '4'), end="  ")
    print(format("LNo", '4'), end="  ")
    print(format("BSNo", '4'))
    print(format("---", '3'), end="  ")
    print(format("----", '4'), end="  ")
    print(format("----", '4'), end="  ")
    print(format("----", '4'), end="  ")
    print(format(" ", '1'), end="  ")
    print(format("----", '4'), end="  ")
    print(format("----", '4'), end="  ")
    print(format("----", '4'))
    bye = []
    if len(matches) % 2 == 1:
        bye = matches.pop(0)
    matches_loop = len(matches)

    for i in range(matches_loop):
        print('{:>3}'.format(i + 1), end="  ")
        for j in range(len(matches[i][0])):
            if j == 0 or j == 1:
                print('{:>4}'.format(matches[i][0][j]), end="  ")
            elif j == 6:
                print('{:>3}'.format(format(matches[i][0][j], '.2f')), end="  ")
        print("-", end="  ")
        for j in reversed(
                range(len(matches[i][1]))):  # siyahları tersten yazdırmak için reversed() fonksiyonunu kullandım
            if j == 0 or j == 1:
                print('{:>4}'.format(matches[i][1][j]), end="  ")
            elif j == 6:
                print('{:>3}'.format(format(matches[i][1][j], '.2f')), end="  ")
        print()

    if len(bye) != 0:  # oyuncu sayısı tekse eşleştirme listesinin son elemanını bye olarak yazdır
        print('{:>3}'.format(matches_loop + 1), end="  ")
        for j in range(len(bye)):
            if j == 0 or j == 1:
                print('{:>4}'.format(bye[j]), end="  ")
            elif j == 6:
                print('{:>3}'.format(format(bye[j], '.2f')), end="  ")
        print("-  BYE")
    return bye


def turnuva_bilgilerini_al(oyuncu_bilgileri, matches):  # turnuvayla ilgili temel bilgileri alıp ilk işlemleri yapan metot
    min_tur_sayisi = ceil(log(len(oyuncu_bilgileri), 2))
    max_tur_sayisi = len(oyuncu_bilgileri) - 1
    tur_sayisi = is_input_valid(
        "Turnuvadaki tur sayısını giriniz (" + str(min_tur_sayisi) + " - " + str(max_tur_sayisi) + "): ",
        "Tur sayısı " + str(min_tur_sayisi) + " ile " + str(max_tur_sayisi) + " arasında olmalıdır : ")

    while int(tur_sayisi) < min_tur_sayisi or int(tur_sayisi) > max_tur_sayisi:
        tur_sayisi = is_input_valid(
            "Tur sayısı " + str(min_tur_sayisi) + " ile " + str(max_tur_sayisi) + " arasında olmalıdır : ",
            "Tur sayısı " + str(min_tur_sayisi) + " ile " + str(max_tur_sayisi) + " arasında olmalıdır : ")
    ilk_turdaki_renk = input(
        "Baslangıç sıralamasına gore ilk oyuncunun ilk turdaki rengini giriniz (b : beyaz / s : siyah ): ")
    while ilk_turdaki_renk not in ["b", "s"]:
        ilk_turdaki_renk = input("Yanlış bir giriş yaptınız. Lütfen yeniden deneyiniz (b : beyaz / s : siyah ): ")

    ilk_siralamayi_olustur(oyuncu_bilgileri, ilk_turdaki_renk)

    ilk_eslestirmeyi_olustur(oyuncu_bilgileri, matches)

    for f in range(len(oyuncu_bilgileri)):
        oyuncu_bilgileri[f][5].pop(0)

    return int(tur_sayisi)


def ilk_siralamayi_olustur(oyuncu_bilgileri, ilk_turdaki_renk):
    loop_length = len(oyuncu_bilgileri)
    for i in range(loop_length):
        if (i + 1) % 2 == 1:
            oyuncu_bilgileri[i] += [[['0', ilk_turdaki_renk, '0']]]
        else:
            if ilk_turdaki_renk == "b":
                oyuncu_bilgileri[i] += [[['0', "s", '0']]]
            else:
                oyuncu_bilgileri[i] += [[['0', "b", '0']]]
        oyuncu_bilgileri[i] += [0.0, 0.0, 0.0, 0.0, 0]  # BH-1, BH-2, SB ve GS ilk değerleri 0 olacak şekilde eklendi.
        oyuncu_bilgileri[i] += [[False for _ in range(loop_length)]]  # oyuncunun kimlerle karşılaştığını kaydeden liste oyuncu bilgilerine ekleniyor


def ilk_eslestirmeyi_olustur(oyuncu_bilgileri, matches):
    beyazlar = []
    siyahlar = []
    for i in range(len(oyuncu_bilgileri)):
        if oyuncu_bilgileri[i][5][0][1] == "b":
            beyazlar.append(oyuncu_bilgileri[i])
        else:
            siyahlar.append(oyuncu_bilgileri[i])

    if len(beyazlar) > len(siyahlar):
        k_range = len(siyahlar)
        matches.append(beyazlar[- 1])
    elif len(beyazlar) < len(siyahlar):
        k_range = len(beyazlar)
        matches.append(siyahlar[- 1])
    else:
        k_range = len(oyuncu_bilgileri) / 2

    for i in range(k_range):
        matches.append([beyazlar[i], siyahlar[i]])


def tur_sonuclarini_al_ve_isle(oyuncu_bilgileri, oyuncu_bilgileri_dict, matches, bye, tur):
    oyuncu_bilgileri_dict.get(bye[0])[5].append(['-', '-', '1'])  # bye işlemi
    oyuncu_bilgileri_dict.get(bye[0])[6] += 1.0  # bye işlemi
    print("\n")
    for n in range(len(matches)):
        mac_sonucu = input("{0}. turda {1}. masadaki maçın sonucunu giriniz (0-5) : ".format(tur, n + 1))
        while mac_sonucu not in ["0", "1", "2", "3", "4", "5"]:
            mac_sonucu = input("0 ile 5 arasında bir giriş yapınız :")

        beyazin_tur_bilgileri = []
        siyahin_tur_bilgileri = []

        beyazin_tur_bilgileri.append(matches[n][1][0])  # beyazın karşılaştığı rakip olarak siyahın bsno'su yazılıyor
        siyahin_tur_bilgileri.append(matches[n][0][0])  # siyahın karşılaştığı rakip olarak beyazın bsno'su yazılıyor
        beyazin_tur_bilgileri.append("b")  # turdaki rengi
        siyahin_tur_bilgileri.append("s")  # turdaki rengi

        if int(mac_sonucu) == 0:
            beyazin_tur_bilgileri.append("½")  # berabere
            siyahin_tur_bilgileri.append("½")  # berabere
            oyuncu_bilgileri_dict.get(matches[n][0][0])[6] += 0.5  # beyaz yarım puan alır
            oyuncu_bilgileri_dict.get(matches[n][1][0])[6] += 0.5  # siyah yarım puan alır
        elif int(mac_sonucu) == 1:
            beyazin_tur_bilgileri.append("1")  # beyaz kazanır
            siyahin_tur_bilgileri.append("0")
            oyuncu_bilgileri_dict.get(matches[n][0][0])[6] += 1  # beyaz 1 puan kazanır
            oyuncu_bilgileri_dict.get(matches[n][0][0])[10] += 1  # beyazın galibiyet sayısı bir artırılır
        elif int(mac_sonucu) == 2:
            beyazin_tur_bilgileri.append("0")
            siyahin_tur_bilgileri.append("1")  # siyah kazanır
            oyuncu_bilgileri_dict.get(matches[n][1][0])[6] += 1  # siyah 1 puan alır
            oyuncu_bilgileri_dict.get(matches[n][1][0])[10] += 1  # siyahın galibiyet sayısı 1 artırılır
        elif int(mac_sonucu) == 3:
            beyazin_tur_bilgileri.append("+")
            siyahin_tur_bilgileri.append("-")  # siyah maça gelmemiş
            oyuncu_bilgileri_dict.get(matches[n][0][0])[6] += 1  # beyaz 1 puan kazanır
            oyuncu_bilgileri_dict.get(matches[n][0][0])[10] += 1  # beyazın galibiyet sayısı bir artırılır
        elif int(mac_sonucu) == 4:
            beyazin_tur_bilgileri.append("-")  # beyaz maça gelmemiş
            siyahin_tur_bilgileri.append("+")
            oyuncu_bilgileri_dict.get(matches[n][1][0])[6] += 1  # siyah 1 puan kazanır
            oyuncu_bilgileri_dict.get(matches[n][1][0])[10] += 1  # siyahın galibiyet sayısı bir artırılır
        elif int(mac_sonucu) == 5:  # rakiplerin ikisi de maça gelmemiş
            beyazin_tur_bilgileri.append("-")
            siyahin_tur_bilgileri.append("-")
        oyuncu_bilgileri_dict.get(matches[n][0][0])[5].append(beyazin_tur_bilgileri)
        oyuncu_bilgileri_dict.get(matches[n][1][0])[5].append(siyahin_tur_bilgileri)
        oyuncu_bilgileri_dict.get(matches[n][0][0])[11][matches[n][1][0]-1] = True
        oyuncu_bilgileri_dict.get(matches[n][1][0])[11][matches[n][0][0]-1] = True

    oyuncu_bilgileri.clear()
    for h in range(len(oyuncu_bilgileri_dict)):
        oyuncu_bilgileri.append(oyuncu_bilgileri_dict.get(h + 1))
    oyunculari_sirala(oyuncu_bilgileri)


def oyunculari_sirala(oyuncu_bilgileri):
    oyuncu_bilgileri.sort(key=itemgetter(1))
    oyuncu_bilgileri.sort(key=itemgetter(2))
    oyuncu_bilgileri.sort(key=itemgetter(4), reverse=True)
    oyuncu_bilgileri.sort(key=itemgetter(3), reverse=True)
    oyuncu_bilgileri.sort(key=itemgetter(6), reverse=True)


def eslestir(oyuncu_bilgileri, oyuncu_bilgileri_dict, matches):

    matches.clear()

    if len(oyuncu_bilgileri) % 2 == 1:  # oyuncu sayısı tekse bye geçecek elemanı bulmak için
        for r in reversed(range(len(oyuncu_bilgileri))):  # tur atlama koşulunu sağlayan elemanı bulana kadar dön
            bye_olabilir_mi = True

            for rr in range(len(oyuncu_bilgileri[r][5])):
                if oyuncu_bilgileri[r][5][rr][0] == '-' or oyuncu_bilgileri[r][5][rr][-1] == '+':
                    bye_olabilir_mi = False  # koşulları sağlamadığı için bu oyuncu bye olamaz
                    break

            if bye_olabilir_mi:
                matches.append(oyuncu_bilgileri[r])  # bye geçecek oyuncuyu eşleşme listesine at
                oyuncu_bilgileri.pop(r)  # oyuncu listesinden bye geçecek oyuncuyu çıkar
                break  # bye oyuncuyu bulduğun için döngüyü sonlandır
            else:  # bulamadıysan döngüye devam et
                continue

    outer_loop = len(oyuncu_bilgileri)
    while outer_loop > 0:
        max_point = oyuncu_bilgileri[0]
        for r in range(1, len(oyuncu_bilgileri)):
            if not oyuncu_bilgileri_dict.get(oyuncu_bilgileri[r][0])[11][max_point[0] - 1]:  # daha önce karşılaşılmamışsa
                if max_point[5][-1][1] == 's':
                    if oyuncu_bilgileri[r][5][-1][1] == 'b' or oyuncu_bilgileri[r][5][-1][1] == '-':  # 1.1 gereği
                        matches.append([max_point, oyuncu_bilgileri[
                            r]])  # koşullara uyan oyuncuyu sıralamanın en üstündeki oyuncuyla eşleşme listesine at
                        oyuncu_bilgileri.pop(r)  # eşleşen oyuncuyu oyuncu listesinden çıkar
                        oyuncu_bilgileri.pop(0)  # eşleşen oyuncuyu oyuncu listesinden çıkar
                        break  # oyuncuyu bulduğun için for döngüsünü sonlandır
                    elif len(oyuncu_bilgileri[r][5]) >= 2 and oyuncu_bilgileri[r][5][-1][1] == 's' and \
                            oyuncu_bilgileri[r][5][-2][1] != 's':  # 1.2 gereği
                        matches.append([max_point, oyuncu_bilgileri[r]])
                        oyuncu_bilgileri.pop(r)
                        oyuncu_bilgileri.pop(0)
                        break
                    elif len(max_point[5]) >= 2 and max_point[5][-2][1] != 's' \
                            and oyuncu_bilgileri[r][5][-1][1] == 's':  # 1.3 gereği
                        matches.append([oyuncu_bilgileri[r], max_point])
                        oyuncu_bilgileri.pop(r)
                        oyuncu_bilgileri.pop(0)
                        break
                    else:  # bulamadıysan döngüye devam et
                        continue
                else:
                    if oyuncu_bilgileri[r][5][-1][1] == 's' or oyuncu_bilgileri[r][5][-1][1] == '-':  # 1.1 gereği
                        matches.append([oyuncu_bilgileri[r], max_point])
                        oyuncu_bilgileri.pop(r)
                        oyuncu_bilgileri.pop(0)
                        break
                    elif len(oyuncu_bilgileri[r][5]) >= 2 and oyuncu_bilgileri[r][5][-1][1] == 'b' and \
                            oyuncu_bilgileri[r][5][-2][1] != 'b':  # 1.2 gereği
                        matches.append([oyuncu_bilgileri[r], max_point])
                        oyuncu_bilgileri.pop(r)
                        oyuncu_bilgileri.pop(0)
                        break
                    elif len(max_point[5]) >= 2 and max_point[5][-2][1] != 'b' \
                            and oyuncu_bilgileri[r][5][-1][1] == 'b':  # 1.3 gereği
                        matches.append([max_point, oyuncu_bilgileri[r]])
                        oyuncu_bilgileri.pop(r)
                        oyuncu_bilgileri.pop(0)
                        break
                    else:  # bulamadıysan döngüye devam et
                        continue

        outer_loop = len(oyuncu_bilgileri)


def buchholz(oyuncu_bilgileri_dict, dict_key):
    puanlar = []

    karsilasma = oyuncu_bilgileri_dict.get(dict_key)[11]  # oyuncunun karşılaşma listesi
    tur_sonuclari = oyuncu_bilgileri_dict.get(dict_key)[5]

    for g in range(len(karsilasma)):
        if g == dict_key - 1:  # kendisiyle karşılaşması söz konusu olmadığı için kendi indisi göz ardı edilir
            pass
        elif karsilasma[g]:
            for ts in range(len(tur_sonuclari)):
                if tur_sonuclari[ts][0] == '-':
                    puanlar.append(0)
                    break
                elif tur_sonuclari[ts][2] == '-':
                    puanlar.append(2)
                    break
                else:
                    puanlar.append(oyuncu_bilgileri_dict.get(g + 1)[6])  # karşılaştığı rakiplerin puanları
                    break

    puanlar.sort()  # puanlar küçükten büyüğe doğru sıralanıyor

    if len(puanlar) > 1:
        puanlar.pop(0)

    return puanlar


def sonneborn_berger(oyuncu_bilgileri_dict, oyuncu_bilgileri):
    galibiyetler = []
    galibiyetlerin_toplami = 0.0
    beraberlikler = []
    beraberliklerin_toplami = 0.0

    tur_sonuclari = oyuncu_bilgileri[5]

    for s in range(len(tur_sonuclari)):
        if tur_sonuclari[s][2] == "½":
            beraberlikler.append(tur_sonuclari[s][0])
        elif tur_sonuclari[s][2] == '+':
            galibiyetler.append(tur_sonuclari[s][0])
        elif tur_sonuclari[s][2] == "1" and tur_sonuclari[s][0] != '-':
            galibiyetler.append(tur_sonuclari[s][0])
        elif tur_sonuclari[s][2] == "1" and tur_sonuclari[s][0] == '-':
            galibiyetlerin_toplami += 2
    for g in range(len(galibiyetler)):
        galibiyetlerin_toplami += oyuncu_bilgileri_dict.get(galibiyetler[g])[6]
    for b in range(len(beraberlikler)):
        beraberliklerin_toplami += oyuncu_bilgileri_dict.get(beraberlikler[b])[6]
    return galibiyetlerin_toplami/2 + beraberliklerin_toplami/2


def esitligi_boz(oyuncu_bilgileri_dict):
    for i in range(len(oyuncu_bilgileri_dict)):
        bh_1_puan = 0.0
        bh_2_puan = 0.0
        bh_1_puanlar = buchholz(oyuncu_bilgileri_dict, i+1)
        for t in range(len(bh_1_puanlar)):
            bh_1_puan += bh_1_puanlar[t]
        oyuncu_bilgileri_dict.get(i+1)[7] += bh_1_puan
        bh_1_puanlar.pop(0)
        for y in range(len(bh_1_puanlar)):
            bh_2_puan += bh_1_puanlar[y]
        oyuncu_bilgileri_dict.get(i + 1)[8] += bh_2_puan
        oyuncu_bilgileri_dict.get(i + 1)[9] += sonneborn_berger(oyuncu_bilgileri_dict, oyuncu_bilgileri_dict.get(i+1))


def main():

    oyuncu_bilgileri = []  # oyuncu bilgilerini tutan 2 boyutlu liste. sıralamalar ve eşleştirmeler bu liste üzerinden yapılacak
    oyuncu_bilgileri_dict = {}  # nihai oyuncu bilgilerini başlangıç sıra no sırasında çarpraz tablo şablonuna göre tutan sözlük
    matches = []  # her turda eşleştirmeleri tutan liste

    oyuncu_bilgilerini_al(oyuncu_bilgileri)

    if len(oyuncu_bilgileri) > 0:

        oyuncu_bilgilerini_yazdir(oyuncu_bilgileri)

        tur_sayisi = turnuva_bilgilerini_al(oyuncu_bilgileri, matches)

        for s in range(len(oyuncu_bilgileri)):
            oyuncu_bilgileri_dict[s + 1] = oyuncu_bilgileri[s]

        bye = eslestirmeleri_yazdir(matches, 1)

        tur_sonuclarini_al_ve_isle(oyuncu_bilgileri, oyuncu_bilgileri_dict, matches, bye, 1)

        for p in range(1, tur_sayisi):
            eslestir(oyuncu_bilgileri, oyuncu_bilgileri_dict, matches)

            bye = eslestirmeleri_yazdir(matches, p + 1)

            tur_sonuclarini_al_ve_isle(oyuncu_bilgileri, oyuncu_bilgileri_dict, matches, bye, p + 1)

        esitligi_boz(oyuncu_bilgileri_dict)

        nihai_siralamayi_yazdir(oyuncu_bilgileri)

        carpraz_tabloyu_yazdir(oyuncu_bilgileri)
    else:
        print("Program Sonlandırıldı.")


main()
