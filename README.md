# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech

## Business Understanding
Jaya Jaya Institut adalah institusi pendidikan tinggi yang sudah berdiri sejak tahun 2000 dan berhasil meluluskan banyak mahasiswa berprestasi. Namun, saat ini institusi menghadapi tantangan serius berupa tingginya angka dropout (DO) mahasiswa. Masalah ini berpotensi menurunkan reputasi kampus serta mengurangi efektivitas proses pembelajaran.

Untuk mengatasi permasalahan tersebut, dilakukan analisis data akademik dan demografis mahasiswa dengan tujuan memprediksi risiko dropout menggunakan teknik machine learning. Hasil prediksi ini nantinya akan diintegrasikan dalam dashboard interaktif yang membantu pihak institusi memantau dan mengambil langkah preventif terhadap performa mahasiswa.
### Permasalahan Bisnis
1. Tingginya **angka mahasiswa yang dropout** tanpa bimbingan pencegahan sejak dini.
2. Minimnya pemahaman mengenai **faktor utama yang memengaruhi dropout**.
3. Belum adanya sistem visualisasi dan model prediktif untuk membantu pengambilan keputusan akademik secara proaktif.

### Cakupan Proyek
* Analisis eksploratif (EDA) dan pembersihan data
* Transformasi dan encoding data kategorikal serta numerik
* Penanganan outliers dan ketidakseimbangan data
* Implementasi model machine learning (Random Forest)
* Deployment model dan visualisasi ke dalam dashboard interaktif dengan Streamlit
* Penyusunan insight dan rekomendasi berbasis data

### Persiapan

Sumber data: 🔗 Link dataset: [Dicoding Student Performance Dataset](https://github.com/dicodingacademy/dicoding_dataset/tree/main/students_performance)
Setup environment:
1. Buka terminal atau PowerShell.
2. Membuat virtual Environment
```
conda create --name jayamaju-segmentation python=3.9
```
3. Aktifkan virtual Environment
```
conda activate jayamaju-segmentation
```
4. Install semua library yang dibutuhkan
```
pip install -r requirements.txt
````

## Business Dashboard
[Dashboard JayaMaju](https://yudisdwi.streamlit.app/)
Student Analisys Dashboard yang digunakan untuk melakukan prediksi kemungkinan siswa dropout. 

Sidebar (Filter Data):

• Gender: Male / Female

• Status Mahasiswa: Dropout, Graduate, Enrolled

• Course/Program Studi: Animation, Tourism, Communication, Journalism, dsb.

Tab Overview :

• Menampilkan jumlah Rata-rata nilai, rata-rata umur, dan total siswa.

• Menampilkan Grafik Distribusi dari Jenis Kelamin, Status Siswa, Status Perkawinan, Umur.

Tab Academic Perfomance :

• Menampilkan Grafik Nilai Akademik Berdasarkan Gender, Jurusan, Dan Perfoma nilai per semester

Tab Analyze :

• Menampilkan beberapa input untuk analisa machine learning siswa yang terancam dropout.

## Menjalankan Sistem Machine Learning
Untuk Menjalankan sistem rekomendasi dan analisis siswa :
1. Clone Repository
```
git clone https://github.com/yudis2/BPDS2.git
cd BPDS2
```
2. Run Dashboard Jaya Maju (Streamlit)
```
streamlit run app.py
```
3. Akses Dashboard Jaya Maju
```
http://localhost:(port)/
```
3. Klik Tab Analyze
```
masukan setiap value yang tersedia
lalu klik tombol submit
```

## Conclusion
• Mayoritas mahasiswa adalah single dan berusia 18–20, sehingga seluruh kebijakan inti harus menargetkan kelompok ini.

• Memahami komposisi demografis mahasiswa.

• Mengoptimalkan strategi pendidikan berdasarkan data nyata.

### Rekomendasi Action Items
- Program dan layanan diarahkan terutama untuk kelompok Single, karena jumlahnya paling besar dan mewakili hampir seluruh populasi mahasiswa dropout.
- Fokus pada Siswa Usia direntang usia 18-20 tahun Meski masih muda, kelompok ini memiliki jumlah dropout tinggi dan hampir mewakili seluruh populasi.