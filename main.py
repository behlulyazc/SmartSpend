# SmartSpend - Veri Analizi Projesi Başlangıcı
print("SmartSpend: Kişisel Harcama Analizine Hoş Geldiniz!")

def harcama_ozeti(harcamalar):
    toplam = sum(harcamalar)
    print(f"Toplam Harcama: {toplam} TL")

# Test verisi
test_verisi = [100, 250, 75]
harcama_ozeti(test_verisi)