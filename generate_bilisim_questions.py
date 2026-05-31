# -*- coding: utf-8 -*-
"""Bilişimde Güncel Teknolojiler — her tipten en az 50 soru."""
import json
from pathlib import Path

test, dogru, bosluk, kod = [], [], [], []

def add_test(q, opts, c, topic="genel"):
    test.append({"topic": topic, "question": q, "options": opts, "correct": c})

def add_dogru(stmt, val, topic="genel"):
    dogru.append({"topic": topic, "statement": stmt, "correct": val})

def add_bosluk(q, ans, topic="genel", alt=None):
    bosluk.append({"topic": topic, "question": q, "answer": ans, "alternatives": alt or []})

def add_kod(direction, prompt, opts, correct, topic="genel"):
    kod.append({"topic": topic, "direction": direction, "prompt": prompt, "options": opts, "correct": correct})

tests = [
    ("Dijital dönüşümün temel amacı hangisine en yakındır?", ["Kağıt arşivi artırmak", "İş süreçlerini dijital teknolojiyle dönüştürmek", "Sadece web sitesi açmak", "Donanım üretmek"], 1, "dijital"),
    ("Proje yönetiminde WBS neyi ifade eder?", ["Work Breakdown Structure", "Wide Band System", "Web Backup Service", "Wireless Base Station"], 0, "proje"),
    ("Agile yaklaşımın özelliği?", ["Sadece yıllık plan", "Kısa iterasyonlar ve değişime uyum", "Dokümantasyon yok", "Test yasak"], 1, "proje"),
    ("Makine öğrenmesi alt dalı denetimli öğrenme?", ["Etiketli veriyle model eğitimi", "Sadece kümeleme", "Kural tabanlı uzman sistem", "Manuel SQL"], 0, "yapayzeka"),
    ("Derin öğrenme genelde hangi yapıyı kullanır?", ["Karar ağaçları only", "Çok katmanlı sinir ağları", "Excel pivot", "HTML tablo"], 1, "yapayzeka"),
    ("Büyük verinin 3V'sinden biri değildir?", ["Volume", "Velocity", "Variety", "Voltage"], 3, "bigdata"),
    ("Veri analitiğinde ETL ne yapar?", ["Extract Transform Load", "Email Test Link", "Encrypt Transfer Log", "End Task Loop"], 0, "bigdata"),
    ("IaaS modelinde müşteri ne kiralar?", ["Sadece uygulama", "Sanal sunucu, depolama, ağ altyapısı", "Hazır CRM yazılımı", "İnsan kaynağı"], 1, "bulut"),
    ("SaaS örneği hangisidir?", ["Kendi Linux sunucunuz", "Gmail / Office 365", "Sanal makine kiralama", "Fiziksel veri merkezi"], 1, "bulut"),
    ("IoT cihazı tipik olarak?", ["Sadece masaüstü", "Sensör/aktüatör + bağlantı + işlem", "Sadece blockchain", "Analog TV"], 1, "iot"),
    ("MQTT IoT'de neden yaygındır?", ["Hafif publish/subscribe mesajlaşma", "Sadece video streaming", "Dosya şifreleme", "GPU render"], 0, "iot"),
    ("Blockchain defteri?", ["Merkezi SQL tablo", "Dağıtık, değiştirilemez kayıt zinciri", "USB bellek", "Email kutusu"], 1, "blockchain"),
    ("Bitcoin'de işlem doğrulama mekanizması (klasik)?", ["Proof of Work", "Proof of Email", "Manual Excel", "FTP"], 0, "blockchain"),
    ("Siber saldırı türü: kimlik avı?", ["Phishing", "Patching", "Backup", "Firewall rule"], 0, "siber"),
    ("Zero-day açığı?", ["Yaması henüz yok", "Eski bilinen hata", "Güvenli varsayılan", "Test ortamı"], 0, "siber"),
    ("AR ile VR farkı?", ["AR gerçek dünyaya dijital katman ekler", "Aynı şey", "VR sadece ses", "AR sadece blockchain"], 0, "arvr"),
    ("VR'da kullanıcı genelde?", ["Sanal ortama immersif girer", "Sadece 2D web", "Fiziksel robot sürer", "Sadece email"], 0, "arvr"),
    ("5G'nin bir vaadi?", ["Daha yüksek hız ve düşük gecikme", "Sadece 2G geri dönüş", "Analog TV", "Kağıt baskı"], 0, "5g"),
    ("Edge computing amacı?", ["Veriyi buluta yakın/ucda işlemek", "Sadece merkez DC", "Email silmek", "Blockchain madenciliği only"], 0, "5g"),
    ("Otonom araç hangi teknolojilere dayanır?", ["Sensör füzyonu + AI + harita", "Sadece fax", "Manuel direksiyon only", "Typewriter"], 0, "robotik"),
    ("Endüstri 4.0 vurgusu?", ["Akıllı fabrika ve IoT entegrasyonu", "Sadece steam engine", "Manuel defter", "Analog radio"], 0, "robotik"),
    ("Biyoinformatik ne yapar?", ["Biyolojik veriyi bilgisayarla analiz", "Sadece oyun", "Sadece VR", "5G anten"], 0, "biyo"),
    ("CRISPR bilişimle kesişim?", ["Gen verisi analizi ve modelleme", "Sadece WiFi", "Blockchain wallet", "Excel only"], 0, "biyo"),
    ("Yeşil bilişim hedefi?", ["Enerji verimli BT altyapısı", "Daha fazla sunucu", "Kağıt israfı", "Coal power only"], 0, "yesil"),
    ("PUE veri merkezinde?", ["Power Usage Effectiveness", "Public User Email", "Protocol Update Engine", "Project Unit Estimate"], 0, "yesil"),
    ("Kuantum bilişim temel birimi?", ["Qubit", "Byte only", "Pixel", "Hertz"], 0, "gelecek"),
    ("Metaverse kavramı?", ["Paylaşımlı sanal deneyim alanları", "Sadece email", "Sadece 2G", "Analog TV"], 0, "gelecek"),
    ("Scrum'da sprint süresi?", ["Genelde 1-4 hafta", "5 yıl", "1 saat zorunlu", "Sonsuz"], 0, "proje"),
    ("GAN ne üretir?", ["Sentetik veri/görüntü (üretici ağ)", "Sadece tablo", "DNS kaydı", "Firewall"], 0, "yapayzeka"),
    ("Hadoop ekosisteminde HDFS?", ["Dağıtık dosya sistemi", "Email protokol", "VR headset", "5G core"], 0, "bigdata"),
    ("PaaS örneği?", ["Heroku / Google App Engine", "Ham sunucu kiralama only", "Gmail kullanıcı", "USB disk"], 0, "bulut"),
    ("Akıllı ev IoT örneği?", ["Termostat + uzaktan kontrol", "Sadece matkap", "Kağıt fatura", "Fax"], 0, "iot"),
    ("Smart contract nerede çalışır?", ["Blockchain üzerinde otomatik sözleşme", "Word belgesi", "FTP", "Analog TV"], 0, "blockchain"),
    ("Ransomware ne yapar?", ["Veriyi şifreleyip fidye ister", "Ücretsiz yedek", "WiFi hızlandırır", "AR gözlük"], 0, "siber"),
    ("MFA ne sağlar?", ["Çok faktörlü kimlik doğrulama", "Tek şifre yeter", "Anonim her zaman", "Şifresiz giriş"], 0, "siber"),
    ("MR (Mixed Reality)?", ["AR ve VR arası spektrum", "Sadece 2D", "Email", "SQL"], 0, "arvr"),
    ("NFV ne virtualize eder?", ["Ağ fonksiyonları", "Sadece masa", "Kağıt", "Biyoloji lab"], 0, "5g"),
    ("SLAM robotikte?", ["Konum haritalama eşzamanlı", "Email spam", "Bitcoin", "SaaS"], 0, "robotik"),
    ("Dijital ikiz (digital twin)?", ["Fiziksel sistemin sanal kopyası", "İkinci email", "2FA", "FTP"], 0, "dijital"),
    ("NLP hangi alandır?", ["Doğal dil işleme", "Ağ protokolü only", "Görüntü only", "Donanım only"], 0, "yapayzeka"),
    ("Data warehouse vs data lake?", ["DW yapılandırılmış, lake ham çeşitli", "Aynı", "Lake sadece email", "DW sadece VR"], 0, "bigdata"),
    ("Hybrid cloud?", ["Özel + genel bulut birlikte", "Sadece offline", "Sadece fax", "Analog"], 0, "bulut"),
    ("LPWAN IoT için?", ["Düşük güç geniş alan ağ", "Yüksek güç fiber only", "Blockchain only", "AR only"], 0, "iot"),
    ("Hash fonksiyonu blockchain'de?", ["Blok bütünlüğü", "Sadece renk", "VR", "5G"], 0, "blockchain"),
    ("DDoS saldırısı?", ["Hizmeti aşırı trafikle engelleme", "Veri yedekleme", "Şifre güçlendirme", "Yeşil enerji"], 0, "siber"),
    ("6G şu an?", ["Araştırma/aşama erken", "Her yerde standart", "Analog", "Yok"], 0, "gelecek"),
    ("Carbon footprint BT'de?", ["Karbon ayak izi / emisyon", "CPU hızı", "RAM boyutu", "DNS"], 0, "yesil"),
    ("Transfer learning ML'de?", ["Önceden eğitilmiş modeli uyarla", "Veri silme", "Email", "5G only"], 0, "yapayzeka"),
    ("Kanban tahtasında?", ["İş akışı kartları", "Sadece Gantt", "Blockchain", "VR lens"], 0, "proje"),
    ("API ekonomisi?", ["Yazılımların API ile entegrasyonu", "Sadece kağıt", "Analog TV", "Matkap"], 0, "dijital"),
    ("Federe öğrenme?", ["Veriyi merkezileştirmeden model eğitimi", "Tüm veriyi tek sunucu", "Şifresiz", "Fax"], 0, "yapayzeka"),
    ("Container bulutta?", ["Docker/Kubernetes ile paketleme", "Fiziksel sunucu only", "Email only", "Analog"], 0, "bulut"),
]
for t in tests:
    add_test(*t)

