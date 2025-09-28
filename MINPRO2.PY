# PROGRAM SISTEM MANAJEMEN DAFTAR KARYAWAN MIE GACOAN
import getpass  # Library untuk input password yang tersembunyi

print("=" * 61)
print("DASAR DASAR PEMPROGRAMAN")
print("MINI PROJECT 2")
print("AULIA SHEVA SAVITRI | 2509116001")
print("=" * 61)

# DATA AWAL KARYAWAN
Karyawan = [
    {"nama": "ipul", "posisi": "Kasir", "shift": "Pagi", "gaji": "4500000"},
    {"nama": "Iput", "posisi": "Koki", "shift": "Sore", "gaji": "5500000"},
    {"nama": "Selamet kopling", "posisi": "Pelayan", "shift": "Malam", "gaji": "4000000"},
    {"nama": "Cece bento", "posisi": "pelayan", "shift": "Pagi", "gaji": "4000000"},
    {"nama": "Ucup Niagara Fruit", "posisi": "Koki", "shift": "Malam", "gaji": "6000000"}
]

# DATA USER UNTUK LOGIN
users = {
    "admin": {"password": "123", "role": "admin"},
    "user": {"password": "123", "role": "user"}
}

current_user = None

def input_aman(prompt=""):
    """Fungsi input yang aman dari Ctrl+C"""
    try:
        return input(prompt)
    except KeyboardInterrupt:
        print("\nJangan pencet Ctrl+C ya...")
        return ""

def input_password_aman(prompt=""):
    """Fungsi input password yang aman dari Ctrl+C dan tersembunyi"""
    try:
        return getpass.getpass(prompt)
    except KeyboardInterrupt:
        print("\nJangan pencet Ctrl+C ya...")
        return ""

def login():
    global current_user
    
    print("\n" + "=" * 61)
    print("SISTEM LOGIN")
    print("=" * 61)
    
    attempts = 3
    while attempts > 0:
        username = input_aman("Username: ")
        if username == "":
            attempts -= 1
            continue
            
        password = input_password_aman("Password: ")
        if password == "":
            attempts -= 1
            continue
        
        if username in users and users[username]["password"] == password:
            current_user = {
                "username": username,
                "role": users[username]["role"]
            }
            print(f"\nLogin berhasil! Hai {username}")
            return True
        else:
            attempts -= 1
            if attempts > 0:
                print(f"Login gagal. Sisa percobaan: {attempts}")
    
    print("Kesempatan habis, sampai jumpa!")
    return False

def tampilkan_menu_utama():
    print("\n" + "=" * 61)
    print("DATA KARYAWAN MIE GACOAN")
    print("=" * 61)
    print("1. Tambah Karyawan Baru")
    print("2. Lihat Semua Karyawan")
    print("3. Ubah Data Karyawan")
    print("4. Hapus Data Karyawan")
    print("5. Keluar")
    print("=" * 61)

def tambah_karyawan():
    if current_user["role"] != "admin":
        print("Maaf, hanya admin yang boleh menambah karyawan")
        return
    
    print("\nTAMBAH KARYAWAN BARU")
    
    nama = input_aman("Nama karyawan: ")
    if nama == "":
        return
            
    posisi = input_aman("Posisi: ")
    if posisi == "":
        return
            
    shift = input_aman("Shift: ")
    if shift == "":
        return
            
    gaji = input_aman("Gaji: ")
    if gaji == "":
        return
        
    if not nama or not posisi or not shift or not gaji:
        print("Data harus lengkap ya...")
        return
    
    if not gaji.isdigit():
        print("Gaji harus angka dong...")
        return
        
    karyawan_baru = {
        "nama": nama,
        "posisi": posisi,
        "shift": shift,
        "gaji": gaji
    }
    Karyawan.append(karyawan_baru)
    print(f"Berhasil tambah {nama}!")

