# Claude Skills ve Model Context Protocol (MCP)

## Teknik Araştırma Raporu

**Hazırlayan:** Mustafa Akgül

**Şirket:** Prodrom Bilişim Teknolojileri Ltd. Şti.

**Proje:** Claude Ekosistemi Araştırması

**Tarih:** Temmuz 2026

---

# 1. Giriş

Yapay zekâ destekli büyük dil modelleri (Large Language Models - LLM), yazılım geliştirme, veri analizi, doküman oluşturma ve iş süreçlerinin otomasyonu gibi birçok alanda yaygın olarak kullanılmaktadır. Anthropic tarafından geliştirilen Claude modeli, güvenlik odaklı yaklaşımı, doğal dil işleme yetenekleri ve geniş bağlam penceresi sayesinde kurumsal kullanım senaryolarında öne çıkmaktadır.

Claude yalnızca soru-cevap üreten bir sohbet modeli değildir. Belgeler üzerinde çalışabilir, kod üretebilir, özetleme yapabilir, iş akışlarını destekleyebilir ve harici sistemlerle bütünleşerek daha gelişmiş görevleri yerine getirebilir.

Bu raporda Claude Skills, Model Context Protocol (MCP), Prompt Engineering teknikleri ve kurumsal kullanım senaryoları incelenmiştir.

---

# 2. Araştırmanın Amacı

Bu çalışmanın amacı;

- Claude Skills kavramını incelemek,
- Model Context Protocol (MCP) mimarisini araştırmak,
- Prompt Engineering tekniklerini karşılaştırmak,
- Kurumsal kullanım senaryoları oluşturmak,
- Yapay zekâ destekli iş akışlarını değerlendirmektir.

  # 3. Claude Skills

## 3.1 Claude Skill Nedir?

Claude Skills, Claude'un belirli görevleri daha etkili ve düzenli şekilde yerine getirebilmesini sağlayan yeteneklerdir. Bu yetenekler sayesinde Claude yalnızca metin üretmekle kalmaz; belge oluşturma, dosya düzenleme, veri analizi, kod üretme ve farklı araçlarla çalışma gibi işlemleri de gerçekleştirebilir.

Skill kavramı, yapay zekâ modelinin belirli bir göreve odaklanmasını sağlayan bilgi, talimat ve araçların bir araya getirilmiş hâli olarak düşünülebilir. Böylece kullanıcı her seferinde aynı talimatları vermek yerine, belirli bir amacı yerine getiren hazır bir yetenekten faydalanabilir.

## 3.2 Belge Oluşturma ve Düzenleme

Claude, uygun araçlarla birlikte kullanıldığında çeşitli belge formatları üzerinde çalışabilir.

Desteklenen yaygın belge türleri:

- DOCX (Microsoft Word)
- PPTX (Microsoft PowerPoint)
- XLSX (Microsoft Excel)
- PDF
- Markdown (.md)
- CSV

Bu belgeler üzerinde;

- yeni belge oluşturma,
- mevcut belgeyi düzenleme,
- özet çıkarma,
- tablo oluşturma,
- rapor hazırlama,
- içerik yeniden düzenleme

gibi işlemler gerçekleştirilebilir.

## 3.3 İş Süreçlerinde Sağladığı Avantajlar

Claude Skills, özellikle tekrarlayan ofis çalışmalarında önemli zaman kazancı sağlayabilir.

Örnek kullanım alanları:

| İş Süreci | Sağladığı Katkı |
|-----------|-----------------|
| Teknik rapor hazırlama | Taslak oluşturma ve düzenleme |
| Sunum hazırlama | Slayt içeriklerinin oluşturulması |
| Kod dokümantasyonu | Kod açıklamalarının hazırlanması |
| Toplantı notları | Özet çıkarılması |
| Veri analizi | Sonuçların yorumlanması |
| Doküman düzenleme | Yazım ve biçimlendirme desteği |

Bu işlemler sayesinde çalışanların rutin iş yükü azalırken daha fazla zaman analiz, planlama ve karar verme süreçlerine ayrılabilir.

## 3.4 Kuruma Özel Skill Önerisi

Araştırma kapsamında kurum için örnek bir Skill önerisi geliştirilmiştir.

**Teknik Rapor Asistanı**

Bu Skill'in amacı, teknik ekip tarafından hazırlanan raporları standart bir formatta oluşturmak ve düzenlemektir.

Önerilen özellikleri:

