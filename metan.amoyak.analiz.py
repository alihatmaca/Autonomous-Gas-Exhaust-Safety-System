import time
import random
import csv
from datetime import datetime

dosya_adi = "sensor_verileri.csv"

# 1. BAŞLANGIÇ DEĞERLERİ (Döngü Dışında Bir Kez)
# Sistem her seferinde farklı bir noktadan başlasın
metan_degeri = random.uniform(2.0, 8.0) 
amonyak_degeri = random.uniform(5.0, 15.0)
sayac = 1 

# Dosyayı baştan oluşturup başlıkları yazıyoruz
with open(dosya_adi, mode='w', newline='') as dosya:
    yazici = csv.writer(dosya)
    yazici.writerow(["No", "Zaman", "Metan_Yuzdesi", "Amonyak_ppm"])

print("Sınırsız 'Akıllı' Simülasyon Başladı... (Geleceği görmek için veri toplanıyor)\n")

try:
    while True:
        simdi = datetime.now().strftime("%H:%M:%S")
        
        # 2. TREND OLUŞTURMA: Bir önceki değerin üzerine küçük bir değişim ekliyoruz
        # Sınır yok, gaz %100'e de gidebilir, %0'a da yaklaşabilir
        metan_degeri += random.uniform(-0.5, 0.5) 
        amonyak_degeri += random.uniform(-0.5, 0.5)

        # Sadece fiziksel koruma: Gaz eksiye düşemez
        metan_degeri = max(0, metan_degeri)
        amonyak_degeri = max(0, amonyak_degeri)
        
        yaz_metan = round(metan_degeri, 2)
        yaz_amonyak = round(amonyak_degeri, 2)
        
        print(f"{sayac} [{simdi}] Metan: %{yaz_metan} | Amonyak: {yaz_amonyak} ppm")
        
        # Veriyi CSV'ye ekliyoruz
        with open(dosya_adi, mode='a', newline='') as dosya:
            yazici = csv.writer(dosya)
            yazici.writerow([sayac, simdi, yaz_metan, yaz_amonyak])
        
        sayac += 1
        time.sleep(1) # Gerçek zamanlı hissi için 1 saniye bekle

except KeyboardInterrupt:
    print("\nSimülasyon durduruldu. Şimdi tahmin kodunu çalıştırabilirsin!")