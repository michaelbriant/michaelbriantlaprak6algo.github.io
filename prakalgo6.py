# elkom 1
print('@@@@@@@ @ @@@@@ @    @ @@@@@ @@@@@ @')
print('@  @  @ @ @     @    @ @   @ @     @')
print('@  @  @ @ @     @@@@@@ @@@@@ @@@@@ @')
print('@  @  @ @ @     @    @ @   @ @     @')
print('@  @  @ @ @@@@@ @    @ @   @ @@@@@ @@@@@')

import math

print('GENAP -> Perpindahan (Diketahui v0 Konstan)')

def hitung_kecepatan_akhir(v0, a, s):
    vt2 = v0**2 + 2 * a * s
    vt = math.sqrt(vt2)
    return vt

# Memasukkan nilai kecepatan awal, percepatan, dan jarak tempuh
kecepatan_awal = int(input("Masukkan v0 = "))
percepatan = int(input("Masukkan a = "))
jarak_tempuh = int(input("Masukkan s = "))

# Memanggil fungsi untuk menghitung kecepatan akhir
hasil = hitung_kecepatan_akhir(kecepatan_awal, percepatan, jarak_tempuh)

print(f"Jarak tempuh jika kecepatan awal adalah {kecepatan_awal} dengan percepatan {percepatan} dan jarak tempuh {jarak_tempuh} adalah {hasil}")


# elkom 2
print('@@@@@@@ @ @@@@@ @    @ @@@@@ @@@@@ @')
print('@  @  @ @ @     @    @ @   @ @     @')
print('@  @  @ @ @     @@@@@@ @@@@@ @@@@@ @')
print('@  @  @ @ @     @    @ @   @ @     @')
print('@  @  @ @ @@@@@ @    @ @   @ @@@@@ @@@@@')


import math

def luas_permukaan_kubus(sisi):
    return 6 * sisi**2

def luas_permukaan_balok(panjang, lebar, tinggi):
    return 2 * (panjang * lebar + panjang * tinggi + lebar * tinggi)

def luas_permukaan_tabung(jari_jari, tinggi):
    return 2 * math.pi * jari_jari * (jari_jari + tinggi)

def luas_permukaan_kerucut(jari_jari, garis_pelukis):
    return math.pi * jari_jari * (jari_jari + garis_pelukis)

def luas_permukaan_bola(jari_jari):
    return 4 * math.pi * jari_jari**2

def main():
    while True:
        print("\nKALKULATOR MENCARI LUAS:")
        print("1. Kubus")
        print("2. Balok")
        print("3. Tabung")
        print("4. Kerucut")
        print("5. Bola")
        print("6. Keluar")

        pilihan = int(input("Mau yang mana: "))

        if pilihan == 1:
            sisi = float(input("Masukkan sisi: "))
            print(f"sisi: {sisi}")
            print(f"Luas: {luas_permukaan_kubus(sisi)}")
        elif pilihan == 2:
            panjang = float(input("Masukkan panjang: "))
            lebar = float(input("Masukkan lebar: "))
            tinggi = float(input("Masukkan tinggi: "))
            print(f"panjang: {panjang}")
            print(f"lebar: {lebar}")
            print(f"tinggi: {tinggi}")
            print(f"Luas: {luas_permukaan_balok(panjang, lebar, tinggi)}")
        elif pilihan == 3:
            jari_jari = float(input("Masukkan jari-jari: "))
            tinggi = float(input("Masukkan tinggi: "))
            print(f"jari - jari: {jari_jari}")
            print(f"tinggi: {tinggi}")
            print(f"Luas: {luas_permukaan_tabung(jari_jari, tinggi)}")
        elif pilihan == 4:
            jari_jari = float(input("Masukkan jari-jari: "))
            garis_pelukis = float(input("Masukkan garis pelukis: "))
            print(f"jari - jari: {jari_jari}")
            print(f"garis pelukis: {garis_pelukis}")
            print(f"Luas: {luas_permukaan_kerucut(jari_jari, garis_pelukis)}")
        elif pilihan == 5:
            jari_jari = float(input("Masukkan jari-jari: "))
            print(f"jari - jari: {jari_jari}")
            print(f"Luas: {luas_permukaan_bola(jari_jari)}")
        elif pilihan == 6:
            print("Terima kasih!")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih nomor dari 1 hingga 6.")

if __name__ == "__main__":
    main()