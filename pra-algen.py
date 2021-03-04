# data matakuliah
matakuliah = ["web","jarkom","struktur data","basis data I",
              "basis data II","microcontroler","microprocessor","Pengantar Pemrograman",
              "Pemrograman Terstruktur","APL","SPK","matematika dasar",
              "statistika", "robotika", "algoritma"]
banyak_mk = len(matakuliah)
input_mk = bin(banyak_mk).replace("0b","")

# data dosen
dosen = ["dosen_1","dosen_2","dosen_3","dosen_4","dosen_5",
         "dosen_6","dosen_7","dosen_8","dosen_9","dosen_10",
         "dosen_11","dosen_12","dosen_13","dosen_14", "dosen_15"]
banyak_dosen = len(dosen)
input_dosen = bin(banyak_dosen).replace("0b","")

# data kelas
kelas = ["A1","A2","A3","A4","A5","A6","A7","A8","A9","B1","B2","B3","B4","B5","B6"]
banyak_kelas = len(kelas)
input_kelas = bin(banyak_kelas).replace("0b","")

# data ruangan
ruangan = ["lab dasar1","lab dasar2","lab dasar3","lab dasar4",
           "lab jaringan1","lab jaringan2","lab jaringan3","lab jaringan4",
           "lab multimedia1","lab multimedia2","lab multimedia3","lab multimedia4",
           "lab micro1","lab micro2","lab micro3", "lab micro4"]
banyak_ruangan = len(ruangan)
input_ruangan = bin(banyak_ruangan).replace("0b","")

# data waktu
waktu = ["Senin, 07.00-07.45", "Senin, 10.00-10.45", "Senin, 14.00-14.45",
         "Selasa, 07.00-07.45", "Selasa, 10.00-10.45", "Selasa, 14.00-14.45",
         "Rabu, 07.00-07.45", "Rabu, 10.00-10.45", "Rabu, 14.00-14.45",
         "Kamis, 07.00-07.45", "Kamis, 10.00-10.45", "Kamis, 14.00-14.45",
         "Jumat, 07.00-07.45", "Jumat, 10.00-10.45", "Jumat, 14.00-14.45",]
banyak_waktu = len(waktu)
input_waktu = bin(banyak_waktu).replace("0b","")

# jumlah inputan binary
banyak_input = len(input_mk) + len(input_dosen) + len(input_kelas) + len(input_ruangan) + len(input_waktu)
print("Banyak Input Biner = "+str(banyak_input))
# banyak_input = bin(banyak_input).replace("0b","")

# input binary
while True:
    biner = input("Masukkan Angka Biner = ")
    if len(biner) >= banyak_input:
        break
    else:
        print("Inputan Biner Kurang")
# binary = "1100101010010011010110100"

# slicing binary
data_mk = biner[:len(input_mk)]
# print(data_mk)
data_dosen = biner[len(data_mk):len(data_mk)+len(input_dosen)]
# print(data_dosen)
data_kelas = biner[len(data_mk)+len(data_dosen):len(data_mk)+len(data_dosen)+len(input_kelas)]
# print(data_kelas)
data_ruangan = biner[len(data_mk)+len(data_dosen)+len(data_kelas):len(data_mk)+len(data_dosen)+len(data_kelas)+len(input_ruangan)]
# print(data_ruangan)
data_waktu = biner[len(data_mk)+len(data_dosen)+len(data_kelas)+len(data_ruangan):]
# print(data_waktu)

# convert binary
data_mk = int(data_mk,2)
data_dosen = int(data_dosen,2)
data_kelas = int(data_kelas,2)
data_ruangan = int(data_ruangan,2)
data_waktu = int(data_waktu,2)

# cetak output
print("Kelas = " + kelas[data_kelas])
print("Waktu = " + waktu[data_waktu])
print("Matakuliah = " + matakuliah[data_mk])
print("Dosen = " + dosen[data_dosen])
print("Ruangan = " + ruangan[data_ruangan])