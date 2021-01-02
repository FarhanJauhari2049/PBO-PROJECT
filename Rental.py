import sqlite3

conn = sqlite3.connect("C:/Users/ASUS/3D Objects/Projet PBO/Rental.db")

tabel = [
    'CREATE TABLE IF NOT EXISTS "user" ("nama" text NOT NULL,"username" text NOT NULL, "password" text NOT NULL, "telp" INTEGER NOT NULL, PRIMARY KEY("username"))',
    'CREATE TABLE IF NOT EXISTS "katalog_Mobil" ("id_Mobil" INTEGER NOT NULL,"merkMobil" text NOT NULL, "jenisMobil" text NOT NULL, "harga_perHari" INTEGER NOT NULL, PRIMARY KEY("id_Mobil"))',
    'CREATE TABLE IF NOT EXISTS "katalog_Sopir" ("id_Sopir" INTEGER NOT NULL,"namaSopir" text NOT NULL, "umurSopir" INTEGER NOT NULL, "alamatSopir" text NOT NULL, "telpSopir" INTEGER NOT NULL,"hargaSopir" INTEGER NOT NULL,   PRIMARY KEY("id_Sopir"))',
    'CREATE TABLE IF NOT EXISTS "hasil_transaksi" ("id_transaksi" INTEGER NOT NULL,"nama" text NOT NULL, "id_Mobil" INTEGER NOT NULL, PRIMARY KEY("id_transaksi"))',]


def buat():
    for i in range(len(tabel)):
        conn.execute(tabel[i])
        conn.commit

buat()