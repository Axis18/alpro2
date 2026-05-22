# 1

# pangkat = [x**5 for x in range(10)]
# print(pangkat)
# dua_pangkat = [2**i for i in range(10)]
# print(dua_pangkat)
# ganjil = [x for x in pangkat if x % 2 != 0]
# print(ganjil)
# genap = [x for x in pangkat if x % 2 == 0]
# print(genap)

# 2

# papan_catur = []
# for i in range(8):
#     baris = [" " for j in range(8)]
#     papan_catur.append(baris)
# # print(papan_catur)

# papan_catur [0][0] = "O"
# papan_catur [0][1] = "X"
# papan_catur [1][2] = "O"
# papan_catur [2][3] = "X"

# for baris in papan_catur:
#     print(baris)

# 3

# nilai = [
#     [[80, 85], [75, 90]],
#     [[88, 92], [70, 78]]
# ]

# total = 0
# jumlah = 0

# for i in nilai:
#     for j in i:
#         for k in j:
#             total = total + k
#             jumlah = jumlah + 1

# rata_rata = total / jumlah
# print("Rata-rata:", rata_rata)

# 4

# def hitung_rata_rata(data):
#     total = 0
#     jumlah = 0

#     for i in data:
#         for j in i:
#             for k in j:
#                 total = total + k
#                 jumlah = jumlah + 1

#     return total / jumlah


# temperatur = [
#     [[30.5, 31.0], [29.8, 30.2]],
#     [[28.9, 29.5], [30.0, 31.2]]
# ]

# hasil = hitung_rata_rata(temperatur)
# print("Rata-rata temperatur:", hasil)

# 5

# hasil = [x * 3 for x in range(1, 11) if x % 2 == 0]
# print(hasil)

# 6

# array = [[i*3 + j + 1 for j in range(3)] for i in range(3)]

# for baris in array:
#     print(baris)

# 7

# data = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# flatten = []

# for baris in data:
#     for elemen in baris:
#         flatten.append(elemen)

# print(flatten)

# 8

def luas_persegi_panjang(panjang, lebar):
    return panjang * lebar

hasil = luas_persegi_panjang(8, 5)
print(hasil)