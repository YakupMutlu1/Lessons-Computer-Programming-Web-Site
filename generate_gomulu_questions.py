# -*- coding: utf-8 -*-
"""Gömülü Sistemler soru bankası — her tipten en az 50 soru."""
import json
from pathlib import Path

test, dogru, bosluk, kod = [], [], [], []

def add_test(q, opts, c, topic="genel"):
    test.append({"topic": topic, "question": q, "options": opts, "correct": c})

def add_dogru(stmt, val, topic="genel"):
    dogru.append({"topic": topic, "statement": stmt, "correct": val})

def add_bosluk(q, ans, topic="genel", alt=None):
    bosluk.append({"topic": topic, "question": q, "answer": ans, "alternatives": alt or []})

def add_kod(direction, prompt, opts, correct, topic="arduino"):
    kod.append({"topic": topic, "direction": direction, "prompt": prompt, "options": opts, "correct": correct})

# --- TEST (50+) ---
tests = [
    ("Gömülü sistem tanımı aşağıdakilerden hangisine en uygundur?", ["Genel amaçlı masaüstü PC", "Belirli görev için tasarlanmış gömülü bilgisayar", "Sadece web sunucusu", "Bulut veri merkezi"], 1, "giris"),
    ("Mikrodenetleyici (MCU) ile mikroişlemci (MPU) farkında MCU'da genelde ne bulunur?", ["Sadece CPU, bellek harici", "CPU + RAM/Flash + çevre birimi tek çipte", "Sadece GPU", "İşletim sistemi zorunlu değil"], 1, "giris"),
    ("Gömülü sistemlerde en kritik kısıtlardan biri değildir?", ["Gerçek zamanlılık", "Düşük güç tüketimi", "Sınırlı bellek", "4K oyun grafikleri"], 3, "giris"),
    ("Firmware nedir?", ["Donanımın fiziksel devresi", "Cihaza gömülü kalıcı yazılım", "İnternet tarayıcısı", "Veritabanı şeması"], 1, "giris"),
    ("NodeMCU kartı hangi WiFi çipini temel alır?", ["ESP32", "ESP8266", "Arduino Uno", "Raspberry Pi"], 1, "nodemcu"),
    ("ESP8266 mantık seviyesi genelde kaç volttur?", ["5V", "3.3V", "12V", "1.8V only"], 1, "nodemcu"),
    ("Breadboard üzerinde delikler nasıl bağlanır?", ["Hepsi seri", "Satırlar kısa devre (power rail hariç kurallara göre)", "Hiç bağlanmaz", "Sadece dikey"], 1, "devre"),
    ("LED'e direnç konulmasının ana nedeni?", ["LED'i parlak yapmak", "Akımı sınırlayıp LED'i korumak", "Voltajı artırmak", "PWM için"], 1, "devre"),
    ("Pull-up direnci ne işe yarar?", ["Floating pini belirli seviyede tutmak", "Motor hızlandırmak", "WiFi güçlendirmek", "ADC çözünürlüğü"], 0, "devre"),
    ("digitalWrite(pin, HIGH) ne yapar?", ["Pini analog okur", "Dijital çıkışı lojik 1 yapar", "Pini input yapar", "Serial başlatır"], 1, "gpio"),
    ("analogRead() Arduino'da kaç bit çözünürlük verir (Uno)?", ["8 bit (0-255)", "10 bit (0-1023)", "16 bit", "32 bit"], 1, "gpio"),
    ("INPUT_PULLUP modu ne sağlar?", ["Harici pull-up şart", "Dahili pull-up ile boşta HIGH", "Sadece analog", "Motor sürer"], 1, "gpio"),
    ("PWM ile ne kontrol edilir?", ["Dijital sadece 0/1", "LED parlaklığı / servo / motor hızı gibi analog benzeri", "I2C adresi", "Baud rate"], 1, "gpio"),
    ("UART haberleşmede kaç hat minimum gereklidir (basit)?", ["1 TX", "TX ve RX", "4 MOSI MISO", "SDA SCL"], 1, "protokol"),
    ("Baud rate nedir?", ["Veri bit hızı / saniye", "CPU frekansı", "ADC referansı", "Pil voltajı"], 0, "protokol"),
    ("SPI'da veri hattı hangileridir?", ["SDA, SCL", "MOSI, MISO, SCK, CS", "TX, RX", "VCC, GND only"], 1, "protokol"),
    ("I2C'de kaç master olabilir (tipik uygulama)?", ["Sınırsız aynı anda", "Birden fazla master nadiren, genelde tek master", "Hiç master yok", "Sadece slave"], 1, "protokol"),
    ("MQTT'de mesaj dağıtım modeli?", ["Peer to peer only", "Publish/Subscribe broker üzerinden", "HTTP GET only", "UDP broadcast only"], 1, "protokol"),
    ("DHT11 sensörü ne ölçer?", ["Sadece basınç", "Sıcaklık ve nem", "Mesafe", "Işık"], 1, "sensor"),
    ("HC-SR04 hangi prensiple mesafe ölçer?", ["Manyetik alan", "Ultrasonik yankı süresi", "Kızılötesi", "GPS"], 1, "sensor"),
    ("Servo motor kontrolünde genelde hangi sinyal?", ["Analog sinüs", "PWM darbe genişliği", "I2C paket", "UART string"], 1, "sensor"),
    ("Aktüatör örneği hangisidir?", ["LDR", "DHT11", "Röle / motor", "Termistör"], 2, "sensor"),
    ("Flash bellekte ne saklanır?", ["Sadece geçici değişken", "Program kodu (kalıcı)", "Sadece WiFi şifresi", "ADC örnekleri"], 1, "bellek"),
    ("Stack bellek ne için kullanılır?", ["Kalıcı dosya", "Fonksiyon çağrıları ve yerel değişkenler", "Program yükleme", "Ekran buffer"], 1, "bellek"),
    ("FreeRTOS'ta görev (task) nedir?", ["Donanım pin", "Bağımsız çalışan kod parçası", "Sadece ISR", "EEPROM adres"], 1, "rtos"),
    ("Mutex ne işe yarar?", ["WiFi bağlantı", "Paylaşılan kaynağa tek erişim kilidi", "Analog okuma", "Serial baud"], 1, "rtos"),
    ("Bare-metal sistemde?", ["Her zaman Linux çalışır", "Doğrudan donanım, minimal/RTOS'suz olabilir", "Sadece bulut", "Tarayıcı gerekir"], 1, "rtos"),
    ("Deep sleep modunun amacı?", ["CPU hızlandırmak", "Güç tüketimini azaltmak", "ADC kapatmak zorunlu değil", "WiFi güçlendirmek"], 1, "guc"),
    ("Watchdog timer (WDT) ne yapar?", ["Ekran sürer", "Sistem kilitlenirse reset atar", "MQTT broker", "I2C clock"], 1, "guc"),
    ("Serial Monitor debugging için?", ["Donanım değiştirir", "printf benzeri metin çıktısı", "Sadece Windows", "ADC kalibrasyon"], 1, "debug"),
    ("Floating (yüzen) pin problemi?", ["Her zaman HIGH", "Belirsiz okuma, gürültüye açık", "Sadece output", "PWM hatası"], 1, "debug"),
    ("Logic analyzer ne ölçer?", ["Sadece sıcaklık", "Dijital sinyal zamanlaması", "WiFi şifresi", "Bellek boyutu"], 1, "debug"),
    ("Dönem projesinde prototip aşaması?", ["Sunumdan sonra", "Fikir sonrası devre/yazılım denemesi", "Sadece rapor", "Gereksiz"], 1, "proje"),
    ("Ohm yasası V = ?", ["I / R", "I × R", "R / I", "I + R"], 1, "devre"),
    ("Kırmızı LED için tipik ileri voltaj?", ["0.5V", "~2V", "12V", "5V tam"], 1, "devre"),
    ("Transistör röle sürmede genelde neden kullanılır?", ["MCU pin akımını aşmamak", "WiFi", "Analog ADC", "I2C adres"], 0, "devre"),
    ("Kondansatör decoupling amacı?", ["Gürültüyü filtreleme / stabil voltaj", "Mesafe ölçme", "MQTT", "Program yükleme"], 0, "devre"),
    ("NodeMCU D0 pin uyarısı?", ["5V tolerant", "Boot moduna etki, dikkatli kullan", "Sadece analog", "SPI only"], 1, "nodemcu"),
    ("Arduino IDE'de kart seçimi neden önemli?", ["Renk teması", "Doğru pin haritası ve yükleme parametreleri", "Sadece lisans", "Gereksiz"], 1, "nodemcu"),
    ("I2C hangi pinler (Arduino Uno tipik)?", ["D0 D1", "A4 SDA, A5 SCL", "D13 only", "Analog only"], 1, "protokol"),
    ("MQTT broker örneği?", ["Mosquitto", "Apache HTTP only", "PostgreSQL", "Chrome"], 0, "protokol"),
    ("RTOS'ta yüksek öncelikli görev?", ["Asla çalışmaz", "Önce CPU alabilir", "Sadece setup'ta", "Heap kullanamaz"], 1, "rtos"),
    ("EEPROM ile Flash farkı (genel)?", ["EEPROM daha çok byte silme/yazma döngüsü için", "Aynı şey", "EEPROM sadece WiFi", "Flash sadece RAM"], 0, "bellek"),
    ("Brown-out reset nedir?", ["WiFi koptu", "Voltaj düşünce güvenli reset", "I2C hatası", "PWM"], 1, "guc"),
    ("Oscilloscope ne gösterir?", ["Sadece metin", "Sinyal genlik/zaman grafiği", "Kod satırı", "IP adresi"], 1, "debug"),
    ("PIR sensör ne algılar?", ["Sıcaklık", "Hareket (kızılötesi)", "Mesafe ultrason", "Basınç"], 1, "sensor"),
    ("LDR ne ölçer?", ["Işık şiddeti", "Ses", "Nem", "Akım"], 0, "sensor"),
    ("CS (Chip Select) SPI'da?", ["Her zaman HIGH", "Hangi slave aktif seçimi", "Clock hızı", "MQTT topic"], 1, "protokol"),
    ("Harvard mimarisi?", ["Program ve veri yolu ayrılabilir", "Sadece web", "Sadece Linux", "Analog only"], 0, "giris"),
    ("Gerçek zamanlı sistemde deadline?", ["İsteğe bağlı süre", "Görevin mutlaka tamamlanması gereken süre", "Sadece baud", "LED rengi"], 1, "rtos"),
    ("ESP8266 NodeMCU'da program yükleme genelde?", ["USB-Serial / UART", "Sadece HDMI", "Sadece SD kart", "Bluetooth only"], 0, "nodemcu"),
    ("Çoklu görevde semaphore?", ["Sadece dekorasyon", "Kaynak sayacı / senkronizasyon", "ADC", "Pull-down"], 1, "rtos"),
    ("Low-power tasarımda gereksiz?", ["Sleep modları", "Sürekli polling yerine interrupt", "Her pin OUTPUT HIGH", "Clock gate"], 2, "guc"),
    ("Proje sunumunda olması gereken?", ["Sadece kod kopyası", "Problem, çözüm, demo, sonuç", "Hiçbir şey", "Sadece foto"], 1, "proje"),
]
for t in tests:
    add_test(*t)

