# Minpro-2
*Nama: Aulia Sheva Savitri*
*NIM: 2509116001*
*SISTEM MANAGEMEN DATA KARYAWAN MIE GACOAN*

# Flowchart
![alt text](https://github.com/auliasheva/Minpro-2/blob/main/minpro2.drawio%20(1).png?raw=true)

Program ini diawali dengan proses login, di mana pengguna diberi tiga kali kesempatan untuk memasukkan username dan password. Jika login berhasil, sistem akan menampilkan identitas beserta role pengguna, yaitu admin atau user. Setelah itu, program menampilkan menu utama yang berisi lima pilihan: tambah karyawan, lihat data karyawan, ubah data karyawan, hapus karyawan, dan keluar.

Hak akses dibedakan berdasarkan role, admin dapat menggunakan semua fitur sedangkan user hanya bisa melihat data karyawan. Setiap pilihan menu memiliki alurnya masing-masing, mulai dari menambah data baru, menampilkan daftar karyawan, mengubah data dengan memilih nomor karyawan, hingga menghapus data dengan konfirmasi. Program berakhir ketika pengguna memilih keluar, dan sistem menampilkan pesan terima kasih sebelum berhenti.


# Output Admnin

* Tampilan Awal Login.
  Program menampilkan identitas pembuat dan judul mini project, kemudian menyapa pengguna. Setelah itu sistem meminta login. Pada gambar ini, login dilakukan dengan username admin. Hasilnya, login berhasil dan sistem menyapa dengan pesan: “Login berhasil! Hai admin”.

![alt text](https://github.com/auliasheva/Minpro-2/blob/main/minpro%202/Cuplikan%20layar%202025-09-28%20221333.png?raw=true)

* Tambah karyawan baru
  Admin memilih menu 1 (Tambah Karyawan Baru) dan kembali menambahkan data karyawan bernama asepa. Setelah diinput, program menampilkan pesan: “Berhasil tambah asepa!”, menandakan data baru berhasil dimasukkan.
  
![alt text](https://github.com/auliasheva/Minpro-2/blob/main/minpro%202/Cuplikan%20layar%202025-09-28%20221355.png?raw=true)


* Melihat Daftar Karyawan
  admnin memilih menu 2 (Lihat Semua Karyawan). Program menampilkan tabel daftar karyawan lengkap berisi nomor, nama, posisi, shift, dan gaji.
![alt text](https://github.com/auliasheva/Minpro-2/blob/main/minpro%202/Cuplikan%20layar%202025-09-28%20221425.png?raw=true)

* Ubah Data Karyawan
  Admin memilih menu 3 (Ubah Data Karyawan). Daftar karyawan ditampilkan, lalu admin memilih nomor 2 (Iput). Data lama ditampilkan, dan admin mengubah shift menjadi malam serta gaji menjadi Rp 5.000.000. Setelah konfirmasi, sistem menampilkan pesan: “Data berhasil diubah!”.
![alt text](https://github.com/auliasheva/Minpro-2/blob/main/minpro%202/Cuplikan%20layar%202025-09-28%20221441.png?raw=true)

* Hapus Data Karyawan
  Admin memilih menu 4 (Hapus Data Karyawan). Daftar karyawan ditampilkan, lalu admin memilih nomor 3 (Selamet kopling). Program meminta konfirmasi sebelum menghapus. Setelah memilih “y”, muncul pesan: “Data Selamet kopling berhasil dihapus!”.
  Admin juga memilih menu 5 untuk keluar dari program. 
![alt text](https://github.com/auliasheva/Minpro-2/blob/main/minpro%202/Cuplikan%20layar%202025-09-28%20221511.png?raw=true)


# Output User
* Tampilan Awal Login
  Program kembali dijalankan, kali ini login dengan username user. Login berhasil dengan pesan: “Login berhasil! Hai user”. Dengan login ini, hak akses terbatas hanya untuk melihat data karyawan.
![alt text](https://github.com/auliasheva/Minpro-2/blob/main/minpro%202/Cuplikan%20layar%202025-09-28%20221643.png?raw=true)

* Tambah Karyawan Baru
  Pengguna memilih menu 1 (Tambah Karyawan Baru). Karena login sebagai user biasa, program menolak permintaan dengan pesan: “Maaf, hanya admin yang boleh menambah karyawan”. Hal ini menunjukkan adanya pembatasan hak akses.  
![alt text](https://github.com/auliasheva/Minpro-2/blob/main/minpro%202/Cuplikan%20layar%202025-09-28%20221658.png?raw=true)

* Melihat Daftar & Mengubah Karyawan
  Pengguna memilih menu 2 (Lihat Semua Karyawan). Program menampilkan tabel daftar karyawan lengkap berisi nomor, nama, posisi, shift, dan gaji. Setelah itu, pengguna mencoba memilih menu 3 (Ubah Data Karyawan), tetapi karena login bukan sebagai admin, muncul pesan: “Maaf, hanya admin yang boleh ubah data”.
![alt text](https://github.com/auliasheva/Minpro-2/blob/main/minpro%202/Cuplikan%20layar%202025-09-28%20221725.png?raw=true)

* Hapus Data Karyawan & Keluar
  Pengguna login sebagai user lalu memilih menu 4 (Hapus Data Karyawan). Program menolak dengan pesan: “Maaf, hanya admin yang boleh hapus data”. Pengguna juga memilih menu 5 (Keluar). Program menampilkan pesan “Terima kasih telah menggunakan program. Sampai jumpa!” lalu berhenti berjalan.
![alt text](https://github.com/auliasheva/Minpro-2/blob/main/minpro%202/Cuplikan%20layar%202025-09-28%20221737.png?raw=true)

#Sekian dan Terimakasih