- Standart rapor şablonunu kullanma
- Başlıkları otomatik oluşturma
- Yazım ve dil kontrolü yapma
- Kaynakça düzenleme
- PDF ve DOCX çıktısı hazırlama
  Bu çalışma kapsamında resmi dokümantasyon incelenmiş, örnek promptlar hazırlanmış ve kurumsal iş süreçlerine yönelik örnek workflow tasarımları geliştirilmiştir.

  # 4. Model Context Protocol (MCP)

## 4.1 MCP Nedir?

Model Context Protocol (MCP), yapay zekâ modellerinin harici veri kaynakları, uygulamalar ve servislerle güvenli ve standart bir yöntem kullanarak iletişim kurmasını sağlayan açık bir protokoldür. Bu yapı sayesinde bir yapay zekâ modeli yalnızca eğitim verisine bağlı kalmaz; ihtiyaç duyduğu anda farklı sistemlerden güncel bilgi alabilir ve bu sistemlerle etkileşim kurabilir.

MCP'nin temel amacı, farklı araçlar ile yapay zekâ modelleri arasında ortak bir iletişim standardı oluşturmaktır. Böylece her uygulama için ayrı entegrasyon geliştirmek yerine tek bir protokol üzerinden birçok sisteme erişim sağlanabilir.

## 4.2 MCP Nasıl Çalışır?

MCP mimarisi genel olarak üç bileşenden oluşur:

- **MCP Host:** Yapay zekâ uygulamasını çalıştıran istemci.
- **MCP Client:** İstekleri ilgili sunucuya ileten bileşen.
- **MCP Server:** Dosya sistemi, veritabanı veya başka bir servise erişim sağlayan bileşen.

Bu yapı sayesinde kullanıcı bir istekte bulunduğunda yapay zekâ modeli gerekli bilgiyi uygun MCP sunucusundan alabilir ve kullanıcıya güncel sonuç sunabilir.

## 4.3 Yaygın MCP Sunucuları

Günümüzde farklı amaçlar için geliştirilen birçok MCP sunucusu bulunmaktadır.

Örnekler:

- Dosya Sistemi (Filesystem)
- GitHub
- PostgreSQL
- SQLite
- Google Drive
- Slack
- Notion

Bu entegrasyonlar sayesinde yapay zekâ modeli yalnızca metin üretmekle kalmaz, aynı zamanda mevcut kurumsal sistemlerle birlikte çalışabilir.

## 4.4 Kurum İçin MCP Önerileri

Araştırma sonucunda kurum içerisinde kullanılabilecek bazı MCP entegrasyon fikirleri aşağıda verilmiştir.

| Entegrasyon | Sağlayacağı Fayda |
|-------------|-------------------|
| GitHub MCP | Kod depolarının analiz edilmesi |
| PostgreSQL MCP | Veritabanı sorgularının desteklenmesi |
| Dosya Sistemi MCP | Teknik dokümanlara erişim |
| Slack MCP | Ekip iletişim süreçlerinin desteklenmesi |

Bu entegrasyonlar sayesinde bilgiye erişim hızlanabilir, manuel işlemler azaltılabilir ve çalışanların verimliliği artırılabilir.
# 5. Prompt Engineering Teknikleri

Prompt Engineering, bir yapay zekâ modelinden daha doğru, tutarlı ve kullanılabilir sonuçlar elde etmek amacıyla verilen istemlerin sistemli biçimde hazırlanmasıdır. İyi hazırlanmış bir prompt; görevi, bağlamı, kısıtları ve beklenen çıktı biçimini açıkça belirtir.

Claude ile çalışırken kullanılan promptun açıklığı, verilen örneklerin kalitesi ve istenen çıktı formatının belirtilmesi sonuç üzerinde doğrudan etkilidir. Özellikle kurumsal görevlerde yalnızca genel bir istek vermek yerine, görevin amacı ve başarı ölçütleri de açıklanmalıdır.

## 5.1 Açık ve Net Talimat Verme

Açık ve net talimat verme, temel prompt tekniklerinden biridir. Bu yöntemde kullanıcı, modelden istediği görevi belirsiz ifadeler yerine ayrıntılı ve doğrudan biçimde açıklar.

İyi bir talimatta aşağıdaki unsurlar bulunabilir:

- Yapılacak görev
- Görevin amacı
- Kullanılacak bağlam
- Uyulması gereken kısıtlar
- İstenen çıktı biçimi
- Hedef kullanıcı veya okuyucu kitlesi

### Belirsiz Prompt Örneği