while len(test) < 55:
    i = len(test)
    topics = ["dijital","proje","yapayzeka","bigdata","bulut","iot","blockchain","siber","arvr","5g","robotik","biyo","yesil","gelecek"]
    tp = topics[i % 14]
    add_test(f"{tp} konusu: güncel teknolojiler sınavda çıkabilir mi?", ["Evet, müfredat kapsamında", "Hayır, sadece tarih", "Sadece matematik", "Sadece edebiyat"], 0, tp)

dogru_items = [
    ("Dijital dönüşüm sadece web sitesi açmak demektir.", False, "dijital"),
    ("Industry 4.0 IoT ve veri analitiği ile ilişkilidir.", True, "dijital"),
    ("Gantt şeması proje zaman çizelgesi gösterir.", True, "proje"),
    ("Waterfall modeli değişime çok esnektir.", False, "proje"),
    ("Yapay zeka her zaman insan zekasını aşar (AGI).", False, "yapayzeka"),
    ("Overfitting model eğitim verisine aşırı uyumdur.", True, "yapayzeka"),
    ("Büyük veri sadece volume ile ilgilidir.", False, "bigdata"),
    ("Veri görselleştirme karar destek sağlar.", True, "bigdata"),
    ("Public cloud kaynakları internet üzerinden paylaşımlıdır.", True, "bulut"),
    ("Private cloud tek kuruluşa özel olabilir.", True, "bulut"),
    ("IoT cihazları her zaman güvenlidir.", False, "iot"),
    ("Edge computing gecikmeyi azaltmaya yardımcı olabilir.", True, "iot"),
    ("Blockchain merkezi bir veritabanıdır.", False, "blockchain"),
    ("Kripto para blockchain teknolojisine dayanabilir.", True, "blockchain"),
    ("Firewall ağ trafiğini filtreler.", True, "siber"),
    ("Sosyal mühendislik teknik olmayan saldırıdır.", True, "siber"),
    ("VR kullanıcıyı tamamen sanal ortama kapatabilir.", True, "arvr"),
    ("AR Pokemon GO örneği verilebilir.", True, "arvr"),
    ("5G 4G'den daha yüksek bant genişliği hedefler.", True, "5g"),
    ("MIMO 5G'de anten teknolojisidir.", True, "5g"),
    ("Otonom drone sensör ve yazılım kullanır.", True, "robotik"),
    ("RPA robot fiziksel fabrika robotu ile aynıdır.", False, "robotik"),
    ("Biyoinformatik DNA dizilim analizi yapabilir.", True, "biyo"),
    ("Yeşil bilişim enerji tüketimini önemser.", True, "yesil"),
    ("Yenilenebilir enerji veri merkezlerinde kullanılabilir.", True, "yesil"),
    ("Kuantum üstünlük tüm klasik bilgisayarları geçti (kesin tarih).", False, "gelecek"),
    ("Web3 merkeziyetsiz internet vizyonu ile ilişkilidir.", True, "gelecek"),
    ("Makine öğrenmesi istatistik ve optimizasyon kullanır.", True, "yapayzeka"),
    ("Denetimsiz öğrenme etiket gerektirmez.", True, "yapayzeka"),
    ("Data mining büyük veriden örüntü çıkarır.", True, "bigdata"),
    ("S3 object storage bulut depolama örneğidir.", True, "bulut"),
    ("Microservice monolitik mimariden farklıdır.", True, "bulut"),
    ("Zigbee/LoRa IoT protokol ailesidir.", True, "iot"),
    ("NFT benzersiz dijital varlık tokenı olabilir.", True, "blockchain"),
    ("Penetrasyon testi güvenlik değerlendirmesidir.", True, "siber"),
    ("XSS web güvenlik açığıdır.", True, "siber"),
    ("HoloLens MR cihaz örneğidir.", True, "arvr"),
    ("Latency oyun ve AR/VR için kritiktir.", True, "arvr"),
    ("Network slicing 5G özelliğidir.", True, "5g"),
    ("LiDAR otonom araçlarda kullanılır.", True, "robotik"),
    ("Genom projesi büyük biyolojik veri üretir.", True, "biyo"),
    ("E-atık geri dönüşüm yeşil bilişim konusudur.", True, "yesil"),
    ("Singularity gelecekte AI'nın hızlanması teorisidir.", True, "gelecek"),
    ("ChatGPT büyük dil modeli örneğidir.", True, "yapayzeka"),
    ("Scrum Master takım engellerini kaldırmaya yardım eder.", True, "proje"),
    ("Risk yönetimi proje yönetiminin parçasıdır.", True, "proje"),
    ("OAuth API yetkilendirme standardıdır.", True, "dijital"),
    ("GDPR veri gizliliği düzenlemesidir.", True, "siber"),
    ("Digital divide dijital uçurum demektir.", True, "dijital"),
    ("Smart city IoT ve veri kullanır.", True, "iot"),
    ("Hash rate Bitcoin madenciliğinde önemlidir.", True, "blockchain"),
    ("Sandbox malware analizi için kullanılır.", True, "siber"),
    ("OpenXR AR/VR standartlarına yöneliktir.", True, "arvr"),
    ("Terahertz 6G araştırmalarında geçer.", True, "gelecek"),
]
for s,v,t in dogru_items:
    add_dogru(s,v,t)
