from speles_koks import *

#Tiek noteikts maksimālais līmenis
max_limenis = sp.virsotnes[len(sp.virsotnes)-1].limenis
if max_limenis % 2 == 0:
    dzilums = max_limenis / 2
else:
    dzilums = int(max_limenis / 2 ) + 1
#Tiek izveidots saraksts ar visām virsotnēm
atk_virsotnes=[]
for x in sp.virsotnes:
    atk_virsotnes.append([x.id,x.skaitlis,x.speletajs1,x.speletajs2,x.limenis])
#Tiek izveidota funkcija, kas atgriež visus bērnus no konkrētas virsotnes
def berni(pasreizeja_virsotne):
    berni = []
    a = []
    a = sp.loki.get(pasreizeja_virsotne[0])
    for x in a:
        for y in atk_virsotnes:
            if x == y[0]:
                berni.append(y)
    if len(berni) == 0:
        berni.append(pasreizeja_virsotne)
    return berni

#Tiek izveidota minimax funkcija, kā ievades parametrs ir virsotnes objekts, vai arī saraksts ar virsotnes objektiem
# Funkcijas paraugs ir ņemts pēc grāmatas piemēra
#Coppin B. (2004). Artificial Intelligence Illuminated. Jones and Bartlett Publishers.
# 150lpp.
def minimax(virs,gen):
    #Ja virsotne ir gala līmenī, tad tiek atgriezta novērtējuma vērtība
    if virs[4] > dzilums:
        gen = True
    if gen:
        if virs[4] == max_limenis or (virs[1] <= 10) or (virs[1] %2 != 0 and virs[1] %3 != 0):
            return virs[4] + virs[2] - virs[3]
    #Ja virsotne nav gala līmenī, tad tiek izveidots saraksts ar visiem bērniem
    if not gen:
        if (virs[4]) == dzilums:
            return virs[4] + virs[2] - virs[3]
    nakosais_stavoklis = berni(virs)
    #if not isinstance(nakosais_stavoklis, list): pārbauda vai ir saraksts
    #Ja nav saraksts, tad tiek izveidots saraksts
    if not isinstance(nakosais_stavoklis, list):
        nakosais_stavoklis = [nakosais_stavoklis]
    #Ja virsotnes līnenis ir pāra skaitlis, tad tiek izvēlēts minimizēšanas algoritms no minimax funkcijas
    if (virs[4] % 2) == 0:
        #Tiek rekursīvi atgriezta minimālā vērtība no visiem bērniem
        return min(minimax(stavoklis,gen) for stavoklis in nakosais_stavoklis)
    #Ja virsotnes līnenis ir nepāra skaitlis, tad tiek izvēlēts maksimizēšanas algoritms no minimax funkcijas
    elif (virs[4] % 2) == 1:
        #Tiek rekursīvi atgriezta maksimālā vērtība no visiem bērniem
        return max(minimax(stavoklis,gen) for stavoklis in nakosais_stavoklis)
