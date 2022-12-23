# P2_Komnum_E6

Praktikum 2 Komputasi Numerik : Integrasi Romberg

Salah satu kelemahan dari metode Trapezoidal adalah kita harus menggunakan jumlah interval yang besar untuk memperoleh akurasi yang diharapkan. Buatlah sebuah program komputer untuk menjelaskan bagaimana metode Integrasi Romberg dapat mengatasi kelemahan tersebut.

# Kelompok 6

Nama Kelompok : 
- Muhammad Adib Syambudi (5025211017)
- Ilham Insan Wafi (5025211255)
- Yusna Millaturrosyidah (5025211254)

Penjelasan Source Code Integrasi Romberg :
1. Langkah pertama adalah karena kita membutuhkan persamaan untuk diuji, maka kita membuat fungsi berisi persamaan :

    a1 + a2*x + a3*x**2 + a4*x**3 + a5*x**4 + a6*x**5
2. Membuat variabel inputan bertipe float untuk ketelitian hasil
3. Untuk inputannya dimulai dari a1 hingga a6 dan batas bawah serta atas
4. Untuk integrasi romberg membutuhkan integrasi trapesium, maka dibuat fungsi trap
5. Untuk fungsi trap nya membutuhkan 4 variabel yaitu batas atas, batas bawah, interval dan ketelitian.
6. Untuk perhitungannya menggunakan iterasi dengan rumus sebagai berikut : 

	xi = x0 + i*h
  
      ss = ss + f(xi)
  
7. Dari variabel diatas, digunakan rumus untuk integrasi trapesium :

	I = h/2 * (f(x0) + 2*ss + f(xN))
8. Dari hasil integrasi trapesium tersebut, kita bisa mendapatkan ketelitian lebih lanjut dengan menggunakan romberg
9. Untuk fungsi romberg nya menggunakan library numpy untuk menampung nilai dari tiap perhitungan dalam matriks
10. Untuk perhitungan pertama menggunakan fungsi trapesium, kemudian untuk perhitungan berikutnya menggunakan iterasi.
11. Pada setiap iterasi nilai dari ketelitian ditingkatkan.
12. Selanjutnya kita menghitung iterasi berikutnya. Setelah didapatkan hasil iterasinya maka kita membandingkan hasil iterasi sebelum dan sesudah.
13. Untuk perhitungan proses diatas menggunakan rumus : I[j,k] = (4**(k - 1) * I[j + 1,k -1] - I[j,k - 1]) / (4**(k - 1) - 1)
14. Iterasi berlanjut hingga nilai dari eror sesuai yang kita harapkan yaitu 0.1
15. Setelah itu tampilkan matriks dari tiap perhitungan. Untuk hasil berada pada index baris ketiga kolom sesudah angka 0.

![hasil](https://user-images.githubusercontent.com/91377793/209265591-c59b66ef-1269-4c5d-b297-4ce2532f7966.jpeg)