def lihat_semua_karyawan():
    print("\nDAFTAR KARYAWAN")
    
    if not Karyawan:
        print("Belum ada data karyawan nih...")
        return
    
    print(f"‖ {'No.':^3} | {'Nama':^18} | {'Posisi':^8} | {'Shift':^6} | {'Gaji':^11} ‖")
    print("=" * 61)
    
    for i, k in enumerate(Karyawan, 1):
        print(f"‖ {i:^3} | {k['nama']:<18} | {k['posisi']:<8} | {k['shift']:<6} | Rp {k['gaji']:<8} ‖")
    
    print("=" * 61)

def ubah_data_karyawan():
    if current_user["role"] != "admin":
        print("Maaf, hanya admin yang boleh ubah data")
        return
    
    print("\nUBAH DATA KARYAWAN")
    
    if not Karyawan:
        print("Belum ada data karyawan")
        return
    
    lihat_semua_karyawan()
    
    index_input = input_aman("Pilih nomor yang mau diubah: ")
    if index_input == "":
        return
            
    if not index_input.isdigit():
        print("Input harus angka ya...")
        return
    
    index = int(index_input) - 1
    
    if index < 0 or index >= len(Karyawan):
        print("Nomor tidak valid...")
        return
    
    karyawan = Karyawan[index]
    print(f"\nData yang akan diubah:")
    print(f"Nama: {karyawan['nama']}")
    print(f"Posisi: {karyawan['posisi']}")
    print(f"Shift: {karyawan['shift']}")
    print(f"Gaji: {karyawan['gaji']}")
    
    print("\nData baru (kosongkan jika tidak berubah):")
    nama_baru = input_aman("Nama baru: ") or karyawan['nama']
    posisi_baru = input_aman("Posisi baru: ") or karyawan['posisi']
    shift_baru = input_aman("Shift baru: ") or karyawan['shift']
    gaji_baru = input_aman("Gaji baru: ") or karyawan['gaji']
    
    if gaji_baru != karyawan['gaji'] and not gaji_baru.isdigit():
        print("Gaji harus angka...")
        return
    
    konfirmasi = input_aman("Yakin mau ubah? (y/n): ")
    if konfirmasi.lower() == 'y':
        Karyawan[index] = {
            "nama": nama_baru,
            "posisi": posisi_baru,
            "shift": shift_baru,
            "gaji": gaji_baru
        }
        print("Data berhasil diubah!")

def hapus_data_karyawan():
    if current_user["role"] != "admin":
        print("Maaf, hanya admin yang boleh hapus data")
        return
    
    print("\nHAPUS DATA KARYAWAN")
    
    if not Karyawan:
        print("Belum ada data karyawan")
        return
    
    lihat_semua_karyawan()
    
    index_input = input_aman("Pilih nomor yang mau dihapus: ")
    if index_input == "":
        return
            
    if not index_input.isdigit():
        print("Input harus angka...")
        return
    
    index = int(index_input) - 1
    
    if index < 0 or index >= len(Karyawan):
        print("Nomor tidak valid...")
        return
    
    karyawan = Karyawan[index]
    konfirmasi = input_aman(f"Yakin mau hapus {karyawan['nama']}? (y/n): ")
    
    if konfirmasi.lower() == 'y':
        karyawan_terhapus = Karyawan.pop(index)
        print(f"Data {karyawan_terhapus['nama']} berhasil dihapus!")

def main_program():
    if not login():
        return
    
    while True:
        tampilkan_menu_utama()
        
        try:
            pilihan = input_aman("Pilihan: ")
            
            if pilihan == "":
                continue
                
            if pilihan == '1':
                tambah_karyawan()
            elif pilihan == '2':
                lihat_semua_karyawan()
            elif pilihan == '3':
                ubah_data_karyawan()
            elif pilihan == '4':
                hapus_data_karyawan()
            elif pilihan == '5':
                print("\nTerima kasih sudah menggunakan sistem ini!")
                print("Sampai jumpa lagi...")
                break
            else:
                print("Pilihan tidak valid, coba lagi...")
                
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    print("SELAMAT DATANG PENGGUNA")
    main_program()