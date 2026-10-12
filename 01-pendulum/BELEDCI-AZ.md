# Fizika Labı: Telefon və İplə g-ni Ölçmək (Bələdçi)

Bu işi təzə qurtarmış biri kimi deyirəm, əgər bu laba başlayırsınızsa, burda yazdığım səhvləri təkrar etməyin.

## 1. Nə lazımdır?
- Telefon (giroskop sensoru üçün)
- Uzun ip və iki stul + çubuq (dayaq üçün)
- Phyphox tətbiqi (qrafikləri çıxarmaq üçün)
- Xətkeş

## 2. Qurğu və Səhvlər
- **Asqı:** Telefon iki paralel şaquli ipdən asılmışdı[cite: 1]. Bu, telefonu fırlanmadan qorumaq üçün yaxşıdır, amma ipin uzunluğunu ölçərkən kütlə mərkəzini dəqiq təyin etmək lazımdır.
- **Ölçü:** Uzunluğu yuxarıdan telefonun tən ortasına (kütlə mərkəzinə) qədər dəqiq ölçün.

## 3. Ölçmələr
- 0.20, 0.30, 0.40, 0.50 və 0.70 metr uzunluqlarda yoxladıq (hərəsindən 2 run). 
- *0.60 m niyə yoxdur?* Çünki həmin uzunluqda ip sürüşdü, səs-küy çox oldu, məlumatı tulladıq.
- Telefonu buraxanda əvvəldə əl hərəkətinə görə xaotik yerlər olur. Kodda həmin yerləri kəsdik (məsələn, L0.50 üçün 10.2 saniyədən, L0.70 üçün 17.5 saniyədən sonranı).

## 4. Hesablama
- Periodları ($) tapandan sonra ^2$ ilə $-in qrafikini çəkirsiniz.
- Düstur: 
  g = \frac{4\pi^2}{\text{maillik}}

## 5. Nəticə
- Bizim aldığımız rəqəm .76 \pm 0.58 \text{ m/s}^2$ çıxdı (normalda 9.81 olmalıdır).
- Bir az çox çıxmasının səbəbi iki paralel ip sistemində uzunluğun tətbiqi və telefonun yellənərkən yüngülcə hərəkət xüsusiyyətləridir.