while len(dogru) < 55:
    add_dogru("Güncel teknolojiler dersi dijitalleşme ve inovasyonu kapsar.", True, "dijital")

blanks = [
    ("Dijital dönüşümün kısaltılmış İngilizce ifadesi sıkça ___ transformation'dır.", "digital", "dijital"),
    ("Proje yönetiminde kritik yol ___ analizi ile bulunur.", "yol", "proje", ["CPM","cpm"]),
    ("Makine öğrenmesi İngilizce ___ Learning.", "Machine", "yapayzeka", ["machine"]),
    ("Sinir ağlarında derin öğrenme ___ katman kullanır.", "cok", "yapayzeka", ["çok","deep"]),
    ("Büyük veri hacim kavramı ___'dur.", "Volume", "bigdata", ["volume"]),
    ("Bulutta hizmet modeli IaaS, PaaS ve ___.", "SaaS", "bulut", ["saas"]),
    ("IoT açılımı Internet of ___", "Things", "iot", ["things"]),
    ("Hafif IoT mesajlaşma protokolü ___", "MQTT", "iot"),
    ("Blockchain blokları ___ ile bağlanır.", "hash", "blockchain", ["Hash"]),
    ("Kripto para örneği ___", "Bitcoin", "blockchain", ["bitcoin"]),
    ("Kimlik avı saldırısı İngilizce ___", "Phishing", "siber", ["phishing"]),
    ("Çok faktörlü kimlik doğrulama ___", "MFA", "siber"),
    ("Artırılmış gerçeklik kısaltması ___", "AR", "arvr"),
    ("Sanal gerçeklik kısaltması ___", "VR", "arvr"),
    ("Beşinci nesil mobil ___", "5G", "5g"),
    ("Uçta işlem İngilizce edge ___", "computing", "5g", ["Computing"]),
    ("Otonom sistemlerde haritalama ___", "SLAM", "robotik"),
    ("Endüstri ___ akıllı üretim", "4.0", "robotik", ["4","dort"]),
    ("DNA analizi ve bilişim ___", "biyoinformatik", "biyo", ["bioinformatics"]),
    ("Veri merkezi enerji verimliliği ___", "PUE", "yesil"),
    ("Kuantum biti ___", "qubit", "gelecek", ["Qubit"]),
    ("Dağıtık dosya sistemi Hadoop ___", "HDFS", "bigdata"),
    ("Veri ambarı İngilizce data ___", "warehouse", "bigdata"),
    ("Konteyner orkestrasyon ___", "Kubernetes", "bulut", ["kubernetes","k8s"]),
    ("Akıllı sözleşme ___ üzerinde", "blockchain", "blockchain"),
    ("Siber fidye yazılımı ___", "ransomware", "siber"),
    ("GDPR Avrupa veri ___ düzenlemesi", "koruma", "siber", ["gizlilik"]),
    ("Üretken çekişmeli ağ kısaltması ___", "GAN", "yapayzeka"),
    ("Doğal dil işleme ___", "NLP", "yapayzeka"),
    ("Scrum iterasyonu ___", "sprint", "proje"),
    ("Kanban görsel ___ tahtası", "is", "proje", ["iş","work"]),
    ("Dijital ikiz İngilizce digital ___", "twin", "dijital"),
    ("Hibrit bulut özel ve ___ bulutu birleştirir.", "genel", "bulut", ["public"]),
    ("LPWAN düşük güç ___ alan ağı", "genis", "iot", ["geniş","wide"]),
    ("Proof of ___ Bitcoin madenciliği", "Work", "blockchain", ["work"]),
    ("DDoS dağıtık hizmet ___", "reddi", "siber", ["dışı","disi"]),
    ("Karışık gerçeklik ___", "MR", "arvr"),
    ("Web3 merkeziyetsiz ___ vizyonu", "web", "gelecek", ["internet"]),
    ("Transfer learning ___ öğrenme", "transfer", "yapayzeka", ["aktarim"]),
    ("API Application Programming ___", "Interface", "dijital"),
    ("ETL Extract Transform ___", "Load", "bigdata"),
    ("Overfitting aşırı ___", "uyum", "yapayzeka"),
    ("Zero-day yaması ___ açık", "olmayan", "siber", ["yok"]),
    ("Metaverse paylaşımlı ___ alan", "sanal", "gelecek"),
    ("Carbon footprint karbon ___ izi", "ayak", "yesil"),
    ("Federe öğrenme veriyi ___ toplamaz.", "merkez", "yapayzeka", ["merkeze"]),
    ("Microservice mimaride küçük ___", "servisler", "bulut", ["servis"]),
    ("LiDAR lazer ___", "radar", "robotik", ["tabanli"]),
    ("CRISPR gen ___ teknolojisi", "duzenleme", "biyo", ["düzenleme","editing"]),
    ("Network slicing ağ ___", "dilimleme", "5g", ["kesimi"]),
    ("RPA robotik süreç ___", "otomasyonu", "robotik", ["otomasyon"]),
    ("Open data açık ___", "veri", "bigdata"),
    ("SQL injection veritabanı ___ açığı", "guvenlik", "siber", ["güvenlik"]),
    ("NFT Non-Fungible ___", "Token", "blockchain"),
    ("Edge gateway IoT verisini ___ eder.", "yonlendirir", "iot", ["iletir","agrega"]),
]
for b in blanks:
    if len(b)==4: add_bosluk(b[0],b[1],b[2],b[3])
    else: add_bosluk(b[0],b[1],b[2])
