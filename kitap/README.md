# Bekçileri Kim Bekleyecek?

**Karar Vericileri Aşan Yapay Zekânın Denetimi ve Hesap Verebilirliği Üzerine Hukuki, Felsefi ve Siyasi Bir İnceleme**

Türk hukukundaki doçentlik eseri / monografi formatında yazılmış kitap taslağı.

## Çıktılar

| Dosya | Açıklama |
|:---|:---|
| `cikti/bekcileri-kim-bekleyecek.pdf` | 16 × 24 cm, Times uyumlu yazı (11 pt metin, 9 pt dipnot), yaklaşık 368 sayfa |
| `cikti/bekcileri-kim-bekleyecek.docx` | Aynı içerik, Word'de düzenlenebilir hâli (içindekiler güncellenmiş) |

## Yapı

| Kaynak dosya | İçerik |
|:---|:---|
| `bolumler/00_on-kisim.md` | Önsöz, Özet, Abstract, Kısaltmalar |
| `bolumler/01_giris.md` | Giriş: problem, araştırma soruları, hipotezler (H1–H5), kapsam, yöntem, kavramlar, plan |
| `bolumler/02a…02b` | Birinci Bölüm: "Bekçiler sorunu"nun soykütüğü (Juvenalis'ten Popper'e, Weber, teknokrasi) |
| `bolumler/03a…03b` | İkinci Bölüm: Olgusal zemin, algokrasi vakaları, bilişsel asimetri, hizalama sorunu |
| `bolumler/04a…04b` | Üçüncü Bölüm: Felsefi perspektif (epistokrasi, Raz, Estlund, Darwall, Kant, sorumluluk boşluğu) |
| `bolumler/05a…05b` | Dördüncü Bölüm: Siyasi perspektif (kodun egemenliği, platform egemenliği, algoritmik vesayet) |
| `bolumler/06a…06b` | Beşinci Bölüm: Anayasal ve idari denetim (AY md. 6, 7, 9, 125, 128, 138; algoritmik idari işlem) |
| `bolumler/07a…07b` | Altıncı Bölüm: Sorumluluk ve hesap sorma (TBK, TCK, idarenin sorumluluğu, elektronik kişilik) |
| `bolumler/08a…08b` | Yedinci Bölüm: Karşılaştırmalı hukuk (AB, Avrupa Konseyi, ABD, BK, Çin, Türkiye) |
| `bolumler/09a…09c` | Sekizinci Bölüm: Çok katmanlı dairesel denetim modeli ve gerekçeli kanun önerisi (41 madde) |
| `bolumler/10_sonuc.md` | Sonuç: 35 tez, hipotezlerin değerlendirilmesi |
| `bolumler/11_kaynakca.md` | Kaynakça (eserler, raporlar, mevzuat, içtihat) |
| `bolumler/12_ek-kavram-sozlugu.md` | Ek: Kavram sözlüğü |

## Derleme

Gereksinimler: `pandoc` (≥ 3), LibreOffice, Python 3 ile `python-docx` ve `pypdf`.

```bash
./derle.sh            # DOCX + PDF üretir, sayfa ve kelime sayısını yazar
./derle.sh --yalniz-docx
```

Dipnotlar Markdown içinde `^[...]` biçiminde satır içi yazılmıştır; numaralandırma derleme sırasında otomatik yapılır.

## Yayına hazırlık öncesi yapılması gerekenler

- **Kaynak doğrulaması:** Tüm künyeler birincil kaynaklardan yeniden kontrol edilmelidir. Klasik eserlere standart pasaj numaralarıyla, çağdaş eserlere eser düzeyinde atıf yapılmıştır; doçentlik eserlerinde beklenen sayfa numaraları, kullanılan baskılara göre eklenmelidir. "Güncel bası" ifadesi geçen Türkçe ders kitaplarında baskı yılı belirtilmelidir.
- **Güncel gelişmeler (Ekim 2026 itibarıyla):** AB Yapay Zekâ Tüzüğü'ndeki "Dijital Omnibüs" ertelemesinin künyesi, TBMM Yapay Zekâ Araştırma Komisyonu raporunun içeriği, Türkiye'deki kanun tekliflerinin durumu, Colorado ve ABD federal düzenlemelerinin son hâli ve Avrupa Konseyi Çerçeve Sözleşmesi'nin imza/onay durumu dipnotlarda doğrulanması gereken noktalar olarak işaretlenmiştir.
- **Yer tutucular:** Kapak ve önsözdeki `[Yazar Adı Soyadı]`, `[Yer]`, `[Tarih]` alanları ile `metadata.yaml` içindeki tarih doldurulmalıdır.
- **Dizin:** Türk akademik yayıncılığında yaygın olan kavram/kişi dizini, sayfa düzeni kesinleştikten sonra eklenmelidir.
