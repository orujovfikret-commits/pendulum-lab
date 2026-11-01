# Fizika Labı: Telefon və Ofis Kreslosu ilə a = ω²R-i Yoxlamaq (Bələdçi)

Bu işi qurtarmış biri kimi deyirəm, əgər bu laba başlayırsınızsa, burda yazdığım səhvləri təkrar etməyin.

1. ## Nə lazımdır?

- Telefon (linear təcil və giroskop sensoru üçün)
- Fırlanan ofis kreslosu
- Yapışqan lent (skotç — telefonu kresloya möhkəm bərkitmək üçün)
- Phyphox tətbiqi (məlumatları qeyd etmək üçün)
- Xətkeş

2. ## Qurğu və Səhvlər
- **Yerləşdirmə:** Telefonu kreslonun oturacağına skotçla düz qoyub radius xətti boyunca bərkitdim. Mərkəzi oxdan telefonun mərkəzinə qədər olan məsafəni ($R$) xətkeşlə dəqiq ölçdüm.
- **Kreslonun mailliyi:** Kreslonun mailliyini (-2° və -3°) qeyd etmək vacibdir, çünki bu, qravitasiya komponentinin təsirini nəzərə almağa kömək edir.

3. ## Ölçmələr
- 0.05, 0.10, 0.15 və 0.20 metr olmaqla dörd fərqli radiusda ölçmələr apardıq (hərəsindən 2 run, üstəgəl əlavə testlər).
- Əllə itələyəndə ilk saniyələrdə yaranan xaotik və səs-küylü hissələri kodda zaman pəncərəsi (time window) vasitəsilə kəsib atdıq, yalnız sərbəst yavaşıma (coasting) fazasını saxladıq.

4. ## Hesablama
- Hər fayl üçün təcilin $\omega^2$-dən asılılıq qrafikini çəkib $R_{\text{fit}}$ tapırıq.
- Bütün $R_{\text{fit}}$-ləri əsl $R$-lə müqayisə edərək $R_{\text{fit}} = k \cdot R + d$ xətti qururuq.
- Nəticə: $k = 0.90 \pm 0.26$, $d = -0.014 \pm 0.035\text{ m}$.

5. ## Səhvlərimdən Dərs
- Kreslo tam dayanmamış tələsik yeni fırlatmanı başlatmayın, bu, məlumatları qarışdırır.
- Yalnız bir fırlatmadan ibarət olan yarımçıq test fayllarını (`R0.20_test.csv` kimi) əvvəlcədən təmizləyin.
- Kodda zaman pəncərəsini seçərkən diqqətli olun ki, uyğun nöqtələr düzgün seçilsin.