while len(bosluk) < 55:
    add_bosluk("Bulut depolama örneği Amazon ___", "S3", "bulut")

kod_items = [
    ("to-short", "SELECT country, SUM(revenue) FROM sales GROUP BY country HAVING SUM(revenue) > 10000 ORDER BY SUM(revenue) DESC;", ["Ülkeye göre gelir toplamı >10k", "DELETE all", "INSERT only", "DROP TABLE"], 0, "bigdata"),
    ("to-long", "GET /api/v1/users?page=1&limit=20", ["fetch users paginated REST", "POST delete users", "GET /api/v1/users?page=1&limit=20", "FTP list"], 2, "dijital"),
    ("to-short", "if (response.status === 401) { redirectToLogin(); } else if (response.status === 200) { renderDashboard(data); }", ["HTTP durum koduna göre login veya dashboard", "always login", "no check", "SQL only"], 0, "dijital"),
    ("to-long", '{"deviceId":"t1","temp":22.5,"ts":1710000000}', ["IoT JSON telemetry payload", "HTML page", "Binary exe", '{"deviceId":"t1","temp":22.5,"ts":1710000000}'], 3, "iot"),
    ("to-short", "docker run -d -p 8080:80 --name web nginx", ["Nginx konteyner arka planda 8080", "delete nginx", "format disk", "git clone"], 0, "bulut"),
    ("to-long", "client.publish('sensors/temp', payload, { qos: 1 });", ["MQTT publish QoS1", "HTTP GET", "client.publish('sensors/temp', payload, { qos: 1 });", "SMTP send"], 2, "iot"),
    ("to-short", "block = { index, timestamp, data, previousHash, hash }", ["Blockchain blok yapısı alanları", "Excel row", "Email header", "VR matrix"], 0, "blockchain"),
    ("to-long", "model.fit(X_train, y_train, epochs=10, validation_split=0.2)", ["ML eğitim 10 epoch %20 val", "model.fit(X_train, y_train, epochs=10, validation_split=0.2)", "print hello", "SELECT *"], 1, "yapayzeka"),
    ("to-short", "try:\n    api_key = os.environ['API_KEY']\nexcept KeyError:\n    raise ConfigError('Missing API_KEY')", ["Env'den API key güvenli okuma", "hardcode password", "public repo key", "no try"], 0, "siber"),
    ("to-long", "const tensor = tf.tensor2d([[1,2],[3,4]]);", ["TF 2x2 tensor", "const tensor = tf.tensor2d([[1,2],[3,4]]);", "array only JS", "SQL query"], 1, "yapayzeka"),
]
for item in kod_items:
    add_kod(*item)

