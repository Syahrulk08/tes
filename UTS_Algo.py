Nama = input("Masukkan Nama Karyawan\t = ")
Golongan = input("Masukkan Golongan (A,B,C)\t = ")
Jam_kerja = int(input("Masukkan Jumlah Jam Kerja\t = "))

if Golongan == "A":
        gaji_pokok = 500000
        tunjangan = gaji_pokok * 10/100
        Gajii = gaji_pokok + tunjangan
        print(Gajii)
    if Jam_kerja >= 200:
        lembur = (Jam_kerja - 200) * 5000
        Gaji = gaji_pokok + tunjangan + lembur
        print(Gaji)
# elif Golongan == "B":
#         gaji_pokok = 700000
#         tunjangan = gaji_pokok * 15/100
#         Gaji = gaji_pokok + tunjangan
#     if Jam_kerja >= 200:
#         lembur = (Jam_kerja - 200) * 7500
#         Gaji = gaji_pokok + tunjangan + lembur
#     else print(Gaji1)
# else Golongan  