```text
Linux hakkında bir rapor hazırla.
```

Bu promptta raporun konusu, uzunluğu, hedef kitlesi ve biçimi belirtilmemiştir. Bu nedenle oluşturulan sonuç kullanıcının gerçek ihtiyacını tam olarak karşılamayabilir.

### Geliştirilmiş Prompt Örneği

```text
Üniversite öğrencilerine yönelik, Linux işletim sisteminin temel özelliklerini açıklayan yaklaşık 500 kelimelik bir teknik rapor hazırla. Raporda Linux'un tarihçesi, açık kaynak yapısı, temel kullanım alanları ve avantajları yer alsın. Çıktıyı Markdown biçiminde, başlıklar ve kısa paragraflar kullanarak oluştur.
```

Geliştirilmiş promptta görev, hedef kitle, kapsam, uzunluk ve çıktı formatı açıkça belirtilmiştir. Böylece modelden alınan cevabın daha düzenli ve kullanılabilir olması beklenir.

## 5.2 Few-Shot Prompting

Few-Shot Prompting, modele görevden önce bir veya daha fazla örnek gösterilmesi yöntemidir. Model, verilen örneklerdeki yapıyı ve cevap biçimini inceleyerek yeni girdiye benzer şekilde cevap üretir.

Bu yöntem özellikle aşağıdaki görevlerde yararlıdır:

- Metin sınıflandırma
- Bilgi çıkarma
- Belirli bir yazım biçimini koruma
- Müşteri mesajlarını kategorilere ayırma
- Standart rapor veya kayıt oluşturma

### Few-Shot Prompt Örneği

```text
Aşağıdaki müşteri mesajlarını "Teknik Sorun", "Fatura" veya "Bilgi Talebi" kategorilerinden biriyle sınıflandır.

Örnek 1:
Mesaj: Uygulamaya giriş yaptığımda hata alıyorum.
Kategori: Teknik Sorun

Örnek 2:
Mesaj: Bu ayki faturam neden daha yüksek geldi?
Kategori: Fatura

Örnek 3:
Mesaj: Ürünün kurumsal paketi hakkında bilgi almak istiyorum.
Kategori: Bilgi Talebi

Yeni mesaj:
Şifremi yeniledim ancak hesabıma hâlâ erişemiyorum.

Kategori:
```

Bu örnekte model, önceki örneklerden sınıflandırma biçimini öğrenir ve yeni mesajı aynı kategori yapısına göre değerlendirir.

## 5.3 XML Etiketleriyle Yapılandırılmış Prompt

XML etiketleri, uzun veya karmaşık promptlarda farklı bilgi bölümlerini birbirinden ayırmak için kullanılabilir. Rol, bağlam, görev, kısıtlar ve çıktı formatı ayrı etiketler içinde tanımlanabilir.

### XML Prompt Örneği

```xml
<role>
Bir siber güvenlik analisti olarak görev yap.
</role>

<context>
Ubuntu tabanlı bir sunucuda güvenlik incelemesi gerçekleştirilmektedir.
</context>

<task>
Verilen güvenlik bulgularını önem derecesine göre değerlendir.
</task>

<constraints>
Kesin olmayan bilgileri gerçekmiş gibi sunma.
Her bulgu için kısa bir çözüm önerisi ver.
</constraints>

<output_format>
Sonucu Markdown tablosu olarak hazırla.
Sütunlar: Bulgu, Risk Seviyesi, Açıklama, Çözüm.
</output_format>
```

Bu yapı sayesinde promptun bölümleri açıkça ayrılır. Özellikle çok sayıda talimat, veri veya örnek içeren görevlerde okunabilirlik ve yönetilebilirlik artar.
## 5.4 Task Decomposition (Görev Bölme)

Task Decomposition, büyük ve karmaşık bir görevin daha küçük ve yönetilebilir alt görevlere ayrılması yaklaşımıdır. Bu teknik, özellikle çok aşamalı işlemlerde modelin her adımı ayrı ayrı ele almasını sağlayarak daha tutarlı sonuçlar elde edilmesine yardımcı olur.

Örneğin tek seferde "Bir sızma testi raporu hazırla." demek yerine süreç aşağıdaki şekilde bölünebilir:

1. Hedef sistemi analiz et.
2. Güvenlik açıklarını listele.
3. Risk seviyelerini değerlendir.
4. Çözüm önerileri hazırla.
5. Teknik raporu oluştur.

