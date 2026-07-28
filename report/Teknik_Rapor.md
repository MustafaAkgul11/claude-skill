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
