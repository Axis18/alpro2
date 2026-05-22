#1 
# my_list = [2, 7, 9, 0, 4, 3, 1]
# swapped = True

# while swapped:
#     swapped = False
#     for i in range(len(my_list) - 1):
#         if my_list[i] < my_list[i + 1]:
#             swapped = True
#             my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]

# print(my_list)

#2 
# my_list = []
# swapped = True
# num = int(input("Masukkan panjang elemen list yang akan diurutkan: "))

# for i in range(num):
#     val = int(input("Masukkan elemen list: "))
#     my_list.append(val)

# while swapped:
#     swapped = False
#     for i in range(len(my_list) - 1):
#         if my_list[i] < my_list[i + 1]:
#             swapped = True
#             my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]

# print("\nSorted:")
# print(my_list)

#3 
# list = [7, 2, 5, 3, 8, 6, 1, 4, 9, 0]

# list.sort()
# print(list)

#4
# list = [9, 8, 7, 6, 5, 4, 3, 2, 1]

# list.reverse()
# print(list)

#5 
# list1 = [1]

# list2 = list1
# list1[0] = 10
# print(list1)
# print(list2)

#6
# list = [0, 1, 2, 3, 4, 5]
# listbaru = list[1:5]
# print(listbaru)

# 7
# list = [0, 1, 2, 3, 4, 5]
# listbaru = list[1:-2]
# print(listbaru)

#8 
# list = [0, 1, 2, 3, 4, 5]
# listbaru = list[-1:1]
# print(listbaru)

#9 
# list = [0, 1, 2, 3, 4, 5]
# listbaru = list[:5]
# print(listbaru)

#10 
# list = [0, 1, 2, 3, 4, 5]
# listbaru = list[1:]
# print(listbaru)

#11 
# list = [0, 1, 2, 3, 4, 5]
# listbaru = list[:]
# print(listbaru)

#12 Menghapus slice
# list = [0, 1, 2, 3, 4, 5]
# del list[1:5]
# print(list)

#13 Menghapus semua elemen list
# list = [0, 1, 2, 3, 4, 5]
# del list[:]
# print(list)

#14 Menghapus list
# listku = [0, 1, 2, 3, 4, 5]
# del listku
# print(listku)

#15 Penggunaan operator in
# listku = ["kambing", "sapi", "ayam"]

# print("kambing" in listku)
# print("kucing" in listku)
# print("anjing" not in listku)
# print("ayam" not in listku)

#16 Simple program dari list - 2
# my_list = [17, 3, 11, 5, 1, 9, 7, 15, 13]
# largest = my_list[0]

# for i in range(1, len(my_list)):
#     if my_list[i] > largest:
#         largest = my_list[i]

# print(largest)

#17 Simple program dari list - 3 (versi for i in my_list)
# my_list = [17, 3, 11, 5, 1, 9, 7, 15, 13]
# largest = my_list[0]

# for i in my_list:
#     if i > largest:
#         largest = i

# print(largest)

#18 Simple program dari list - mencari index
# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# to_find = 5
# found = False

# for i in range(len(my_list)):
#     found = my_list[i] == to_find
#     if found:
#         break

# if found:
#     print("Elemen ditemukan pada index ke-", i)
# else:
#     print("Tidak ada di dalam list")

#19 Kuis 21
# tebakanku = [3, 7, 11, 42, 34, 49]
# undian = [5, 9, 11, 42, 3, 49]
# sama = list(set(tebakanku) & set(undian))
# print(sama)

#20 Kuis 22
datalist = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]

unik = []
for angka in datalist:
    if angka not in unik:
        unik.append(angka)

print(unik)