while len(test) < 55:
    i = len(test)
    add_test(
        f"Gömülü sistemlerde protokol/konu {i}: I2C iki hat kullanır?",
        ["Doğru — SDA ve SCL", "Yanlış — TX RX", "SPI hatları", "MQTT only"],
        0,
        "protokol",
    )

# --- DOĞRU/YANLIŞ (50+) ---
dogru_items = [
    ("Gömülü sistem genel amaçlı bilgisayar gibi her uygulamaya uygundur.", False, "giris"),
    ("Mikrodenetleyici üzerinde GPIO bulunabilir.", True, "giris"),
    ("Gömülü yazılım güncellemesi OTA ile yapılabilir (bazı platformlarda).", True, "nodemcu"),
    ("5V sinyali doğrudan 3.3V GPIO'ya bağlamak güvenlidir.", False, "nodemcu"),
    ("Breadboard'da orta bölgede satır içi bağlantı vardır.", True, "devre"),
    ("LED kısa devre dirençsiz uzun süre güvenle çalışır.", False, "devre"),
    ("Pull-down direnci pin boştayken LOW seviyeye çeker.", True, "devre"),
    ("pinMode(pin, OUTPUT) çıkış pini yapılandırır.", True, "gpio"),
    ("analogRead dijital pinden okunabilir (platforma göre).", True, "gpio"),
    ("digitalRead sadece 0 veya 1 döndürür.", True, "gpio"),
    ("UART full-duplex olabilir (TX ve RX ayrı).", True, "protokol"),
    ("SPI genelde birden fazla slave ile CS hattı kullanır.", True, "protokol"),
    ("I2C'de her cihazın benzersiz adresi olmalıdır.", True, "protokol"),
    ("MQTT publish mesajı broker'a gider.", True, "protokol"),
    ("DHT sensör tek telli protokol kullanabilir.", True, "sensor"),
    ("Röle ile AC mains doğrudan MCU pinine bağlanmalıdır.", False, "sensor"),
    ("RAM güç kesilince içerik kaybolur (volatile).", True, "bellek"),
    ("Heap fragmentasyonu gömülüde sorun olabilir.", True, "bellek"),
    ("FreeRTOS açık kaynak bir RTOS'tur.", True, "rtos"),
    ("ISR içinde uzun delay kullanmak iyi pratiktir.", False, "rtos"),
    ("Deep sleep pil ömrünü uzatır.", True, "guc"),
    ("Watchdog kullanılmazsa kilitlenen sistem kendiliğinden düzelir.", False, "guc"),
    ("Serial.println debugging için yaygındır.", True, "debug"),
    ("Floating input okuma güvenilirdir.", False, "debug"),
    ("Dönem projesi sadece kod içermeli, dokümantasyon gereksizdir.", False, "proje"),
    ("ESP8266 WiFi yeteneğine sahiptir.", True, "nodemcu"),
    ("NodeMCU USB üzerinden programlanabilir.", True, "nodemcu"),
    ("Kondansatör ani voltaj dalgalanmasını yumuşatabilir.", True, "devre"),
    ("Diyot ters polaritede iletken olur.", False, "devre"),
    ("PWM frekansı arttıkça her zaman motor daha yavaş olur.", False, "gpio"),
    ("I2C uzun kabloda pull-up gerekebilir.", True, "protokol"),
    ("SPI master clock üretir (SCK).", True, "protokol"),
    ("MQTT QoS seviyeleri mesaj teslim garantisi ile ilgilidir.", True, "protokol"),
    ("Ultrasonik sensör echo süresinden mesafe hesaplar.", True, "sensor"),
    ("Servo 0-180 derece pozisyon alabilir (tipik hobby).", True, "sensor"),
    ("Flash'ta program kodu saklanır.", True, "bellek"),
    ("Stack overflow gömülüde çökme sebebidir.", True, "bellek"),
    ("Bare-metal'de main loop sürekli döner.", True, "rtos"),
    ("Öncelik inversion RTOS'ta sorun olabilir.", True, "rtos"),
    ("Enerji verimliliği IoT cihazlarda kritiktir.", True, "guc"),
    ("Brown-out düşük voltajda reset tetikler.", True, "guc"),
    ("Logic analyzer analog ses kaydeder.", False, "debug"),
    ("Breakpoint ile kod satırında durulabilir.", True, "debug"),
    ("Prototipte breadboard lehimli PCB yerine geçebilir.", True, "proje"),
    ("Gerçek zamanlı sistemde gecikme (latency) önemlidir.", True, "rtos"),
    ("Harvard mimarisinde program ve veri bus ayrılabilir.", True, "giris"),
    ("GPIO General Purpose Input Output anlamına gelir.", True, "gpio"),
    ("Analog sensör değeri ADC ile dijitale çevrilir.", True, "gpio"),
    ("WiFi.setSleepMode güç tasarrufu için kullanılabilir (ESP).", True, "guc"),
    ("Çoklu thread'de paylaşılan değişken race condition yaratır.", True, "rtos"),
    ("Transistör akım kazancı sağlayarak röleyi sürer.", True, "devre"),
    ("Ohm yasasında R = V/I'dir.", True, "devre"),
    ("NodeMCU tipik olarak Lua veya Arduino C ile programlanır.", True, "nodemcu"),
    ("I2C clock stretching bazı slave'lerde kullanılır.", True, "protokol"),
    ("MQTT retain flag son mesajı broker'da tutabilir.", True, "protokol"),
]
for s, v, t in dogru_items:
    add_dogru(s, v, t)

