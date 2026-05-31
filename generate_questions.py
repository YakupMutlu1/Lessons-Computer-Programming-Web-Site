# -*- coding: utf-8 -*-
"""Final sınavı soru bankası üretici — her tipten en az 50 soru."""
import json
import random
from pathlib import Path

random.seed(42)

test = []
dogru = []
bosluk = []
kod = []

def add_test(q, opts, correct_idx, topic="genel"):
    test.append({"topic": topic, "question": q, "options": opts, "correct": correct_idx})

def add_dogru(statement, is_true, topic="genel"):
    dogru.append({"topic": topic, "statement": statement, "correct": is_true})

def add_bosluk(q, answer, topic="genel", alt=None):
    bosluk.append({"topic": topic, "question": q, "answer": answer, "alternatives": alt or []})

def add_kod(direction, prompt, options, correct_idx, topic="javascript"):
    kod.append({"topic": topic, "direction": direction, "prompt": prompt, "options": options, "correct": correct_idx})

# ========== TEST SORULARI (50+) ==========
test_items = [
    ("JavaScript hangi şirket tarafından ilk olarak geliştirilmiştir?", ["Microsoft", "Netscape", "Google", "Apple"], 1, "javascript"),
    ("ECMAScript standartlaştırmasını hangi kuruluş yapmıştır?", ["IEEE", "ECMA", "W3C", "ISO"], 1, "javascript"),
    ("typeof 42 ifadesinin sonucu nedir?", ['"integer"', '"number"', '"float"', '"numeric"'], 1, "javascript"),
    ('"2" + "3" ifadesinin sonucu nedir?', ['5', '"23"', 'NaN', 'Error'], 1, "javascript"),
    ("camelCase örneği hangisidir?", ["first_name", "FirstName", "firstName", "FIRSTNAME"], 2, "javascript"),
    ("Dizi indeksleri hangi sayıdan başlar?", ["1", "0", "-1", "İsteğe bağlı"], 1, "javascript"),
    (".includes() metodu ne döndürür?", ["İndeks numarası", "boolean", "string", "undefined"], 1, "javascript"),
    ("Math.floor(6.9) değeri nedir?", ["7", "6", "6.9", "0"], 1, "javascript"),
    ("while döngüsünde sonsuz döngüyü önlemek için ne yapılmalıdır?", ["break kullanılmaz", "Koşul değişkeni güncellenmeli", "return zorunlu", "alert eklenmeli"], 1, "javascript"),
    ("=== operatörü neyi kontrol eder?", ["Sadece değer", "Sadece tip", "Değer ve tip", "Referans"], 2, "javascript"),
    ("Harici JavaScript dosyası nereye bağlanmalıdır (en iyi uygulama)?", ["<head> başında", "<body> sonunda", "Her yerde aynı", "CSS içinde"], 1, "dom"),
    ("DOM'da document.body neyi temsil eder?", ["<html>", "<head>", "<body> elementi", "Tüm belge"], 2, "dom"),
    ("querySelector() ne döndürür?", ["Tüm eşleşenler dizisi", "İlk eşleşen element", "Sadece ID", "NodeList"], 1, "dom"),
    ("getElementById() ile getElementsByClassName() arasındaki fark?", ["İkisi de dizi döner", "Id tek element, class dizi benzeri", "Class daha hızlı", "Fark yok"], 1, "dom"),
    ("addEventListener'da handleClick() yerine handleClick yazılmasının nedeni?", ["Sözdizim hatası", "Fonksiyonu hemen çağırmamak", "Performans", "ES6 kuralı"], 1, "dom"),
    ("this anahtar kelimesi event handler içinde neye referans verir?", ["window", "document", "Olayı tetikleyen element", "Fonksiyon"], 2, "dom"),
    ("switch ifadesinde break unutulursa ne olur?", ["Hata verir", "Sonraki case'lere düşer (fall-through)", "Döngü başlar", "return otomatik"], 1, "dom"),
    ("jQuery seçici kısa yazımı nedir?", ["jQuery()", "jq()", "$()", "select()"], 2, "jquery"),
    ("jQuery'de stil için tercih edilen yöntem hangisidir?", [".css() ile inline", ".addClass() ile CSS sınıfı", "style attribute", "document.write"], 1, "jquery"),
    (".attr('href', 'url') iki parametreyle ne yapar?", ["Değer okur", "Değer ayarlar", "Element siler", "Class ekler"], 1, "jquery"),
    ("Git Bash'te üst dizine çıkmak için hangi komut?", ["cd up", "cd ..", "cd /", "pwd .."], 1, "terminal"),
    ("Boş dosya oluşturmak için hangi komut?", ["mkdir", "touch", "create", "new"], 1, "terminal"),
    ("Express'te middleware konumu nerede olmalıdır?", ["Rotalardan sonra", "İstek ile rota arasında", "Sadece hata sonrası", "package.json'da"], 1, "express"),
    ("body-parser urlencoded extended:true ne sağlar?", ["JSON parse", "Karmaşık form yapıları", "Dosya yükleme", "Session"], 1, "express"),
    ("EJS'de <%= değişken %> ne yapar?", ["Kod çalıştırır", "Kaçışlı çıktı yazar", "Ham HTML yazar", "Yorum"], 1, "express"),
    ("res.render() ile res.send() farkı?", ["Aynı", "render şablon+veri, send düz metin/HTML", "send daha hızlı", "render sadece JSON"], 1, "express"),
    ("EJS views klasörü neden zorunludur?", ["Express kuralı", "Şablonların varsayılan konumu", "npm gereği", "Güvenlik"], 1, "express"),
    ("locals.meyveler kontrolü ne için kullanılır?", ["Hız", "Tanımsız değişken hatasını önlemek", "Şifreleme", "Cache"], 1, "express"),
    ("Veri kalıcılığı için ne kullanılır?", ["Değişkenler", "Veritabanı", "alert", "console.log"], 1, "sql"),
    ("SQL'de PRIMARY KEY ne işe yarar?", ["Foreign referans", "Satırı benzersiz tanımlar", "Sıralama", "JOIN"], 1, "sql"),
    ("FOREIGN KEY neye referans verir?", ["Aynı tablo", "Başka tablodaki PRIMARY KEY", "Index", "View"], 1, "sql"),
    ("INNER JOIN ne döndürür?", ["Tüm sol kayıtlar", "Her iki tabloda eşleşenler", "Sadece sağ", "NULL'lar dahil tümü"], 1, "sql"),
    ("SELECT * FROM urunler WHERE fiyat > 50 ne yapar?", ["50 kayıt siler", "fiyat>50 satırları getirir", "Tablo oluşturur", "Günceller"], 1, "sql"),
    ("NoSQL verileri genelde nerede saklanır?", ["Tablolar", "JSON benzeri belgeler", "CSV only", "XML"], 1, "sql"),
    ("PostgreSQL için Node paketi hangisidir?", ["postgres-node", "pg", "sql-client", "db-pg"], 1, "postgres"),
    ("db.query() ne döndürür?", ["String", "sonuc.rows gibi sonuç nesnesi", "Boolean", "Connection"], 1, "postgres"),
    ("Şifre saklamada endüstri standardı hangisidir?", ["Düz metin", "AES şifreleme", "bcrypt hash", "Base64"], 2, "guvenlik"),
    ("Hash fonksiyonu geri çevrilebilir mi?", ["Evet, anahtarla", "Hayır, pratikte geri çevrilemez", "Evet, her zaman", "Sadece MD5'te"], 1, "guvenlik"),
    ("Çerezlerde genelde ne saklanır?", ["Şifre düz metin", "Session ID", "Tüm kullanıcı verisi", "HTML"], 1, "auth"),
    ("Passport kurulum sırasında ilk ne eklenir?", ["passport.initialize", "express-session", "Rotalar", "bcrypt"], 1, "auth"),
    ("serializeUser ne kaydeder?", ["Tüm kullanıcı objesi", "Genelde kullanıcı ID", "Şifre hash", "Email"], 1, "auth"),
    ("req.isAuthenticated() ne kontrol eder?", ["Veritabanı bağlantısı", "Kullanıcı giriş yapmış mı", "CSRF", "Cookie boyutu"], 1, "auth"),
    ("dotenv.config() ne yapar?", [".env siler", ".env'i process.env'e yükler", "Git ignore ekler", "Port açar"], 1, "auth"),
    (".env dosyası Git'e neden eklenmemeli?", ["Çok büyük", "Sırlar açığa çıkar", "Çalışmaz", "Lisans"], 1, "auth"),
    ("API kısaltması ne anlama gelir?", ["Application Program Interface", "Advanced Protocol Integration", "Automated Page Index", "Active Port ID"], 0, "api"),
    ("REST API hangi protokolü kullanır?", ["FTP", "HTTP", "SMTP", "WebSocket only"], 1, "api"),
    ("GET isteği genelde ne için kullanılır?", ["Veri silme", "Veri alma", "Dosya yükleme", "Oturum kapatma"], 1, "api"),
    ("Query parametresi URL'de nasıl başlar?", ["#", "?", "&", "/"], 1, "api"),
    ("JSON.stringify() ne yapar?", ["JSON'ı nesneye çevirir", "Nesneyi JSON string yapar", "Dosya okur", "API çağırır"], 1, "api"),
    ("Axios'un avantajı nedir?", ["Sadece tarayıcı", "HTTP isteklerini kolaylaştırır", "Veritabanı bağlar", "EJS render eder"], 1, "api"),
    ("CORS sorununu sunucu tarafı istek neden çözer?", ["Daha hızlı", "API anahtarı tarayıcıda açılmaz", "HTML gerekmez", "POST yasak değil"], 1, "api"),
    ("DELETE /api/users/123 ne yapar?", ["123 kullanıcıyı getirir", "123 ID'li kullanıcıyı siler", "123 kayıt ekler", "Liste sayfası"], 1, "api"),
    ("typeof '42' sonucu nedir?", ['"number"', '"string"', '"boolean"', "undefined"], 1, "javascript"),
    ("var ile let arasındaki temel fark (ES6)?", ["let fonksiyon kapsamlı", "let blok kapsamlı", "var blok kapsamlı", "Fark yok"], 1, "javascript"),
    (".slice(0, 3) 'Merhaba' için ne döner?", ["Mer", "Merh", "M", "haba"], 1, "javascript"),
    ("return kullanılmayan fonksiyon ne döner?", ["null", "0", "undefined", "false"], 2, "javascript"),
    ("Math.random() hangi aralıkta değer üretir?", ["1 ile 10", "0 ile 1 (1 dahil değil)", "-1 ile 1", "0 ile 100"], 1, "javascript"),
    ("Zar (1-6) için doğru formül hangisidir?", ["Math.random()*6", "Math.floor(Math.random()*6)+1", "Math.ceil(Math.random()*5)", "Math.random()+1"], 1, "javascript"),
    ("&& operatörü ne zaman true döner?", ["Bir koşul true", "Tüm koşullar true", "Hiçbiri false değilse yeter", "Her zaman"], 1, "javascript"),
    ("for döngüsünde i++ ne yapar?", ["i'yi 2 artırır", "i'yi 1 artırır", "Döngüyü bitirir", "i'yi sıfırlar"], 1, "javascript"),
    ("document.addEventListener('keypress', fn) ne dinler?", ["Sadece mouse", "Klavye tuş basımı", "Form submit", "Sayfa kapanması"], 1, "dom"),
    ("event.key ne verir?", ["Tuş kodu sayı", "Basılan karakter", "Shift durumu", "Element id"], 1, "dom"),
    ("new Audio('ses.mp3').play() ne yapar?", ["Görsel gösterir", "Ses çalar", "Video durdurur", "Fetch yapar"], 1, "dom"),
    ("express.static('public') ne sunar?", ["JSON API", "public klasöründeki statik dosyalar", "EJS şablonları", "Session"], 1, "express"),
    ("INSERT INTO tablo VALUES (...) ne yapar?", ["Okur", "Kayıt ekler", "Siler", "Tablo oluşturur"], 1, "sql"),
    ("CREATE TABLE ne yapar?", ["Veri okur", "Yeni tablo tanımlar", "JOIN yapar", "Index siler"], 1, "sql"),
    ("bcrypt.compareSync ne yapar?", ["Şifreyi çözer", "Girilen şifre ile hash'i karşılaştırır", "Hash üretmez", "Cookie yazar"], 1, "guvenlik"),
    ("MD5 hash güvenli mi (şifre için)?", ["Evet, en güvenli", "Hayır, çok hızlı kırılır", "Sadece PostgreSQL'de", "Evet, bcrypt'ten iyi"], 1, "guvenlik"),
    ("passport-local stratejisi ne doğrular?", ["OAuth token", "Kullanıcı adı/şifre", "API key", "JWT only"], 1, "auth"),
    ("PATCH metodu REST'te ne için?", ["Tam güncelleme", "Kısmi güncelleme", "Silme", "Oluşturma"], 1, "api"),
]

