# -*- coding: utf-8 -*-
import json
from pathlib import Path

test, dogru, bosluk, kod = [], [], [], []

def add_test(q, opts, c, topic="genel"):
    test.append({"topic": topic, "question": q, "options": opts, "correct": c})
def add_dogru(s, v, t="genel"):
    dogru.append({"topic": t, "statement": s, "correct": v})
def add_bosluk(q, a, t="genel", alt=None):
    bosluk.append({"topic": t, "question": q, "answer": a, "alternatives": alt or []})
def add_kod(d, p, o, c, t="genel"):
    kod.append({"topic": t, "direction": d, "prompt": p, "options": o, "correct": c})

tests = [
    ("CIA Triad'da 'C' neyi ifade eder?", ["Confidentiality (Gizlilik)", "Control", "Certificate", "Compliance"], 0, "giris"),
    ("DDoS saldırısı öncelikle hangi CIA bileşenini ihlal eder?", ["Gizlilik", "Bütünlük", "Erişilebilirlik", "Kimlik doğrulama"], 2, "giris"),
    ("Phishing'in Türkçe karşılığı?", ["Kimlik avı / Oltalama", "Şifreleme", "Yedekleme", "Firewall"], 0, "giris"),
    ("HTTPS hangi protokolü kullanır?", ["FTP", "HTTP + TLS", "Telnet", "SMTP only"], 1, "giris"),
    ("KVKK hangi ülke düzenlemesidir?", ["AB GDPR", "Türkiye kişisel veri kanunu", "ABD HIPAA", "ISO 27001"], 1, "giris"),
    ("PAN ağ türü kapsamı?", ["1-10 metre", "Şehir", "Ülke", "Kıta"], 0, "ag"),
    ("WAN örneği?", ["Bluetooth kulaklık", "İnternet", "Ev Wi-Fi", "USB"], 1, "ag"),
    ("OSI modelinde kaç katman vardır?", ["5", "7", "4", "10"], 1, "ag"),
    ("Router görevi?", ["Paketleri ağlar arası yönlendirir", "Sadece MAC ile switch gibi", "Modem sinyali çevirir", "Şifreleme yapar only"], 0, "ag"),
    ("ARP spoofing hangi katmanda?", ["Fiziksel", "Veri bağlantı (Layer 2)", "Uygulama", "Sunum"], 1, "ag"),
    ("Simetrik şifrelemede anahtar sayısı?", ["Aynı anahtar şifreleme ve çözme", "İki farklı public/private", "Anahtar yok", "Sınırsız"], 0, "kripto"),
    ("AES günümüzde hangi kategori?", ["Güvensiz DES", "Modern simetrik standart", "Sadece hash", "Asimetrik"], 1, "kripto"),
    ("RSA hangi tür şifreleme?", ["Simetrik", "Asimetrik", "Hash", "Sıkıştırma"], 1, "kripto"),
    ("SHA-256 ne yapar?", ["Şifreleme geri çözülür", "Hash / özet üretir", "Sertifika imzalar only", "VPN kurar"], 1, "kripto"),
    ("MD5 güvenlik için?", ["Hâlâ önerilir", "Kırılgan, şifre için kullanılmamalı", "En güçlü hash", "TLS yerine"], 1, "kripto"),
    ("PKI ne sağlar?", ["Dijital sertifika altyapısı", "Sadece firewall", "Antivirus", "DDoS koruma"], 0, "kripto"),
    ("Kimlik doğrulama faktörleri: bilgi, sahiplik, ___", ["Biyometri", "Ağ", "Hash", "VPN"], 0, "kimlik"),
    ("2FA ne demek?", ["İki faktörlü kimlik doğrulama", "İki firewall", "İki IP", "İki router"], 0, "kimlik"),
    ("RBAC neye dayanır?", ["Rol tabanlı erişim", "Rastgele şifre", "Router backup", "Root access only"], 0, "kimlik"),
    ("Brute force saldırısı?", ["Tüm kombinasyonları dener", "Sözlük only", "Phishing", "DDoS"], 0, "kimlik"),
    ("Credential stuffing?", ["Sızmış şifreleri başka sitelerde dener", "Şifre hashler", "VPN", "SSL handshake"], 0, "kimlik"),
    ("Malware genel adı?", ["Zararlı yazılım", "Yararlı yazılım", "Açık kaynak", "Firmware only"], 0, "malware"),
    ("WannaCry türü?", ["Ransomware", "Sadece adware", "Browser eklentisi", "Driver"], 0, "malware"),
    ("Trojan özelliği?", ["Kendini faydalı gibi gizler", "E-posta ile çoğalır only", "Donanım bozar only", "Şifrelemez"], 0, "malware"),
    ("Zero-day açık?", ["Yaması henüz yok", "Herkes bilir", "Açık kaynak", "Test ortamı"], 0, "malware"),
    ("C2 sunucusu?", ["Zararlı yazılım komut alır", "İkinci firewall", "Certificate", "Cloud backup"], 0, "malware"),
    ("Spear phishing?", ["Hedefli oltalama", "Genel spam", "Sesli arama only", "USB"], 0, "sosyal"),
    ("Vishing?", ["Telefon ile oltalama", "Video", "SMS", "USB drop"], 0, "sosyal"),
    ("Smishing?", ["SMS phishing", "Email", "Social media only", "VPN"], 0, "sosyal"),
    ("Pretexting?", ["Sahte senaryo ile güven kazanma", "Şifre hash", "DDoS", "ARP"], 0, "sosyal"),
    ("IoT OWASP Top 10?", ["IoT güvenlik riskleri listesi", "Web framework", "Email protokol", "5G standard"], 0, "iot"),
    ("MQTT güvenlik önerisi?", ["TLS + güçlü kimlik doğrulama", "Şifresiz her zaman", "FTP", "Telnet"], 0, "iot"),
    ("OTA güncelleme riski?", ["İmzasız firmware", "Her zaman güvenli", "Sadece mobil", "Yok"], 0, "iot"),
    ("IDS vs IPS fark?", ["IDS uyarır, IPS engelleyebilir", "Aynı", "IPS sadece log", "IDS şifreler"], 0, "izleme"),
    ("Wireshark?", ["Paket analiz aracı", "Antivirus", "Firewall", "Hash tool"], 0, "izleme"),
    ("Penetrasyon testi?", ["Yetkili saldırı simülasyonu", "İzinsiz hack", "Sadece antivirus", "Backup"], 0, "izleme"),
    ("Zaafiyet taraması?", ["Açıkları otomatik bulur", "Saldırı yapar always", "Şifre kırar only", "DDoS"], 0, "izleme"),
    ("SIEM?", ["Merkezi log ve olay korelasyonu", "Email", "Router", "GPU"], 0, "izleme"),
    ("TLS SSL'in yerini aldı mı?", ["Evet, TLS güncel", "Hayır SSL kullanılır", "İkisi yok", "Sadece IPsec"], 0, "protokol"),
    ("IPsec hangi katmanda?", ["Ağ katmanı", "Uygulama only", "Fiziksel", "Sunum"], 0, "protokol"),
    ("SSH portu genelde?", ["22", "80", "443", "25"], 0, "protokol"),
    ("ISO 27001?", ["Bilgi güvenliği yönetim standardı", "Şifreleme algoritması", "Antivirus", "Wi-Fi"], 0, "protokol"),
    ("IRT ekibi?", ["Olay müdahale ekibi", "Internet router team", "IoT research", "Image render"], 0, "olay"),
    ("Olay müdahale: Hazırlık, Tespit, Sınırlama, ___", ["Kurtarma", "Silme only", "Ignore", "Marketing"], 0, "olay"),
    ("SOAR?", ["Güvenlik otomasyonu", "Social media", "SSL", "SAP"], 0, "olay"),
    ("Dijital vatandaşlık?", ["İnternette sorumlu davranış", "Sadece programlama", "Hack", "Mining"], 0, "etik"),
    ("Etik hacker?", ["Yetkili güvenlik testi yapan", "Kara şapka", "Spam gönderen", "Phisher"], 0, "etik"),
    ("Morris Worm yılı?", ["1988", "2024", "1969", "2000"], 0, "giris"),
    ("Stuxnet?", ["Endüstriyel sistemlere siber silah", "Email virus", "Mobile ad", "Browser"], 0, "malware"),
    ("EternalBlue hangi saldırıda?", ["WannaCry", "ILOVEYOU", "Melissa", "Morris"], 0, "malware"),
    ("VPN amacı?", ["Güvenli tünel / gizlilik", "Hız artırma only", "Antivirus", "Email filter"], 0, "ag"),
    ("Firewall?", ["Trafik filtreler", "Virüs siler", "Şifre üretir", "Backup"], 0, "ag"),
    ("Digital footprint?", ["Dijital iz", "Hash", "TLS", "MAC"], 0, "giris"),
    ("OAuth kullanımı?", ["Yetkilendirme / API erişim", "Şifreleme", "DDoS", "ARP"], 0, "kimlik"),
]
for t in tests: add_test(*t)
while len(test) < 55:
    add_test("Güvenlikte HTTPS padlock ne gösterir?", ["Güvensiz site", "TLS kullanımı", "Ücretsiz site", "VPN"], 1, "protokol")

