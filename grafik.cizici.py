import pandas as pd
import matplotlib.pyplot as plt

# 1. Veriyi Pandas ile okuyoruz (Artık bunu biliyorsun)
df = pd.read_csv("sensor_verileri.csv")

# 2. Grafik penceresini ve boyutunu hazırlıyoruz
plt.figure(figsize=(10, 6)) # 10 birim genişlik, 6 birim yükseklik

# 3. Çizgileri ekliyoruz
# plot(X ekseni, Y ekseni, etiketi, rengi)
plt.plot(df['No'], df['Metan_Yuzdesi'], label='Metan (%)', color='red', linewidth=2)
plt.plot(df['No'], df['Amonyak_ppm'], label='Amonyak (ppm)', color='blue', linewidth=1.5)

# 4. Grafiği süslüyoruz (Anlaşılır hale getiriyoruz)
plt.title("Otonom Tahliye Sistemi - Gaz Konsantrasyon Takibi")
plt.xlabel("Ölçüm Numarası (Sıra No)")
plt.ylabel("Değer (Yüzde / PPM)")
plt.grid(True) # Arkaya kareli defter çizgileri ekler (okumayı kolaylaştırır)
plt.legend() # Sağ üste hangi renk neyin nesi kutucuğunu koyar

# 5. Ekranda gösteriyoruz
print("Grafik oluşturuluyor, lütfen bekle...")
plt.show()