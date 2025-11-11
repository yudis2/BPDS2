# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech

## Business Understanding
Jelaskan latar belakang bisnis dari perushaan tersebut.
Jaya Jaya Institut adalah institusi pendidikan tinggi yang sudah berdiri sejak tahun 2000 dan berhasil meluluskan banyak mahasiswa berprestasi. Namun, saat ini institusi menghadapi tantangan serius berupa tingginya angka dropout (DO) mahasiswa. Masalah ini berpotensi menurunkan reputasi kampus serta mengurangi efektivitas proses pembelajaran.

Untuk mengatasi permasalahan tersebut, dilakukan analisis data akademik dan demografis mahasiswa dengan tujuan memprediksi risiko dropout menggunakan teknik machine learning. Hasil prediksi ini nantinya akan diintegrasikan dalam dashboard interaktif yang membantu pihak institusi memantau dan mengambil langkah preventif terhadap performa mahasiswa.

---
### Permasalahan Bisnis
1. Tingginya **angka mahasiswa yang dropout** tanpa bimbingan pencegahan sejak dini.
2. Minimnya pemahaman mengenai **faktor utama yang memengaruhi dropout**.
3. Belum adanya sistem visualisasi dan model prediktif untuk membantu pengambilan keputusan akademik secara proaktif.

### Cakupan Proyek* Analisis eksploratif (EDA) dan pembersihan data
* Transformasi dan encoding data kategorikal serta numerik
* Penanganan outliers dan ketidakseimbangan data
* Implementasi model machine learning (Random Forest)
* Deployment model dan visualisasi ke dalam dashboard interaktif dengan Streamlit
* Penyusunan insight dan rekomendasi berbasis data
### Persiapan

Sumber data: 
🔗 Link dataset: [Dicoding Student Performance Dataset](https://github.com/dicodingacademy/dicoding_dataset/tree/main/students_performance)
Setup environment:
```
1. Buka terminal atau PowerShell.
```
```
2. Membuat virtual Environment
conda create --name jayamaju-segmentation python=3.9
```
```
3. Aktifkan virtual Environment
conda activate jayamaju-segmentation
```
```
4. Install semua library yang dibutuhkan
pip install -r requirements.txt
````

## Business Dashboard
Jelaskan tentang business dashboard yang telah dibuat. Jika ada, sertakan juga link untuk mengakses dashboard tersebut.
[Dashboard JayaMaju](https://yudisdwi.streamlit.app/)
Student Analisys Dashboard yang digunakan untuk melakukan prediksi kemungkinan karyawan resign (attrition prediction). Berikut penjelasannya:
Struktur Dashboard
```
Sidebar (kiri):
• Gender: Male / Female
• Status Mahasiswa: Dropout, Graduate, Enrolled
• Course/Program Studi: Animation, Tourism, Communication, Journalism, dsb.
```
```
Data Overview
Menampilkan metrik utama secara ringkas:
Average Admission Grade: 126.98
Average Age: 23.3 tahun
Total Students: 4424 mahasiswa
```
## Menjalankan Sistem Machine Learning
Jelaskan cara menjalankan protoype sistem machine learning yang telah dibuat. Selain itu, sertakan juga link untuk mengakses prototype tersebut.
1. Clone Repository
```
git clone https://github.com/yudis2/BPDS2.git
cd BPDS
```
2. Run Dashboard Jaya Maju (Streamlit)
```
streamlit run app.py
```
3. Akses Dashboard Jaya Maju
```
http://localhost:(port)/
```

## Conclusion

• Mengidentifikasi area yang memerlukan perhatian (misal dropout tinggi).

• Memahami komposisi demografis mahasiswa.

• Mengoptimalkan strategi pendidikan berdasarkan data nyata.

### Rekomendasi Action Items

• Implementasikan program pembinaan akademik dan mentoring berdasarkan pola performa mahasiswa.

• Evaluasi kurikulum atau metode pengajaran pada program dengan tingkat kelulusan rendah.

• Gunakan dashboard ini sebagai alat monitoring berkelanjutan bagi dekan dan kepala program studi.