dogru_items = [
    ("İnternet güvenliği siber güvenlikten daha dar kapsamlıdır.", True, "giris"),
    ("CIA: Confidentiality, Integrity, Availability.", True, "giris"),
    ("Phishing teknik olmayan sosyal saldırıdır.", True, "sosyal"),
    ("DES hâlâ güvenli kabul edilir.", False, "kripto"),
    ("Public key herkesle paylaşılabilir.", True, "kripto"),
    ("Hash geri çevrilebilir olmalıdır.", False, "kripto"),
    ("bcrypt şifre saklamada kullanılır.", True, "kimlik"),
    ("MFA iki veya daha fazla faktör kullanır.", True, "kimlik"),
    ("Ransomware fidye talep edebilir.", True, "malware"),
    ("Virüs kendini kopyalayabilir.", True, "malware"),
    ("Zero-day yaması vardır.", False, "malware"),
    ("IDS otomatik engelleme yapar always.", False, "izleme"),
    ("Pen test izinsiz yapılmalıdır.", False, "izleme"),
    ("TLS 1.3 güncel önerilir.", True, "protokol"),
    ("HTTPS port 443 kullanır.", True, "protokol"),
    ("IPsec VPN temelini oluşturur.", True, "protokol"),
    ("ISO 27001 sertifikasyon standardıdır.", True, "protokol"),
    ("KVKK kişisel veri korur.", True, "giris"),
    ("WLAN güvenlik riski sahte AP içerir.", True, "ag"),
    ("Switch MAC adresi ile çalışır.", True, "ag"),
    ("ARP poisoning MITM sağlayabilir.", True, "ag"),
    ("Spear phishing hedeflidir.", True, "sosyal"),
    ("Tailgating fiziksel sosyal mühendisliktir.", True, "sosyal"),
    ("IoT cihazları varsayılan güvenlidir.", False, "iot"),
    ("GDPR AB veri koruma düzenlemesidir.", True, "iot"),
    ("Olay müdahalede iletişim önemlidir.", True, "olay"),
    ("Post-incident review önerilir.", True, "olay"),
    ("Etik hacking yazılı izin gerektirir.", True, "etik"),
    ("Telif hakkı ihlali etik sorundur.", True, "etik"),
    ("Siber zorbalık internet etiği konusudur.", True, "etik"),
    ("WannaCry 2017 ransomware.", True, "malware"),
    ("Exploit açıktan yararlanır.", True, "malware"),
    ("Payload zararlı eylemdir.", True, "malware"),
    ("Snort IDS/IPS olabilir.", True, "izleme"),
    ("Wireshark pasif izleme yapar.", True, "izleme"),
    ("RBAC rol bazlıdır.", True, "kimlik"),
    ("MAC erişim kontrol modelidir.", True, "kimlik"),
    ("Dictionary attack wordlist kullanır.", True, "kimlik"),
    ("ECC RSA'dan küçük anahtarla güvenlik sağlar.", True, "kripto"),
    ("Dijital imza inkar edilemezlik sağlar.", True, "kripto"),
    ("SSL deprecated, TLS kullanılır.", True, "protokol"),
    ("QUIC HTTP/3 ile ilişkilidir.", True, "protokol"),
    ("Man-in-the-middle şifrelenmemiş trafikte kolay.", True, "ag"),
    ("Firewall default deny iyi pratiktir.", True, "ag"),
    ("2FA SMS zayıf olabilir SIM swap.", True, "kimlik"),
    ("Stuxnet zero-day kullandı.", True, "malware"),
    ("SOC 7/24 izleme merkezi.", True, "izleme"),
    ("Threat modeling saldırıları önceden düşünür.", True, "izleme"),
    ("Black hat yasa dışı niyet.", True, "etik"),
    ("White hat savunma için test yapar.", True, "etik"),
    ("Deepfake sosyal mühendislik riski.", True, "sosyal"),
    ("Baiting USB drop örneğidir.", True, "sosyal"),
]
for s,v,t in dogru_items: add_dogru(s,v,t)
while len(dogru) < 55:
    add_dogru("Güvenlik süreçtir, sadece ürün değildir.", True, "giris")

