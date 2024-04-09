## ***MI_33grupa_projekts***
 
#Lai sāktu spēli, tā ir jāpalaiž no user_gui.py faila

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
4. Tika izveidots spēles koka izpētes algoritms, kurš novērtē uzvaras virotnes un datora gājienus.
5. Tiek izveidota HNF balstoties uz spēles nosacījumiem.
6. Mini-Max un Alpha-Beta algoritmu izveide, lai dators atrastu optimālākos ceļus uz uzvaru.
7. Grafiskās saskarnes izveide.

#### Papildus ieviestie nosacījumi
1. Tiek ģenerēti 5 skaitļi, kas dalās ar 36, nevis gan ar 2, gan 3. Noteikumi mainīti, lai spēle būtu garāka un skaitļi varētu dalīties vairāk kā 2-3 reizes.
2. Tiek pielietota Bounded-MiniMax un Bounded-AlphaBeta funkcija, tā, lai var izmantot HNF. (Coppin B. (2004). Artificial Intelligence Illuminated. Jones and Bartlett Publishers. 151.lpp)