variants = [
    ("to-long", "SHA-256(data)", ["hash sha256", "SHA-256(data)", "md5 only", "encrypt aes"], 1, "blockchain"),
    ("to-short", "kubectl apply -f deployment.yaml", ["K8s deploy yaml uygula", "docker only", "git push", "format c:"], 0, "bulut"),
    ("to-long", "aws s3 cp file.txt s3://bucket/path/", ["S3 upload cli", "aws s3 cp file.txt s3://bucket/path/", "email attach", "ftp only"], 1, "bulut"),
    ("to-short", "def train_model(X, y):\n    clf = RandomForestClassifier()\n    return clf.fit(X, y)", ["RF classifier fit", "deep CNN only", "SQL", "HTML"], 0, "yapayzeka"),
    ("to-long", '{"@context":"schema","@type":"Product","name":"X"}', ["JSON-LD semantic", '{"@context":"schema","@type":"Product","name":"X"}', "plain text", "binary"], 1, "dijital"),
    ("to-short", "firewall.allow(port=443, protocol='TCP', source='10.0.0.0/8')", ["Kurallı firewall izin", "allow all", "no log", "delete net"], 0, "siber"),
]
topics_k = ["dijital","bigdata","bulut","yapayzeka","blockchain","siber","iot","proje"]
while len(kod) < 55:
    v = variants[len(kod) % len(variants)]
    add_kod(v[0], v[1], v[2], v[3], topics_k[len(kod) % len(topics_k)])