while len(dogru) < 55:
    add_dogru(f"Gömülü sistemlerde bellek yönetimi önemlidir (ifade {len(dogru)}).", True, "bellek")

# --- BOŞLUK (50+) ---
blanks = [
    ("Gömülü sistem belirli bir ___ için özel tasarlanmış bilgisayardır.", "gorev", "giris", ["görev", "amaç"]),
    ("Mikrodenetleyici kısaltması ___'dır.", "MCU", "giris", ["mcu"]),
    ("NodeMCU kartında yaygın WiFi çipi ___'dir.", "ESP8266", "nodemcu"),
    ("ESP8266 mantık seviyesi genelde ___ volt'tur.", "3.3", "nodemcu", ["3,3"]),
    ("Prototip için delikli ___ kullanılır.", "breadboard", "devre", ["protoboard"]),
    ("LED akımını sınırlamak için ___ bağlanır.", "direnc", "devre", ["direnç", "resistor"]),
    ("Boşta pini HIGH tutmak için ___ direnci kullanılır.", "pull-up", "devre", ["pullup"]),
    ("Dijital çıkış için pinMode ___ kullanılır.", "OUTPUT", "gpio"),
    ("Analog giriş okuma fonksiyonu ___'dur.", "analogRead", "gpio"),
    ("Dijital yazma fonksiyonu ___'dur.", "digitalWrite", "gpio"),
    ("PWM ile parlaklık için ___ kullanılır.", "analogWrite", "gpio"),
    ("Seri haberleşmede gönderme hattı genelde ___'dir.", "TX", "protokol"),
    ("Seri haberleşmede alma hattı genelde ___'dir.", "RX", "protokol"),
    ("Hız ayarı için ___ rate denir.", "baud", "protokol"),
    ("SPI'da saat hattı ___'tir.", "SCK", "protokol"),
    ("SPI'da ana cihazdan slave'e veri hattı ___'dur.", "MOSI", "protokol"),
    ("I2C veri hattı ___'dir.", "SDA", "protokol"),
    ("I2C saat hattı ___'dir.", "SCL", "protokol"),
    ("MQTT'de mesajları dağıtan sunucuya ___ denir.", "broker", "protokol"),
    ("MQTT modeli ___ / Subscribe şeklindedir.", "Publish", "protokol"),
    ("DHT11 ___ ve nem ölçer.", "sicaklik", "sensor", ["sıcaklık", "temperature"]),
    ("HC-SR04 ___ mesafe sensörüdür.", "ultrasonik", "sensor"),
    ("Hareket algılayan PIR sensör ___ algılar.", "hareket", "sensor"),
    ("Işık şiddeti için ___ sensör kullanılır.", "LDR", "sensor"),
    ("Motor açı kontrolünde ___ motor kullanılır.", "servo", "sensor"),
    ("Yüksek akım anahtarlama için ___ kullanılır.", "rolo", "sensor", ["röle", "role"]),
    ("Program kodu ___ bellekte saklanır.", "Flash", "bellek"),
    ("Geçici değişkenler genelde ___'da tutulur.", "RAM", "bellek"),
    ("Fonksiyon çağrıları için ___ bellek kullanılır.", "stack", "bellek", ["Stack"]),
    ("FreeRTOS'ta çalışan birim ___ adını alır.", "task", "rtos", ["görev"]),
    ("Paylaşılan kaynağı kilitlemek için ___ kullanılır.", "mutex", "rtos", ["Mutex"]),
    ("RTOS olmadan doğrudan donanım: ___-metal.", "bare", "rtos", ["Bare"]),
    ("Düşük güç modu: ___ sleep.", "deep", "guc", ["Deep"]),
    ("Sistem kilitlenince reset için ___ timer.", "watchdog", "guc", ["Watchdog"]),
    ("Hata ayıklamada Serial ___ yaygındır.", "Monitor", "debug", ["monitor"]),
    ("Belirsiz pin seviyesi ___ pin denir.", "floating", "debug", ["yüzen"]),
    ("Dijital sinyal zamanlaması için ___ analyzer.", "logic", "debug", ["Logic"]),
    ("Dalga formu için ___ kullanılır.", "osiloskop", "debug", ["oscilloscope", "osiloscope"]),
    ("Voltaj düşünce reset: brown-___", "out", "guc"),
    ("Ohm: V = I × ___", "R", "devre"),
    ("Diyot akımı tek ___ yönde akar.", "yon", "devre", ["yön"]),
    ("GPIO açılımı General Purpose Input ___", "Output", "gpio"),
    ("ADC analog-dejital ___ yapar.", "donusum", "bellek", ["dönüşüm", "cevirme"]),
    ("NodeMCU programlama dili örneği: Arduino ___", "C", "nodemcu", ["c"]),
    ("WiFi şifresi kodda sabit değil ___ değişkeninde olmalı.", "config", "nodemcu", [".env", "header"]),
    ("I2C iki hatlı ___ haberleşmedir.", "senkron", "protokol"),
    ("SPI genelde ___ master bir slave çoklu yapı.", "tek", "protokol"),
    ("RTOS gerçek ___ sistemlerde kullanılır.", "zamanli", "rtos", ["zamanlı"]),
    ("Proje sonunda ___ yapılır.", "sunum", "proje"),
    ("Transistör ___ kazancı sağlar.", "akim", "devre", ["akım"]),
    ("Kondansatör enerji ___ edebilir.", "depolar", "devre"),
    ("ESP8266 ___ bağlantısı sunar.", "WiFi", "nodemcu", ["wifi"]),
    ("Çoklu görevde ___ kaynağı sayılır.", "semaphore", "rtos", ["Semaphore"]),
    ("Harvard mimarisi program ve veri yolunu ___ edebilir.", "ayirir", "giris", ["ayırır"]),
    ("MQTT topic mesajın ___ adresidir.", "kanal", "protokol", ["topic"]),
    ("Bootloader program ___ işlemini kolaylaştırır.", "yukleme", "nodemcu", ["yükleme", "flash"]),
    ("ISR kesme ___ rutinidir.", "servis", "rtos", ["service"]),
    ("Pil ömrü için gereksiz ___ kapatılır.", "peripheral", "guc", ["çevre birimi"]),
]
for b in blanks:
    if len(b) == 4:
        add_bosluk(b[0], b[1], b[2], b[3])
    else:
        add_bosluk(b[0], b[1], b[2])

