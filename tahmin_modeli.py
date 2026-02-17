import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import time
import os

# --- AYARLAR ---
DOSYA_YOLU = "sensor_verileri.csv"
SINYAL_DOSYASI = "sinyal.txt" # C++ kodunun okuyacağı dosya
PENCERE_BOYUTU = 10           # Son kaç saniyeye bakılacak?
METAN_ESIK = 10.0             # %10 Metan tehlike sınırı
AMONYAK_ESIK = 20.0           # 25 ppm Amonyak tehlike sınırı

def analiz_dongusu():
    print("Otonom Gaz Analiz Sistemi Başlatılıyor...")
    
    while True:
        try:
            # 1. VERİ KONTROLÜ
            if not os.path.exists(DOSYA_YOLU):
                print("Veri dosyası bekleniyor...")
                time.sleep(1)
                continue
                
            df = pd.read_csv(DOSYA_YOLU)
            
            if len(df) < PENCERE_BOYUTU:
                print(f"Yeterli veri yok ({len(df)}/{PENCERE_BOYUTU})...")
                time.sleep(1)
                continue

            # 2. KAYAN PENCERE (ROLLING WINDOW) HAZIRLIĞI
            son_veriler = df.tail(PENCERE_BOYUTU)
            X = son_veriler[['No']] # Özellik ismiyle beraber alıyoruz (Warning almamak için)
            
            # 3. MODEL EĞİTİMİ VE SKOR HESAPLAMA
            # Metan Modeli
            y_metan = son_veriler['Metan_Yuzdesi']
            model_metan = LinearRegression().fit(X, y_metan)
            skor_metan = model_metan.score(X, y_metan) * 100
            
            # Amonyak Modeli
            y_amonyak = son_veriler['Amonyak_ppm']
            model_amonyak = LinearRegression().fit(X, y_amonyak)
            skor_amonyak = model_amonyak.score(X, y_amonyak) * 100

            # 4. GELECEK TAHMİNİ (İsimli DataFrame kullanarak Warning'i engelliyoruz)
            son_no = son_veriler['No'].iloc[-1]
            tahmin_verisi = pd.DataFrame([[son_no + 1]], columns=['No'])
            
            tahmin_metan = model_metan.predict(tahmin_verisi)[0]
            tahmin_amonyak = model_amonyak.predict(tahmin_verisi)[0]

            # 5. EKRANI TEMİZLE VE DASHBOARD'U YAZDIR
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"=============================================")
            print(f"   OTONOM GAZ TAKİP VE TAHMİN PANELİ")
            print(f"   Son Ölçüm No: {son_no} | Durum: {'!!! TEHLİKE !!!' if tahmin_metan > METAN_ESIK or tahmin_amonyak > AMONYAK_ESIK else 'NORMAL'}")
            print(f"=============================================")
            print(f" GAZ TİPİ  | TAHMİN (T+1) | GÜVEN SKORU (R2)")
            print(f"-----------|--------------|------------------")
            print(f" METAN     | %{tahmin_metan:6.2f}      | %{skor_metan:6.2f}")
            print(f" AMONYAK   | {tahmin_amonyak:6.2f} ppm  | %{skor_amonyak:6.2f}")
            print(f"=============================================")

            # 6. OTONOM KARAR VE C++ ENTEGRASYONU (Sinyal Yazma)
            with open(SINYAL_DOSYASI, "w") as f:
                if tahmin_metan > METAN_ESIK or tahmin_amonyak > AMONYAK_ESIK:
                    print("\n[!] AKSİYON: Tahliye Sistemi Aktif!")
                    f.write("1") # C++ tarafı "1" görünce fanı açacak
                else:
                    print("\n[+] AKSİYON: Sistem Beklemede.")
                    f.write("0") # C++ tarafı "0" görünce fanı kapatacak

            time.sleep(1) # 1 saniye bekle ve döngüyü kolla

        except PermissionError:
            # Dosya o an simülasyon tarafından yazılıyorsa çakışma olmaması için
            time.sleep(0.1)
            continue
        except KeyboardInterrupt:
            print("\nSistem kullanıcı tarafından durduruldu.")
            break

if __name__ == "__main__":
    analiz_dongusu()