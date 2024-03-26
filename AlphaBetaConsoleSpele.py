from speles_koks import *

#Tiek noteikts maksimālais līmenis
max_limenis = sp.virsotnes[len(sp.virsotnes)-1].limenis
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
    return berni

def alphabeta(virs, alpha, beta):

    #Ja virsotne ir gala līmenī, tad tiek atgriezta novērtējuma vērtība
    if virs[4] == max_limenis:
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
            svars = alphabeta(stavoklis, alpha, beta)
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
            svars = alphabeta(stavoklis, alpha, beta)
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
        if virsotne[2] == virsotne[3]:
            return print("rezultāts ir neizšķirts")
            
        elif virsotne[2] > virsotne[3]:
            print("uzvar pirmais speletajs")
            return print("pirma speletaja punkti:", virsotne[2],"\notra speletaja punkti:", virsotne[3])
                

        elif virsotne[2] < virsotne[3]:
            print("uzvar otrais speletajs")
            return print("pirma speletaja punkti:", virsotne[2],"\notra speletaja punkti:", virsotne[3])
                

def spele(kurs_sak, virsotne):
    cond = True
    while cond:
        print("Pašreizejais skaitlis:",virsotne[1])
        if virsotne[1] %2 != 0 and virsotne[1] %3 !=0:
            rezultati(virsotne)
            cond = False
        else:

            if kurs_sak == "pc":
                print(virsotne)
                print("Datora gajiens:")
                result = alphabeta(virsotne,float('-inf'), float('inf'))
                nakosais_gajiens = berni(virsotne)
                print(nakosais_gajiens)
                if len(nakosais_gajiens) == 2:
                    if nakosais_gajiens[0][5] == nakosais_gajiens[1][5] == result:
                        pirma_virsotne = nakosais_gajiens[0][4] + nakosais_gajiens[0][2] - nakosais_gajiens[0][3]
                        otra_virsotne = nakosais_gajiens[1][4] + nakosais_gajiens[1][2] - nakosais_gajiens[1][3]
                        if pirma_virsotne > otra_virsotne:
                            datora_izvele = nakosais_gajiens[0]
                            datora_dalitajs = virsotne[1]/datora_izvele[1]
                            print("Dators izvēlējās sadalit ar:", datora_dalitajs)
                            spele("human", nakosais_gajiens[0])
                        else:
                            datora_izvele = nakosais_gajiens[1]
                            datora_dalitajs = virsotne[1]/datora_izvele[1]
                            print("Dators izvēlējās sadalit ar:", datora_dalitajs)
                            spele("human", nakosais_gajiens[1])
                    
                    elif nakosais_gajiens[0][5] == result and nakosais_gajiens[1][5] != result:
                        datora_izvele = nakosais_gajiens[0]
                        datora_dalitajs = virsotne[1]/datora_izvele[1]
                        print("Dators izvēlējās sadalit ar:", datora_dalitajs)
                        spele("human", nakosais_gajiens[0])

                    elif nakosais_gajiens[1][5] == result and nakosais_gajiens[0][5] != result:
                        datora_izvele = nakosais_gajiens[1]
                        datora_dalitajs = virsotne[1]/datora_izvele[1]
                        print("Dators izvēlējās sadalit ar:", datora_dalitajs)
                        spele("human", nakosais_gajiens[1])
                

                elif len(nakosais_gajiens) == 1:
                        datora_izvele = nakosais_gajiens
                        print(datora_izvele)
                        datora_dalitajs = virsotne[1]/datora_izvele[0][1]
                        print("Dators izvēlējās sadalit ar:", datora_dalitajs)
                        spele("human", nakosais_gajiens[0])

    


            elif kurs_sak == "human":
                cilveka_gajiens = input("Ievadiet skaitli, ar kuru vēlaties dalīt pašreizējo skaitli: 2 vai 3\n")
                if virsotne[1] % int(cilveka_gajiens) == 0:
                    result = virsotne[1] / int(cilveka_gajiens)
                    for x in atk_virsotnes:
                        if x[1] == result:
                            nakama_virsotne = x
                            break
                    spele("pc", nakama_virsotne)
                else:
                    print("Ar jusu skaitli:", cilveka_gajiens, "nevar iegut veselo rezulatatu")





def pirmais_gajiens():
    while True:
        speles_sakums = input("izvēlieties, kurš sāks pirmais. Ievadiet pc, lai dators būtu pirmais vai human, lai jūs\n")
        if speles_sakums == "pc":
            spele("pc", atk_virsotnes[0])
        elif speles_sakums == "human":
            spele("human", atk_virsotnes[0])

    

def sak_spele():
    while True:
        speles_sakums = input("Ievadiet start, lai sāktu spēli, vai exit, lai izietu\n")
        if speles_sakums == "start":
            pirmais_gajiens()
        elif speles_sakums == "exit":
            break


sak_spele()
