# TUGAS CAPSTONE PROJECT MODULE 1  - PURWADHIKA DATA SCIENTIST
# NAMA : RIZKI NUGRAHA -JCDSOL-012 (C)
# CASE STUDY : DATA PASIEN RUMAH SAKIT

dataPasien = [
    {
        'ID Pasien': 1101,
        'Nama Pasien': 'Andi',
        'Usia': 30,
        'Alamat': 'Jakarta',
        'Jenis Kelamin': 'Pria',
        'Status': 'Rawat inap',
    },
    {
        'ID Pasien': 1102,
        'Nama Pasien': 'Santi',
        'Usia': 25,
        'Alamat': 'Bandung',
        'Jenis Kelamin': 'Wanita',
        'Status': 'Rawat jalan',
    },
    {
        'ID Pasien': 1103,
        'Nama Pasien': 'Rizki',
        'Usia': 31,
        'Alamat': 'Bekasi',
        'Jenis Kelamin': 'Pria',
        'Status': 'Rawat jalan',
    },
    {
        'ID Pasien': 1104,
        'Nama Pasien': 'Nia',
        'Usia': 21,
        'Alamat': 'Depok',
        'Jenis Kelamin': 'Wanita',
        'Status': 'Rawat jalan',
    },
    {
        'ID Pasien': 1105,
        'Nama Pasien': 'Budi',
        'Usia': 27,
        'Alamat': 'Tangerang',
        'Jenis Kelamin': 'Pria',
        'Status': 'Rawat inap',
    }
]

# Main menu
def main_menu ():
    print(' ')
    print('======= Data Pasien Rumah Sakit Sehat Selalu =======')
    print(' ')
    print('1.','Daftar Data Pasien')
    print('2.','Tambah Data Pasien')
    print('3.','Ubah Data Pasien')
    print('4.','Hapus Data Pasien')
    print('5.','Keluar')
    print(' ')
    input_main_menu = input('Silakan pilih menu dengan input angka 1-5:')
    print(' ')

    if input_main_menu == '1':
        angka1()
    elif input_main_menu == '2':
        angka2()
    elif input_main_menu == '3':
        angka3()
    elif input_main_menu == '4':
        angka4()
    elif input_main_menu == '5':
        print('\n======= Terima kasih, Anda berhasil keluar =======\n')
        exit()
    else:
        print(' ')
        print('Pilihan Anda Salah dan Silahkan Masukan Angka Yang Benar')
        print(' ')
        main_menu()

# Fungsi Read Data
def angka1():
    while True:
        print('''==== Daftar Data Pasien ====
 1. Tampilkan Data Pasien
 2. Pilih Pasien Tertentu
 3. Kembali ke Menu Utama\n''')
                            
        SubMenu = int(input('''pilih daftar menu [1-3] : '''))
        if SubMenu == 1 :
            DaftarPasien()
        elif SubMenu == 2 :
            PasienTertentu()
        elif SubMenu == 3 :
            print('')
            main_menu()
        else :
            print('')
            print('Pilihan Anda Salah dan Silahkan Masukan Angka Yang Benar:')
            print(' ')
            angka1()
            break


# Tampilkan Data Pasien
def DaftarPasien():
    print(f'''\n \t\t\t==== Data Pasien Rumah Sakit Sehat Selalu ====\n''')

    print('''Nomor \t| ID Pasien  \t| Nama Pasien  \t| Usia \t| Alamat \t| Jenis Kelamin | Status''')
    for i in range (len(dataPasien)):
        print(f'''{i+1} \t| {dataPasien[i]['ID Pasien']}  \t| {dataPasien[i]['Nama Pasien']}    \t| {dataPasien[i]['Usia']} \t| {dataPasien[i]['Alamat']} \t| {dataPasien[i]['Jenis Kelamin']}  \t| {dataPasien[i]['Status']}''')
    print('')
                   
                   
