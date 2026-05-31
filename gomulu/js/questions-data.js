window.QUIZ_DATA = {
  "meta": {
    "title": "Gömülü Sistemler Soru Bankası",
    "course": "gomulu",
    "testOnly": true,
    "counts": {
      "test": 223
    }
  },
  "test": [
    {
      "topic": "giris",
      "question": "Gömülü sistem tanımı aşağıdakilerden hangisine en uygundur?",
      "options": [
        "Genel amaçlı masaüstü PC",
        "Belirli görev için tasarlanmış gömülü bilgisayar",
        "Sadece web sunucusu",
        "Bulut veri merkezi"
      ],
      "correct": 1,
      "id": "GT1"
    },
    {
      "topic": "giris",
      "question": "Mikrodenetleyici (MCU) ile mikroişlemci (MPU) farkında MCU'da genelde ne bulunur?",
      "options": [
        "Sadece CPU, bellek harici",
        "CPU + RAM/Flash + çevre birimi tek çipte",
        "Sadece GPU",
        "İşletim sistemi zorunlu değil"
      ],
      "correct": 1,
      "id": "GT2"
    },
    {
      "topic": "giris",
      "question": "Gömülü sistemlerde en kritik kısıtlardan biri değildir?",
      "options": [
        "Gerçek zamanlılık",
        "Düşük güç tüketimi",
        "Sınırlı bellek",
        "4K oyun grafikleri"
      ],
      "correct": 3,
      "id": "GT3"
    },
    {
      "topic": "giris",
      "question": "Firmware nedir?",
      "options": [
        "Donanımın fiziksel devresi",
        "Cihaza gömülü kalıcı yazılım",
        "İnternet tarayıcısı",
        "Veritabanı şeması"
      ],
      "correct": 1,
      "id": "GT4"
    },
    {
      "topic": "nodemcu",
      "question": "NodeMCU kartı hangi WiFi çipini temel alır?",
      "options": [
        "ESP32",
        "ESP8266",
        "Arduino Uno",
        "Raspberry Pi"
      ],
      "correct": 1,
      "id": "GT5"
    },
    {
      "topic": "nodemcu",
      "question": "ESP8266 mantık seviyesi genelde kaç volttur?",
      "options": [
        "5V",
        "3.3V",
        "12V",
        "1.8V only"
      ],
      "correct": 1,
      "id": "GT6"
    },
    {
      "topic": "devre",
      "question": "Breadboard üzerinde delikler nasıl bağlanır?",
      "options": [
        "Hepsi seri",
        "Satırlar kısa devre (power rail hariç kurallara göre)",
        "Hiç bağlanmaz",
        "Sadece dikey"
      ],
      "correct": 1,
      "id": "GT7"
    },
    {
      "topic": "devre",
      "question": "LED'e direnç konulmasının ana nedeni?",
      "options": [
        "LED'i parlak yapmak",
        "Akımı sınırlayıp LED'i korumak",
        "Voltajı artırmak",
        "PWM için"
      ],
      "correct": 1,
      "id": "GT8"
    },
    {
      "topic": "devre",
      "question": "Pull-up direnci ne işe yarar?",
      "options": [
        "Floating pini belirli seviyede tutmak",
        "Motor hızlandırmak",
        "WiFi güçlendirmek",
        "ADC çözünürlüğü"
      ],
      "correct": 0,
      "id": "GT9"
    },
    {
      "topic": "gpio",
      "question": "digitalWrite(pin, HIGH) ne yapar?",
      "options": [
        "Pini analog okur",
        "Dijital çıkışı lojik 1 yapar",
        "Pini input yapar",
        "Serial başlatır"
      ],
      "correct": 1,
      "id": "GT10"
    },
    {
      "topic": "gpio",
      "question": "analogRead() Arduino'da kaç bit çözünürlük verir (Uno)?",
      "options": [
        "8 bit (0-255)",
        "10 bit (0-1023)",
        "16 bit",
        "32 bit"
      ],
      "correct": 1,
      "id": "GT11"
    },
    {
      "topic": "gpio",
      "question": "INPUT_PULLUP modu ne sağlar?",
      "options": [
        "Harici pull-up şart",
        "Dahili pull-up ile boşta HIGH",
        "Sadece analog",
        "Motor sürer"
      ],
      "correct": 1,
      "id": "GT12"
    },
    {
      "topic": "gpio",
      "question": "PWM ile ne kontrol edilir?",
      "options": [
        "Dijital sadece 0/1",
        "LED parlaklığı / servo / motor hızı gibi analog benzeri",
        "I2C adresi",
        "Baud rate"
      ],
      "correct": 1,
      "id": "GT13"
    },
    {
      "topic": "protokol",
      "question": "UART haberleşmede kaç hat minimum gereklidir (basit)?",
      "options": [
        "1 TX",
        "TX ve RX",
        "4 MOSI MISO",
        "SDA SCL"
      ],
      "correct": 1,
      "id": "GT14"
    },
    {
      "topic": "protokol",
      "question": "Baud rate nedir?",
      "options": [
        "Veri bit hızı / saniye",
        "CPU frekansı",
        "ADC referansı",
        "Pil voltajı"
      ],
      "correct": 0,
      "id": "GT15"
    },
    {
      "topic": "protokol",
      "question": "SPI'da veri hattı hangileridir?",
      "options": [
        "SDA, SCL",
        "MOSI, MISO, SCK, CS",
        "TX, RX",
        "VCC, GND only"
      ],
      "correct": 1,
      "id": "GT16"
    },
    {
      "topic": "protokol",
      "question": "I2C'de kaç master olabilir (tipik uygulama)?",
      "options": [
        "Sınırsız aynı anda",
        "Birden fazla master nadiren, genelde tek master",
        "Hiç master yok",
        "Sadece slave"
      ],
      "correct": 1,
      "id": "GT17"
    },
    {
      "topic": "protokol",
      "question": "MQTT'de mesaj dağıtım modeli?",
      "options": [
        "Peer to peer only",
        "Publish/Subscribe broker üzerinden",
        "HTTP GET only",
        "UDP broadcast only"
      ],
      "correct": 1,
      "id": "GT18"
    },
    {
      "topic": "sensor",
      "question": "DHT11 sensörü ne ölçer?",
      "options": [
        "Sadece basınç",
        "Sıcaklık ve nem",
        "Mesafe",
        "Işık"
      ],
      "correct": 1,
      "id": "GT19"
    },
    {
      "topic": "sensor",
      "question": "HC-SR04 hangi prensiple mesafe ölçer?",
      "options": [
        "Manyetik alan",
        "Ultrasonik yankı süresi",
        "Kızılötesi",
        "GPS"
      ],
      "correct": 1,
      "id": "GT20"
    },
    {
      "topic": "sensor",
      "question": "Servo motor kontrolünde genelde hangi sinyal?",
      "options": [
        "Analog sinüs",
        "PWM darbe genişliği",
        "I2C paket",
        "UART string"
      ],
      "correct": 1,
      "id": "GT21"
    },
    {
      "topic": "sensor",
      "question": "Aktüatör örneği hangisidir?",
      "options": [
        "LDR",
        "DHT11",
        "Röle / motor",
        "Termistör"
      ],
      "correct": 2,
      "id": "GT22"
    },
    {
      "topic": "bellek",
      "question": "Flash bellekte ne saklanır?",
      "options": [
        "Sadece geçici değişken",
        "Program kodu (kalıcı)",
        "Sadece WiFi şifresi",
        "ADC örnekleri"
      ],
      "correct": 1,
      "id": "GT23"
    },
    {
      "topic": "bellek",
      "question": "Stack bellek ne için kullanılır?",
      "options": [
        "Kalıcı dosya",
        "Fonksiyon çağrıları ve yerel değişkenler",
        "Program yükleme",
        "Ekran buffer"
      ],
      "correct": 1,
      "id": "GT24"
    },
    {
      "topic": "rtos",
      "question": "FreeRTOS'ta görev (task) nedir?",
      "options": [
        "Donanım pin",
        "Bağımsız çalışan kod parçası",
        "Sadece ISR",
        "EEPROM adres"
      ],
      "correct": 1,
      "id": "GT25"
    },
    {
      "topic": "rtos",
      "question": "Mutex ne işe yarar?",
      "options": [
        "WiFi bağlantı",
        "Paylaşılan kaynağa tek erişim kilidi",
        "Analog okuma",
        "Serial baud"
      ],
      "correct": 1,
      "id": "GT26"
    },
    {
      "topic": "rtos",
      "question": "Bare-metal sistemde?",
      "options": [
        "Her zaman Linux çalışır",
        "Doğrudan donanım, minimal/RTOS'suz olabilir",
        "Sadece bulut",
        "Tarayıcı gerekir"
      ],
      "correct": 1,
      "id": "GT27"
    },
    {
      "topic": "guc",
      "question": "Deep sleep modunun amacı?",
      "options": [
        "CPU hızlandırmak",
        "Güç tüketimini azaltmak",
        "ADC kapatmak zorunlu değil",
        "WiFi güçlendirmek"
      ],
      "correct": 1,
      "id": "GT28"
    },
    {
      "topic": "guc",
      "question": "Watchdog timer (WDT) ne yapar?",
      "options": [
        "Ekran sürer",
        "Sistem kilitlenirse reset atar",
        "MQTT broker",
        "I2C clock"
      ],
      "correct": 1,
      "id": "GT29"
    },
    {
      "topic": "debug",
      "question": "Serial Monitor debugging için?",
      "options": [
        "Donanım değiştirir",
        "printf benzeri metin çıktısı",
        "Sadece Windows",
        "ADC kalibrasyon"
      ],
      "correct": 1,
      "id": "GT30"
    },
    {
      "topic": "debug",
      "question": "Floating (yüzen) pin problemi?",
      "options": [
        "Her zaman HIGH",
        "Belirsiz okuma, gürültüye açık",
        "Sadece output",
        "PWM hatası"
      ],
      "correct": 1,
      "id": "GT31"
    },
    {
      "topic": "debug",
      "question": "Logic analyzer ne ölçer?",
      "options": [
        "Sadece sıcaklık",
        "Dijital sinyal zamanlaması",
        "WiFi şifresi",
        "Bellek boyutu"
      ],
      "correct": 1,
      "id": "GT32"
    },
    {
      "topic": "proje",
      "question": "Dönem projesinde prototip aşaması?",
      "options": [
        "Sunumdan sonra",
        "Fikir sonrası devre/yazılım denemesi",
        "Sadece rapor",
        "Gereksiz"
      ],
      "correct": 1,
      "id": "GT33"
    },
    {
      "topic": "devre",
      "question": "Ohm yasası V = ?",
      "options": [
        "I / R",
        "I × R",
        "R / I",
        "I + R"
      ],
      "correct": 1,
      "id": "GT34"
    },
    {
      "topic": "devre",
      "question": "Kırmızı LED için tipik ileri voltaj?",
      "options": [
        "0.5V",
        "~2V",
        "12V",
        "5V tam"
      ],
      "correct": 1,
      "id": "GT35"
    },
    {
      "topic": "devre",
      "question": "Transistör röle sürmede genelde neden kullanılır?",
      "options": [
        "MCU pin akımını aşmamak",
        "WiFi",
        "Analog ADC",
        "I2C adres"
      ],
      "correct": 0,
      "id": "GT36"
    },
    {
      "topic": "devre",
      "question": "Kondansatör decoupling amacı?",
      "options": [
        "Gürültüyü filtreleme / stabil voltaj",
        "Mesafe ölçme",
        "MQTT",
        "Program yükleme"
      ],
      "correct": 0,
      "id": "GT37"
    },
    {
      "topic": "nodemcu",
      "question": "NodeMCU D0 pin uyarısı?",
      "options": [
        "5V tolerant",
        "Boot moduna etki, dikkatli kullan",
        "Sadece analog",
        "SPI only"
      ],
      "correct": 1,
      "id": "GT38"
    },
    {
      "topic": "nodemcu",
      "question": "Arduino IDE'de kart seçimi neden önemli?",
      "options": [
        "Renk teması",
        "Doğru pin haritası ve yükleme parametreleri",
        "Sadece lisans",
        "Gereksiz"
      ],
      "correct": 1,
      "id": "GT39"
    },
    {
      "topic": "protokol",
      "question": "I2C hangi pinler (Arduino Uno tipik)?",
      "options": [
        "D0 D1",
        "A4 SDA, A5 SCL",
        "D13 only",
        "Analog only"
      ],
      "correct": 1,
      "id": "GT40"
    },
    {
      "topic": "protokol",
      "question": "MQTT broker örneği?",
      "options": [
        "Mosquitto",
        "Apache HTTP only",
        "PostgreSQL",
        "Chrome"
      ],
      "correct": 0,
      "id": "GT41"
    },
    {
      "topic": "rtos",
      "question": "RTOS'ta yüksek öncelikli görev?",
      "options": [
        "Asla çalışmaz",
        "Önce CPU alabilir",
        "Sadece setup'ta",
        "Heap kullanamaz"
      ],
      "correct": 1,
      "id": "GT42"
    },
    {
      "topic": "bellek",
      "question": "EEPROM ile Flash farkı (genel)?",
      "options": [
        "EEPROM daha çok byte silme/yazma döngüsü için",
        "Aynı şey",
        "EEPROM sadece WiFi",
        "Flash sadece RAM"
      ],
      "correct": 0,
      "id": "GT43"
    },
    {
      "topic": "guc",
      "question": "Brown-out reset nedir?",
      "options": [
        "WiFi koptu",
        "Voltaj düşünce güvenli reset",
        "I2C hatası",
        "PWM"
      ],
      "correct": 1,
      "id": "GT44"
    },
    {
      "topic": "debug",
      "question": "Oscilloscope ne gösterir?",
      "options": [
        "Sadece metin",
        "Sinyal genlik/zaman grafiği",
        "Kod satırı",
        "IP adresi"
      ],
      "correct": 1,
      "id": "GT45"
    },
    {
      "topic": "sensor",
      "question": "PIR sensör ne algılar?",
      "options": [
        "Sıcaklık",
        "Hareket (kızılötesi)",
        "Mesafe ultrason",
        "Basınç"
      ],
      "correct": 1,
      "id": "GT46"
    },
    {
      "topic": "sensor",
      "question": "LDR ne ölçer?",
      "options": [
        "Işık şiddeti",
        "Ses",
        "Nem",
        "Akım"
      ],
      "correct": 0,
      "id": "GT47"
    },
    {
      "topic": "protokol",
      "question": "CS (Chip Select) SPI'da?",
      "options": [
        "Her zaman HIGH",
        "Hangi slave aktif seçimi",
        "Clock hızı",
        "MQTT topic"
      ],
      "correct": 1,
      "id": "GT48"
    },
    {
      "topic": "giris",
      "question": "Harvard mimarisi?",
      "options": [
        "Program ve veri yolu ayrılabilir",
        "Sadece web",
        "Sadece Linux",
        "Analog only"
      ],
      "correct": 0,
      "id": "GT49"
    },
    {
      "topic": "rtos",
      "question": "Gerçek zamanlı sistemde deadline?",
      "options": [
        "İsteğe bağlı süre",
        "Görevin mutlaka tamamlanması gereken süre",
        "Sadece baud",
        "LED rengi"
      ],
      "correct": 1,
      "id": "GT50"
    },
    {
      "topic": "nodemcu",
      "question": "ESP8266 NodeMCU'da program yükleme genelde?",
      "options": [
        "USB-Serial / UART",
        "Sadece HDMI",
        "Sadece SD kart",
        "Bluetooth only"
      ],
      "correct": 0,
      "id": "GT51"
    },
    {
      "topic": "rtos",
      "question": "Çoklu görevde semaphore?",
      "options": [
        "Sadece dekorasyon",
        "Kaynak sayacı / senkronizasyon",
        "ADC",
        "Pull-down"
      ],
      "correct": 1,
      "id": "GT52"
    },
    {
      "topic": "guc",
      "question": "Low-power tasarımda gereksiz?",
      "options": [
        "Sleep modları",
        "Sürekli polling yerine interrupt",
        "Her pin OUTPUT HIGH",
        "Clock gate"
      ],
      "correct": 2,
      "id": "GT53"
    },
    {
      "topic": "proje",
      "question": "Proje sunumunda olması gereken?",
      "options": [
        "Sadece kod kopyası",
        "Problem, çözüm, demo, sonuç",
        "Hiçbir şey",
        "Sadece foto"
      ],
      "correct": 1,
      "id": "GT54"
    },
    {
      "topic": "protokol",
      "question": "Gömülü sistemlerde protokol/konu 54: I2C iki hat kullanır?",
      "options": [
        "Doğru — SDA ve SCL",
        "Yanlış — TX RX",
        "SPI hatları",
        "MQTT only"
      ],
      "correct": 0,
      "id": "GT55"
    },
    {
      "topic": "giris",
      "question": "Aşağıdaki ifade doğru mudur?\n«Gömülü sistem genel amaçlı bilgisayar gibi her uygulamaya uygundur.»",
      "options": [
        "Sadece bazı durumlarda doğru",
        "Hayır, ifade yanlıştır",
        "Ders notlarında geçmiyor",
        "Evet, ifade doğrudur"
      ],
      "correct": 1,
      "id": "GT56"
    },
    {
      "topic": "giris",
      "question": "Aşağıdaki ifade doğru mudur?\n«Mikrodenetleyici üzerinde GPIO bulunabilir.»",
      "options": [
        "Ders notlarında geçmiyor",
        "Sadece bazı durumlarda doğru",
        "Evet, ifade doğrudur",
        "Hayır, ifade yanlıştır"
      ],
      "correct": 2,
      "id": "GT57"
    },
    {
      "topic": "nodemcu",
      "question": "Aşağıdaki ifade doğru mudur?\n«Gömülü yazılım güncellemesi OTA ile yapılabilir (bazı platformlarda).»",
      "options": [
        "Hayır, ifade yanlıştır",
        "Ders notlarında geçmiyor",
        "Sadece bazı durumlarda doğru",
        "Evet, ifade doğrudur"
      ],
      "correct": 3,
      "id": "GT58"
    },
    {
      "topic": "nodemcu",
      "question": "Aşağıdaki ifade doğru mudur?\n«5V sinyali doğrudan 3.3V GPIO'ya bağlamak güvenlidir.»",
      "options": [
        "Hayır, ifade yanlıştır",
        "Sadece bazı durumlarda doğru",
        "Evet, ifade doğrudur",
        "Ders notlarında geçmiyor"
      ],
      "correct": 0,
      "id": "GT59"
    },
    {
      "topic": "devre",
      "question": "Aşağıdaki ifade doğru mudur?\n«Breadboard'da orta bölgede satır içi bağlantı vardır.»",
      "options": [
        "Hayır, ifade yanlıştır",
        "Sadece bazı durumlarda doğru",
        "Ders notlarında geçmiyor",
        "Evet, ifade doğrudur"
      ],
      "correct": 3,
      "id": "GT60"
    },
    {
      "topic": "devre",
      "question": "Aşağıdaki ifade doğru mudur?\n«LED kısa devre dirençsiz uzun süre güvenle çalışır.»",
      "options": [
        "Hayır, ifade yanlıştır",
        "Ders notlarında geçmiyor",
        "Sadece bazı durumlarda doğru",
        "Evet, ifade doğrudur"
      ],
      "correct": 0,
      "id": "GT61"
    },
    {
      "topic": "devre",
      "question": "Aşağıdaki ifade doğru mudur?\n«Pull-down direnci pin boştayken LOW seviyeye çeker.»",
      "options": [
        "Sadece bazı durumlarda doğru",
        "Hayır, ifade yanlıştır",
        "Evet, ifade doğrudur",
        "Ders notlarında geçmiyor"
      ],
      "correct": 2,
      "id": "GT62"
    },
    {
      "topic": "gpio",
      "question": "Aşağıdaki ifade doğru mudur?\n«pinMode(pin, OUTPUT) çıkış pini yapılandırır.»",
      "options": [
        "Hayır, ifade yanlıştır",
        "Ders notlarında geçmiyor",
        "Evet, ifade doğrudur",
        "Sadece bazı durumlarda doğru"
      ],
      "correct": 2,
      "id": "GT63"
    },
    {
      "topic": "gpio",
      "question": "Aşağıdaki ifade doğru mudur?\n«analogRead dijital pinden okunabilir (platforma göre).»",
      "options": [
        "Evet, ifade doğrudur",
        "Sadece bazı durumlarda doğru",
        "Hayır, ifade yanlıştır",
        "Ders notlarında geçmiyor"
      ],
      "correct": 0,
      "id": "GT64"
    },
    {
      "topic": "gpio",
      "question": "Aşağıdaki ifade doğru mudur?\n«digitalRead sadece 0 veya 1 döndürür.»",
      "options": [
        "Sadece bazı durumlarda doğru",
        "Ders notlarında geçmiyor",
        "Evet, ifade doğrudur",
        "Hayır, ifade yanlıştır"
      ],
      "correct": 2,
      "id": "GT65"
    },
    {
      "topic": "protokol",
      "question": "Aşağıdaki ifade doğru mudur?\n«UART full-duplex olabilir (TX ve RX ayrı).»",
      "options": [
        "Sadece bazı durumlarda doğru",
        "Hayır, ifade yanlıştır",
        "Ders notlarında geçmiyor",
        "Evet, ifade doğrudur"
      ],
      "correct": 3,
      "id": "GT66"
    },
    {
      "topic": "protokol",
      "question": "Aşağıdaki ifade doğru mudur?\n«SPI genelde birden fazla slave ile CS hattı kullanır.»",
      "options": [
        "Ders notlarında geçmiyor",
        "Sadece bazı durumlarda doğru",
        "Hayır, ifade yanlıştır",
        "Evet, ifade doğrudur"
      ],
      "correct": 3,
      "id": "GT67"
    },
    {
      "topic": "protokol",
      "question": "Aşağıdaki ifade doğru mudur?\n«I2C'de her cihazın benzersiz adresi olmalıdır.»",
      "options": [
        "Ders notlarında geçmiyor",
        "Hayır, ifade yanlıştır",
        "Evet, ifade doğrudur",
        "Sadece bazı durumlarda doğru"
      ],
      "correct": 2,
      "id": "GT68"
    },
    {
      "topic": "protokol",
      "question": "Aşağıdaki ifade doğru mudur?\n«MQTT publish mesajı broker'a gider.»",
      "options": [
        "Sadece bazı durumlarda doğru",
        "Ders notlarında geçmiyor",
        "Hayır, ifade yanlıştır",
        "Evet, ifade doğrudur"
      ],
      "correct": 3,
      "id": "GT69"
    },
    {
      "topic": "sensor",
      "question": "Aşağıdaki ifade doğru mudur?\n«DHT sensör tek telli protokol kullanabilir.»",
      "options": [
        "Evet, ifade doğrudur",
        "Hayır, ifade yanlıştır",
        "Ders notlarında geçmiyor",
        "Sadece bazı durumlarda doğru"
      ],
      "correct": 0,
      "id": "GT70"
    },
    {
      "topic": "sensor",
      "question": "Aşağıdaki ifade doğru mudur?\n«Röle ile AC mains doğrudan MCU pinine bağlanmalıdır.»",
      "options": [
        "Ders notlarında geçmiyor",
        "Evet, ifade doğrudur",
        "Sadece bazı durumlarda doğru",
        "Hayır, ifade yanlıştır"
      ],
      "correct": 3,
      "id": "GT71"
    },
    {
      "topic": "bellek",
      "question": "Aşağıdaki ifade doğru mudur?\n«RAM güç kesilince içerik kaybolur (volatile).»",
      "options": [
        "Hayır, ifade yanlıştır",
        "Ders notlarında geçmiyor",
        "Sadece bazı durumlarda doğru",
        "Evet, ifade doğrudur"
      ],
      "correct": 3,
      "id": "GT72"
    },
    {
      "topic": "bellek",
      "question": "Aşağıdaki ifade doğru mudur?\n«Heap fragmentasyonu gömülüde sorun olabilir.»",
      "options": [
        "Hayır, ifade yanlıştır",
        "Ders notlarında geçmiyor",
        "Evet, ifade doğrudur",
        "Sadece bazı durumlarda doğru"
      ],
      "correct": 2,
      "id": "GT73"
    },
    {
      "topic": "rtos",
      "question": "Aşağıdaki ifade doğru mudur?\n«FreeRTOS açık kaynak bir RTOS'tur.»",
      "options": [
        "Ders notlarında geçmiyor",
        "Sadece bazı durumlarda doğru",
        "Hayır, ifade yanlıştır",
        "Evet, ifade doğrudur"
      ],
      "correct": 3,
      "id": "GT74"
    },
    {
      "topic": "rtos",
      "question": "Aşağıdaki ifade doğru mudur?\n«ISR içinde uzun delay kullanmak iyi pratiktir.»",
      "options": [
        "Evet, ifade doğrudur",
        "Hayır, ifade yanlıştır",
        "Sadece bazı durumlarda doğru",
        "Ders notlarında geçmiyor"
      ],
      "correct": 1,
      "id": "GT75"
    },
    {
      "topic": "guc",
      "question": "Aşağıdaki ifade doğru mudur?\n«Deep sleep pil ömrünü uzatır.»",
      "options": [
        "Evet, ifade doğrudur",
        "Sadece bazı durumlarda doğru",
        "Ders notlarında geçmiyor",
        "Hayır, ifade yanlıştır"
      ],
      "correct": 0,
      "id": "GT76"
    },
    {
      "topic": "guc",
      "question": "Aşağıdaki ifade doğru mudur?\n«Watchdog kullanılmazsa kilitlenen sistem kendiliğinden düzelir.»",
      "options": [
        "Evet, ifade doğrudur",
        "Ders notlarında geçmiyor",
        "Sadece bazı durumlarda doğru",
        "Hayır, ifade yanlıştır"
      ],
      "correct": 3,
      "id": "GT77"
    },
    {
      "topic": "debug",
      "question": "Aşağıdaki ifade doğru mudur?\n«Serial.println debugging için yaygındır.»",
      "options": [
        "Hayır, ifade yanlıştır",
        "Ders notlarında geçmiyor",
        "Sadece bazı durumlarda doğru",
        "Evet, ifade doğrudur"
      ],
      "correct": 3,
      "id": "GT78"
    },
    {
      "topic": "debug",
      "question": "Aşağıdaki ifade doğru mudur?\n«Floating input okuma güvenilirdir.»",
      "options": [
        "Sadece bazı durumlarda doğru",
        "Ders notlarında geçmiyor",
        "Evet, ifade doğrudur",
        "Hayır, ifade yanlıştır"
      ],
      "correct": 3,
      "id": "GT79"
    },
    {
      "topic": "proje",
      "question": "Aşağıdaki ifade doğru mudur?\n«Dönem projesi sadece kod içermeli, dokümantasyon gereksizdir.»",
      "options": [
        "Sadece bazı durumlarda doğru",
        "Evet, ifade doğrudur",
        "Hayır, ifade yanlıştır",
        "Ders notlarında geçmiyor"
      ],
      "correct": 2,
      "id": "GT80"
    },
    {
      "topic": "nodemcu",
      "question": "Aşağıdaki ifade doğru mudur?\n«ESP8266 WiFi yeteneğine sahiptir.»",
      "options": [
        "Hayır, ifade yanlıştır",
        "Ders notlarında geçmiyor",
        "Evet, ifade doğrudur",
        "Sadece bazı durumlarda doğru"
      ],
      "correct": 2,
      "id": "GT81"
    },
    {
      "topic": "nodemcu",
      "question": "Aşağıdaki ifade doğru mudur?\n«NodeMCU USB üzerinden programlanabilir.»",
      "options": [
        "Ders notlarında geçmiyor",
        "Sadece bazı durumlarda doğru",
        "Hayır, ifade yanlıştır",
        "Evet, ifade doğrudur"
      ],
      "correct": 3,
      "id": "GT82"
    },
    {
      "topic": "devre",
      "question": "Aşağıdaki ifade doğru mudur?\n«Kondansatör ani voltaj dalgalanmasını yumuşatabilir.»",
      "options": [
        "Hayır, ifade yanlıştır",
        "Ders notlarında geçmiyor",
        "Evet, ifade doğrudur",
        "Sadece bazı durumlarda doğru"
      ],
      "correct": 2,
      "id": "GT83"
    },
    {
      "topic": "devre",
      "question": "Aşağıdaki ifade doğru mudur?\n«Diyot ters polaritede iletken olur.»",
      "options": [
        "Ders notlarında geçmiyor",
        "Hayır, ifade yanlıştır",
        "Evet, ifade doğrudur",
        "Sadece bazı durumlarda doğru"
      ],
      "correct": 1,
      "id": "GT84"
    },
    {
      "topic": "gpio",
      "question": "Aşağıdaki ifade doğru mudur?\n«PWM frekansı arttıkça her zaman motor daha yavaş olur.»",
      "options": [
        "Evet, ifade doğrudur",
        "Hayır, ifade yanlıştır",
        "Sadece bazı durumlarda doğru",
        "Ders notlarında geçmiyor"
      ],
      "correct": 1,
      "id": "GT85"
    },
    {
      "topic": "protokol",
      "question": "Aşağıdaki ifade doğru mudur?\n«I2C uzun kabloda pull-up gerekebilir.»",
      "options": [
        "Sadece bazı durumlarda doğru",
        "Evet, ifade doğrudur",
        "Ders notlarında geçmiyor",
        "Hayır, ifade yanlıştır"
      ],
      "correct": 1,
      "id": "GT86"
    },
    {
      "topic": "protokol",
      "question": "Aşağıdaki ifade doğru mudur?\n«SPI master clock üretir (SCK).»",
      "options": [
        "Evet, ifade doğrudur",
        "Ders notlarında geçmiyor",
        "Sadece bazı durumlarda doğru",
        "Hayır, ifade yanlıştır"
      ],
      "correct": 0,
      "id": "GT87"
    },
    {
      "topic": "protokol",
      "question": "Aşağıdaki ifade doğru mudur?\n«MQTT QoS seviyeleri mesaj teslim garantisi ile ilgilidir.»",
      "options": [
        "Evet, ifade doğrudur",
        "Hayır, ifade yanlıştır",
        "Sadece bazı durumlarda doğru",
        "Ders notlarında geçmiyor"
      ],
      "correct": 0,
      "id": "GT88"
    },
    {
      "topic": "sensor",
      "question": "Aşağıdaki ifade doğru mudur?\n«Ultrasonik sensör echo süresinden mesafe hesaplar.»",
      "options": [
        "Hayır, ifade yanlıştır",
        "Ders notlarında geçmiyor",
        "Evet, ifade doğrudur",
        "Sadece bazı durumlarda doğru"
      ],
      "correct": 2,
      "id": "GT89"
    },
    {
      "topic": "sensor",
      "question": "Aşağıdaki ifade doğru mudur?\n«Servo 0-180 derece pozisyon alabilir (tipik hobby).»",
      "options": [
        "Hayır, ifade yanlıştır",
        "Sadece bazı durumlarda doğru",
        "Evet, ifade doğrudur",
        "Ders notlarında geçmiyor"
      ],
      "correct": 2,
      "id": "GT90"
    },
    {
      "topic": "bellek",
      "question": "Aşağıdaki ifade doğru mudur?\n«Flash'ta program kodu saklanır.»",
      "options": [
        "Hayır, ifade yanlıştır",
        "Sadece bazı durumlarda doğru",
        "Ders notlarında geçmiyor",
        "Evet, ifade doğrudur"
      ],
      "correct": 3,
      "id": "GT91"
    },
    {
      "topic": "bellek",
      "question": "Aşağıdaki ifade doğru mudur?\n«Stack overflow gömülüde çökme sebebidir.»",
      "options": [
        "Hayır, ifade yanlıştır",
        "Evet, ifade doğrudur",
        "Sadece bazı durumlarda doğru",
        "Ders notlarında geçmiyor"
      ],
      "correct": 1,
      "id": "GT92"
    },
    {
      "topic": "rtos",
      "question": "Aşağıdaki ifade doğru mudur?\n«Bare-metal'de main loop sürekli döner.»",
      "options": [
        "Evet, ifade doğrudur",
        "Sadece bazı durumlarda doğru",
        "Hayır, ifade yanlıştır",
        "Ders notlarında geçmiyor"
      ],
      "correct": 0,
      "id": "GT93"
    },
    {
      "topic": "rtos",
      "question": "Aşağıdaki ifade doğru mudur?\n«Öncelik inversion RTOS'ta sorun olabilir.»",
      "options": [
        "Hayır, ifade yanlıştır",
        "Evet, ifade doğrudur",
        "Ders notlarında geçmiyor",
        "Sadece bazı durumlarda doğru"
      ],
      "correct": 1,
      "id": "GT94"
    },
    {
      "topic": "guc",
      "question": "Aşağıdaki ifade doğru mudur?\n«Enerji verimliliği IoT cihazlarda kritiktir.»",
      "options": [
        "Ders notlarında geçmiyor",
        "Hayır, ifade yanlıştır",
        "Sadece bazı durumlarda doğru",
        "Evet, ifade doğrudur"
      ],
      "correct": 3,
      "id": "GT95"
    },
    {
      "topic": "guc",
      "question": "Aşağıdaki ifade doğru mudur?\n«Brown-out düşük voltajda reset tetikler.»",
      "options": [
        "Ders notlarında geçmiyor",
        "Hayır, ifade yanlıştır",
        "Evet, ifade doğrudur",
        "Sadece bazı durumlarda doğru"
      ],
      "correct": 2,
      "id": "GT96"
    },
    {
      "topic": "debug",
      "question": "Aşağıdaki ifade doğru mudur?\n«Logic analyzer analog ses kaydeder.»",
      "options": [
        "Sadece bazı durumlarda doğru",
        "Hayır, ifade yanlıştır",
        "Evet, ifade doğrudur",
        "Ders notlarında geçmiyor"
      ],
      "correct": 1,
      "id": "GT97"
    },
    {
      "topic": "debug",
      "question": "Aşağıdaki ifade doğru mudur?\n«Breakpoint ile kod satırında durulabilir.»",
      "options": [
        "Ders notlarında geçmiyor",
        "Hayır, ifade yanlıştır",
        "Sadece bazı durumlarda doğru",
        "Evet, ifade doğrudur"
      ],
      "correct": 3,
      "id": "GT98"
    },
    {
      "topic": "proje",
      "question": "Aşağıdaki ifade doğru mudur?\n«Prototipte breadboard lehimli PCB yerine geçebilir.»",
      "options": [
        "Ders notlarında geçmiyor",
        "Evet, ifade doğrudur",
        "Sadece bazı durumlarda doğru",
        "Hayır, ifade yanlıştır"
      ],
      "correct": 1,
      "id": "GT99"
    },
    {
      "topic": "rtos",
      "question": "Aşağıdaki ifade doğru mudur?\n«Gerçek zamanlı sistemde gecikme (latency) önemlidir.»",
      "options": [
        "Hayır, ifade yanlıştır",
        "Evet, ifade doğrudur",
        "Ders notlarında geçmiyor",
        "Sadece bazı durumlarda doğru"
      ],
      "correct": 1,
      "id": "GT100"
    },
    {
      "topic": "giris",
      "question": "Aşağıdaki ifade doğru mudur?\n«Harvard mimarisinde program ve veri bus ayrılabilir.»",
      "options": [
        "Sadece bazı durumlarda doğru",
        "Evet, ifade doğrudur",
        "Ders notlarında geçmiyor",
        "Hayır, ifade yanlıştır"
      ],
      "correct": 1,
      "id": "GT101"
    },
    {
      "topic": "gpio",
      "question": "Aşağıdaki ifade doğru mudur?\n«GPIO General Purpose Input Output anlamına gelir.»",
      "options": [
        "Ders notlarında geçmiyor",
        "Hayır, ifade yanlıştır",
        "Sadece bazı durumlarda doğru",
        "Evet, ifade doğrudur"
      ],
      "correct": 3,
      "id": "GT102"
    },
    {
      "topic": "gpio",
      "question": "Aşağıdaki ifade doğru mudur?\n«Analog sensör değeri ADC ile dijitale çevrilir.»",
      "options": [
        "Hayır, ifade yanlıştır",
        "Sadece bazı durumlarda doğru",
        "Evet, ifade doğrudur",
        "Ders notlarında geçmiyor"
      ],
      "correct": 2,
      "id": "GT103"
    },
    {
      "topic": "guc",
      "question": "Aşağıdaki ifade doğru mudur?\n«WiFi.setSleepMode güç tasarrufu için kullanılabilir (ESP).»",
      "options": [
        "Ders notlarında geçmiyor",
        "Evet, ifade doğrudur",
        "Hayır, ifade yanlıştır",
        "Sadece bazı durumlarda doğru"
      ],
      "correct": 1,
      "id": "GT104"
    },
    {
      "topic": "rtos",
      "question": "Aşağıdaki ifade doğru mudur?\n«Çoklu thread'de paylaşılan değişken race condition yaratır.»",
      "options": [
        "Hayır, ifade yanlıştır",
        "Sadece bazı durumlarda doğru",
        "Ders notlarında geçmiyor",
        "Evet, ifade doğrudur"
      ],
      "correct": 3,
      "id": "GT105"
    },
    {
      "topic": "devre",
      "question": "Aşağıdaki ifade doğru mudur?\n«Transistör akım kazancı sağlayarak röleyi sürer.»",
      "options": [
        "Ders notlarında geçmiyor",
        "Hayır, ifade yanlıştır",
        "Sadece bazı durumlarda doğru",
        "Evet, ifade doğrudur"
      ],
      "correct": 3,
      "id": "GT106"
    },
    {
      "topic": "devre",
      "question": "Aşağıdaki ifade doğru mudur?\n«Ohm yasasında R = V/I'dir.»",
      "options": [
        "Hayır, ifade yanlıştır",
        "Ders notlarında geçmiyor",
        "Sadece bazı durumlarda doğru",
        "Evet, ifade doğrudur"
      ],
      "correct": 3,
      "id": "GT107"
    },
    {
      "topic": "nodemcu",
      "question": "Aşağıdaki ifade doğru mudur?\n«NodeMCU tipik olarak Lua veya Arduino C ile programlanır.»",
      "options": [
        "Evet, ifade doğrudur",
        "Ders notlarında geçmiyor",
        "Sadece bazı durumlarda doğru",
        "Hayır, ifade yanlıştır"
      ],
      "correct": 0,
      "id": "GT108"
    },
    {
      "topic": "protokol",
      "question": "Aşağıdaki ifade doğru mudur?\n«I2C clock stretching bazı slave'lerde kullanılır.»",
      "options": [
        "Evet, ifade doğrudur",
        "Sadece bazı durumlarda doğru",
        "Ders notlarında geçmiyor",
        "Hayır, ifade yanlıştır"
      ],
      "correct": 0,
      "id": "GT109"
    },
    {
      "topic": "protokol",
      "question": "Aşağıdaki ifade doğru mudur?\n«MQTT retain flag son mesajı broker'da tutabilir.»",
      "options": [
        "Ders notlarında geçmiyor",
        "Evet, ifade doğrudur",
        "Sadece bazı durumlarda doğru",
        "Hayır, ifade yanlıştır"
      ],
      "correct": 1,
      "id": "GT110"
    },
    {
      "topic": "giris",
      "question": "Boşluğa uygun cevap hangisidir?\nGömülü sistem belirli bir ……… için özel tasarlanmış bilgisayardır.",
      "options": [
        "gorev",
        "HTML",
        "SPI",
        "HTTP"
      ],
      "correct": 0,
      "id": "GT111"
    },
    {
      "topic": "giris",
      "question": "Boşluğa uygun cevap hangisidir?\nMikrodenetleyici kısaltması ………'dır.",
      "options": [
        "MCU",
        "SPI",
        "HTTP",
        "HTML"
      ],
      "correct": 0,
      "id": "GT112"
    },
    {
      "topic": "nodemcu",
      "question": "Boşluğa uygun cevap hangisidir?\nNodeMCU kartında yaygın WiFi çipi ………'dir.",
      "options": [
        "SPI",
        "HTTP",
        "HTML",
        "ESP8266"
      ],
      "correct": 3,
      "id": "GT113"
    },
    {
      "topic": "nodemcu",
      "question": "Boşluğa uygun cevap hangisidir?\nESP8266 mantık seviyesi genelde ……… volt'tur.",
      "options": [
        "HTTP",
        "HTML",
        "SPI",
        "3.3"
      ],
      "correct": 3,
      "id": "GT114"
    },
    {
      "topic": "devre",
      "question": "Boşluğa uygun cevap hangisidir?\nPrototip için delikli ……… kullanılır.",
      "options": [
        "HTML",
        "breadboard",
        "HTTP",
        "SPI"
      ],
      "correct": 1,
      "id": "GT115"
    },
    {
      "topic": "devre",
      "question": "Boşluğa uygun cevap hangisidir?\nLED akımını sınırlamak için ……… bağlanır.",
      "options": [
        "SPI",
        "HTTP",
        "HTML",
        "direnc"
      ],
      "correct": 3,
      "id": "GT116"
    },
    {
      "topic": "devre",
      "question": "Boşluğa uygun cevap hangisidir?\nBoşta pini HIGH tutmak için ……… direnci kullanılır.",
      "options": [
        "HTML",
        "HTTP",
        "pull-up",
        "SPI"
      ],
      "correct": 2,
      "id": "GT117"
    },
    {
      "topic": "gpio",
      "question": "Boşluğa uygun cevap hangisidir?\nDijital çıkış için pinMode ……… kullanılır.",
      "options": [
        "SPI",
        "HTML",
        "OUTPUT",
        "HTTP"
      ],
      "correct": 2,
      "id": "GT118"
    },
    {
      "topic": "gpio",
      "question": "Boşluğa uygun cevap hangisidir?\nAnalog giriş okuma fonksiyonu ………'dur.",
      "options": [
        "analogRead",
        "SPI",
        "HTML",
        "HTTP"
      ],
      "correct": 0,
      "id": "GT119"
    },
    {
      "topic": "gpio",
      "question": "Boşluğa uygun cevap hangisidir?\nDijital yazma fonksiyonu ………'dur.",
      "options": [
        "HTML",
        "digitalWrite",
        "HTTP",
        "SPI"
      ],
      "correct": 1,
      "id": "GT120"
    },
    {
      "topic": "gpio",
      "question": "Boşluğa uygun cevap hangisidir?\nPWM ile parlaklık için ……… kullanılır.",
      "options": [
        "HTTP",
        "SPI",
        "analogWrite",
        "HTML"
      ],
      "correct": 2,
      "id": "GT121"
    },
    {
      "topic": "protokol",
      "question": "Boşluğa uygun cevap hangisidir?\nSeri haberleşmede gönderme hattı genelde ………'dir.",
      "options": [
        "SPI",
        "HTTP",
        "TX",
        "HTML"
      ],
      "correct": 2,
      "id": "GT122"
    },
    {
      "topic": "protokol",
      "question": "Boşluğa uygun cevap hangisidir?\nSeri haberleşmede alma hattı genelde ………'dir.",
      "options": [
        "HTML",
        "SPI",
        "HTTP",
        "RX"
      ],
      "correct": 3,
      "id": "GT123"
    },
    {
      "topic": "protokol",
      "question": "Boşluğa uygun cevap hangisidir?\nHız ayarı için ……… rate denir.",
      "options": [
        "baud",
        "HTML",
        "SPI",
        "HTTP"
      ],
      "correct": 0,
      "id": "GT124"
    },
    {
      "topic": "protokol",
      "question": "Boşluğa uygun cevap hangisidir?\nSPI'da saat hattı ………'tir.",
      "options": [
        "SPI",
        "SCK",
        "HTTP",
        "HTML"
      ],
      "correct": 1,
      "id": "GT125"
    },
    {
      "topic": "protokol",
      "question": "Boşluğa uygun cevap hangisidir?\nSPI'da ana cihazdan slave'e veri hattı ………'dur.",
      "options": [
        "HTTP",
        "SPI",
        "HTML",
        "MOSI"
      ],
      "correct": 3,
      "id": "GT126"
    },
    {
      "topic": "protokol",
      "question": "Boşluğa uygun cevap hangisidir?\nI2C veri hattı ………'dir.",
      "options": [
        "SPI",
        "HTML",
        "SDA",
        "HTTP"
      ],
      "correct": 2,
      "id": "GT127"
    },
    {
      "topic": "protokol",
      "question": "Boşluğa uygun cevap hangisidir?\nI2C saat hattı ………'dir.",
      "options": [
        "HTTP",
        "HTML",
        "SCL",
        "SPI"
      ],
      "correct": 2,
      "id": "GT128"
    },
    {
      "topic": "protokol",
      "question": "Boşluğa uygun cevap hangisidir?\nMQTT'de mesajları dağıtan sunucuya ……… denir.",
      "options": [
        "HTTP",
        "broker",
        "HTML",
        "SPI"
      ],
      "correct": 1,
      "id": "GT129"
    },
    {
      "topic": "protokol",
      "question": "Boşluğa uygun cevap hangisidir?\nMQTT modeli ……… / Subscribe şeklindedir.",
      "options": [
        "HTML",
        "Publish",
        "SPI",
        "HTTP"
      ],
      "correct": 1,
      "id": "GT130"
    },
    {
      "topic": "sensor",
      "question": "Boşluğa uygun cevap hangisidir?\nDHT11 ……… ve nem ölçer.",
      "options": [
        "HTTP",
        "HTML",
        "SPI",
        "sicaklik"
      ],
      "correct": 3,
      "id": "GT131"
    },
    {
      "topic": "sensor",
      "question": "Boşluğa uygun cevap hangisidir?\nHC-SR04 ……… mesafe sensörüdür.",
      "options": [
        "SPI",
        "HTML",
        "HTTP",
        "ultrasonik"
      ],
      "correct": 3,
      "id": "GT132"
    },
    {
      "topic": "sensor",
      "question": "Boşluğa uygun cevap hangisidir?\nHareket algılayan PIR sensör ……… algılar.",
      "options": [
        "SPI",
        "HTTP",
        "HTML",
        "hareket"
      ],
      "correct": 3,
      "id": "GT133"
    },
    {
      "topic": "sensor",
      "question": "Boşluğa uygun cevap hangisidir?\nIşık şiddeti için ……… sensör kullanılır.",
      "options": [
        "LDR",
        "HTTP",
        "SPI",
        "HTML"
      ],
      "correct": 0,
      "id": "GT134"
    },
    {
      "topic": "sensor",
      "question": "Boşluğa uygun cevap hangisidir?\nMotor açı kontrolünde ……… motor kullanılır.",
      "options": [
        "HTTP",
        "servo",
        "HTML",
        "SPI"
      ],
      "correct": 1,
      "id": "GT135"
    },
    {
      "topic": "sensor",
      "question": "Boşluğa uygun cevap hangisidir?\nYüksek akım anahtarlama için ……… kullanılır.",
      "options": [
        "HTTP",
        "rolo",
        "HTML",
        "SPI"
      ],
      "correct": 1,
      "id": "GT136"
    },
    {
      "topic": "bellek",
      "question": "Boşluğa uygun cevap hangisidir?\nProgram kodu ……… bellekte saklanır.",
      "options": [
        "Flash",
        "HTTP",
        "SPI",
        "HTML"
      ],
      "correct": 0,
      "id": "GT137"
    },
    {
      "topic": "bellek",
      "question": "Boşluğa uygun cevap hangisidir?\nGeçici değişkenler genelde ………'da tutulur.",
      "options": [
        "RAM",
        "HTML",
        "SPI",
        "HTTP"
      ],
      "correct": 0,
      "id": "GT138"
    },
    {
      "topic": "bellek",
      "question": "Boşluğa uygun cevap hangisidir?\nFonksiyon çağrıları için ……… bellek kullanılır.",
      "options": [
        "HTTP",
        "HTML",
        "stack",
        "SPI"
      ],
      "correct": 2,
      "id": "GT139"
    },
    {
      "topic": "rtos",
      "question": "Boşluğa uygun cevap hangisidir?\nFreeRTOS'ta çalışan birim ……… adını alır.",
      "options": [
        "HTML",
        "HTTP",
        "task",
        "SPI"
      ],
      "correct": 2,
      "id": "GT140"
    },
    {
      "topic": "rtos",
      "question": "Boşluğa uygun cevap hangisidir?\nPaylaşılan kaynağı kilitlemek için ……… kullanılır.",
      "options": [
        "SPI",
        "HTML",
        "mutex",
        "HTTP"
      ],
      "correct": 2,
      "id": "GT141"
    },
    {
      "topic": "rtos",
      "question": "Boşluğa uygun cevap hangisidir?\nRTOS olmadan doğrudan donanım: ………-metal.",
      "options": [
        "SPI",
        "bare",
        "HTTP",
        "HTML"
      ],
      "correct": 1,
      "id": "GT142"
    },
    {
      "topic": "guc",
      "question": "Boşluğa uygun cevap hangisidir?\nDüşük güç modu: ……… sleep.",
      "options": [
        "SPI",
        "HTML",
        "HTTP",
        "deep"
      ],
      "correct": 3,
      "id": "GT143"
    },
    {
      "topic": "guc",
      "question": "Boşluğa uygun cevap hangisidir?\nSistem kilitlenince reset için ……… timer.",
      "options": [
        "HTML",
        "HTTP",
        "watchdog",
        "SPI"
      ],
      "correct": 2,
      "id": "GT144"
    },
    {
      "topic": "debug",
      "question": "Boşluğa uygun cevap hangisidir?\nHata ayıklamada Serial ……… yaygındır.",
      "options": [
        "HTTP",
        "Monitor",
        "HTML",
        "SPI"
      ],
      "correct": 1,
      "id": "GT145"
    },
    {
      "topic": "debug",
      "question": "Boşluğa uygun cevap hangisidir?\nBelirsiz pin seviyesi ……… pin denir.",
      "options": [
        "HTML",
        "floating",
        "HTTP",
        "SPI"
      ],
      "correct": 1,
      "id": "GT146"
    },
    {
      "topic": "debug",
      "question": "Boşluğa uygun cevap hangisidir?\nDijital sinyal zamanlaması için ……… analyzer.",
      "options": [
        "HTML",
        "HTTP",
        "SPI",
        "logic"
      ],
      "correct": 3,
      "id": "GT147"
    },
    {
      "topic": "debug",
      "question": "Boşluğa uygun cevap hangisidir?\nDalga formu için ……… kullanılır.",
      "options": [
        "HTML",
        "SPI",
        "osiloskop",
        "HTTP"
      ],
      "correct": 2,
      "id": "GT148"
    },
    {
      "topic": "guc",
      "question": "Boşluğa uygun cevap hangisidir?\nVoltaj düşünce reset: brown-………",
      "options": [
        "out",
        "HTTP",
        "HTML",
        "SPI"
      ],
      "correct": 0,
      "id": "GT149"
    },
    {
      "topic": "devre",
      "question": "Boşluğa uygun cevap hangisidir?\nOhm: V = I × ………",
      "options": [
        "R",
        "HTML",
        "HTTP",
        "SPI"
      ],
      "correct": 0,
      "id": "GT150"
    },
    {
      "topic": "devre",
      "question": "Boşluğa uygun cevap hangisidir?\nDiyot akımı tek ……… yönde akar.",
      "options": [
        "HTTP",
        "yon",
        "SPI",
        "HTML"
      ],
      "correct": 1,
      "id": "GT151"
    },
    {
      "topic": "gpio",
      "question": "Boşluğa uygun cevap hangisidir?\nGPIO açılımı General Purpose Input ………",
      "options": [
        "HTTP",
        "HTML",
        "SPI",
        "Output"
      ],
      "correct": 3,
      "id": "GT152"
    },
    {
      "topic": "bellek",
      "question": "Boşluğa uygun cevap hangisidir?\nADC analog-dejital ……… yapar.",
      "options": [
        "SPI",
        "HTML",
        "HTTP",
        "donusum"
      ],
      "correct": 3,
      "id": "GT153"
    },
    {
      "topic": "nodemcu",
      "question": "Boşluğa uygun cevap hangisidir?\nNodeMCU programlama dili örneği: Arduino ………",
      "options": [
        "HTML",
        "SPI",
        "C",
        "HTTP"
      ],
      "correct": 2,
      "id": "GT154"
    },
    {
      "topic": "nodemcu",
      "question": "Boşluğa uygun cevap hangisidir?\nWiFi şifresi kodda sabit değil ……… değişkeninde olmalı.",
      "options": [
        "HTTP",
        "SPI",
        "HTML",
        "config"
      ],
      "correct": 3,
      "id": "GT155"
    },
    {
      "topic": "protokol",
      "question": "Boşluğa uygun cevap hangisidir?\nI2C iki hatlı ……… haberleşmedir.",
      "options": [
        "HTML",
        "SPI",
        "senkron",
        "HTTP"
      ],
      "correct": 2,
      "id": "GT156"
    },
    {
      "topic": "protokol",
      "question": "Boşluğa uygun cevap hangisidir?\nSPI genelde ……… master bir slave çoklu yapı.",
      "options": [
        "SPI",
        "tek",
        "HTML",
        "HTTP"
      ],
      "correct": 1,
      "id": "GT157"
    },
    {
      "topic": "rtos",
      "question": "Boşluğa uygun cevap hangisidir?\nRTOS gerçek ……… sistemlerde kullanılır.",
      "options": [
        "SPI",
        "zamanli",
        "HTML",
        "HTTP"
      ],
      "correct": 1,
      "id": "GT158"
    },
    {
      "topic": "proje",
      "question": "Boşluğa uygun cevap hangisidir?\nProje sonunda ……… yapılır.",
      "options": [
        "HTTP",
        "sunum",
        "HTML",
        "SPI"
      ],
      "correct": 1,
      "id": "GT159"
    },
    {
      "topic": "devre",
      "question": "Boşluğa uygun cevap hangisidir?\nTransistör ……… kazancı sağlar.",
      "options": [
        "SPI",
        "HTML",
        "HTTP",
        "akim"
      ],
      "correct": 3,
      "id": "GT160"
    },
    {
      "topic": "devre",
      "question": "Boşluğa uygun cevap hangisidir?\nKondansatör enerji ……… edebilir.",
      "options": [
        "HTML",
        "depolar",
        "SPI",
        "HTTP"
      ],
      "correct": 1,
      "id": "GT161"
    },
    {
      "topic": "nodemcu",
      "question": "Boşluğa uygun cevap hangisidir?\nESP8266 ……… bağlantısı sunar.",
      "options": [
        "HTML",
        "SPI",
        "WiFi",
        "HTTP"
      ],
      "correct": 2,
      "id": "GT162"
    },
    {
      "topic": "rtos",
      "question": "Boşluğa uygun cevap hangisidir?\nÇoklu görevde ……… kaynağı sayılır.",
      "options": [
        "HTTP",
        "semaphore",
        "SPI",
        "HTML"
      ],
      "correct": 1,
      "id": "GT163"
    },
    {
      "topic": "giris",
      "question": "Boşluğa uygun cevap hangisidir?\nHarvard mimarisi program ve veri yolunu ……… edebilir.",
      "options": [
        "HTML",
        "SPI",
        "HTTP",
        "ayirir"
      ],
      "correct": 3,
      "id": "GT164"
    },
    {
      "topic": "protokol",
      "question": "Boşluğa uygun cevap hangisidir?\nMQTT topic mesajın ……… adresidir.",
      "options": [
        "SPI",
        "HTML",
        "kanal",
        "HTTP"
      ],
      "correct": 2,
      "id": "GT165"
    },
    {
      "topic": "nodemcu",
      "question": "Boşluğa uygun cevap hangisidir?\nBootloader program ……… işlemini kolaylaştırır.",
      "options": [
        "HTML",
        "SPI",
        "yukleme",
        "HTTP"
      ],
      "correct": 2,
      "id": "GT166"
    },
    {
      "topic": "rtos",
      "question": "Boşluğa uygun cevap hangisidir?\nISR kesme ……… rutinidir.",
      "options": [
        "servis",
        "HTML",
        "HTTP",
        "SPI"
      ],
      "correct": 0,
      "id": "GT167"
    },
    {
      "topic": "guc",
      "question": "Boşluğa uygun cevap hangisidir?\nPil ömrü için gereksiz ……… kapatılır.",
      "options": [
        "SPI",
        "peripheral",
        "HTTP",
        "HTML"
      ],
      "correct": 1,
      "id": "GT168"
    },
    {
      "topic": "gpio",
      "question": "Aşağıdaki kod/ifadenin uzun / doğru açıklaması hangisidir?\n\npinMode(13, OUTPUT);",
      "options": [
        "configure(13, OUT)",
        "pinMode(13, OUTPUT);",
        "setPinOutput(13)",
        "mode pin 13 out"
      ],
      "correct": 1,
      "id": "GT169"
    },
    {
      "topic": "gpio",
      "question": "Aşağıdaki kod/ifadenin kısa / doğru açıklaması hangisidir?\n\nvoid setup() {\n  Serial.begin(115200);\n  pinMode(2, INPUT_PULLUP);\n}\nvoid loop() {\n  Serial.println(digitalRead(2));\n  delay(500);\n}",
      "options": [
        "analog only",
        "WiFi.begin",
        "pinMode only",
        "Serial+pullup input okuma döngüsü"
      ],
      "correct": 3,
      "id": "GT170"
    },
    {
      "topic": "gpio",
      "question": "Aşağıdaki kod/ifadenin uzun / doğru açıklaması hangisidir?\n\ndigitalWrite(LED, HIGH);",
      "options": [
        "LED=1",
        "gpio_set(LED)",
        "write digital LED on",
        "digitalWrite(LED, HIGH);"
      ],
      "correct": 3,
      "id": "GT171"
    },
    {
      "topic": "gpio",
      "question": "Aşağıdaki kod/ifadenin kısa / doğru açıklaması hangisidir?\n\nif (analogRead(A0) > 512) { digitalWrite(13, HIGH); } else { digitalWrite(13, LOW); }",
      "options": [
        "I2C read",
        "A0 yarıda LED aç/kapa",
        "always HIGH",
        "Serial only"
      ],
      "correct": 1,
      "id": "GT172"
    },
    {
      "topic": "protokol",
      "question": "Aşağıdaki kod/ifadenin uzun / doğru açıklaması hangisidir?\n\nWire.begin();",
      "options": [
        "start_i2c()",
        "SDA.setup()",
        "I2C baslat",
        "Wire.begin();"
      ],
      "correct": 3,
      "id": "GT173"
    },
    {
      "topic": "debug",
      "question": "Aşağıdaki kod/ifadenin kısa / doğru açıklaması hangisidir?\n\nwhile (!Serial) { ; }",
      "options": [
        "MQTT connect",
        "delay only",
        "infinite loop wrong",
        "Serial hazır olana bekle (USB)"
      ],
      "correct": 3,
      "id": "GT174"
    },
    {
      "topic": "gpio",
      "question": "Aşağıdaki kod/ifadenin uzun / doğru açıklaması hangisidir?\n\nanalogWrite(9, 128);",
      "options": [
        "digital 128",
        "analogWrite(9, 128);",
        "pwm 9 half",
        "write analog 128 pin 9"
      ],
      "correct": 1,
      "id": "GT175"
    },
    {
      "topic": "gpio",
      "question": "Aşağıdaki kod/ifadenin kısa / doğru açıklaması hangisidir?\n\nfor (int i = 0; i < 10; i++) {\n  digitalWrite(LED, HIGH);\n  delay(200);\n  digitalWrite(LED, LOW);\n  delay(200);\n}",
      "options": [
        "analog fade",
        "LED 10 kez yanıp söner",
        "SPI transfer",
        "single blink"
      ],
      "correct": 1,
      "id": "GT176"
    },
    {
      "topic": "protokol",
      "question": "Aşağıdaki kod/ifadenin uzun / doğru açıklaması hangisidir?\n\nSPI.begin();",
      "options": [
        "spi start",
        "wire begin",
        "serial begin",
        "SPI.begin();"
      ],
      "correct": 3,
      "id": "GT177"
    },
    {
      "topic": "protokol",
      "question": "Aşağıdaki kod/ifadenin kısa / doğru açıklaması hangisidir?\n\nclient.publish(\"home/temp\", String(temp).c_str());",
      "options": [
        "HTTP GET",
        "MQTT publish sıcaklık",
        "Serial print only",
        "digitalWrite"
      ],
      "correct": 1,
      "id": "GT178"
    },
    {
      "topic": "gpio",
      "question": "Aşağıdaki kod/ifadenin uzun / doğru açıklaması hangisidir?\n\npinMode(BUTTON, INPUT_PULLUP);",
      "options": [
        "INPUT_PULLUP on BUTTON",
        "OUTPUT BUTTON",
        "button pullup config",
        "pinMode(BUTTON, INPUT_PULLUP);"
      ],
      "correct": 3,
      "id": "GT179"
    },
    {
      "topic": "guc",
      "question": "Aşağıdaki kod/ifadenin kısa / doğru açıklaması hangisidir?\n\nESP.deepSleep(1e8);",
      "options": [
        "reboot",
        "WiFi disconnect only",
        "ESP uzun uyku modu",
        "analogRead"
      ],
      "correct": 2,
      "id": "GT180"
    },
    {
      "topic": "protokol",
      "question": "Aşağıdaki kod/ifadenin uzun / doğru açıklaması hangisidir?\n\nSerial.begin(9600);",
      "options": [
        "begin serial 9600",
        "UART 9600 only comment",
        "baud 9600 serial",
        "Serial.begin(9600);"
      ],
      "correct": 3,
      "id": "GT181"
    },
    {
      "topic": "sensor",
      "question": "Aşağıdaki kod/ifadenin kısa / doğru açıklaması hangisidir?\n\nint mesafe = duration * 0.034 / 2;",
      "options": [
        "I2C",
        "ultrasonik cm yaklaşık formül",
        "temp formula",
        "random"
      ],
      "correct": 1,
      "id": "GT182"
    },
    {
      "topic": "sensor",
      "question": "Aşağıdaki kod/ifadenin uzun / doğru açıklaması hangisidir?\n\nservo.write(90);",
      "options": [
        "pwm 90 only",
        "servo.write(90);",
        "servo 90 derece",
        "angle(90)"
      ],
      "correct": 1,
      "id": "GT183"
    },
    {
      "topic": "gpio",
      "question": "Aşağıdaki kod/ifadenin kısa / doğru açıklaması hangisidir?\n\ndigitalWrite(RELAY, !digitalRead(RELAY));",
      "options": [
        "Röle toggle",
        "analog",
        "always on",
        "MQTT"
      ],
      "correct": 0,
      "id": "GT184"
    },
    {
      "topic": "gpio",
      "question": "Aşağıdaki kod/ifadenin uzun / doğru açıklaması hangisidir?\n\ndelay(1000);",
      "options": [
        "sleep(1)",
        "delay(1000);",
        "pause_ms(1000)",
        "wait 1s"
      ],
      "correct": 1,
      "id": "GT185"
    },
    {
      "topic": "rtos",
      "question": "Aşağıdaki kod/ifadenin kısa / doğru açıklaması hangisidir?\n\nif (xSemaphoreTake(mutex, portMAX_DELAY)) {\n  shared++;\n  xSemaphoreGive(mutex);\n}",
      "options": [
        "mutex ile kritik bölge",
        "no protection",
        "Serial only",
        "GPIO"
      ],
      "correct": 0,
      "id": "GT186"
    },
    {
      "topic": "nodemcu",
      "question": "Aşağıdaki kod/ifadenin uzun / doğru açıklaması hangisidir?\n\nWiFi.begin(ssid, password);",
      "options": [
        "connect_wifi()",
        "WiFi.begin(ssid, password);",
        "mqtt begin",
        "wifi connect"
      ],
      "correct": 1,
      "id": "GT187"
    },
    {
      "topic": "gpio",
      "question": "Aşağıdaki kod/ifadenin kısa / doğru açıklaması hangisidir?\n\nattachInterrupt(digitalPinToInterrupt(2), ISR, FALLING);",
      "options": [
        "pin2 düşen kenar kesme",
        "PWM",
        "SPI",
        "polling only"
      ],
      "correct": 0,
      "id": "GT188"
    },
    {
      "topic": "gpio",
      "question": "Aşağıdaki kod/ifadenin uzun / doğru açıklaması hangisidir?\n\nmap(val, 0, 1023, 0, 255);",
      "options": [
        "convert",
        "map(val, 0, 1023, 0, 255);",
        "analog only",
        "scale adc to byte"
      ],
      "correct": 1,
      "id": "GT189"
    },
    {
      "topic": "protokol",
      "question": "Aşağıdaki kod/ifadenin kısa / doğru açıklaması hangisidir?\n\nWire.requestFrom(0x68, 6, true);",
      "options": [
        "I2C 0x68'den 6 byte iste",
        "SPI read",
        "publish",
        "UART"
      ],
      "correct": 0,
      "id": "GT190"
    },
    {
      "topic": "gpio",
      "question": "Aşağıdaki kod/ifadenin uzun / doğru açıklaması hangisidir?\n\ndigitalRead(pin) == HIGH",
      "options": [
        "read pin high",
        "pin high check",
        "digitalRead(pin) == HIGH",
        "isHigh(pin)"
      ],
      "correct": 2,
      "id": "GT191"
    },
    {
      "topic": "rtos",
      "question": "Aşağıdaki kod/ifadenin kısa / doğru açıklaması hangisidir?\n\nvoid IRAM_ATTR ISR() { flag = true; }",
      "options": [
        "slow ISR",
        "ESP kesme hızlı RAM",
        "main only",
        "delay in ISR"
      ],
      "correct": 1,
      "id": "GT192"
    },
    {
      "topic": "bellek",
      "question": "Aşağıdaki kod/ifadenin uzun / doğru açıklaması hangisidir?\n\nEEPROM.read(addr);",
      "options": [
        "ram get",
        "EEPROM.read(addr);",
        "read eeprom",
        "flash read"
      ],
      "correct": 1,
      "id": "GT193"
    },
    {
      "topic": "rtos",
      "question": "Aşağıdaki kod/ifadenin kısa / doğru açıklaması hangisidir?\n\nconst int LED = 13;\npinMode(LED, OUTPUT);",
      "options": [
        "blink random",
        "MQTT",
        "SPI",
        "LED pin 13 output setup"
      ],
      "correct": 3,
      "id": "GT194"
    },
    {
      "topic": "guc",
      "question": "Aşağıdaki kod/ifadenin uzun / doğru açıklaması hangisidir?\n\nSerial.print(\"Temp:\");",
      "options": [
        "printf only",
        "print temp label",
        "Serial.print(\"Temp:\");",
        "cout"
      ],
      "correct": 2,
      "id": "GT195"
    },
    {
      "topic": "debug",
      "question": "Aşağıdaki kod/ifadenin kısa / doğru açıklaması hangisidir?\n\ntone(8, 440, 500);",
      "options": [
        "buzzer 440Hz 500ms",
        "digital only",
        "WiFi",
        "I2C"
      ],
      "correct": 0,
      "id": "GT196"
    },
    {
      "topic": "gpio",
      "question": "Aşağıdaki kod/ifadenin uzun / doğru açıklaması hangisidir?\n\nnoTone(8);",
      "options": [
        "end sound",
        "noTone(8);",
        "mute",
        "stop tone 8"
      ],
      "correct": 1,
      "id": "GT197"
    },
    {
      "topic": "protokol",
      "question": "Aşağıdaki kod/ifadenin kısa / doğru açıklaması hangisidir?\n\nif (millis() - last > 1000) {\n  last = millis();\n  // işlem\n}",
      "options": [
        "non-blocking 1sn interval",
        "delay(1000) loop",
        "sleep",
        "while true"
      ],
      "correct": 0,
      "id": "GT198"
    },
    {
      "topic": "nodemcu",
      "question": "Aşağıdaki kod/ifadenin uzun / doğru açıklaması hangisidir?\n\nclient.subscribe(\"cmd/#\");",
      "options": [
        "mqtt sub wildcard",
        "HTTP",
        "client.subscribe(\"cmd/#\");",
        "publish only"
      ],
      "correct": 2,
      "id": "GT199"
    },
    {
      "topic": "sensor",
      "question": "Aşağıdaki kod/ifadenin kısa / doğru açıklaması hangisidir?\n\ndigitalWrite(LED, digitalRead(BUTTON));",
      "options": [
        "analog",
        "SPI",
        "Buton durumunu LED'e yansıt",
        "random LED"
      ],
      "correct": 2,
      "id": "GT200"
    },
    {
      "topic": "rtos",
      "question": "Aşağıdaki kod/ifadenin uzun / doğru açıklaması hangisidir?\n\npinMode(5, INPUT);",
      "options": [
        "pinMode(5, INPUT);",
        "input pin 5",
        "set input",
        "gpio 5 in"
      ],
      "correct": 0,
      "id": "GT201"
    },
    {
      "topic": "guc",
      "question": "Aşağıdaki kod/ifadenin kısa / doğru açıklaması hangisidir?\n\nconst int LED = 13;\npinMode(LED, OUTPUT);",
      "options": [
        "MQTT",
        "LED pin 13 output setup",
        "blink random",
        "SPI"
      ],
      "correct": 1,
      "id": "GT202"
    },
    {
      "topic": "debug",
      "question": "Aşağıdaki kod/ifadenin uzun / doğru açıklaması hangisidir?\n\nSerial.print(\"Temp:\");",
      "options": [
        "printf only",
        "print temp label",
        "Serial.print(\"Temp:\");",
        "cout"
      ],
      "correct": 2,
      "id": "GT203"
    },
    {
      "topic": "gpio",
      "question": "Aşağıdaki kod/ifadenin kısa / doğru açıklaması hangisidir?\n\ntone(8, 440, 500);",
      "options": [
        "buzzer 440Hz 500ms",
        "digital only",
        "I2C",
        "WiFi"
      ],
      "correct": 0,
      "id": "GT204"
    },
    {
      "topic": "protokol",
      "question": "Aşağıdaki kod/ifadenin uzun / doğru açıklaması hangisidir?\n\nnoTone(8);",
      "options": [
        "stop tone 8",
        "mute",
        "noTone(8);",
        "end sound"
      ],
      "correct": 2,
      "id": "GT205"
    },
    {
      "topic": "nodemcu",
      "question": "Aşağıdaki kod/ifadenin kısa / doğru açıklaması hangisidir?\n\nif (millis() - last > 1000) {\n  last = millis();\n  // işlem\n}",
      "options": [
        "non-blocking 1sn interval",
        "sleep",
        "while true",
        "delay(1000) loop"
      ],
      "correct": 0,
      "id": "GT206"
    },
    {
      "topic": "sensor",
      "question": "Aşağıdaki kod/ifadenin uzun / doğru açıklaması hangisidir?\n\nclient.subscribe(\"cmd/#\");",
      "options": [
        "HTTP",
        "mqtt sub wildcard",
        "publish only",
        "client.subscribe(\"cmd/#\");"
      ],
      "correct": 3,
      "id": "GT207"
    },
    {
      "topic": "rtos",
      "question": "Aşağıdaki kod/ifadenin kısa / doğru açıklaması hangisidir?\n\ndigitalWrite(LED, digitalRead(BUTTON));",
      "options": [
        "Buton durumunu LED'e yansıt",
        "random LED",
        "SPI",
        "analog"
      ],
      "correct": 0,
      "id": "GT208"
    },
    {
      "topic": "guc",
      "question": "Aşağıdaki kod/ifadenin uzun / doğru açıklaması hangisidir?\n\npinMode(5, INPUT);",
      "options": [
        "set input",
        "pinMode(5, INPUT);",
        "gpio 5 in",
        "input pin 5"
      ],
      "correct": 1,
      "id": "GT209"
    },
    {
      "topic": "debug",
      "question": "Aşağıdaki kod/ifadenin kısa / doğru açıklaması hangisidir?\n\nconst int LED = 13;\npinMode(LED, OUTPUT);",
      "options": [
        "MQTT",
        "SPI",
        "LED pin 13 output setup",
        "blink random"
      ],
      "correct": 2,
      "id": "GT210"
    },
    {
      "topic": "gpio",
      "question": "Aşağıdaki kod/ifadenin uzun / doğru açıklaması hangisidir?\n\nSerial.print(\"Temp:\");",
      "options": [
        "Serial.print(\"Temp:\");",
        "cout",
        "printf only",
        "print temp label"
      ],
      "correct": 0,
      "id": "GT211"
    },
    {
      "topic": "protokol",
      "question": "Aşağıdaki kod/ifadenin kısa / doğru açıklaması hangisidir?\n\ntone(8, 440, 500);",
      "options": [
        "digital only",
        "buzzer 440Hz 500ms",
        "I2C",
        "WiFi"
      ],
      "correct": 1,
      "id": "GT212"
    },
    {
      "topic": "nodemcu",
      "question": "Aşağıdaki kod/ifadenin uzun / doğru açıklaması hangisidir?\n\nnoTone(8);",
      "options": [
        "mute",
        "stop tone 8",
        "noTone(8);",
        "end sound"
      ],
      "correct": 2,
      "id": "GT213"
    },
    {
      "topic": "sensor",
      "question": "Aşağıdaki kod/ifadenin kısa / doğru açıklaması hangisidir?\n\nif (millis() - last > 1000) {\n  last = millis();\n  // işlem\n}",
      "options": [
        "non-blocking 1sn interval",
        "while true",
        "delay(1000) loop",
        "sleep"
      ],
      "correct": 0,
      "id": "GT214"
    },
    {
      "topic": "rtos",
      "question": "Aşağıdaki kod/ifadenin uzun / doğru açıklaması hangisidir?\n\nclient.subscribe(\"cmd/#\");",
      "options": [
        "HTTP",
        "publish only",
        "mqtt sub wildcard",
        "client.subscribe(\"cmd/#\");"
      ],
      "correct": 3,
      "id": "GT215"
    },
    {
      "topic": "guc",
      "question": "Aşağıdaki kod/ifadenin kısa / doğru açıklaması hangisidir?\n\ndigitalWrite(LED, digitalRead(BUTTON));",
      "options": [
        "analog",
        "SPI",
        "random LED",
        "Buton durumunu LED'e yansıt"
      ],
      "correct": 3,
      "id": "GT216"
    },
    {
      "topic": "debug",
      "question": "Aşağıdaki kod/ifadenin uzun / doğru açıklaması hangisidir?\n\npinMode(5, INPUT);",
      "options": [
        "input pin 5",
        "gpio 5 in",
        "set input",
        "pinMode(5, INPUT);"
      ],
      "correct": 3,
      "id": "GT217"
    },
    {
      "topic": "gpio",
      "question": "Aşağıdaki kod/ifadenin kısa / doğru açıklaması hangisidir?\n\nconst int LED = 13;\npinMode(LED, OUTPUT);",
      "options": [
        "blink random",
        "MQTT",
        "SPI",
        "LED pin 13 output setup"
      ],
      "correct": 3,
      "id": "GT218"
    },
    {
      "topic": "protokol",
      "question": "Aşağıdaki kod/ifadenin uzun / doğru açıklaması hangisidir?\n\nSerial.print(\"Temp:\");",
      "options": [
        "cout",
        "printf only",
        "Serial.print(\"Temp:\");",
        "print temp label"
      ],
      "correct": 2,
      "id": "GT219"
    },
    {
      "topic": "nodemcu",
      "question": "Aşağıdaki kod/ifadenin kısa / doğru açıklaması hangisidir?\n\ntone(8, 440, 500);",
      "options": [
        "buzzer 440Hz 500ms",
        "digital only",
        "I2C",
        "WiFi"
      ],
      "correct": 0,
      "id": "GT220"
    },
    {
      "topic": "sensor",
      "question": "Aşağıdaki kod/ifadenin uzun / doğru açıklaması hangisidir?\n\nnoTone(8);",
      "options": [
        "stop tone 8",
        "noTone(8);",
        "mute",
        "end sound"
      ],
      "correct": 1,
      "id": "GT221"
    },
    {
      "topic": "rtos",
      "question": "Aşağıdaki kod/ifadenin kısa / doğru açıklaması hangisidir?\n\nif (millis() - last > 1000) {\n  last = millis();\n  // işlem\n}",
      "options": [
        "while true",
        "delay(1000) loop",
        "non-blocking 1sn interval",
        "sleep"
      ],
      "correct": 2,
      "id": "GT222"
    },
    {
      "topic": "guc",
      "question": "Aşağıdaki kod/ifadenin uzun / doğru açıklaması hangisidir?\n\nclient.subscribe(\"cmd/#\");",
      "options": [
        "publish only",
        "mqtt sub wildcard",
        "client.subscribe(\"cmd/#\");",
        "HTTP"
      ],
      "correct": 2,
      "id": "GT223"
    }
  ]
};
