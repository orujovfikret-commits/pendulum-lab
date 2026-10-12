# Fizika Labı: Telefon və İplə g-ni Ölçmək (Bələdçi)

Bu işi qurtarmış biri kimi deyirəm, əgər bu laba başlayırsınızsa, burda yazdığım səhvləri təkrar etməyin.

## 1. Nə lazımdır?
- Telefon (giroskop sensoru üçün)
- Uzun ip və iki stul + çubuq (dayaq üçün)
- Phyphox tətbiqi (qrafikləri çıxarmaq üçün)
- Xətkeş

## 2. Qurğu və Səhvlər
- **Asqı:** Telefon iki paralel şaquli ipdən asılmışdı. İplərin yuxarıda və aşağıda arasındakı məsafəni yoxlasanız eyni olduğunu görərsiniz (parallel asqı). Bu, telefonu fırlanmadan qorumaq üçündür.
- **Ölçü:** Uzunluğu yuxarıdan telefonun tən ortasına (kütlə mərkəzinə) qədər şaquli olaraq dəqiq ölçün.

## 3. Ölçmələr
- 0.20, 0.30, 0.40, 0.50 və 0.70 metr uzunluqlarda ölçdük (hərəsindən 2 run).
- Telefonu buraxanda əvvəldə əl hərəkətinə görə xaotik yerlər olur. Kodda həmin yerləri kəsdik (məsələn, L0.50 üçün 10.2 saniyədən, L0.70 üçün 17.5 saniyədən sonranı).

## 4. Hesablama
- Periodları (T) tapandan sonra T^2 ilə L-in qrafikini çəkirsiniz.
- Düstur: g = 4 * pi^2 / maillik

## 5. Nəticə
- Bizim aldığımız rəqəm 10.76 ± 0.58 m/s^2 çıxdı (normalda 9.81 olmalıdır).
- Qrafikdəki xəttin kəsişməsini (c) mailliyə bölsəniz (0.1842 / 3.669), təxminən 0.05 m (5 sm) edir ki, bu da uzunluq ölçərkən baş verən kiçik sistematik fərqi göstərir.
