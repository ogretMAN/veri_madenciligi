# veri_madenciligi
Birliktelik Kuralları (Association Rules)

Veri madenciliği ve makine öğrenmesinde kullanılan Birliktelik Kuralları (Association Rules) algoritması için geliştirdiğim Türkçe fonksiyon ve değişken isimlendirmelerinden oluşan python programıdır.

KULLANIMI
1. birliktelik.py dosyasını projenize dahil edin
    import birliktelik as b
    
2. Birliktelik nesnesini örnekleyin  
    Kullanım    birliktelik("dosyaAdi", "destekEsikDegeri", "guvenEsikDegeri")
    B1 = b.Birliktelik("vt.txt", 0.5, 0.9)

3. vt içindeki verileri görüntülemek için
    B1.verileriYaz()
    
4. İki öğeli birliktelik kuralları (A => B şeklinde)
    B1.ikiliKurallar()
    
5. Üç öğeli birliktelik kuralları (A, B => C ya da A => B, C vb. kombinasyonlar şeklinde)
    B1.ucluKurallar()
    
NOT: Yazdığım program txt dosyasını okumaktadır. txt dosyası içerisindeki tüm veriler bitişik, virgüllerle birbirinden ayrılmış olmalıdır.

Örnek
veri1,veri2,veri4...
veri2,veri3,veri1...
.
.
.