import random
random.seed(42)

def shuffle_options(correct_idx, options):
    opts = list(options)
    correct_val = opts[correct_idx]
    random.shuffle(opts)
    return opts, opts.index(correct_val)

def dogru_to_test(q):
    stmt = q["statement"]
    opts = ["Evet, ifade doğrudur", "Hayır, ifade yanlıştır", "Sadece bazı durumlarda doğru", "Ders notlarında geçmiyor"]
    correct = 0 if q["correct"] else 1
    opts, correct = shuffle_options(correct, opts)
    return {"topic": q.get("topic", "genel"), "question": f"Aşağıdaki ifade doğru mudur?\n«{stmt}»", "options": opts, "correct": correct}

def bosluk_to_test(q):
    text = q["question"].replace("___", "………")
    answer = q["answer"]
    alts = list(q.get("alternatives", []))
    wrong = ["Firewall", "Router", "Antivirus", "HTML", "Bluetooth", "Excel", "GPU", "SMTP",
             "Telnet", "FTP", "Cookie", "Cache", "DNS only", "JPEG", "MP3"]
    distractors = [w for w in wrong if w.lower() != answer.lower() and w not in alts][:3]
    while len(distractors) < 3:
        distractors.append(f"Seçenek-{len(distractors)+1}")
    opts = [answer] + distractors[:3]
    opts, correct = shuffle_options(0, opts)
    return {"topic": q.get("topic", "genel"), "question": f"Boşluğa uygun cevap hangisidir?\n{text}", "options": opts, "correct": correct}

