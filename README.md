# P1_Komnum_E5

Anggota Kelompok 5 :
  1. Ahda Filza Ghaffaru, 5025211144
  2. Muhammad Rafi Insan Fillah, 5025211169
  3. Muhammad Rafi Sutrisno, 5025211167

Screenshot Jalannya Program:
![image](https://user-images.githubusercontent.com/99827242/197975542-2fec3a1c-f8b0-4007-bbf2-fea02a0df2f1.png)


Penjelasan Singkat:
  1. Pada tahap pertama, akan di-import plotting library dari python yaitu matplotlib serta numpy dengan      tujuan untuk menampilkan hasil grafik fungsi saat program dijalankan.
  2. Kami membuat 2 fungsi yang dinamakan function dan midPoint. Fungsi function disini bertujuan untuk menghitung hasil akhir ketika nilai x disubstitusikan ke dalam fungsi. Sementara, fungsi midPoint berfungsi untuk menghitung titik tengah (x3).
  3. Kemudian, program akan meminta input x1, x2, dan jumlah iterasi kepada pengguna. Jika x1 lebih dari x2, maka posisi mereka akan ditukar.
  4. Nilai-nilai koordinat x akan disimpan pada xPrint dengan rentang x1 - x2 dengan beda 0.1, kemudian hasil substitusi (f(x)) akan disimpan pada yPrint sebagai koordinat y.
  5. Kemudian menggunakan for lakukan looping sebanyak rentang iterasi yang dimasukkan pada input.
  6. Masukkan nilai x1 dan x2 kedalam fungsi function untuk mendapatkan hasil fungsinya lalu untuk mencari nilai x3 masukkan kedua nilai x1 dan x2 kedalam fungsi midpoint dan masukaan nilai x3 yang didapat ke fungsi function untuk mencari hasil fungsi x3.
  7. Print x1, x2, x3, f(x1), (x2), f(x3) dengan 8 angka dibelakang koma.
  8. Selanjutnya menggunakan percabangan if cek pergantian antara x1, x2,  dan x3. Jika f(x3) positif maka x3 akan mengganti x2 dan jika f(x3) negatif maka x3 akan mengganti x1. 
  9. Setelah looping telah selesai maka print nilai terakhir dari x1 dan x2 yang merupakan rentang jawaban yang diinginkan sesuai jumlah iterasi.
  10. Lalu menunjukkan grafik.

