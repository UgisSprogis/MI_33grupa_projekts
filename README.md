## ***MI_33grupa_projekts***
### Definētās prasības spēles programmatūrai.
- Spēles sākumā spēles programmatūra gadījuma ceļā saģenerē 5 skaitļus diapazonā no 10000 līdz 20000
- Skaitļiem obligāti jādalās gan ar 3, gan ar 2. (Tātad dalās ar 6)
- Cilvēks-spēlētājs izvēlas, ar kuru no saģenerētajiem skaitļiem viņš vēlas sākt spēli. 

#### Spēles apraksts.
Spēles sākumā ir dots cilvēka-spēlētāja izvēlētais skaitlis. Abiem spēlētājiem ir 0 punktu. Spēlētāji izdara gājienus pēc kārtas, katrā gājienā dalot pašreizējā brīdī esošu skaitli ar 2 vai 3. Skaitli ir iespējams sadalīt tikai tajā gadījumā, ja rezultātā veidojas vesels skaitlis. Ja tiek veikta dalīšana ar 2, tad pretinieka punktu skaitam tiek pieskaitīti 2 punkti. Ja tiek veikta dalīšana ar 3, tad paša spēlētāja punktu skaitam tiek pieskaitīti 3 punkti. Spēle beidzas, kā tikko ir iegūts skaitlis, kas ir mazāks vai vienāds ar 10. Ja spēlētāju punktu skaits ir vienāds, tad rezultāts ir neizšķirts. Pretējā gadījumā uzvar spēlētājs, kam ir vairāk punktu.

#### Kas tiek paveikts šī projekta ietvaros.
1. Tiek ģenerēti 5 skaitļi, kas dalās ar 6 (ar 2 un 3)
2. Tiek ģenerēts spēles koks izvēlētajam skaitlim.
3. Tiek atrastas uzvaras virsotnes, atkarībā vai sāk dators, vai sāk spēlētājs.
4. Ar heiristiskas funkcijas palīdzību datora gājienos, tiek novērtētas virsotnes un to svari.
5. Mini-Max un Alpha-Beta algoritmu izveide, lai dators atrastu optimālākos ceļus uz uzvaru.
6. Grafiskās saskarnes izveide.