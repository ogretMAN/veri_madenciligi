#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Copyright 2020 Selçuk Sinan KIRAT

English Text
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

---------------------------------------------------------

Türkçe Metin
Apache Lisansı, Sürüm 2.0 (işbu “Lisans”) ile lisanslanan
bu dosyayı, işbu lisansla uyumlu olan durumlar dışında kullanamazsınız.
Lisansın bir kopyasını        

http://www.apache.org/licenses/LICENSE-2.0

adresinden temin edebilirsiniz.
Yürürlükteki bir yasada belirtilmediği veya yazılı olarak
beyan edilmediği sürece, işbu lisans altında dağıtılan
yazılım “hiçbir değişiklik yapılmadan” esasıyla dağıtılmış
olup, açıkça veya üstü kapalı olarak, HİÇBİR TEMİNAT VEYA
KOŞUL İÇERMEZ. Özel dil uygulama izinleri ve işbu lisans altındaki kısıtlamalar için lisansa bakınız.

Selçuk Sinan KIRAT (Bilgisayar Öğretmeni)
http://www.selcuksinankirat.com

"""

import birliktelik as b

# Birliktelik("dosya_adi.txt", destekEsikDegeri, guvenEsikDegeri)
B1 = b.Birliktelik("vt.txt", 0.5, 0.9)
B1.verileriYaz()
B1.ikiliKurallar()
B1.ucluKurallar()