# 📊 SmartSpend: Python ile Kişisel Harcama Analiz Sistemi

Bu proje, bir veri analisti adayı olarak Python, Pandas ve Matplotlib kütüphanelerini kullanarak ham veriden anlamlı sonuçlar çıkarma sürecimi yansıtmaktadır. Proje, kişisel harcama verilerini temizler, görselleştirir ve önceden tanımlanmış bütçe limitlerine göre kullanıcıyı uyarır.

## 🚀 Öne Çıkan Özellikler

* **Veri Temizleme (Data Cleaning):** CSV dosyasındaki boş satırlar ve hatalı girişler Pandas filtreleri ile otomatik olarak temizlenir.
* **Kategori Bazlı Analiz:** Harcamalar; Gıda, Eğitim, Eğlence gibi kategorilere göre gruplandırılarak toplam maliyetleri hesaplanır.
* **Görselleştirme:** Matplotlib kütüphanesi kullanılarak harcama dağılımı profesyonel bir pasta grafiği (Pie Chart) ile sunulur.
* **Akıllı Bütçe Kontrolü:** Belirlenen bütçe limitleri aşıldığında terminal üzerinden kullanıcıya uyarı mesajları gönderilir.

## 🛠️ Kullanılan Teknolojiler

* **Dil:** Python 3.13.2
* **Kütüphaneler:** * `Pandas` (Veri işleme ve analizi)
  * `Matplotlib` (Veri görselleştirme)
* **Araçlar:** VS Code, Git & GitHub

## 📂 Proje Yapısı

* `main.py`: Veri okuma, temizleme ve analiz fonksiyonlarını içeren ana kod dosyası.
* `harcamalar.csv`: Analiz edilen ham veri seti.
* `README.md`: Proje dokümantasyonu.

## 📝 Karşılaşılan Zorluklar ve Çözümler

* **Kirli Veri:** Veri setindeki boş satırların analizi bozması `dropna()` ve `strip()` yöntemleri kullanılarak engellendi.

---
*Bu proje Erciyes Üniversitesi Bilgisayar Mühendisliği 3. sınıf öğrencisi **Behlül Yazıcı** tarafından geliştirilmiştir.*
