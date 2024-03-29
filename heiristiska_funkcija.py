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

#Tiek piešķirti svari pēc heiristiskas funkcijas min-max un alfa-beta algoritma
def svara_pieskirsana_beigam(vai_izsaukts):
    virsotnu_svari = []
    max_limenis = sp.virsotnes[len(sp.virsotnes)-1].limenis
    #Nosacījumi gan dalāmam, gan nedalāmam skaitlim, kad to dala uz pusi
    if max_limenis%2 == 0:
        puslimenis = int(max_limenis/2)
    else:
        puslimenis = int(max_limenis/2+1)
    #Piešķir pirmajai koka pusei svaru
    if not vai_izsaukts and max_limenis > 3:
        vai_izsaukts = True
        print("Pirmā daļa koka svariem:")
        #Cikls, kas piešķir pirmajai koka daļas beigām heiristisko vērtību (Pirmajā reizē)
        for x in (sp.virsotnes):
            if x.limenis > puslimenis:
                break
            if x.limenis == puslimenis:
                virsotnes_svars = x.limenis + x.speletajs1 - x.speletajs2
                #Pievieno virsotni un tās svaru sarakstam
                virsotnu_svari.append([x.id, virsotnes_svars])
    #Piešķir otrai koka pusei svaru, kad tas tiek izsaukts otru reizi
    elif vai_izsaukts or max_limenis < 3:
        if max_limenis < 35:
            print("Līmenis pārāk mazs, lai koku dalītu")
        print("Otrā daļa koka svariem:")
        for x in (sp.virsotnes):
            if x.limenis == max_limenis:
                virsotnes_svars = x.limenis + x.speletajs1 - x.speletajs2
                #Pievieno virsotni un tās svaru sarakstam
                virsotnu_svari.append([x.id, virsotnes_svars])
    return virsotnu_svari



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
# print("Virsotnes loki ar svaru datora gājienos:")
# print(masivs_ar_svaru(svara_pieskirsana(sak_dators),atrast_lokus()))
print("Svara pieskirsana beigam")

vai_izsaukts = True # Mainīgais priekš tā, lai svars spētu orientēties kurai daļai grafa piešķirt svaru
print(svara_pieskirsana_beigam(False))
print(svara_pieskirsana_beigam(True))

print(sp.virsotnes)
def minimax():
    next_limenis = []
    berni = []
    max_limenis = sp.virsotnes[len(sp.virsotnes)-1].limenis
    labakie_celi = []
    for x in sp.virsotnes:
        if x.limenis == max_limenis-1:
            next_limenis.append(x.id)
    for x in sp.loki:
        for y in next_limenis:
            if y == x:
                # virsotnes_svars = x.limenis + x.speletajs1 - x.speletajs2
                berni.append([y,sp.loki[x]])
    print("Berni")
    
    return berni
        # try: 
        #     #Ja ir loki, tad tos pievieno sarakstam
        #     for y in sp.loki[x.id]:
        #         next_limenis.append([x.id, y[0]])
        # except KeyError:
        #     break
            
print(minimax())



sak_dators = True
#Funkcija, kas atgriež uzvaras strupceļus izvēlētajai secībai, kā arguments tiek padots , kurš pēc kārtas sāk dators
def uzvaras_strupceli(sak_dators):
    #Izveido sarakstu, kurā tiks glabāti uzvaras strupceļi
    uzvaras_strupceli = []
    #Pārbauda, vai virsotne ir uzvaras strupceļa virsotne atkarībā no noteiktās spēles secības
    for x in sp.virsotnes:
        #Ja skaitlis dalās ar 3 un 2, tad tā nav uzvaras strupceļa virsotne
        if ((x.skaitlis%3)!=0) and ((x.skaitlis%2)!=0) and (sak_dators==True) and (x.speletajs1>x.speletajs2):
            uzvaras_strupceli.append(x.id)
        elif ((x.skaitlis%3)!=0) and ((x.skaitlis%2)!=0) and (sak_dators==False) and (x.speletajs2>x.speletajs1):
            uzvaras_strupceli.append(x.id)
    return uzvaras_strupceli

print("Uzvaras virsotnes datoram - ", uzvaras_strupceli(sak_dators))