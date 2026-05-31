# Ders Çalışma Platformu

Bilgisayar Programcılığı 2. sınıf dersleri için hazırlanmış, **statik HTML/CSS/JavaScript** tabanlı final sınavı çalışma sitesi. Her dersin modül bazlı ders notları ve ayrı soru bankası bulunur.

## Özellikler

- **Ana sayfa** (`index.html`): Tüm derslere tek ekrandan erişim
- **Ders notları**: Yan menü, modül/konu navigasyonu, arama kutusu
- **Soru bankası**: Sayfalama (10 soru/sayfa), konu filtresi, karıştırma, sayfa ve genel sonuç kontrolü
- **Karanlık tema**, ders bazlı renk vurguları
- Sunucu gerektirmez; `file://` ile açılabilir (sorular `questions-data.js` üzerinden yüklenir)

## Dersler

| Ders | Ders notları | Soru bankası | Soru sayısı / tip |
|------|--------------|--------------|-------------------|
| Görsel Programlama II | `home.html` | `sorular.html` | 260+ (çoktan seçmeli, doğru/yanlış, boşluk, kod) |
| Gömülü Sistemler | `gomulu/index.html` | `gomulu/sorular.html` | 223 çoktan seçmeli |
| Bilişimde Güncel Teknolojiler | `bilisim/index.html` | `bilisim/sorular.html` | 220 çoktan seçmeli |
| Mesleki İngilizce | `mesleki/index.html` | `mesleki/sorular.html` | 220 çoktan seçmeli |
| İnternet Güvenliği | `guvenlik/index.html` | `guvenlik/sorular.html` | 220 çoktan seçmeli |

> **Not:** Site açılış sayfası `index.html` dosyasıdır. Görsel Programlama II ders notları `home.html` dosyasındadır (dosya adları bilinçli olarak bu şekilde kullanılır).

## Hızlı başlangıç

1. Projeyi bilgisayarınıza kopyalayın veya klonlayın.
2. `index.html` dosyasını tarayıcıda açın (çift tıklama veya sürükle-bırak).
3. İstediğiniz dersten **Ders Notları** veya **Soru Bankası** linkine tıklayın.

İsteğe bağlı yerel sunucu (bazı tarayıcılarda `fetch` için):

```bash
# Python 3
python -m http.server 8080
# Tarayıcı: http://localhost:8080/
```

## Proje yapısı

```
ders/
├── index.html              # Ana sayfa (ders seçimi)
├── home.html               # Görsel Programlama II — ders notları
├── sorular.html            # Görsel Programlama II — soru bankası
├── css/
│   ├── style.css           # Ders notları stilleri
│   └── quiz.css            # Soru bankası stilleri
├── js/
│   ├── app.js              # Not sayfası: arama, menü
│   ├── quiz.js             # Soru bankası mantığı
│   ├── questions-data.js   # GP soru verisi (file:// uyumlu)
│   └── data/questions.json
├── gomulu/                 # Gömülü Sistemler
├── bilisim/                # Bilişimde Güncel Teknolojiler
├── mesleki/                # Mesleki İngilizce
├── guvenlik/               # İnternet Güvenliği
│   ├── index.html
│   ├── sorular.html
│   ├── data/questions.json
│   └── js/questions-data.js
├── docs/                   # Kaynak PDF/PPTX metin çıktıları
├── generate_questions.py   # GP soru üretici
├── generate_gomulu_questions.py
├── generate_bilisim_questions.py
├── generate_mesleki_questions.py
├── generate_guvenlik_questions.py
└── extract_docs.py         # Doküman metin çıkarma
```

Her ders klasöründe `index.html` (notlar), `sorular.html` (quiz), `data/questions.json` ve `js/questions-data.js` bulunur.

## Soru bankası kullanımı

- **Konu filtresi:** Yalnızca seçilen modül/konudaki soruları gösterir.
- **Soruları karıştır:** Sıra ve şık sırasını değiştirir.
- **Bu Sayfayı Kontrol Et:** Görünen 10 sorunun cevaplarını işaretler.
- **Özet Sonuç:** Tüm yüklü sorular için doğru/yanlış özeti.
- **Sıfırla:** Seçimleri ve sonuç panelini temizler.

Çoktan seçmeli-only derslerde (`QUIZ_TEST_ONLY`) yan menüde soru tipi sekmesi yoktur; tüm sorular A–D şıklı test formatındadır.

## Soru verisini yeniden üretme

Soru bankalarını güncellemek için Python 3 gerekir:

```bash
python generate_questions.py          # Görsel Programlama II
python generate_gomulu_questions.py
python generate_bilisim_questions.py
python generate_mesleki_questions.py
python generate_guvenlik_questions.py
```

Her script ilgili dersin `data/questions.json` ve `js/questions-data.js` dosyalarını yazar.

## Teknoloji

- HTML5, CSS3 (özel değişkenler, grid/flex)
- Vanilla JavaScript (framework yok)
- JSON soru verisi; tarayıcıda `window.QUIZ_DATA` olarak gömülü yükleme

## Geliştirme notları

- Yeni ders eklerken: klasör + `index.html` + `sorular.html` + `questions-data.js` + `quiz.js` bağlantıları; ana sayfaya kart ekleyin.
- Ana sayfaya dönüş linkleri: kök dizinden `index.html`, alt klasörlerden `../index.html`.
- Görsel Programlama notları: `home.html`; ana sayfa: `index.html`.

## Lisans

Kişisel eğitim ve sınav hazırlığı amaçlıdır. Ders materyalleri ilgili üniversite ve öğretim üyelerinin müfredatına dayanır.
