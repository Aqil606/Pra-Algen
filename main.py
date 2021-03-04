matakuliah = ["web","jarkom","struktur data","basis data I",
              "basis data II","microcontroler","microprocessor","Pengantar Pemrograman",
              "Pemrograman Terstruktur","APL","SPK","matematika dasar",
              "statistika", "robotika", "algoritma", "fisika"]

banyak_mk = len(matakuliah)
input_mk = bin(banyak_mk).replace("0b","")
banyak_input = int(len(input_mk))
banyak_input = bin(banyak_input).replace("0b","")
print(banyak_input)

while True:
    binary = input("Masukkan Angka Biner = ")
    if len(binary) == banyak_input:
        print(binary)
        break
    else:
        print("Inputan Salah")