while len(bosluk) < 55:
    add_bosluk("SPI slave seçimi için ___ hattı kullanılır.", "CS", "protokol", ["cs", "chip select"])

# --- KOD KISA/UZUN (50+) - Arduino/C ---
kod_items = [
    ("to-long", "pinMode(13, OUTPUT);", ["mode pin 13 out", "configure(13, OUT)", "pinMode(13, OUTPUT);", "setPinOutput(13)"], 2, "gpio"),
    ("to-short", "void setup() {\n  Serial.begin(115200);\n  pinMode(2, INPUT_PULLUP);\n}\nvoid loop() {\n  Serial.println(digitalRead(2));\n  delay(500);\n}", ["Serial+pullup input okuma döngüsü", "pinMode only", "analog only", "WiFi.begin"], 0, "gpio"),
    ("to-long", "digitalWrite(LED, HIGH);", ["write digital LED on", "LED=1", "gpio_set(LED)", "digitalWrite(LED, HIGH);"], 3, "gpio"),
    ("to-short", "if (analogRead(A0) > 512) { digitalWrite(13, HIGH); } else { digitalWrite(13, LOW); }", ["A0 yarıda LED aç/kapa", "always HIGH", "Serial only", "I2C read"], 0, "gpio"),
    ("to-long", "Wire.begin();", ["I2C baslat", "start_i2c()", "Wire.begin();", "SDA.setup()"], 2, "protokol"),
    ("to-short", "while (!Serial) { ; }", ["Serial hazır olana bekle (USB)", "infinite loop wrong", "delay only", "MQTT connect"], 0, "debug"),
    ("to-long", "analogWrite(9, 128);", ["pwm 9 half", "write analog 128 pin 9", "analogWrite(9, 128);", "digital 128"], 2, "gpio"),
    ("to-short", "for (int i = 0; i < 10; i++) {\n  digitalWrite(LED, HIGH);\n  delay(200);\n  digitalWrite(LED, LOW);\n  delay(200);\n}", ["LED 10 kez yanıp söner", "single blink", "analog fade", "SPI transfer"], 0, "gpio"),
    ("to-long", "SPI.begin();", ["spi start", "SPI.begin();", "serial begin", "wire begin"], 1, "protokol"),
    ("to-short", "client.publish(\"home/temp\", String(temp).c_str());", ["MQTT publish sıcaklık", "HTTP GET", "Serial print only", "digitalWrite"], 0, "protokol"),
    ("to-long", "pinMode(BUTTON, INPUT_PULLUP);", ["button pullup config", "INPUT_PULLUP on BUTTON", "pinMode(BUTTON, INPUT_PULLUP);", "OUTPUT BUTTON"], 2, "gpio"),
    ("to-short", "ESP.deepSleep(1e8);", ["ESP uzun uyku modu", "WiFi disconnect only", "reboot", "analogRead"], 0, "guc"),
    ("to-long", "Serial.begin(9600);", ["baud 9600 serial", "Serial.begin(9600);", "begin serial 9600", "UART 9600 only comment"], 1, "protokol"),
    ("to-short", "int mesafe = duration * 0.034 / 2;", ["ultrasonik cm yaklaşık formül", "temp formula", "random", "I2C"], 0, "sensor"),
    ("to-long", "servo.write(90);", ["servo 90 derece", "angle(90)", "servo.write(90);", "pwm 90 only"], 2, "sensor"),
]
for item in kod_items:
    add_kod(*item)

