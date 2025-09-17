# CVL Assignment 01 - Histogram Equalization

## Deskripsi

Penggunaan **histogram equalization** pada gambar yang gelap untuk meningkatkan kontras dan memperjelas detail gambar. 
Histogram equalization adalah teknik yang menyebarkan distribusi intensitas piksel sehingga gambar menjadi lebih terang dan detail lebih terlihat.

## Cara Kerja

1. Program membaca gambar grayscale dari file.
2. Histogram intensitas piksel dihitung.
3. Melakukan Cumulative Distribution Function (CDF) dari histogram.
4. Setiap nilai piksel pada gambar asli dipetakan ke nilai baru berdasarkan CDF.
5. Gambar hasil equalization disimpan dan ditampilkan.

## Perbandingan Gambar

| Sebelum (Original)                | Sesudah (Enhanced)                |
|------------------------------------|-----------------------------------|
| ![Original Image](dark_image.jpg)  | ![Enhanced Image](enhanced_dark_image.jpg) |

- **Gambar Sebelum:** Gambar asli tampak gelap dan detail kurang jelas.
- **Gambar Sesudah:** Setelah histogram equalization, gambar menjadi lebih terang dan detail lebih jelas.

## Cara Menjalankan

1. Pastikan `numpy` dan `opencv-python` sudah terpasang:
   ```
   pip install -r requirements.txt
   ```
2. Jalankan program:
   ```
   python CVL_Assignment01.py
   ```

## Referensi

- [Histogram Equalization - Wikipedia](https://en.wikipedia.org/wiki/Histogram_equalization)
- [OpenCV Documentation](https://docs.opencv.org/)