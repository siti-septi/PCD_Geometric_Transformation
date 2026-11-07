
import imageio.v3 as iio
import numpy as np
import matplotlib.pyplot as plt
from scipy import ndimage
from pathlib import Path

# ==========================================
# 1. MEMBACA GAMBAR ASLI
# ==========================================

folder = Path(__file__).parent

img = iio.imread(folder / "gambar.jpg")

# Memastikan gambar memiliki 3 kanal warna RGB
if img.ndim == 2:
    img = np.stack([img] * 3, axis=-1)
elif img.shape[2] == 4:
    img = img[:, :, :3]

print("Gambar berhasil dibaca!")
print("Ukuran gambar asli:", img.shape)

# ==========================================
# 2. TRANSLATION (PERGESERAN)
# ==========================================

# Menggeser gambar 80 piksel ke kanan
# dan 50 piksel ke bawah
translation = ndimage.shift(
    img,
    shift=(50, 80, 0),
    mode="constant",
    cval=0
)

# ==========================================
# 3. SCALING (PERUBAHAN UKURAN)
# ==========================================

# Memperkecil gambar dengan faktor 0,5
scaling_05 = ndimage.zoom(
    img,
    zoom=(0.5, 0.5, 1),
    order=1
)

# Memperbesar gambar dengan faktor 2
scaling_2 = ndimage.zoom(
    img,
    zoom=(2, 2, 1),
    order=1
)

# ==========================================
# 4. ROTATION (PERPUTARAN)
# ==========================================

rotation_45 = ndimage.rotate(
    img, 45, reshape=True, order=1, mode="constant", cval=0
)

rotation_90 = ndimage.rotate(
    img, 90, reshape=True, order=1, mode="constant", cval=0
)

rotation_180 = ndimage.rotate(
    img, 180, reshape=True, order=1, mode="constant", cval=0
)

# ==========================================
# 5. HORIZONTAL FLIP
# ==========================================

horizontal_flip = np.fliplr(img)

# ==========================================
# 6. VERTICAL FLIP
# ==========================================

vertical_flip = np.flipud(img)

# ==========================================
# 7. MENYIMPAN HASIL TRANSFORMASI
# ==========================================

hasil = {
    "hasil_translation.png": translation,
    "hasil_scaling_05.png": scaling_05,
    "hasil_scaling_2.png": scaling_2,
    "hasil_rotation_45.png": rotation_45,
    "hasil_rotation_90.png": rotation_90,
    "hasil_rotation_180.png": rotation_180,
    "hasil_horizontal_flip.png": horizontal_flip,
    "hasil_vertical_flip.png": vertical_flip
}

for nama_file, gambar in hasil.items():
    gambar_simpan = np.clip(gambar, 0, 255).astype(np.uint8)
    iio.imwrite(folder / nama_file, gambar_simpan)
    print("Berhasil menyimpan:", nama_file)

# ==========================================
# 8. MENAMPILKAN GAMBAR ASLI DAN HASIL
# ==========================================

judul = [
    "Gambar Asli",
    "Translation",
    "Scaling 0.5",
    "Scaling 2",
    "Rotation 45 Derajat",
    "Rotation 90 Derajat",
    "Rotation 180 Derajat",
    "Horizontal Flip",
    "Vertical Flip"
]

daftar_gambar = [
    img,
    translation,
    scaling_05,
    scaling_2,
    rotation_45,
    rotation_90,
    rotation_180,
    horizontal_flip,
    vertical_flip
]

fig, axes = plt.subplots(3, 3, figsize=(14, 12))

fig.subplots_adjust(
    top=0.90,
    hspace=0.35,
    wspace=0.15
)

for ax, gambar, nama in zip(axes.flat, daftar_gambar, judul):
    ax.imshow(np.clip(gambar, 0, 255).astype(np.uint8))
    ax.set_title(nama)
    ax.axis("off")

plt.suptitle(
    "HASIL GEOMETRIC TRANSFORMATION",
    fontsize=16,
    fontweight="bold",
    y=0.98
)

plt.tight_layout(rect=[0, 0, 1, 0.94])

# Menyimpan tampilan gabungan
plt.savefig(
    folder / "hasil_transformasi_lengkap.png",
    dpi=150,
    bbox_inches="tight"
)

print("\nSemua proses transformasi berhasil!")
print("Hasil gabungan tersimpan sebagai hasil_transformasi_lengkap.png")

plt.show()