Bu yaklaşım hem hata oranını azaltır hem de her aşamanın ayrı ayrı kontrol edilmesini kolaylaştırır.

---

## 5.5 Prompt Tekniklerinin Karşılaştırılması

| Teknik | Avantajı | Kullanım Alanı |
|---------|----------|----------------|
| Açık ve Net Talimat | Daha doğru cevaplar üretir | Genel amaçlı görevler |
| Few-Shot Prompting | Belirli formatı öğretir | Sınıflandırma ve standart çıktılar |
| XML Prompting | Karmaşık istemleri düzenler | Uzun ve çok aşamalı görevler |
| Task Decomposition | Büyük görevleri yönetilebilir hâle getirir | Teknik analiz ve raporlama |

---

## 5.6 Test Edilen Prompt Örnekleri ve Gözlemler

Araştırma kapsamında farklı prompt teknikleri kullanılarak örnek istemler hazırlanmıştır.

### Test 1 – Açık Talimat

**Sonuç:**

Model, istenen çıktı biçimine büyük ölçüde uygun ve düzenli bir cevap üretmiştir.

---

### Test 2 – Few-Shot Prompt

**Sonuç:**

Örnekler sayesinde model aynı biçimde ve tutarlı sınıflandırmalar gerçekleştirmiştir.

---

### Test 3 – XML Prompt

**Sonuç:**

Görev, bağlam ve çıktı biçiminin ayrı etiketlerle belirtilmesi istemin okunabilirliğini artırmış ve daha düzenli cevaplar üretilmesini sağlamıştır.

---

### Genel Değerlendirme

Yapılan testler sonucunda açık talimatlar, uygun örnekler ve yapılandırılmış istemlerin birlikte kullanıldığı durumlarda daha tutarlı ve kaliteli çıktılar elde edildiği gözlemlenmiştir. Özellikle kurumsal kullanım senaryolarında görevin amacı, kısıtları ve çıktı biçiminin açık şekilde belirtilmesi önerilmektedir.
# 6. Başarılı Kullanım Örnekleri

Claude ve benzeri büyük dil modelleri günümüzde birçok sektörde aktif olarak kullanılmaktadır. Doğru prompt teknikleri ve uygun entegrasyonlarla iş süreçlerinde önemli verimlilik artışları sağlanabilmektedir.

### 6.1 Yazılım Geliştirme

Yazılım ekipleri Claude'u;

- Kod açıklamaları oluşturma,
- Dokümantasyon hazırlama,
- Kod inceleme (Code Review),
- Test senaryoları oluşturma,
- Hata analizleri

gibi görevlerde destek amaçlı kullanabilmektedir.

### 6.2 Müşteri Hizmetleri

Müşteri destek ekipleri;

- Sık sorulan soruların cevaplanması,
- E-posta taslaklarının hazırlanması,
- Destek taleplerinin sınıflandırılması,
- Önceliklendirme işlemleri

gibi süreçlerde yapay zekâdan yararlanabilmektedir.

### 6.3 Teknik Doküman Hazırlama

Claude;

- Teknik rapor,
- Toplantı özeti,
- Kullanım kılavuzu,
- Proje dokümantasyonu

hazırlama süreçlerinde taslak oluşturma ve düzenleme desteği sağlayabilir.

---

# 7. Workflow Tasarımları

Workflow, belirli bir işin başlangıcından tamamlanmasına kadar izlenen adımların planlı biçimde yürütülmesini ifade eder.

Bu araştırma kapsamında kurum içerisinde kullanılabilecek iki örnek workflow önerilmiştir.

## Workflow 1 – Teknik Rapor Hazırlama

```text
Konu Belirleme
      ↓
Bilgi Toplama
      ↓
Claude ile Taslak Oluşturma
      ↓
İnsan Kontrolü
      ↓
Son Düzenleme
      ↓
PDF/DOCX Teslimi
```

Bu workflow sayesinde rapor hazırlama sürecinde zaman tasarrufu sağlanabilir. Son kontrolün insan tarafından yapılması doğruluk açısından önemlidir.

---

## Workflow 2 – Müşteri Destek Süreci

```text
Müşteri Talebi
      ↓
Talebin Analizi
      ↓
Claude ile Taslak Cevap
      ↓
Personel Kontrolü
      ↓
Müşteriye Gönderim
```

Bu süreçte yapay zekâ ilk taslağı hazırlarken, nihai karar ve gönderim yetkisi insan kullanıcıda kalmaktadır. Böylece hem hız hem de kalite artırılabilir.

