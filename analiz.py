import pandas as pd

# 1. VERİYİ YÜKLEME
# CSV dosyamızı okuyup 'df' (DataFrame) isimli akıllı tabloya aktarıyoruz
df = pd.read_csv("sensor_verileri.csv")

print("--- VERİ SETİNE GENEL BAKIŞ ---")
# İlk 10 satırı göstererek her şey yolunda mı bakıyoruz
print(df.head(10))

print("\n--- İSTATİSTİKSEL ANALİZ ---")
# Bu komut sana ortalamayı, en düşük/en yüksek değerleri şak diye verir
print(df.describe())

# 2. ÖZEL SORGULAR (Filtreleme)
print("\n--- KRİTİK DURUM ANALİZİ ---")

# Metan gazının %12'den büyük olduğu anları bulalım
yuksek_metan = df[df['Metan_Yuzdesi'] > 12.0]
print(f"Metan gazının %12'yi geçtiği toplam an sayısı: {len(yuksek_metan)}")

# Amonyak gazının en yüksek (zirve) yaptığı anı bulalım
en_yuksek_amonyak = df['Amonyak_ppm'].max()
zirve_an = df[df['Amonyak_ppm'] == en_yuksek_amonyak]

print(f"Zirve Amonyak Değeri: {en_yuksek_amonyak} ppm")
print("Zirve anındaki tüm kayıt:")
print(zirve_an)

# 3. VERİYİ KAYDETME (Opsiyonel)
# Sadece tehlikeli anları içeren ayrı bir Excel/CSV dosyası oluşturmak istersen:
yuksek_metan.to_csv("tehlikeli_metan_kayitlari.csv", index=False)
print("\nTehlikeli kayıtlar ayrı bir dosyaya aktarıldı.")