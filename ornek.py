#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
English License Notification

<Python Program of Data Mining Association Rules>

    Copyright (C) <2020>  <Selçuk Sinan KIRAT>
    
    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.
    
    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.
    
    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
    
---------------------------------------------------------

Türkçe Lisans Bildirimi

<Veri Madenciliği Birliktelik Kuralları Python Programı>

    Copyright (C) <2020> <Selçuk Sinan KIRAT>
    
    Bu program özgür yazılımdır: Özgür Yazılım Vakfı tarafından yayımlanan GNU Genel Kamu Lisansı’nın sürüm 3 ya da 
    (isteğinize bağlı olarak) daha sonraki sürümlerinin hükümleri altında yeniden dağıtabilir ve/veya değiştirebilirsiniz.
    
    Bu program, yararlı olması umuduyla dağıtılmış olup, programın BİR TEMİNATI YOKTUR; TİCARETİNİN YAPILABİLİRLİĞİNE VE 
    ÖZEL BİR AMAÇ İÇİN UYGUNLUĞUNA dair bir teminat da vermez. Ayrıntılar için GNU Genel Kamu Lisansı’na göz atınız.
    
    Bu programla birlikte GNU Genel Kamu Lisansı’nın bir kopyasını elde etmiş olmanız gerekir. 
    Eğer elinize ulaşmadıysa <http://www.gnu.org/licenses/> adresine bakınız.
    
    Tükrçe çeviri: http://ozgurlisanslar.org.tr/gpl/gpl-v3/
    
    Selçuk Sinan KIRAT (Bilgisayar Öğretmeni)
    http://www.selcuksinankirat.com
"""

import birliktelik as b

# Birliktelik("dosya_adi.txt", destekEsikDegeri, guvenEsikDegeri)
B1 = b.Birliktelik("vt.txt", 0.5, 0.9)
B1.verileriYaz()
B1.ikiliKurallar()
B1.ucluKurallar()