for q, opts, c, t in test_items:
    add_test(q, opts, c, t)

# Ek test soruları şablonla genişlet
extra_tests = [
    ("Hangi veri tipi true/false değer alır?", ["Number", "String", "Boolean", "Array"], 2),
    ("prompt() dönüş tipi genelde nedir?", ["number", "string veya null", "boolean", "object"], 1),
    ("alert() ne yapar?", ["Konsola yazar", "Açılır pencere gösterir", "Dosya okur", "POST gönderir"], 1),
    ("Rezerve kelime olarak hangisi kullanılamaz?", ["myVar", "userName", "function", "data1"], 2),
    ("HTMLCollection ile NodeList farkı sınavda?", ["Aynı", "Canlı/yapı farkları olabilir", "Sadece jQuery", "IE only"], 1),
    ("innerHTML ne ayarlar?", ["CSS class", "Elementin HTML içeriği", "src", "href"], 1),
    ("preventDefault ne yapar?", ["Varsayılan tarayıcı davranışını engeller", "Element siler", "Ajax başlatır", "Cookie yazar"], 0),
    ("fadeOut() jQuery'de ne yapar?", ["Anında gizler", "Opaklık azaltarak gizler", "Siler", "Klonlar"], 1),
    ("npm init -y ne oluşturur?", ["node_modules", "package.json", ".env", "index.html"], 1),
    ("nodemon ne işe yarar?", ["Paket yükler", "Dosya değişince sunucuyu yeniden başlatır", "Test çalıştırır", "Git commit"], 1),
]
topics_cycle = ["javascript", "dom", "jquery", "express", "sql", "postgres", "api", "auth"]
for i, (q, opts, c) in enumerate(extra_tests):
    add_test(q, opts, c, topics_cycle[i % len(topics_cycle)])

