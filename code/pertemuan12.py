#1
# def penjumlahan(x):
#     bilangan = 7
#     return x + 7

# print(penjumlahan(4))
# print(bilangan)

# #2
# print("--soal 2--")
# bilangan = 2
# def perkalian_bilangan(x):
#     return x * bilangan

# print(perkalian_bilangan(7))

# #3
# print("--soal 3--")
# def perkalian_bilangan2(x):
#     bilangan = 5  # variabel lokal, menutupi yang global
#     return x * bilangan

# print(perkalian_bilangan2(7))

# #4
# print("--soal 4--")
# bilangan = 2
# print(bilangan)

# def return_bilangan():
#     global bilangan
#     bilangan = 5
#     return bilangan

# print(return_bilangan())
# print(bilangan)

# #5
# print("--soal 5--")
# def hitung_imt(berat, tinggi):
#     imt = berat / (tinggi ** 2)
#     return imt

# def kategori_imt(imt):
#     if imt < 18.5:
#         return "Berat badan kurang"
#     elif imt >= 18.5 and imt < 25:
#         return "Berat badan normal"
#     elif imt >= 25 and imt < 30:
#         return "Berat badan berlebih"
#     else:
#         return "Obesitas"

# berat = float(input("Masukkan berat badan (kg): "))
# tinggi = float(input("Masukkan tinggi badan (meter): "))
# imt = hitung_imt(berat, tinggi)
# kategori = kategori_imt(imt)
# print("Nilai IMT kamu:", round(imt, 2))
# print("Kategori:", kategori)

# #6
# print("--soal 6--")
# def cek_segitiga(a, b, c):
#     if a + b <= c:
#         return False
#     if b + c <= a:
#         return False
#     if c + a <= b:
#         return False
#     return True

# print(cek_segitiga(1, 1, 1))
# print(cek_segitiga(1, 1, 3))

# #7
# print("--soal 7--")
# def cek_segitiga(a, b, c):
#     if a + b <= c or b + c <= a or c + a <= b:
#         return False
#     return True

# print(cek_segitiga(1, 1, 1))
# print(cek_segitiga(1, 1, 3))

# #8
# print("--soal 8--")
# def cek_segitiga(a, b, c):
#     return a + b > c and b + c > a and c + a > b

# print(cek_segitiga(1, 1, 1))
# print(cek_segitiga(1, 1, 3))

# #9
# print("--soal 9--")
# def faktorial(n):
#     if n < 0:
#         return None
#     if n < 2:
#         return 1
#     hasil = 1
#     for i in range(2, n + 1):
#         hasil = hasil * i
#     return hasil

# n = int(input("Masukkan nilai yang ingin di faktorial: "))
# print(n, "! =", faktorial(n))

# #10
# print("--soal 10--")
# def fibonacci(n):
#     if n < 1:
#         return None
#     if n < 3:
#         return 1
#     elem_1 = elem_2 = 1
#     hasil_jumlah = 0
#     for i in range(n - 2):
#         hasil_jumlah = elem_1 + elem_2
#         elem_1 = elem_2
#         elem_2 = hasil_jumlah
#     return hasil_jumlah

# for i in range(1, 10):
#     print(i, "->", fibonacci(i))

# #11
# print("--soal 11--")
# def faktorial_rekursif(n):
#     if n < 0:
#         return None
#     if n < 2:
#         return 1
#     return n * faktorial_rekursif(n - 1)

# n = int(input("Masukkan nilai faktorial (rekursif): "))
# print(n, "! =", faktorial_rekursif(n))

# #12
# print("--soal 12--")
# def fibonacci_rekursif(n):
#     if n < 1:
#         return None
#     if n < 3:
#         return 1
#     return fibonacci_rekursif(n - 1) + fibonacci_rekursif(n - 2)

# for i in range(1, 10):
#     print(i, "->", fibonacci_rekursif(i))