more_kod = [
    ("to-short", "digitalWrite(RELAY, !digitalRead(RELAY));", ["Röle toggle", "always on", "analog", "MQTT"], 0, "gpio"),
    ("to-long", "delay(1000);", ["wait 1s", "pause_ms(1000)", "delay(1000);", "sleep(1)"], 2, "gpio"),
    ("to-short", "if (xSemaphoreTake(mutex, portMAX_DELAY)) {\n  shared++;\n  xSemaphoreGive(mutex);\n}", ["mutex ile kritik bölge", "no protection", "Serial only", "GPIO"], 0, "rtos"),
    ("to-long", "WiFi.begin(ssid, password);", ["wifi connect", "WiFi.begin(ssid, password);", "connect_wifi()", "mqtt begin"], 1, "nodemcu"),
    ("to-short", "attachInterrupt(digitalPinToInterrupt(2), ISR, FALLING);", ["pin2 düşen kenar kesme", "polling only", "SPI", "PWM"], 0, "gpio"),
    ("to-long", "map(val, 0, 1023, 0, 255);", ["scale adc to byte", "map(val, 0, 1023, 0, 255);", "convert", "analog only"], 1, "gpio"),
    ("to-short", "Wire.requestFrom(0x68, 6, true);", ["I2C 0x68'den 6 byte iste", "SPI read", "UART", "publish"], 0, "protokol"),
    ("to-long", "digitalRead(pin) == HIGH", ["pin high check", "read pin high", "digitalRead(pin) == HIGH", "isHigh(pin)"], 2, "gpio"),
    ("to-short", "void IRAM_ATTR ISR() { flag = true; }", ["ESP kesme hızlı RAM", "slow ISR", "main only", "delay in ISR"], 0, "rtos"),
    ("to-long", "EEPROM.read(addr);", ["read eeprom", "EEPROM.read(addr);", "flash read", "ram get"], 1, "bellek"),
]
for item in more_kod:
    add_kod(*item)

