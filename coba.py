import sqlite3

class Database :
    def __init__(self):
        self.connect = sqlite3.connect("C:/Users/ASUS/3D Objects/Projet PBO/Rental.db")

class User(Database):
    def __init__(self):
        Database.__init__(self)
        self.nama = None
        self.username = None
        self.password = None
        self.telp = None

    def TambahUser (self): 
        self.nama = input ("Masukkan nama : ")
        self.username = input ("Masukkan username : ")
        self.password = input ("Masukkan password : ")
        self.telp = input ("Masukkan no. telp : ")

        query = 'INSERT INTO user (nama,username,password,telp) VALUES (?,?,?,?)'
        isi = (self.nama,self.username,self.password,self.telp)
        self.connect.execute(query,isi)
        self.connect.commit()

    def HapusUser(self, hapus):
        for row in self.connect.execute('SELECT * FROM user'):
            print(row)
        query = 'DELETE FROM user WHERE username = ?'
        isi = hapus,
        self.connect.execute(query,isi)
        self.connect.commit()

    def LihatData(self) :
        query = 'SELECT * FROM user'
        cursor = self.connect.cursor().execute(query)
        for row in cursor :
            print(f'{row[0]}, {row[1]}, {row[2]}, {row[3]}')  

class katalog_Mobil(Database):
    def __init__ (self):
        Database.__init__(self)
        self.id_Mobil = None
        self.merkMobil = None
        self.jenisMobil = None
        self.harga_perHari = None

    def TambahMobil(self):
        self.id_Mobil = input ("Masukkan id Mobil : ")
        self.merkMobil = input ("Masukkan Merk Mobil: ")
        self.jenisMobil = input ("Masukkan Jenis Mobil : ")
        self.harga_perHari = input ("Masukkan harga per hari : ")
         
        query = 'INSERT INTO katalog_Mobil(id_Mobil,merkMobil,jenisMobil,harga_perHari) VALUES (?,?,?,?)'
        isi = (self.id_Mobil,self.merkMobil,self.jenisMobil,self.harga_perHari)
        self.connect.execute(query,isi)
        self.connect.commit()

    def HapusMobil(self, hapus):
        for row in self.connect.execute('SELECT * FROM katalog_Mobil'):
            print(row)
        query = 'DELETE FROM katalog_mobil WHERE id_mobil = ?'
        isi = hapus,
        self.connect.execute(query,isi)
        self.connect.commit()
   
    def LihatData(self):
        query= 'SELECT * FROM katalog_Mobil'
        cursor = self.connect.cursor().execute(query)
        for row in cursor :
            print(f'{row[0]}, {row[1]}, {row[2]}, {row[3]}')
               
class katalog_Sopir(Database):
    def __init__ (self):
        Database.__init__(self)
        self.id_Sopir = None
        self.namaSopir = None
        self.umurSopir = None
        self.alamatSopir = None
        self.telpSopir = None
        self.hargaSopir = None

    def TambahSopir(self):
        self.id_Sopir = input ("Masukkan id Sopir : ")
        self.namaSopir = input ("Masukkan nama Sopir : ")
        self.umurSopir = input ("Masukkan umur Sopir : ")
        self.alamatSopir = input ("Masukkan alamat Sopir : ")
        self.telpSopir = input ("Masukkan telp Sopir : ")
        self.hargaSopir = input("Masukkan harga sopir :")

        query = 'INSERT INTO katalog_Sopir(id_Sopir,namaSopir,umurSopir,alamatSopir,telpSopir,hargaSopir) VALUES (?,?,?,?,?,?)'
        isi = (self.id_Sopir,self.namaSopir,self.umurSopir,self.alamatSopir,self.telpSopir,self.hargaSopir)
        self.connect.execute(query,isi)
        self.connect.commit()

    def HapusSopir(self, hapus):
        for row in self.connect.execute('SELECT * FROM katalog_Sopir'):
            print(row)
        query = 'DELETE FROM katalog_Sopir WHERE id_Sopir = ?'
        isi = hapus,
        self.connect.execute(query,isi)
        self.connect.commit()

    def LihatData(self):
        query= 'SELECT * FROM katalog_Sopir'
        cursor = self.connect.cursor().execute(query)
        for row in cursor :
            print(f'{row[0]}, {row[1]}, {row[2]}, {row[3]}, {row[4]},{row[5]}')

