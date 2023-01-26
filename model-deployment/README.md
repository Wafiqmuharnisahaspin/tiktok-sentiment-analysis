# Deployment Model Regresi Linier

## Deskripsi singkat

Repository ini berisi semua file yang dibutuhkan untuk melakukan deployment model Machine Learning Regresi Linier. Adapun model yang digunakan merupakan model untuk memprediksi biaya asuransi berdasarkan:

#

## Sekilas mengenai input model

#

## Folder, file, dan kegunaannya

-   templates/
    -   index.html --> Berisi template website
-   app.py --> Berisi konfigurasi route untuk API
-   model.pkl --> Model Regresi Linier yang sudah di-training
-   request.py --> Berisi percobaan pemanggilan API dengan payload data JSON
-   requirements.txt --> Berisi daftar dependency/package Python yang diperlukan untuk menjalankan API dan model Regresi Linier

#

## Cara menjalankan API pada komputer Anda

### Menjalankan API


### Akses melalui Website

Setelah API berjalan:

1. Anda akan diberikan URL untuk membuka website berupa `localhost:5000/` atau `127.0.0.1:5000/`
1. Buka URL dengan browser, coba masukkan data yang ingin di prediksi
1. Anda akan diberikan estimasi biaya asuransi pada sisi kanan halaman website

### Mencoba Akses API menggunakan payload JSON

Setelah API berjalan:

1. Buka terminal/comand prompt/power shell
1. Jalankan perintah `python request.py`
1. Setelah berhasil dieksekusi, Anda akan diberikan data response berupa JSON juga seperti contoh berikut:\
   `{'Age': 20, 'Insurance Cost': 3146.79, 'Sex': 'Male', 'Smoker': 'No'}`
1. Hasil prediksi biaya asuransi terdapat pada value dari key `'Insurance Cost'` yang dapat Anda manfaatkan untuk aplikasi lain.