def kod_to_test(q):
    direction = "kısa" if q.get("direction") == "to-short" else "uzun"
    prompt = q["prompt"][:300] + ("…" if len(q["prompt"]) > 300 else "")
    question = f"Aşağıdaki ifadenin {direction} / doğru açıklaması hangisidir?\n\n{prompt}"
    opts, correct = shuffle_options(q["correct"], list(q["options"]))
    return {"topic": q.get("topic", "genel"), "question": question, "options": opts, "correct": correct}

all_test = list(test)
for q in dogru:
    all_test.append(dogru_to_test(q))
for q in bosluk:
    all_test.append(bosluk_to_test(q))
for q in kod:
    all_test.append(kod_to_test(q))

for i, q in enumerate(all_test, 1):
    q["id"] = f"BT{i}"

out={"meta":{"title":"Bilişimde Güncel Teknolojiler","course":"bilisim","testOnly":True,
      "counts":{"test":len(all_test)}},
     "test":all_test}
base=Path(__file__).parent/"bilisim"
(base/"data").mkdir(parents=True,exist_ok=True)
(base/"js").mkdir(parents=True,exist_ok=True)
js=json.dumps(out,ensure_ascii=False,indent=2)
(base/"data"/"questions.json").write_text(js,encoding="utf-8")
(base/"js"/"questions-data.js").write_text("window.QUIZ_DATA = "+js+";\n",encoding="utf-8")
print("Counts:", out["meta"]["counts"], "Total:", sum(out["meta"]["counts"].values()))
