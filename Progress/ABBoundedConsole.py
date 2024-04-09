from speles_koks import *

#Tiek noteikts maksimālais līmenis
max_limenis = sp.virsotnes[len(sp.virsotnes)-1].limenis
half_limenis = int((sp.virsotnes[len(sp.virsotnes)-1].limenis)/2)+1
print("Half limenis ir: " + str(half_limenis))
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

def alphabeta(virs, alpha, beta, generets):
    #Ja virsotne ir gala līmenī, tad tiek atgriezta novērtējuma vērtība
    if virs[4] > half_limenis:
        generets = True
    if not generets:
        if virs[4] == half_limenis or (virs[1] <= 10) or (virs[1] %2 != 0 and virs[1] %3 != 0):
            return virs[4] + virs[2] - virs[3]
    if generets:
        if virs[4] == max_limenis or (virs[1] <= 10) or (virs[1] %2 != 0 and virs[1] %3 != 0):
            return virs[4] + virs[2] - virs[3]
    #Ja virsotne nav gala līmenī, tad tiek izveidots saraksts ar visiem bērniem
    nakosais_stavoklis = berni(virs)
    #if not isinstance(nakosais_stavoklis, list): pārbauda vai ir saraksts
    #Ja nav saraksts, tad tiek izveidots saraksts
    if not isinstance(nakosais_stavoklis, list):
        nakosais_stavoklis = [nakosais_stavoklis]
    #Ja virsotnes līnenis ir pāra skaitlis, tad tiek izvēlēts minimizēšanas algoritms no minimax funkcijas
    if (virs[4] % 2) == 0:
        #Tiek rekursīvi atgriezta minimālā vērtība no visiem bērniem
        for stavoklis in nakosais_stavoklis:
            svars = alphabeta(stavoklis, alpha, beta, generets)
            if len(stavoklis)<6:
                atk_virsotnes[atk_virsotnes.index(stavoklis)] += [svars]
            beta = min(beta, svars)
            #Pārbaude: ja alfa ir lielāka vai vienāda ar beta, neapsveram ceļu tālāk
            if alpha >= beta:
                print(alpha,"alpha")
                print(beta,"beta")
                print(stavoklis)
                break
        return svars
    #Ja virsotnes līnenis ir nepāra skaitlis, tad tiek izvēlēts maksimizēšanas algoritms no minimax funkcijas
    elif (virs[4] % 2) == 1:
        #Tiek rekursīvi atgriezta maksimālā vērtība no visiem bērniem
        for stavoklis in nakosais_stavoklis:
            svars = alphabeta(stavoklis, alpha, beta, generets)
            if len(stavoklis)<6:
                atk_virsotnes[atk_virsotnes.index(stavoklis)] += [svars]
            alpha = max(alpha, svars) 
            #Pārbaude: ja alfa ir lielāka vai vienāda ar beta, neapsveram ceļu tālāk
            if alpha >= beta:
                print(alpha,"alpha")
                print(beta,"beta")
                print(stavoklis)
                break
        return svars

#Tiek izprintēta alphabeta funkcijas atgrieztā vērtība
# print("Jādodas uz virsotni, kuras novērtējums pēc alphabeta funkcijas ir:")
print(atk_virsotnes)
print(berni(atk_virsotnes[0]))

def rezultati(virsotne):
    if virsotne[2] == virsotne[3]:
        print("rezultāts ir neizšķirts")
        print("pirma speletaja punkti:", virsotne[2],"\notra speletaja punkti:", virsotne[3])
            
    elif virsotne[2] > virsotne[3]:
        print("uzvar pirmais speletajs")
        print("pirma speletaja punkti:", virsotne[2],"\notra speletaja punkti:", virsotne[3])
                

    elif virsotne[2] < virsotne[3]:
        print("uzvar otrais speletajs")
        print("pirma speletaja punkti:", virsotne[2],"\notra speletaja punkti:", virsotne[3])
                

