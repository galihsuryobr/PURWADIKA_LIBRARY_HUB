#dictionary list untuk menamlikan daftar buku 
koleksi_buku = [
    {'id':'B001', 'judul':'The High Mountain of Portugal', 'penulis': 'Yann Martel', 'status':'Tersedia'},
    {'id':'B002', 'judul':'The Thursday Murder Club', 'penulis':'Richard Osman', 'status':'Tersedia'},
    {'id':'B003', 'judul':'1984', 'penulis':'George Orwell', 'status':'Tersedia'},
    {'id':'B004', 'judul':'The Black Cat', 'penulis':'Edgar Allan Poe','status':'Tersedia'},
    {'id':'B005', 'judul':'The Song of Achilles', 'penulis':'Madeline Miller', 'status': 'Tersedia'}
]


#tabel daftar buku 
def cetak_tabel_buku (daftar_buku, hanya_tersedia=False):
    print(f"{'-'*97}")
    print(f"|{'ID':<5}|{'jUDUL BUKU':<30}|{'PENULIS':<25}|{'STATUS':<25}")
    print(f"{'-'*97}")

    ada_buku =False
    for buku in daftar_buku:
        if hanya_tersedia and buku ['status']!='Tersedia':
            continue

        print(f"|{buku ['id']:<5}|{buku ['judul']:<30}|{buku['penulis']:<25}|{buku['status']:<25}|")
        ada_buku=True

    print(f"{'-'*97}")
    return ada_buku

#menampilkan daftar buku dan menu pencarian 
def tampilkan_semua_buku():
    print('\n --- KOLEKSI SEMUA BUKU ---')
    if not koleksi_buku:
        print('Perpustakaan Kosong, Belum Ada Buku.')
        return
    cetak_tabel_buku(koleksi_buku)

def tampilkan_buku_tersedia():
    print('\n--- BUKU YANG TERSEDIA ---')
    ada_buku=cetak_tabel_buku(koleksi_buku, hanya_tersedia=True)
    if not ada_buku:
        print('Maaf, Semua Buku Sedang Dipinjam.')

def cari_buku_judul():
    print('--- CARI BUKU ---')
    cari = input('Masukkan judul buku yang dicari:').lower()

    buku_ditemukan=[]
    for buku in koleksi_buku:
        if cari in buku['judul'].lower():
            buku_ditemukan.append(buku)

    if not buku_ditemukan:
        print ('Buku dengan judul tersebut tidak ditemukan.')
    else:
        cetak_tabel_buku(buku_ditemukan)

#menu untuk pinjam, kembalikan dan edit status 
def pinjam_buku():
    print('\n--- PINJAM BUKU ---')
    nama= input('Masukkan nama anda :')
    id_cari=input('Masukkan ID buku yang ingin dipinjam : ').upper()

    for buku in koleksi_buku:
        if buku['id'] == id_cari:
            if buku['status']=='Tersedia':
                buku['status'] = f'Dipinjam ({nama})'
                print(f"Berhasil! Buku '{buku['judul']}' sekarang dipinjam oleh {nama}.")
                return
            else:
                print('Maaf, buku tersebut sedang dupinjam oleh orang lain.')
                return
    print('ID buku tidak ditemukan.')

def kembalikan_buku():
    print('\n--- KEMBALIKAN BUKU ---')
    id_cari=input('Masukkan ID buku yang dikembalikan :').upper()

    for buku in koleksi_buku:
        if buku['id']== id_cari:
            if buku['status'] !='Tersedia':
                buku['status']= 'Tersedia'
                print(f"Terimakasih! Buku '{buku['judul']}' telah dikembalikan.")
                return
            else:
                print('Buku sudah ada di perpustakaan (Tidak sedang dipinjam).')
    print('ID buku tidaak ditemukan')

#menambah daftar buku 
def tambah_buku():
    print('\n--- TAMBAH DAFTAR BUKU ---')
    judul=input('Masukkan judul buku :')
    penulis=input('Masukkan nama penulis :')

    #membuat ID otomatis 
    if koleksi_buku:
        #mengambil id terakhir berupa angka dan menambahkan 1 
        id_terakhir_angka=int(koleksi_buku[-1]['id'][1:])
        angka_baru=id_terakhir_angka + 1 
    else:
        angka_baru = 1 

    #:03d berfungsi memformat angka 1 menjadi '001',angka 10 menjadi '010'
    id_baru=f"B{angka_baru:03d}"

    buku_baru={'id':id_baru, 'judul': judul, 'penulis': penulis, 'status':'Tersedia'}
    koleksi_buku.append(buku_baru)
    print(f"Buku '{judul}' berhasil ditambahkan dengan ID: {id_baru}!")


#menghapus daftar buku 
def hapus_buku():
    print('\n--- HAPUS DAFTAR BUKU ---')
    id_hapus = input('Masukkan ID buku yang ingin dihapus: ').strip().upper()
    
    for buku in koleksi_buku:
        if buku['id'].upper() == id_hapus:
            
            #hapus buku agar gagal menghapus buku yang sedang dipinjam 
            if buku['status'].strip() != 'Tersedia':
                print(f"Gagal! Buku dengan ID {id_hapus} tidak dapat dihapus karena sedang dipinjam (Status saat ini: {buku['status']}).")
                return
            else:
                #Buku hanya akan terhapus jika statusnya benar-benar murni 'Tersedia'
                koleksi_buku.remove(buku)
                print(f"Buku dengan ID {id_hapus} berhasil dihapus dari sistem.")
                return
                
    print("Gagal! ID buku tidak ditemukan.")


#menu utama 
while True:
    print('\n==============================')
    print('     PURWADHIKA LIBRARY HUB     ')
    print('==============================')
    print('1. Lihat & Cari Buku')
    print('2. Pinjam Buku')
    print('3. Kembalikan Buku')
    print('4. Tambah Daftar Buku')
    print('5. Hapus Daftar Buku')
    print('6. Keluar Aplikasi')

    pilihan=input('Pilih Menu (1-6) : ')

    if pilihan == '1':
        while True:
            print('\n--- Lihat & Cari Buku ---')
            print('1. Lihat Semua Koleksi Buku')
            print('2. Lihat Semua Buku Tersedia')
            print('3. Cari Berdasarkan Judul')
            print('4. Kembali ke Menu Utama')
            sub_pilihan=input('Pilih Sub-Menu (1-4):')

            if sub_pilihan=='1':
                tampilkan_semua_buku()
            elif sub_pilihan=='2':
                tampilkan_buku_tersedia()
            elif sub_pilihan=='3':
                cari_buku_judul()
            elif sub_pilihan=='4':
                break
            else:
                print('Pilihan Tidak Valid!')

    elif pilihan=='2':
        pinjam_buku()
    elif pilihan=='3':
        kembalikan_buku()
    elif pilihan=='4':
        tambah_buku()
    elif pilihan=='5':
        hapus_buku()
    elif pilihan=='6':
        print('\nTerimakasih telah menggunakan Purwadhika Library Hub!')
        break
    else:
        print('Pilihan tidak valid! Silakan memasukkan angka 1 sd 6.')