# 50'ye tamamlamak için numaralı varyantlar
templates = [
    ("{n}. modülde öğrenilen {konu} ile ilgili hangisi doğrudur?", ["Yanlış tanım A", "Doğru kavram", "Alakasız C", "Hatalı D"], 1),
]
konular = [
    ("JavaScript", "yorumlanan bir dildir"),
    ("DOM", "HTML'i nesne ağacına dönüştürür"),
    ("jQuery", "DOM manipülasyonunu kısaltır"),
    ("Express", "Node.js web framework'üdür"),
    ("EJS", "şablon motorudur"),
    ("SQL", "ilişkisel veritabanı dilidir"),
    ("PostgreSQL", "açık kaynak RDBMS'tir"),
    ("bcrypt", "şifre hashlemek için kullanılır"),
    ("Passport", "kimlik doğrulama middleware'idir"),
    ("REST", "HTTP metodlarıyla kaynak yönetir"),
]
idx = 0
while len(test) < 55:
    k, dogru_metin = konular[idx % len(konular)]
    n = (idx // len(konular)) + 1
    add_test(
        f"{k} hakkında hangi ifade doğrudur?",
        [f"{k} tarayıcıda çalışmaz", dogru_metin, f"{k} sadece CSS içindir", f"{k} SQL'in yerine geçer"],
        1,
        k.lower()[:6] if k != "PostgreSQL" else "postgres",
    )
    idx += 1

# ========== DOĞRU / YANLIŞ (50+) ==========
dogru_items = [
    ("JavaScript ve Java aynı programlama dilidir.", False, "javascript"),
    ("typeof operatörü bir string döndürür.", True, "javascript"),
    ('"5" + 3 sonucu "53"tür.', True, "javascript"),
    ("Dizi indeksleri 0'dan başlar.", True, "javascript"),
    (".includes() büyük/küçük harfe duyarlıdır.", True, "javascript"),
    ("=== operatörü tip dönüşümü yapmaz.", True, "javascript"),
    ("var ile tanımlanan değişken blok kapsamlıdır (ES6 öncesi davranış farklı).", True, "javascript"),
    ("Fonksiyon adından sonra () çağrı anlamına gelir.", True, "javascript"),
    ("Math.random() asla tam 1.0 döndürmez.", True, "javascript"),
    ("while döngüsünde koşul false olunca döngü biter.", True, "javascript"),
    ("Harici script etiketi body sonuna konulması önerilir.", True, "dom"),
    ("Satır içi onclick JavaScript önerilen yöntemdir.", False, "dom"),
    ("document.querySelector('.btn') ilk eşleşeni döndürür.", True, "dom"),
    ("getElementsByTagName dizi benzeri koleksiyon döndürür.", True, "dom"),
    ("addEventListener üçüncü parametre capture phase içindir (opsiyonel).", True, "dom"),
    ("Event listener'a handleClick() verilirse fonksiyon hemen çalışır.", True, "dom"),
    ("innerHTML XSS riski taşıyabilir, dikkatli kullanılmalı.", True, "dom"),
    ("switch'te default case zorunludur.", False, "dom"),
    ("this event handler içinde elemente referans verebilir.", True, "dom"),
    ("jQuery bir programlama dilidir.", False, "jquery"),
    ("$() jQuery seçicisinin kısa yazımıdır.", True, "jquery"),
    (".addClass() ile stil dosyasına dokunmadan görünüm değiştirilebilir.", True, "jquery"),
    (".append() elementin içine sona ekler.", True, "jquery"),
    ("Git Bash Windows'ta Unix benzeri komutlar sağlar.", True, "terminal"),
    ("rm komutu klasörleri varsayılan olarak recursive siler.", False, "terminal"),
    ("Middleware Express'te istekten sonra çalışır.", False, "express"),
    ("req.body body-parser olmadan form POST'ta dolu gelir.", False, "express"),
    ("EJS dosyaları .ejs uzantılıdır.", True, "express"),
    ("<% %> etiketi EJS'de çıktı üretir.", False, "express"),
    ("<%= %> HTML kaçış karakteri uygular.", True, "express"),
    ("<%- %> ham HTML çıktısı verir.", True, "express"),
    ("locals nesnesi EJS'de otomatik kullanılabilir.", True, "express"),
    ("Sunucu yeniden başlayınca bellekteki değişkenler kalır.", False, "sql"),
    ("SQL tablolarında şema önceden tanımlanır.", True, "sql"),
    ("NoSQL her zaman SQL'den daha hızlıdır.", False, "sql"),
    ("PRIMARY KEY bir satırı benzersiz tanımlar.", True, "sql"),
    ("FOREIGN KEY herhangi bir metin olabilir.", False, "sql"),
    ("INNER JOIN eşleşmeyen kayıtları da getirir.", False, "sql"),
    ("WHERE SELECT ile birlikte kullanılabilir.", True, "sql"),
    ("pg paketi PostgreSQL ile Node bağlantısı kurar.", True, "postgres"),
    ("await db.connect() asenkron bağlantı için kullanılır.", True, "postgres"),
    ("Şifreleri düz metin saklamak kabul edilebilir.", False, "guvenlik"),
    ("Hash fonksiyonu şifreleme anahtarı gerektirmez.", True, "guvenlik"),
    ("bcrypt yavaş tasarlanmıştır, brute-force'u zorlaştırır.", True, "guvenlik"),
    ("Çerezler tarayıcıda saklanır.", True, "auth"),
    ("Session verisi tamamen çerezde saklanmalıdır (best practice: sunucu session, çerezde id).", False, "auth"),
    ("passport.initialize() session'dan önce gelmelidir.", False, "auth"),
    ("serializeUser tüm şifreyi session'a yazar.", False, "auth"),
    (".env dosyası GitHub'a push edilmelidir.", False, "auth"),
    ("process.env.SESSION_SECRET ortam değişkenine erişir.", True, "auth"),
    ("API iki yazılım arasında iletişim köprüsüdür.", True, "api"),
    ("REST sadece XML kullanır.", False, "api"),
    ("JSON JavaScript nesnelerine benzer sözdizimine sahiptir.", True, "api"),
    ("JSON.parse() string'i nesneye çevirir.", True, "api"),
    ("Axios sadece Node'da çalışır.", False, "api"),
    ("Query parametreleri ? ile başlar.", True, "api"),
    ("Path parametresi URL yolunun parçasıdır.", True, "api"),
    ("GET isteği gövde (body) ile veri taşımak için idealdir.", False, "api"),
    ("POST form verilerini genelde body'de taşır.", True, "api"),
    ("Rate limit API kötüye kullanımını sınırlayabilir.", True, "api"),
]

for stmt, val, topic in dogru_items:
    add_dogru(stmt, val, topic)

while len(dogru) < 55:
    i = len(dogru)
    add_dogru(f"Final konusu {i}: Express rota tanımı app.get('/') ile yapılır.", True, "express")

# ========== BOŞLUK DOLDURMA (50+) ==========
bosluk_items = [
    ("JavaScript'in yaratıcısı Brendan ___'dır.", "Eich", "javascript"),
    ("Standart adı ___ Script'tir (kısaltma ES).", "ECMA", "javascript"),
    ("Konsolu açmak için F12 veya Ctrl+Shift+___ kullanılır.", "I", "javascript"),
    ("String birleştirmede + operatörü iki ___ birleştirir.", "string", "javascript"),
    ("Değişken tipini öğrenmek için ___() kullanılır.", "typeof", "javascript"),
    ("Kullanıcıdan girdi almak için ___() fonksiyonu kullanılır.", "prompt", "javascript"),
    ("Anlamlı değişken adları için ___Case kullanılır.", "camel", "javascript"),
    ("'Merhaba'.___ özelliği karakter sayısını verir (8).", "length", "javascript"),
    ("'Abubakar'.slice(0,3) sonucu ___'dır.", "Abu", "javascript"),
    ("1-6 arası zar: Math.floor(Math.random() * 6) + ___", "1", "javascript"),
    ("Katı eşitlik operatörü ___'dir.", "===", "javascript"),
    ("Dizide eleman var mı kontrolü: dizi.___('deger')", "includes", "javascript"),
    ("Tekrarlayan işler için ___ döngüsü kullanılır.", "while", "javascript"),
    ("Fonksiyondan değer döndürmek için ___ anahtar kelimesi kullanılır.", "return", "javascript"),
    ("Aşağı yuvarlama: Math.___()", "floor", "javascript"),
    ("Harici JS dosyası ___ etiketi ile bağlanır.", "script", "javascript"),
    ("DOM'da belge kökü ___ nesnesidir.", "document", "javascript"),
    ("İlk eşleşen element: document.___('h1')", "querySelector", "dom"),
    ("Benzersiz id ile seçim: document.___('baslik')", "getElementById", "dom"),
    ("HTML içeriği değiştirmek: element.___ = 'yeni'", "innerHTML", "dom"),
    ("Tıklama dinlemek: element.addEventListener('___', fn)", "click", "dom"),
    ("Event handler'da tıklanan element: ___", "this", "dom"),
    ("Çoklu case için ___ ifadesi kullanılır.", "switch", "dom"),
    ("Ses çalmak: new ___('yol.mp3').play()", "Audio", "dom"),
    ("Klavye karakteri: event.___", "key", "dom"),
    ("jQuery kısa seçici: ___('h1')", "$", "jquery"),
    ("Sınıf eklemek: $('h1').___('aktif')", "addClass", "jquery"),
    ("href değiştirmek: $('a').___('href', 'url')", "attr", "jquery"),
    ("Element sonuna eklemek: $('ul').___('<li>')", "append", "jquery"),
    ("Yavaşça gizlemek: $('div').___()", "fadeOut", "jquery"),
    ("Dizin listelemek: ___", "ls", "terminal"),
    ("Klasör oluşturmak: ___ klasorAdi", "mkdir", "terminal"),
    ("Dosya silmek: ___ dosya.txt", "rm", "terminal"),
    ("Üst dizin: cd ___", "..", "terminal"),
    ("Express'te ara katman: ___", "middleware", "express"),
    ("Form verisi parse: bodyParser.___()", "urlencoded", "express"),
    ("Form POST verisi: req.___", "body", "express"),
    ("Şablon render: res.___('index', {data})", "render", "express"),
    ("EJS değişken yazdırma: <%= ___ %>", "degisken", "express"),
    ("EJS kod bloğu: <% ___ %>", "kod", "express"),
    ("EJS güvenli kontrol: locals.___", "degisken", "express"),
    ("Kalıcı veri için ___ kullanılır.", "veritabani", "sql", ["veritabanı", "database"]),
    ("Tablo oluşturma: ___ TABLE", "CREATE", "sql"),
    ("Veri ekleme: ___ INTO", "INSERT", "sql"),
    ("Veri okuma: ___ * FROM", "SELECT", "sql"),
    ("Filtreleme: WHERE ___ > 50", "fiyat", "sql", ["kosul", "sutun"]),
    ("Birincil anahtar: ___ KEY", "PRIMARY", "sql"),
    ("Yabancı anahtar: ___ KEY", "FOREIGN", "sql"),
    ("Tabloları birleştirme: INNER ___", "JOIN", "sql"),
    ("Node PostgreSQL paketi: ___", "pg", "postgres"),
    ("Sorgu çalıştırma: db.___()", "query", "postgres"),
    ("Şifre hash: ___", "bcrypt", "guvenlik"),
    ("Ortam dosyası: ___", ".env", "auth"),
    ("Env yükleyici: ___", "dotenv", "auth"),
    ("Oturum middleware: express-___", "session", "auth"),
    ("Kimlik kütüphanesi: ___", "passport", "auth"),
    ("Giriş kontrolü: req.___()", "isAuthenticated", "auth"),
    ("API: Application Programming ___", "Interface", "api"),
    ("Veri formatı: ___", "JSON", "api"),
    ("Nesneyi string yapma: JSON.___()", "stringify", "api"),
    ("String'i nesne yapma: JSON.___()", "parse", "api"),
    ("HTTP istemci: ___", "axios", "api"),
    ("Veri alma metodu: ___", "GET", "api"),
    ("Veri oluşturma metodu: ___", "POST", "api"),
    ("Query başlangıcı: ___", "?", "api"),
]

for item in bosluk_items:
    if len(item) == 4:
        add_bosluk(item[0], item[1], item[2], item[3])
    else:
        add_bosluk(item[0], item[1], item[2])

while len(bosluk) < 55:
    add_bosluk(f"Express varsayılan dinleme metodu: app.___(3000, callback)", "listen", "express")

# ========== KOD KISA/UZUN (50+) ==========
kod_pairs = [
    ("to-short",
     "for (var i = 0; i < buttons.length; i++) {\n  buttons[i].addEventListener('click', function() {\n    alert('Tıklandı!');\n  });\n}",
     ["buttons.forEach(b => b.onclick = () => alert('Tıklandı!'))", "document.querySelector('button').click()", "buttons.addEventListener('click')", "alert(buttons)"],
     0, "dom"),
    ("to-long",
     "const r = Math.floor(Math.random() * 6) + 1;",
     ["var r = Math.random() * 6 + 1;", "let r = Math.ceil(Math.random() * 6);", "const r = parseInt(Math.random() * 6) + 1;", "var r = Math.floor(Math.random() * 6) + 1;"],
     3, "javascript"),
    ("to-short",
     "document.querySelector('h1').style.color = 'red';\ndocument.querySelector('h1').style.fontSize = '24px';",
     ["$('h1').css({color:'red',fontSize:'24px'})", "h1 { color: red }", "document.h1.color = red", "querySelectorAll('h1')[0] = red"],
     0, "jquery"),
    ("to-long",
     "$('button').click(() => $('h1').css('color', 'red'));",
     ["document.querySelector('button').addEventListener('click', function() {\n  document.querySelector('h1').style.color = 'red';\n});",
      "onclick=\"$('h1').css('color','red')\"",
      "button.color = red",
      "$('h1').red()"],
     0, "dom"),
    ("to-short",
     "if (score > 80) {\n  console.log('Harika');\n} else if (score > 50) {\n  console.log('İyi');\n} else {\n  console.log('Çalış');\n}",
     ["console.log(score>80?'Harika':score>50?'İyi':'Çalış')", "switch(score)", "alert(score)", "score.log()"],
     0, "javascript"),
    ("to-long",
     "const n = arr.length;",
     ["let n = 0; for(let i=0;i<arr.length;i++) n++;", "const n = arr.size;", "var n = arr.count();", "const n = arr.length;"],
     3, "javascript"),
    ("to-short",
     "app.use(express.static('public'));\napp.use(bodyParser.urlencoded({ extended: true }));\napp.use(session({ secret: process.env.SESSION_SECRET }));\napp.use(passport.initialize());\napp.use(passport.session());",
     ["// tek satırda hepsi", "app.middleware(all)", "require('setup')()", "Sıra: static → body → session → passport init → passport session"],
     3, "express"),
    ("to-long",
     "res.render('index', { name: user });",
     ["res.send('<h1>'+user+'</h1>')", "res.json({name:user})", "return index.html", "res.render('index', { name: user });"],
     3, "express"),
    ("to-short",
     "const hash = await bcrypt.hash(password, 12);\nconst ok = await bcrypt.compare(password, storedHash);",
     ["if(password===stored) {}", "encrypt(password,key)", "md5(password)", "bcrypt tek satır: hash ve compare"],
     3, "guvenlik"),
    ("to-long",
     "const { rows } = await db.query('SELECT * FROM users');",
     ["db.select('*').from('users')", "const rows = db.querySync()", "await db.get('users')", "const result = await db.query('SELECT * FROM users');\nconst rows = result.rows;"],
     3, "postgres"),
    ("to-short",
     "fetch('/api').then(r=>r.json()).then(d=>console.log(d));",
     ["axios.get('/api').then(r=>console.log(r.data))", "GET /api", "XMLHttpRequest open send", "document.fetch"],
     0, "api"),
    ("to-long",
     "JSON.parse(str);",
     ["eval('('+str+')')", "str.toObject()", "parseJSON(str)  // ES5", "JSON.parse(str);"],
     3, "api"),
    ("to-short",
     "element.addEventListener('click', function(e) {\n  e.preventDefault();\n  this.classList.toggle('active');\n});",
     ["element.onclick = toggle", "$('.el').click(()=>$('.el').toggleClass('active'))", "element.click(prevent)", "onClick=preventDefault"],
     1, "dom"),
    ("to-long",
     "const dice = Math.floor(Math.random()*6)+1;",
     ["var dice = Math.random()*6", "let dice = Math.round(Math.random()*5)+1", "const dice = Math.floor(Math.random()*6)+1;", "dice = random(1,6)"],
     2, "javascript"),
    ("to-short",
     "users.filter(u => u.age >= 18).map(u => u.name);",
     ["for(names){}", "users.names(18)", "SELECT name FROM users", "filter+map ile yetişkin isimleri"],
     3, "javascript"),
]

for direction, prompt, opts, correct, topic in kod_pairs:
    add_kod(direction, prompt, opts, correct, topic)

# Daha fazla kod sorusu üret
short_long_bank = [
    ("to-long", "arr.includes(x)", "if (arr.indexOf(x) !== -1)", ["arr.indexOf(x) >= 0", "arr.has(x)", "arr.find(x)", "if (arr.indexOf(x) !== -1)"], 3),
    ("to-short", "let s = '';\nfor (const c of str) {\n  if (c !== ' ') s += c;\n}", ["s = str.replace(/ /g,'')", "s = str.split(' ').join('')", "s = str.trim()", "delete spaces str"], 0),
    ("to-long", "$('#btn').on('click', fn);", ["document.getElementById('btn').addEventListener('click', fn)", "$('#btn').click(fn) only", "btn.onclick=fn", "jQuery('#btn').click(fn)"], 0),
    ("to-short", "if (x) { return true; } else { return false; }", ["return !!x", "return x ? true : false", "return x === true", "return Boolean(x)"], 0),
    ("to-long", "const app = express();\napp.listen(3000);", ["express().listen(3000)", "createServer(express).listen(3000)", "npm start 3000", "const app = express();\napp.listen(3000);"], 3),
    ("to-short", "try {\n  const data = await axios.get(url);\n  console.log(data.data);\n} catch (e) {\n  console.error(e);\n}", ["axios.get(url).then(...).catch(...)", "fetch only", "XMLHttpRequest", "get url log"], 0),
    ("to-long", "obj.key", ["obj['key']", "obj->key", "obj::key", "obj.key"], 3),
    ("to-short", "function add(a,b){return a+b}", ["const add = (a,b) => a+b", "add = a+b", "function add(){a+b}", "var sum = a+b"], 0),
    ("to-long", "`<p>${name}</p>`", ["'<p>'+name+'</p>'", "concat name p", "p name", "`<p>${name}</p>`"], 3),
    ("to-short", "const copy = [...arr];", ["const copy = arr", "const copy = arr.slice()", "arr.clone()", "copy = arr.map(x=>x)"], 1),
    ("to-long", "app.post('/submit', (req,res)=>{ res.render('ok',{n:req.body.name}); });",
     ["GET only", "res.send(name)", "app.post('/submit', (req,res)=>{ res.render('ok',{n:req.body.name}); });", "form.action=ok"], 2),
    ("to-short", "passport.use(new LocalStrategy((user, pass, done) => { /* verify */ }));",
     ["auth.login()", "LocalStrategy uzun kurulum + verify callback", "session.login", "req.login only"], 1),
    ("to-long", "process.env.DB_HOST", ["env.DB_HOST", "config.db.host hardcoded", "getenv('DB_HOST') PHP", "process.env.DB_HOST"], 3),
    ("to-short", "SELECT c.ad, s.siparis_no FROM siparisler s INNER JOIN musteriler c ON s.musteri_id = c.id;",
     ["İki tablo JOIN ile müşteri adı ve sipariş no", "SELECT * only", "No JOIN", "DELETE siparisler"], 0),
    ("to-long", "module.exports = router;", ["export router", "exports = router", "return router", "module.exports = router;"], 3),
    ("to-short", "document.addEventListener('DOMContentLoaded', init);", ["window.onload = init only", "init() hemen", "<body onload=init>", "DOMContentLoaded ile init"], 0),
    ("to-long", "const [a,b] = [1,2];", ["var a=1,b=2", "split array", "const a=1; const b=2;", "const [a,b] = [1,2];"], 3),
    ("to-short", "async function getData() {\n  const res = await fetch(url);\n  return res.json();\n}", ["fetch(url).then(r=>r.json())", "sync fetch", "axios only sync", "getData sync"], 0),
    ("to-long", "app.set('view engine', 'ejs');", ["use ejs", "template=ejs", "engine ejs package", "app.set('view engine', 'ejs');"], 3),
    ("to-short", "if (!req.isAuthenticated()) return res.redirect('/login');", ["Giriş yoksa login'e yönlendir", "always redirect", "res.send login", "logout"], 0),
]

topics_k = ["javascript", "dom", "jquery", "express", "sql", "api", "auth", "postgres"]
for i, item in enumerate(short_long_bank):
    direction, prompt, opts, correct = item[0], item[1], item[2], item[3]
    add_kod(direction, prompt, opts, correct, topics_k[i % len(topics_k)])

# Ek kod soruları - çeşitlilik
more_kod = [
    ("to-short", "const doubled = numbers.map(n => n * 2);", ["for loop push", "numbers * 2", "map ile her eleman 2 ile çarpılır", "double(numbers)"], 2),
    ("to-long", "names.forEach(n => console.log(n));", ["for(let i=0;i<names.length;i++) console.log(names[i])", "names.log()", "each names", "names.forEach(n => console.log(n));"], 3),
    ("to-short", "export default function App() {}", ["module.exports = App", "export App default", "ES6 default export kısa", "require App"], 2),
    ("to-long", "const {password, ...rest} = user;", ["delete user.password", "rest = user without password", "omit password", "const {password, ...rest} = user;"], 3),
    ("to-short", "router.get('/users', async (req,res)=>{\n  const r = await db.query('SELECT * FROM users');\n  res.json(r.rows);\n});",
     ["GET /users JSON döner", "res.send html", "POST users", "static file"], 0),
]
for i, item in enumerate(more_kod):
    add_kod(item[0], item[1], item[2], item[3], topics_k[i % 5])

# 50+ kod sorusu için varyantlar
variants = [
    ("to-long", "i++", ["i = i + 1", "i += 0", "++i only same always", "i = i + 1"], 0),
    ("to-short", "i = i + 1;", ["i++", "i+=1", "increment(i)", "add(i,1)"], 0),
    ("to-long", "str.length", ["str.size()", "len(str)", "str.count()", "str.length"], 3),
    ("to-short", "if (a === b) { return true; } return false;", ["return a === b", "return a == b always", "compare(a,b)", "a===b?true:false"], 0),
    ("to-long", "Array.isArray(x)", ["x instanceof Array", "typeof x === 'array'", "x.type==='array'", "Array.isArray(x)"], 3),
    ("to-short", "const unique = [...new Set(arr)];", ["filter duplicates manual", "Set ile tekrarsız dizi", "arr.unique()", "distinct arr"], 1),
    ("to-long", "btn.disabled = true;", ["btn.setAttribute('disabled','')", "btn.disable()", "btn.attr disabled", "btn.disabled = true;"], 3),
    ("to-short", "form.addEventListener('submit', e => {\n  e.preventDefault();\n});", ["submit engelle", "form.delete()", "return false only IE", "prevent submit default"], 0),
    ("to-long", "require('dotenv').config()", ["import dotenv; dotenv.config() ES modules", "loadEnv()", "env.read()", "require('dotenv').config()"], 0),
    ("to-short", "app.use((req,res,next)=>{ console.log(req.method); next(); });", ["logging middleware", "stop request", "res.send log", "no next()"], 0),
]
while len(kod) < 55:
    v = variants[len(kod) % len(variants)]
    add_kod(v[0], v[1], v[2], v[3], topics_k[len(kod) % len(topics_k)])

# ID ata
for i, q in enumerate(test, 1):
    q["id"] = f"T{i}"
for i, q in enumerate(dogru, 1):
    q["id"] = f"D{i}"
for i, q in enumerate(bosluk, 1):
    q["id"] = f"B{i}"
for i, q in enumerate(kod, 1):
    q["id"] = f"K{i}"

out = {
    "meta": {
        "title": "Görsel Programlama II Final Soru Bankası",
        "counts": {"test": len(test), "dogru": len(dogru), "bosluk": len(bosluk), "kod": len(kod)},
    },
    "test": test,
    "dogru": dogru,
    "bosluk": bosluk,
    "kod": kod,
}

path = Path(__file__).parent / "data" / "questions.json"
path.parent.mkdir(exist_ok=True)
json_str = json.dumps(out, ensure_ascii=False, indent=2)
path.write_text(json_str, encoding="utf-8")

js_path = Path(__file__).parent / "js" / "questions-data.js"
js_path.write_text("window.QUIZ_DATA = " + json_str + ";\n", encoding="utf-8")
print(f"Yazıldı: {path}")
print(f"Yazıldı: {js_path}")
print(f"Test: {len(test)}, Doğru/Yanlış: {len(dogru)}, Boşluk: {len(bosluk)}, Kod: {len(kod)}")
print(f"Toplam: {len(test)+len(dogru)+len(bosluk)+len(kod)}")
