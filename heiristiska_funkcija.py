#Tiek veikts imports no speles_koks.py
from speles_koks import *
#Funkcija, kas piešķir svaru virsotnēm datora gājienos
def svara_pieskirsana(sak_dators):
    #Izveido sarakstu, kurā tiks glabāti virsotņu svari
    virsotnu_svari = []
    for x in sp.virsotnes:
        #Ja sāk dators un līmenis uz kuru dodas dators ir pāra skaitlis, tad tiek piešķirts svars
        if sak_dators and x.limenis%2 == 0:
            virsotnes_svars = x.limenis + x.speletajs1 - x.speletajs2
            #Pievieno virsotni un tās svaru sarakstam
            virsotnu_svari.append([x.id, virsotnes_svars])
            #Ja nesāk dators un līmenis uz kuru dodas dators ir nepāra skaitlis un nav 1, tad tiek piešķirts svars
        if not sak_dators and x.limenis%2 != 0 and x.limenis != 1:
            virsotnes_svars = x.limenis + x.speletajs1 - x.speletajs2
            #Pievieno virsotni un tās svaru sarakstam
            virsotnu_svari.append([x.id, virsotnes_svars])
    return virsotnu_svari
print("Virsotņu svari uz kurām var iet dators:")
print(svara_pieskirsana(sak_dators))

#Funkcija, kas atrod visus iespējamos lokus.
def atrast_lokus():
    visi_loki = []
    #Iziet cauri visām virsotnēm un pārbauda, vai ir loki
    for x in sp.virsotnes:
        try: 
            #Ja ir loki, tad tos pievieno sarakstam
            for y in sp.loki[x.id]:
                visi_loki.append([x.id, y])
        except KeyError:
            break
    return visi_loki

#Funkcija, kas apvieno virsotnes ar svaru un loku
def masivs_ar_svaru(masivs_ar_svaru, loki):
    masivs_ar_svaru = []
    #Iziet cauri visiem lokiem un to svariem
    for x in loki:
        for y in masivs_ar_svaru:
            #
            if x[1] == y[0]:
                #Pievieno virsotni, svaru un loku sarakstam
                masivs_ar_svaru.append([x[0],x[1],y[1]])
    return masivs_ar_svaru
#Izvada virsotnes ar to lokiem datora gājienos un mērķa svaru
print("Virsotnes loki ar svaru datora gājienos:")
print(masivs_ar_svaru(svara_pieskirsana(sak_dators),atrast_lokus()))