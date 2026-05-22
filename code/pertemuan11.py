#1
# def Ucapan(benar=True):
#     print("Satu...")
#     print("Dua...")
#     print("Tiga...")
#     if not benar:
#         return
#     print("Selamat Datang")

# Ucapan()

#2
# def Ucapan(benar=True):
#     print("Satu...")
#     print("Dua...")
#     print("Tiga...")
#     if not benar:
#         return
#     print("Selamat Datang")

# Ucapan(False)

#3
# def apalah():
#     return "mania"

# Object = apalah()
# print("kicau", Object)

#4
# def apalah():
#     print("Apaa")
#     return "kicau"

# print("P")
# print("P")
# apalah()

#5
# def adadeh(n):
#     if (n % 2 == 0):
#         return True

# print(adadeh(4))
# print(adadeh(5))

#6
# def jumlah(kicau):
#     x = 0
#     for element in kicau:
#         x += element
#     return x

# print(jumlah([1, 2, 3, 4, 5]))

#7
# def jumlah(kicau):
#     x = 0
#     for element in kicau:
#         x += element
#     return x

# print(jumlah(7))

#8
# def jumlah(n):
#     adalah = []
#     for i in range(1, n):
#         adalah.insert(0, i)
#     return adalah

# print(jumlah(11))

#9
# def tahun_kabisat(tahun):
#     if (tahun % 4 == 0 and tahun % 100 != 0) or (tahun % 400 == 0):
#         return True
#     else:
#         return False

# data_uji = [1900, 2000, 2016, 1987]
# data_hasil = [False, True, True, False]

# for i in range(len(data_uji)):
#     th = data_uji[i]
#     print(th, "->", end="")
#     hasil = tahun_kabisat(th)
#     if hasil == data_hasil[i]:
#         print("ok")
#     else:
#         print("Gagal")

#10
# def tahun_kabisat(tahun):
#     if (tahun % 4 == 0 and tahun % 100 != 0) or (tahun % 400 == 0):
#         return True
#     else:
#         return False

# def hari_dalam_bulan(tahun, bulan):
#     hari_per_bulan = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#     if bulan == 2 and tahun_kabisat(tahun):
#         return 29
#     else:
#         return hari_per_bulan[bulan]

# data_uji = [1900, 2000, 2016, 1987]
# data_bulan = [2, 2, 1, 11]
# data_hasil = [28, 29, 31, 30]

# for i in range(len(data_uji)):
#     thn = data_uji[i]
#     bln = data_bulan[i]
#     print(f"Tahun: {thn}, Bulan: {bln} -> ", end="")
#     hasil = hari_dalam_bulan(thn, bln)
#     if hasil == data_hasil[i]:
#         print("ok")
#     else:
#         print("Gagal")

#11
# def tahun_kabisat(tahun):
#     if (tahun % 4 == 0 and tahun % 100 != 0) or (tahun % 400 == 0):
#         return True
#     return False

# def hari_didalam_bulan(tahun, bulan):
#     if bulan < 1 or bulan > 12:
#         return None
#     hari_per_bulan = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#     if bulan == 2 and tahun_kabisat(tahun):
#         return 29
#     return hari_per_bulan[bulan]

# def hari_pada_tahun(tahun, bulan, hari):
#     batas_hari = hari_didalam_bulan(tahun, bulan)
#     if batas_hari is None or hari < 1 or hari > batas_hari:
#         return None
#     total_hari = 0
#     for m in range(1, bulan):
#         total_hari += hari_didalam_bulan(tahun, m)
#     total_hari += hari
#     return total_hari

# print(hari_pada_tahun(2000, 12, 31))

#12
# def cek_prima(bilangan):
#     if bilangan <= 1:
#         return False
#     for n in range(2, bilangan):
#         if bilangan % n == 0:
#             return False
#     return True

# for i in range(1, 20):
#     if cek_prima(i + 1):
#         print(i + 1, end=" ")
# print()

#13
def Liter100km_ke_mpg(liter):
    mil = 100000 / 1609.344
    galon = liter / 3.785411784
    return mil / galon

def mpg_ke_Liter100km(mpg):
    liter_per_galon = 3.785411784
    ratusan_km = (mpg * 1609.344) / 100000
    return liter_per_galon / ratusan_km

print(Liter100km_ke_mpg(3.9))
print(Liter100km_ke_mpg(7.5))
print(Liter100km_ke_mpg(10.0))
print(mpg_ke_Liter100km(60.3))
print(mpg_ke_Liter100km(31.4))
print(mpg_ke_Liter100km(23.5))