blanks = [
    ("CIA: C = ___ (Gizlilik)", "Confidentiality", "giris", ["confidentiality"]),
    ("CIA: I = ___ (Bütünlük)", "Integrity", "giris"),
    ("CIA: A = ___ (Erişilebilirlik)", "Availability", "giris"),
    ("Kimlik avı İngilizce: ___", "Phishing", "giris", ["phishing"]),
    ("Zararlı yazılım: ___", "Malware", "malware"),
    ("Fidye yazılımı: ___", "Ransomware", "malware"),
    ("Yaması olmayan açık: ___-day", "Zero", "malware", ["zero"]),
    ("İki faktörlü doğrulama: ___", "2FA", "kimlik", ["MFA"]),
    ("Rol tabanlı erişim: ___", "RBAC", "kimlik"),
    ("Simetrik algoritma örneği: ___", "AES", "kripto"),
    ("Asimetrik algoritma: ___", "RSA", "kripto"),
    ("Hash örneği: SHA-___", "256", "kripto"),
    ("Güvenli web: HTTP + ___", "TLS", "protokol", ["SSL"]),
    ("Ağ katmanı VPN: ___", "IPsec", "protokol"),
    ("Uzak güvenli kabuk: ___", "SSH", "protokol"),
    ("Paket analiz: ___", "Wireshark", "izleme"),
    ("Saldırı tespit: ___", "IDS", "izleme"),
    ("Saldırı önleme: ___", "IPS", "izleme"),
    ("Merkezi log: ___", "SIEM", "izleme"),
    ("Yetkili sızma testi: ___ test", "Penetration", "izleme", ["pen"]),
    ("Kişisel veri kanunu TR: ___", "KVKK", "giris"),
    ("AB veri koruma: ___", "GDPR", "iot"),
    ("Olay müdahale ekibi: ___", "IRT", "olay"),
    ("Otomasyon platformu: ___", "SOAR", "olay"),
    ("Hedefli phishing: Spear ___", "Phishing", "sosyal"),
    ("SMS phishing: ___", "Smishing", "sosyal"),
    ("Telefon phishing: ___", "Vishing", "sosyal"),
    ("Sahte erişim noktası: Evil ___", "Twin", "ag", ["twin"]),
    ("MAC taklit: MAC ___", "spoofing", "ag"),
    ("Dağıtık hizmet reddi: ___", "DDoS", "giris"),
    ("Komut kontrol: ___", "C2", "malware"),
    ("Zararlı yük: ___", "Payload", "malware"),
    ("Açıktan yararlanma: ___", "Exploit", "malware"),
    ("7 katman model: ___", "OSI", "ag"),
    ("Kişisel alan ağı: ___", "PAN", "ag"),
    ("Geniş alan ağı: ___", "WAN", "ag"),
    ("Bilgi güvenliği standardı: ISO ___", "27001", "protokol"),
    ("IoT hafif protokol: ___", "MQTT", "iot"),
    ("Dijital sertifika: ___", "PKI", "kripto"),
    ("Sanal özel ağ: ___", "VPN", "ag"),
    ("Güvenlik duvarı: ___", "Firewall", "ag", ["firewall"]),
    ("Dijital iz: Digital ___", "Footprint", "giris"),
    ("Sosyal mühendislik hedefi: ___", "insan", "sosyal", ["İnsan"]),
    ("Beyaz şapka: White ___", "hat", "etik"),
    ("Kara şapka: Black ___", "hat", "etik"),
    ("Standart şifreleme: AES-___", "256", "kripto"),
    ("Eski simetrik: ___", "DES", "kripto"),
    ("İnternet protokol güvenliği: IP___", "sec", "protokol", ["IPsec"]),
    ("Güvenlik operasyon merkezi: ___", "SOC", "izleme"),
    ("Zaafiyet tarama İngilizce: Vulnerability ___", "scan", "izleme", ["scanning"]),
    ("Bütünlük kontrolü: ___", "Hash", "kripto"),
    ("Public anahtar şifreler, private ___", "decrypts", "kripto", ["çözer"]),
]
for b in blanks:
    if len(b)==4: add_bosluk(b[0],b[1],b[2],b[3])
    else: add_bosluk(b[0],b[1],b[2])