class Transaksi(Database):
    def __init__ (self):
        Database.__init__(self)
        self.id_transaksi = None
        self.nama = None
        self.id_mobil= None
    
    def HasilTransaksi(self):
        self.nama = input ("Masukkan nama anda : ")
        self.id_mobil = input ("Masukkan id_mobil yang dipesan : ")
   
        query = 'INSERT INTO hasil_transaksi(id_transaksi,nama,id_mobil) VALUES (?,?,?)'
        isi = (self.id_transaksi,self.nama,self.id_mobil)
        self.connect.execute(query,isi)
        self.connect.commit()
    
    def HapusTransaksi(self, hapus):
        for row in self.connect.execute('SELECT * FROM hasil_transaksi'):
            print(row)
        query = 'DELETE FROM hasil_transaksi WHERE id_transaksi = ?'
        isi = hapus,
        self.connect.execute(query,isi)
        self.connect.commit()
    
    def LihatData(self):
        query= 'SELECT * FROM hasil_transaksi'
        cursor = self.connect.cursor().execute(query)
        for row in cursor :
            print(f'{row[0]}, {row[1]}, {row[2]}')
 
obj = User()
ktm = katalog_Mobil()
kts = katalog_Sopir()
trn = Transaksi()
    
def MenuAdmin():
    print("""
    ==+Menu Admin+==
    1.Mengecek Data User
    2.Menambah Data user
    3.Menghapus Data User
    4.Mengecek Katalog Mobil
    5.Menambah Katalog Mobil
    6.Menghapus Katalog Mobil
    7.Mengecek Data Sopir
    8.Menambah Data Sopir
    9.Menghapus Data Sopir
    10.Mengecek data transaksi
    11.Menghapus data transaksi
    12.Exit
    """)

    pilihan = input("Masukkan Pilihan menu : ")
    if pilihan == "1" :
        obj.LihatData()
    elif pilihan == "2" :
        obj.TambahUSer()
    elif pilihan == "3" :
        hapus = input('Masukkan username dari user yang akan dihapus: ')
        obj.HapusUser (hapus)
    elif pilihan == "4" :
        ktm.LihatData()
    elif pilihan == "5" :
        ktm.TambahMobil()
    elif pilihan == "6" :
        hapus = input('Masukkan id_Mobil yang akan dihapus: ')
        ktm.HapusMobil(hapus)
    elif pilihan == "7" :
        kts.LihatData()
    elif pilihan == "8" :
        kts.TambahSopir()
    elif pilihan == "9" :
        hapus = input('Masukkan id_Sopir yang akan dihapus: ')
        kts.HapusSopir(hapus)
    elif pilihan == "10" :
        trn.LihatData()
    elif pilihan == "11" :
        trn.LihatData()
        hapus = input("Masukkan id transaksi yang akan di hapus : ")
        trn.HapusTransaksi(hapus)
    elif pilihan == "12":
        exit()



def MenuUser():
    print("""
    ==Menu==
    1.Katalog Mobil
    2.Katalog Sopir
    3.Transaksi Saya
    4.Keluar
    """)
    pilih = input("Pilih Menu : ")
    if pilih == "1":
        ktm.LihatData()
        print("""
        1. Pesan
        2. Kembali
        """)
        beli = input("Pilihan : ")
        if beli == "1":
            trn.HasilTransaksi()
            trn.LihatData()
            MenuUser()
        elif beli == "2":
            MenuUser()
    elif pilih == "2":
        kts.LihatData()
        print("""
        1. Pesan
        2. Kembali
        """)
        beli = input("Pilihan : ")
        if beli == "1":
            trn.HasilTransaksi()
            trn.LihatData()
            MenuUser()
        elif beli == "2":
            MenuUser()
    elif pilih == "3":
        trn.LihatData()
        print("""
        Kembali ke menu ?
        1. Ya
        2. Tidak
        """)
        beli = input("Pilihan : ")
        if beli == "1":
            MenuUser()
        elif beli == "2":
            exit() 
    elif pilih == "4":
        exit()

def Main():
    print("====Selamat Datang Di Brother Rental Car====")
    print("""
    ===Login / Register===
    1. Login
    2. Register
    (input 1 / 2)
    """)
    masuk = input("Masukkan pilihan : ")
    if masuk == "1":
        username_admin = "admin"
        print("""
        SIapakah anda ?
        1. Admin
        2. User
        """)
        status = input("Masukkan status anda (1 / 2) : ")
        if status =="1":
            pastikan = input("Jika anda admin, masukkan username admin : ")
            if pastikan == username_admin:

                while True:
                    MenuAdmin()
            else:
                print("Anda bukan admin!! Silahkan restart program!!")
        elif status == "2":
            MenuUser()

    elif masuk == "2":
        obj.TambahUser()
        print("Data Anda telah ditambahkan")
        Main()

Main()