# Menampilkan Unique Pasien
def PasienTertentu():
    inputid_pasien = int(input('''Silahkan masukkan id pasien :'''))
    for i in range(len(dataPasien)):
        if inputid_pasien == dataPasien[i]['ID Pasien']:
            print(f'''\n \t\t\t\t ==== Data Pasien Ada ====\n''')
            print('')
            print('''Nomor \t| ID Pasien  \t| Nama Pasien  \t| Usia \t| Alamat \t| Jenis Kelamin | Status''')
            print(f'''{i+1} \t| {dataPasien[i]['ID Pasien']}  \t| {dataPasien[i]['Nama Pasien']}  \t| {dataPasien[i]['Usia']} \t| {dataPasien[i]['Alamat']} \t| {dataPasien[i]['Jenis Kelamin']}  \t| {dataPasien[i]['Status']}''')
            print('')
            break
        elif (i == len(dataPasien)-1) and (inputid_pasien != dataPasien[i]['ID Pasien']):
            print(f'\n ==== Data yang dimasukkan tidak ada ====\n')
            print('')
           

# # Fungsi Create Data
def angka2():
    while True:
        TambahDataPasien = input('''==== Tambah Data Pasien ====
 1. Tambah Data Pasien
 2. Kembali ke Menu Utama

pilih daftar menu [1-2] : ''')

        if TambahDataPasien == '1':
            DaftarPasien()
            IdPasien = int(input('\nSilahkan masukkan id baru : '))
            for i in range (len(dataPasien)):
                if IdPasien == dataPasien[i]['ID Pasien']:
                    print(f'\n ==== Data Pasien Sudah Ada ====\n')
                    print('')
                    angka2()
                elif(i == len(dataPasien)-1) and (IdPasien != dataPasien[i]['ID Pasien']):
                    Nama_Pasien = input('nama : ').capitalize()
                    Usia = input('usia : ').capitalize()
                    Alamat = input('alamat : ').capitalize()
                    Jenis_Kelamin = input('jenis_kelamin : ').capitalize()
                    Status = input('status : ').capitalize()
            cekdata = input('''Anda yakin menambah data ini (Y/T))? : ''').capitalize()
            if cekdata == 'Y':
                dataPasien.append({
                    'ID Pasien' : IdPasien,
                    'Nama Pasien' : Nama_Pasien,
                    'Usia' : Usia,
                    'Alamat' : Alamat,
                    'Jenis Kelamin' : Jenis_Kelamin,
                    'Status' : Status
                    })
                print('\n \t\t\t\t=== Data berhasil ditambahkan === ')
                DaftarPasien()
                continue
            elif cekdata == 'T' : 
                print(f'\n ==== Data tidak ditambahkan ====\n')
                print('')
                continue
        elif TambahDataPasien == '2' : 
            print('')
            main_menu()
        else:
                print('''Pilihan Anda Salah dan Silahkan Masukan Angka Yang Benar:''')
                print('')
                angka2()