while len(bosluk) < 55:
    add_bosluk("HTTPS = HTTP + ___", "TLS", "protokol")

kod_items = [
    ("to-short", "If an unauthorized person reads email in transit without encryption, which CIA principle is violated?\nAnswer in one line: Confidentiality / Gizlilik breach.", ["Confidentiality violated", "Integrity only", "Availability", "None"], 0, "giris"),
    ("to-long", "DDoS web server.", ["Denial of Service attacks Availability of the web server.", "A distributed denial-of-service attack floods the server with traffic, violating availability (CIA).", "DDoS web server.", "Spam email"], 1, "giris"),
    ("to-short", "Use strong password + 2FA + don't click suspicious links.", ["Layered authentication and phishing awareness for account security.", "Only antivirus", "Disable firewall", "Share password"], 0, "kimlik"),
    ("to-long", "phish email get password", ["Phishing email tricks user into revealing credentials on fake login page.", "Spear phishing uses urgency and brand impersonation to steal passwords via fake sites.", "phish email get password", "secure email"], 1, "sosyal"),
    ("to-short", "TLS handshake: client hello, server hello, cert verify, key exchange, finished.", ["Full TLS handshake establishes encrypted session with certificate validation.", "HTTP GET only", "FTP login", "ARP request"], 0, "protokol"),
    ("to-long", "IDS alert", ["IDS detected suspicious signature and generated alert for SOC analyst review.", "Intrusion Detection System identified anomaly, logged event, SIEM correlated alert.", "IDS alert", "Backup done"], 1, "izleme"),
    ("to-short", "Prepare, Detect, Contain, Eradicate, Recover, Lessons Learned.", ["NIST-style incident response lifecycle phases.", "Just reboot", "Ignore", "Delete logs"], 0, "olay"),
    ("to-long", "malware C2", ["Malware beacons to command-and-control server for instructions and exfiltration.", "Infected host communicates with C2 infrastructure to receive commands and upload stolen data.", "malware C2", "safe update"], 1, "malware"),
]
for i in kod_items: add_kod(*i)
variants = [
    ("to-long", "encrypt with AES", ["Encrypt data using AES symmetric algorithm with secure key management.", "encrypt with AES", "hash SHA", "plain text"], 0, "kripto"),
    ("to-short", "Never share OTP. Bank never asks password by phone.", ["Reject vishing; banks don't ask for OTP/password via unsolicited calls.", "Share OTP", "Email password", "Click all links"], 0, "sosyal"),
    ("to-long", "FW allow 443", ["Firewall rule: allow inbound TCP 443 for HTTPS traffic from internet to web server.", "FW allow 443", "block all", "open 22 public"], 0, "ag"),
    ("to-short", "Hash password with bcrypt before storing in database.", ["Store only salted bcrypt hash, never plaintext passwords.", "Save plain password", "MD5 only", "No hash"], 0, "kimlik"),
]
topics_k = ["giris","kripto","kimlik","malware","izleme","protokol","olay","sosyal"]
while len(kod) < 55:
    v = variants[len(kod) % len(variants)]
    add_kod(v[0], v[1], v[2], v[3], topics_k[len(kod) % len(topics_k)])