def spele_alphabeta(kurs_sak, virsotne, generets):
    print("Pašreizejais skaitlis:",virsotne[1])
    if virsotne[1] %2 != 0 and virsotne[1] %3 or virsotne[1] <= 10:
        rezultati(virsotne)
        return
    else:
        if kurs_sak == "pc":
            print(virsotne)
            print("Datora gajiens:")
            result = alphabeta(virsotne,float('-inf'), float('inf'), generets)
            nakosais_gajiens = berni(virsotne)
            if virsotne[4] == half_limenis:
                generets = True
                result = alphabeta(virsotne,float('-inf'), float('inf'), generets)
            else:
                generets = False
                result = alphabeta(virsotne,float('-inf'), float('inf'), generets)
            if virsotne[4] == half_limenis:
                generets = True
                result = alphabeta(virsotne,float('-inf'), float('inf'), generets)
            else:
                generets = False
                result = alphabeta(virsotne,float('-inf'), float('inf'), generets)
            if nakosais_gajiens[0] == virsotne:
                for x in sp.virsotnes:
                        if x.limenis > half_limenis:
                            print("Tika uzģenerēta otrā daļa virsotnēm")
                            generets = True
                            atk_virsotnes.append([x.id,x.skaitlis,x.speletajs1,x.speletajs2,x.limenis])
                for y in atk_virsotnes:
                    if y[4] >= half_limenis:
                        alphabeta(y,float('-inf'), float('inf'), generets)
                nakosais_gajiens = berni(virsotne)
                result = alphabeta(virsotne,float('-inf'), float('inf'), generets)
            print("Nākošais gājiens: " + str(nakosais_gajiens))
            if len(nakosais_gajiens) == 2:
                if nakosais_gajiens[0][5] == nakosais_gajiens[1][5] == result:
                    pirma_virsotne = virsotne[1]/nakosais_gajiens[0][1]
                    otra_virsotne = virsotne[1]/nakosais_gajiens[1][1]
                    if pirma_virsotne > otra_virsotne:
                        datora_izvele = nakosais_gajiens[0]
                        datora_dalitajs = virsotne[1]/datora_izvele[1]
                        print("Dators izvēlējās sadalit ar:", datora_dalitajs)
                        spele_alphabeta("human", nakosais_gajiens[0], generets)
                    else:
                        datora_izvele = nakosais_gajiens[1]
                        datora_dalitajs = virsotne[1]/datora_izvele[1]
                        print("Dators izvēlējās sadalit ar:", datora_dalitajs)
                        spele_alphabeta("human", nakosais_gajiens[1], generets)
                    
                elif nakosais_gajiens[0][5] == result and nakosais_gajiens[1][5] != result:
                    datora_izvele = nakosais_gajiens[0]
                    datora_dalitajs = virsotne[1]/datora_izvele[1]
                    print("Dators izvēlējās sadalit ar:", datora_dalitajs)
                    spele_alphabeta("human", nakosais_gajiens[0], generets)

                elif nakosais_gajiens[1][5] == result and nakosais_gajiens[0][5] != result:
                    datora_izvele = nakosais_gajiens[1]
                    datora_dalitajs = virsotne[1]/datora_izvele[1]
                    print("Dators izvēlējās sadalit ar:", datora_dalitajs)
                    spele_alphabeta("human", nakosais_gajiens[1], generets)
            elif len(nakosais_gajiens) == 1:
                    datora_izvele = nakosais_gajiens
                    print(datora_izvele)
                    datora_dalitajs = virsotne[1]/datora_izvele[0][1]
                    print("Dators izvēlējās sadalit ar:", datora_dalitajs)
                    spele_alphabeta("human", nakosais_gajiens[0], generets)

    


        elif kurs_sak == "human":
            nakama_virsotne = 0
            cilveka_gajiens = input("Ievadiet skaitli, ar kuru vēlaties dalīt pašreizējo skaitli: 2 vai 3\n")
            if virsotne[1] % int(cilveka_gajiens) == 0:
                result = virsotne[1] / int(cilveka_gajiens)
                if speles_sakums == "2":
                    if cilveka_gajiens == "2":
                        for x in atk_virsotnes:
                            if (x[1] == result) and ((virsotne[2])==x[2]) and ((virsotne[3]+2)==x[3]):
                                nakama_virsotne = x
                                break
                    else:
                        for x in atk_virsotnes:
                            if (x[1] == result) and ((virsotne[2]+3)==x[2]) and ((virsotne[3])==x[3]):
                                nakama_virsotne = x
                                break
                    if nakama_virsotne == 0:
                        for x in sp.virsotnes:
                            if x.limenis > half_limenis:
                                generets = True
                                atk_virsotnes.append([x.id,x.skaitlis,x.speletajs1,x.speletajs2,x.limenis])
                        if cilveka_gajiens == "2":
                            for y in atk_virsotnes:
                                if (y[1] == result) and ((virsotne[2]+2)==y[2]) and ((virsotne[3])==y[3]):
                                    nakama_virsotne = y
                                    break
                        else:
                            for y in atk_virsotnes:
                                if (y[1] == result) and ((virsotne[2])==y[2]) and ((virsotne[3]+3)==y[3]):
                                    nakama_virsotne = y
                                    break
                else:
                    if cilveka_gajiens == "2":
                        for x in atk_virsotnes:
                            if (x[1] == result) and ((virsotne[2]+2)==x[2]) and ((virsotne[3])==x[3]):
                                nakama_virsotne = x
                                break
                    else:
                        for x in atk_virsotnes:
                            if (x[1] == result) and ((virsotne[2])==x[2]) and ((virsotne[3]+3)==x[3]):
                                nakama_virsotne = x
                                break
                if nakama_virsotne == 0:
                        for x in sp.virsotnes:
                            if x.limenis > half_limenis:
                                generets = True
                                atk_virsotnes.append([x.id,x.skaitlis,x.speletajs1,x.speletajs2,x.limenis])
                        if cilveka_gajiens == "2":
                            for y in atk_virsotnes:
                                if (y[1] == result) and ((virsotne[2])==y[2]) and ((virsotne[3]+2)==y[3]):
                                    nakama_virsotne = y
                                    break
                        else:
                            for y in atk_virsotnes:
                                if (y[1] == result) and ((virsotne[2]+3)==y[2]) and ((virsotne[3])==y[3]):
                                    nakama_virsotne = y
                                    break
                spele_alphabeta("pc", nakama_virsotne, generets)
            else:
                print("Ar jusu skaitli:", cilveka_gajiens, "nevar iegut veselo rezulatatu")
                spele_alphabeta("human", virsotne, generets)






def pirmais_gajiens():
    global speles_sakums
    speles_sakums = input("izvēlieties, kurš sāks pirmais. Ievadiet pc, lai dators būtu pirmais vai human, lai jūs\n1. dators\n2. human\n")
    if speles_sakums == "1":
        spele_alphabeta("pc", atk_virsotnes[0], False)
    elif speles_sakums == "2":
        spele_alphabeta("human", atk_virsotnes[0], False)

    

def sak_spele():
    speles_sakums = input("Ievadiet start, lai sāktu spēli, vai exit, lai izietu\n1. Start\n2. Exit\n")
    if speles_sakums == "1":
        pirmais_gajiens()

sak_spele()
