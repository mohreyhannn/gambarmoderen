import cv2
import numpy as np
from matplotlib import pyplot as plt

# === 1. Baca Gambar Hitam Putih ===
img_gray = cv2.imread('img-2.jpeg', cv2.IMREAD_GRAYSCALE)

if img_gray is None:
    print("❌ Gambar tidak ditemukan!")
    exit()

# === 2. Penyesuaian Intensitas (Brightness & Contrast) ===
alpha = 1.3  # kontras
beta = 20    # kecerahan
img_adj = cv2.convertScaleAbs(img_gray, alpha=alpha, beta=beta)

# === 3. Buat Warna Dasar dengan Color Map ===
# Kita pakai colormap natural seperti OCEAN atau PINK untuk dasar pewarnaan
colorized = cv2.applyColorMap(img_adj, cv2.COLORMAP_OCEAN)

# === 4. Penyesuaian Warna Tambahan (Hue & Saturation) ===
# Konversi ke HSV untuk ubah saturasi dan hue agar tampak alami
hsv = cv2.cvtColor(colorized, cv2.COLOR_BGR2HSV)

h, s, v = cv2.split(hsv)
s = cv2.add(s, 40)   # Tambah saturasi (warna lebih hidup)
v = cv2.add(v, 20)   # Tambah intensitas (lebih terang)

# Gabungkan lagi
hsv = cv2.merge((h, s, v))
final_img = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)

# === 5. Tampilkan Hasil ===
plt.figure(figsize=(10,5))
plt.subplot(1,2,1)
plt.title("Asli (Hitam Putih)")
plt.imshow(img_gray, cmap='gray')
plt.axis('off')

plt.subplot(1,2,2)
plt.title("Setelah Penyesuaian Intensitas & Warna")
plt.imshow(cv2.cvtColor(final_img, cv2.COLOR_BGR2RGB))
plt.axis('off')

plt.show()

# === 6. Simpan Hasil ===
cv2.imwrite('foto_modern.jpg', final_img)
print("✅ Gambar sudah disimpan sebagai 'foto_modern.jpg'")