# # Fungsi Update Data
def angka3():
    while True:
        UbahDataPasien = input('''==== Ubah Data Pasien ====
 1. Ubah Data Pasien
 2. Kembali ke Menu Utama

pilih daftar menu [1-2] : ''')
        if UbahDataPasien == '1':
            DaftarPasien()
            IdPasien = int(input('\nSilahkan masukkan id pasien yang ingin anda update : '))
            for i in range (len(dataPasien)):
                if IdPasien == dataPasien[i]['ID Pasien']:
                    while True:
                        print(f'''\n \t\t\t====  Data Pasien :  ====\n''')
                        print('')
                        print('''Nomor \t| ID Pasien  \t| Nama Pasien  \t| Usia \t| Alamat \t| Jenis Kelamin | Status''')
                        print(f'''{i+1} \t| {dataPasien[i]['ID Pasien']}  \t| {dataPasien[i]['Nama Pasien']}  \t| {dataPasien[i]['Usia']} \t| {dataPasien[i]['Alamat']} \t| {dataPasien[i]['Jenis Kelamin']}  \t| {dataPasien[i]['Status']}''')
                        print('')
                        break
                    cekdata = input('Anda yakin untuk update data (Y/T) : ').capitalize()
                    if cekdata == 'Y':
                        update_detail = input('''Silahkan pilih data yang ingin anda update (ID Pasien, Nama Pasien, Usia, Alamat, Jenis Kelamin, Status ): ''').capitalize()
                        if update_detail == dataPasien[i]['ID Pasien'] :
                            update_detail = update_detail                  
                        else:
                            update_detail = update_detail
                            ubah_data = input(f'Silahkan masukkan {update_detail} yang baru : ').capitalize()
                        while True:
                            Konfirmasi = input('Anda yakin untuk update data (Y/T) : ').capitalize()
                            if Konfirmasi == 'Y':
                                dataPasien[i][update_detail] = ubah_data
                                print(f'''\n \t\t\t==== Data sudah diupdate ====\n''')
                                DaftarPasien()
                                print('')
                                angka3()
                            elif Konfirmasi == 'T':
                                print('\n ==== Data tidak ditambahkan ====\n')
                                print('')
                                angka3()
                    elif cekdata == 'T':
                        print('\n ==== Data tidak diubah ====\n')
                        print('')
                        angka3()
                elif (i == len(dataPasien)-1) and (IdPasien != dataPasien[i]['ID Pasien']):
                        print('\n ==== Data yang dimasukkan tidak ada ====\n')
                        print('')
        elif UbahDataPasien == '2' : 
            print('')
            main_menu()  
        else:
            print('''Pilihan Anda Salah dan Silahkan Masukan Angka Yang Benar:''')
            print('')
            angka3()    


# Fungsi Delete Data
def angka4():
    while True:
        HapusDataPasien = input('''==== Hapus Data Pasien ==== 
 1. Hapus Data Pasien
 2. Kembali ke Menu Utama

pilih daftar menu [1-2] : ''')
            
        if HapusDataPasien == '1':
                DaftarPasien()
                IdPasien = int(input('\nSilahkan masukkan id pasien yang ingin dihapus : '))
                for i in range (len(dataPasien)):
                    if IdPasien == dataPasien[i]['ID Pasien']:
                        while True:
                            print('''\n \t\t\t\t\t==== Data Pasien :  ====\n''')
                            print('')
                            print('''Nomor \t| ID Pasien  \t| Nama Pasien  \t| Usia \t| Alamat \t| Jenis Kelamin | Status''')
                            print(f'''{i+1} \t| {dataPasien[i]['ID Pasien']}  \t| {dataPasien[i]['Nama Pasien']}  \t| {dataPasien[i]['Usia']} \t| {dataPasien[i]['Alamat']} \t| {dataPasien[i]['Jenis Kelamin']}  \t| {dataPasien[i]['Status']}''')
                            break
                        Konfirmasi = input('Anda yakin untuk delete data (Y/T) : ').capitalize()
                        if Konfirmasi == 'Y':
                            del dataPasien[i]
                            print(f'''\n \t\t\t== Data pasien : {IdPasien} sudah berhasil dihapus ==''')
                            DaftarPasien()
                            print('')
                            angka4()
                        elif Konfirmasi == 'T':
                            print('\n ==== Data tidak dihapus ====\n')
                            print('')
                            angka4()
                    elif (i == len(dataPasien)-1) and (IdPasien != dataPasien[i]['ID Pasien']):
                            print('\n==== Data yang dimasukkan tidak ada ====\n')
                            print('')
        elif HapusDataPasien == '2' : 
            print('')
            main_menu()
        else:
            print('''Pilihan Anda Salah dan Silahkan Masukan Angka Yang Benar:''')
            print('')
            angka4()    
        
main_menu()
