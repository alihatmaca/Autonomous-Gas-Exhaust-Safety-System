#include <iostream>
#include <fstream>
#include <string>
#include <thread>
#include <chrono>

using namespace std;

void fan_kontrol_sistemi() {
    string dosya_adi = "sinyal.txt";
    string sinyal;

    cout << "=== OTONOM TAHLIYE KONTROL MERKEZI (C++) ===" << endl;
    cout << "Python'dan gelen sinyaller bekleniyor..." << endl;

    while (true) {
        ifstream sinyal_dosyasi(dosya_adi);

        if (sinyal_dosyasi.is_open()) {
            getline(sinyal_dosyasi, sinyal);
            sinyal_dosyasi.close();

            if (sinyal == "1") {
                cout << "[!] KRITIK: Gaz Tahliyesi Baslatildi! (Fan: ON)" << endl;
                // Gerçek projede burada röleyi tetikleyecek kod olur.
            } else if (sinyal == "0") {
                cout << "[+] DURUM: Gaz Seviyesi Guvenli. (Fan: OFF)" << endl;
            } else {
                cout << "[?] UYARI: Gecersiz Sinyal Alindi." << endl;
            }
        } else {
            cout << "[x] HATA: Sinyal dosyasi okunamadi!" << endl;
        }

        // Sistemi yormamak için 1 saniye bekle (Polling frequency)
        this_thread::sleep_for(chrono::seconds(1));
    }
}

int main() {
    fan_kontrol_sistemi();
    return 0;
}