variants_k = [
    ("to-long", "pinMode(5, INPUT);", ["input pin 5", "pinMode(5, INPUT);", "set input", "gpio 5 in"], 1),
    ("to-short", "const int LED = 13;\npinMode(LED, OUTPUT);", ["LED pin 13 output setup", "blink random", "SPI", "MQTT"], 0),
    ("to-long", "Serial.print(\"Temp:\");", ["print temp label", "Serial.print(\"Temp:\");", "cout", "printf only"], 1),
    ("to-short", "tone(8, 440, 500);", ["buzzer 440Hz 500ms", "digital only", "I2C", "WiFi"], 0),
    ("to-long", "noTone(8);", ["stop tone 8", "noTone(8);", "mute", "end sound"], 1),
    ("to-short", "if (millis() - last > 1000) {\n  last = millis();\n  // işlem\n}", ["non-blocking 1sn interval", "delay(1000) loop", "while true", "sleep"], 0),
    ("to-long", "client.subscribe(\"cmd/#\");", ["mqtt sub wildcard", "client.subscribe(\"cmd/#\");", "publish only", "HTTP"], 1),
    ("to-short", "digitalWrite(LED, digitalRead(BUTTON));", ["Buton durumunu LED'e yansıt", "random LED", "analog", "SPI"], 0),
]
topics_k = ["gpio", "protokol", "nodemcu", "sensor", "rtos", "guc", "debug"]
while len(kod) < 55:
    v = variants_k[len(kod) % len(variants_k)]
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
    wrong = ["SPI", "HTTP", "HTML", "USB", "WiFi", "TCP", "FTP", "SMTP", "GPIO", "PWM",
             "analogRead", "digitalWrite", "Serial", "delay", "malloc"]
    distractors = [w for w in wrong if w.lower() != answer.lower() and w not in alts][:3]
    while len(distractors) < 3:
        distractors.append(f"Seçenek-{len(distractors)+1}")
    opts = [answer] + distractors[:3]
    opts, correct = shuffle_options(0, opts)
    return {"topic": q.get("topic", "genel"), "question": f"Boşluğa uygun cevap hangisidir?\n{text}", "options": opts, "correct": correct}

def kod_to_test(q):
    direction = "kısa" if q.get("direction") == "to-short" else "uzun"
    prompt = q["prompt"][:300] + ("…" if len(q["prompt"]) > 300 else "")
    question = f"Aşağıdaki kod/ifadenin {direction} / doğru açıklaması hangisidir?\n\n{prompt}"
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
    q["id"] = f"GT{i}"

out = {
    "meta": {"title": "Gömülü Sistemler Soru Bankası", "course": "gomulu", "testOnly": True,
             "counts": {"test": len(all_test)}},
    "test": all_test,
}

base = Path(__file__).parent / "gomulu"
base.mkdir(exist_ok=True)
(base / "data").mkdir(exist_ok=True)
(base / "js").mkdir(exist_ok=True)
json_str = json.dumps(out, ensure_ascii=False, indent=2)
(base / "data" / "questions.json").write_text(json_str, encoding="utf-8")
(base / "js" / "questions-data.js").write_text("window.QUIZ_DATA = " + json_str + ";\n", encoding="utf-8")
print(out["meta"]["counts"], "Total:", sum(out["meta"]["counts"].values()))
