import pandas as pd
import matplotlib.pyplot as plt

def veriyi_yukle(dosya_yolu):
    return pd.read_csv(dosya_yolu, skip_blank_lines=True).dropna(subset=['Miktar'])

def harcamalari_analiz_et_ve_ciz(df):
    
    df['Kategori'] = df['Kategori'].astype(str).str.strip()
    kategori_ozeti = df.groupby('Kategori')['Miktar'].sum()
    
    plt.figure(figsize=(10, 7))
    kategori_ozeti.plot(kind='pie', autopct='%1.1f%%', startangle=140)
    plt.title('Harcama Dagilimim')
    plt.ylabel('')
    plt.show()

def butce_kontrol(df):
    
    limitler = {
        "Gıda": 1000,
        "Eğitim": 700,
        "Eğlence": 700,
        "Kıyafet": 1000,
        "Ulaşım": 500
    }
    print("\n--- Bütçe Kontrol Raporu ---")
    kategori_toplamlari = df.groupby('Kategori')['Miktar'].sum()
    
    for kat, miktar in kategori_toplamlari.items():
        if kat in limitler:
            limit = limitler[kat]
            if miktar > limit:
                print(f"DİKKAT: {kat} limitini {miktar-limit} TL aştın!")
            else:
                print(f"{kat} bütçe dahilinde. (Kalan: {limit-miktar} TL)")

def yeni_harcama_ekle(dosya_yolu):
    print("\n--- 📝 Yeni Harcama Girişi ---")
    tarih = input("Tarih (YYYY-MM-DD formatında): ")
    kategori = input("Kategori (Gıda, Eğitim, Kıyafet vb.): ")
    miktar = input("Miktar (Harcanan miktare TL şeklinde ): ")
    acıklama = input("Kısa bir açıklama: ")

    yeni_satir = f"\n{tarih},{kategori},{miktar},{acıklama}"

    with open(dosya_yolu, "a", encoding="utf-8") as f:
        f.write(yeni_satir)
    
    print(f" Başarılı: {kategori} kategorisindeki {miktar} TL'lik harcama kaydedildi!")

if __name__ == "__main__":
    dosya = 'harcamalar.csv'
    
    secim = input("Yeni harcama eklemek ister misin? (e/h): ").lower()
    if secim == 'e':
        yeni_harcama_ekle(dosya)
    
    veriler = veriyi_yukle(dosya)
    harcamalari_analiz_et_ve_ciz(veriler)
    butce_kontrol(veriler)