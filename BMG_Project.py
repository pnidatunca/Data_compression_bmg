# ----------------------------------------
# RLE ENCODE (Sıkıştırma) Fonksiyonu
# ----------------------------------------
def encode(text):
    result = ""          # Sıkıştırılmış sonucu tutacak string
    count = 1            # Aynı karakterleri saymak için sayaç

    # Metni baştan sona geziyoruz (2. karakterden itibaren)
    for i in range(1, len(text)):
        if text[i] == text[i-1]:   # Eğer önceki karakterle aynıysa
            count += 1             # Sayacı artır
        else:
            # Farklı karakter görünce önceki grubun sonucunu ekle
            result += str(count) + text[i-1]
            count = 1              # Sayaç sıfırlanır (yeniden başlar)

    # Döngü bittiğinde son karakter grubunu da eklememiz gerekir
    if text:
        result += str(count) + text[-1]

    return result                  # Sıkıştırılmış metni döndür


# ----------------------------------------
# RLE DECODE (Açma) Fonksiyonu
# ----------------------------------------
def decode(encoded):
    result = ""       # Açılmış metin burada birikecek
    number = ""       # Karakter sayısını (ör: "12") geçici tutar

    for ch in encoded:
        if ch.isdigit():         # Eğer karakter bir rakamsa
            number += ch         # Sayının sonuna ekle (örn: "1" → "12")
        else:
            # Rakamsal olmayan karakter gördüğümüzde:
            # number = kaç kere yazılacağı (örn: "5")
            # ch = tekrar edilecek karakter (örn: "A")
            result += int(number) * ch
            number = ""          # Sayacı sıfırla

    return result                # Açılmış metni döndür


# ----------------------------------------
# Sıkıştırma Oranı Hesaplama Fonksiyonu
# ----------------------------------------
def compression_ratio(original, encoded):
    if not original:       # Boş metin durumunda oran 0 kabul edilir
        return 0

    # Sıkıştırma oranı = (1 - yeni_boyut / eski_boyut) * 100
    ratio = (1 - len(encoded) / len(original)) * 100
    return round(ratio, 2)   # Yüzdeyi 2 basamakla yuvarla


# ----------------------------------------
# KULLANICI ETKİLEŞİMİ
# ----------------------------------------
text = input("Metni girin: ")    # Kullanıcıdan metni al

encoded = encode(text)           # Encode işlemini yap
decoded = decode(encoded)        # Encode edilmiş metni geri çevir
ratio = compression_ratio(text, encoded)    # Sıkıştırma oranı hesapla

# Sonuçları ekrana yazdır
print("Sıkıştırılmış:", encoded)
print("Çözülmüş:", decoded)
print("Sıkıştırma Oranı (%):", ratio)