import random
random.seed(42)

def shuffle_options(correct_idx, options):
    """Doğru cevabın indeksini karıştırılmış listede döndür."""
    opts = list(options)
    correct_val = opts[correct_idx]
    random.shuffle(opts)
    return opts, opts.index(correct_val)

def dogru_to_test(q):
    stmt = q["statement"]
    opts = ["Evet, ifade doğrudur", "Hayır, ifade yanlıştır", "Sadece bazı durumlarda doğru", "PDF'te geçmiyor"]
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

# Tüm soru tiplerini çoktan seçmeliye dönüştür
all_test = list(test)
for q in dogru:
    all_test.append(dogru_to_test(q))
for q in bosluk:
    all_test.append(bosluk_to_test(q))
for q in kod:
    all_test.append(kod_to_test(q))

for i, q in enumerate(all_test, 1):
    q["id"] = f"T{i}"

out = {
    "meta": {
        "title": "İnternet Güvenliği",
        "course": "guvenlik",
        "testOnly": True,
        "counts": {"test": len(all_test)},
    },
    "test": all_test,
}
base=Path(__file__).parent/"guvenlik"
(base/"data").mkdir(parents=True,exist_ok=True)
(base/"js").mkdir(parents=True,exist_ok=True)
js=json.dumps(out,ensure_ascii=False,indent=2)
(base/"data"/"questions.json").write_text(js,encoding="utf-8")
(base/"js"/"questions-data.js").write_text("window.QUIZ_DATA = "+js+";\n",encoding="utf-8")
print(out["meta"]["counts"], "Total:", sum(out["meta"]["counts"].values()))
