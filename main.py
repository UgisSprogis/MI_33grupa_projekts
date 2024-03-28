#Tiek importēts random, lai varētu izvēlēties nejaušus skaitļus
import random
#Spēles skaitļu ģenerators
def speles_skaitli():
    #Izveido sarakstus skaitlu_saraksts un pieci_skaitli
    skaitlu_saraksts = set()
    pieci_skaitli = set()
    #Izvēlas skaitļus no 20000 līdz 50000
    #Ja skaitlis dalās ar 6 (dalās ar 2 un 3), tad to pievieno sarakstam
    for i in range(20000,50000):
        if i%36==0:
            skaitlu_saraksts.add(i)
            #Izvēlas 5 nejaušus skaitļus no saraksta
            #Izvēlētos skaitļus pievieno pieci_skaitli
            #Tiek izmantots sorted, lai nebūtu konflikti ar random.sample
    pieci_skaitli = random.sample(sorted(skaitlu_saraksts), 5)
    return pieci_skaitli

#Šī funkcija ļauj izvēlēties skaitli no pieci_skaitli saraksta
def skaitla_izvele():
    pieci_skaitli = speles_skaitli()
    print("Spēles skaitļi ir:")
    #Izvada visus pieci_skaitli saraksta skaitļus
    for x in pieci_skaitli:
        print(f"{pieci_skaitli.index(x)+1}. ", x)
    #Ļauj cilvēkam izvēlēties skaitli no saraksta
    izveletais_skaitlis = int(input("Izvēlieties skaitli no spēles skaitļiem: "))-1
    sk = pieci_skaitli[izveletais_skaitlis]
    #Izvada izvēlēto skaitli
    print(f"Jūsu izvēlētais skaitlis ir: {sk}")
    return sk

#########################################################################

class Virsotne:
    def __init__(self, id, skaitlis, speletajs1, speletajs2, limenis):
        self.id=id
        self.skaitlis=skaitlis
        self.speletajs1=speletajs1
        self.speletajs2=speletajs2
        self.limenis=limenis


#Spēles koka klase
class SpelesKoks:
    def __init__(self):
        self.virsotnes = []
        self.loki=dict()
    def pievienot_virsotni(self, virsotne):
        self.virsotnes.append(virsotne)
    def pievienot_loku(self, sak_virsotne_id, beig_virsotne_id):
        self.loki[sak_virsotne_id] = self.loki.get(sak_virsotne_id, []) + [beig_virsotne_id]
#funkcija, kas parbauda gājienu, kā parametrus saņem gājiena tipu, visu virsotņu sarakstu un pašreizējo virsotni
def gajiens(gajiena_tips,gen_virsotnes,pasreizeja_virsotne):
    #Ja gājiens ir 2, tad dalītājs ir 2, ja 3, tad dalītājs ir 3
    if gajiena_tips=='2':
        dalitajs = 2
    else:
        dalitajs = 3
    #Ja skaitlis dalās ar dalītāju, tad turpmākais kods izveidos jaunu virsotni un atjaunos informāciju par virsotnes datiem
    if (pasreizeja_virsotne[1]%dalitajs==0) and (pasreizeja_virsotne[1]>10):
        global j
        id_new = 'A'+str(j)
        j+=1
        #jaunais skaitlis ir pašreizējās virsotnes saraksta pirmais elements, kas norāda uz skaitli.
        jaunais_skaitlis = pasreizeja_virsotne[1]
        #Šeit tiek iegūts jaunais skaitlis atbilstoši gājienu tipam
        if (gajiena_tips=='2') and (pasreizeja_virsotne[1]%2==0):
            jaunais_skaitlis = pasreizeja_virsotne[1]/2
        elif (gajiena_tips=='3') and (pasreizeja_virsotne[1]%3==0):
            jaunais_skaitlis = pasreizeja_virsotne[1]/3
        #Šajā koda blokā tiek pārvaudīts, kāds ir spēles līmenis, un tad tiek atbilstosi veiktajam gājienam un spēles nosacījumiem tiek piesķirti spēlētājiem punkti.
        if (gajiena_tips=='2'):
            if (pasreizeja_virsotne[4]%2)==0:
                speletajs1_new=pasreizeja_virsotne[2]+int(gajiena_tips)
                speletajs2_new=pasreizeja_virsotne[3]
            else:
                speletajs1_new=pasreizeja_virsotne[2]
                speletajs2_new=pasreizeja_virsotne[3]+int(gajiena_tips)
        else:
            if (pasreizeja_virsotne[4]%2)==0:
                speletajs1_new=pasreizeja_virsotne[2]
                speletajs2_new=pasreizeja_virsotne[3]+int(gajiena_tips)
            else:
                speletajs1_new=pasreizeja_virsotne[2]+int(gajiena_tips)
                speletajs2_new=pasreizeja_virsotne[3]
        #Tiek atjaunots spēles līmenis
        limenis_new=pasreizeja_virsotne[4]+1
        #Izveido jauno virsotni
        jauna_virsotne=Virsotne(id_new,jaunais_skaitlis,speletajs1_new,speletajs2_new,limenis_new)
        #Pārbauda duplikātu virsotnes
        virsotnes_parbaude=False
        #i norāda uz virsotni ejot cauri visām iterācijām
        i=0
        #Kamēr nav pārbaudītas visas virsotnes un nav atrasts neviens dublikāts, tad tiek turpināts cikls
        while (not virsotnes_parbaude) and (i<=len(sp.virsotnes)-1):
            if (sp.virsotnes[i].skaitlis==jauna_virsotne.skaitlis) and (sp.virsotnes[i].speletajs1==jauna_virsotne.speletajs1) and (sp.virsotnes[i].speletajs2==jauna_virsotne.speletajs2) and (sp.virsotnes[i].limenis==jauna_virsotne.limenis):
                virsotnes_parbaude=True
            else:
                i+=1
        #Ja nav atrasts neviens dublikāts, tad tiek pievienota jauna virsotne un loks
        if not virsotnes_parbaude:
            sp.pievienot_virsotni(jauna_virsotne)
            gen_virsotnes.append([id_new,jaunais_skaitlis,speletajs1_new,speletajs2_new,limenis_new])
            sp.pievienot_loku(pasreizeja_virsotne[0],id_new)
        else:
            j-=1
            sp.pievienot_loku(pasreizeja_virsotne[0],sp.virsotnes[i].id)

#Izveido spēles koka objektu
sp=SpelesKoks()
#Izveido sarakstu, kurā tiks glabātas virsotnes
gen_virsotnes = []
#Izvēlas skaitli no saraksta
speles_skaitlis = skaitla_izvele()
#Izvada izvēlēto skaitli
print("Spēles skaitlis ir:", speles_skaitlis)
#Pievieno pirmo virsotni
sp.pievienot_virsotni(Virsotne("A1", speles_skaitlis, 0, 0, 1))
#Pievieno pirmo virsotni sarakstam
gen_virsotnes.append(["A1", speles_skaitlis, 0, 0, 1])
#Šis mainīgais skaita virsotnes. Sākas ar 2, tāpēc ka pirmā virsotne jau ir pievienota
j=2
#Kamēr virsotņu saraksts nav tukšs, tad tiek veikti gājieni
while len(gen_virsotnes)>0:
    pasreizeja_virsotne=gen_virsotnes[0]
    #Tiek veikti gājieni, pēc kārtas 2 un 3, ja tie ir iespējami
    gajiens('2',gen_virsotnes,pasreizeja_virsotne)
    gajiens('3',gen_virsotnes,pasreizeja_virsotne)
    #Pēc gājiena tiek izdzēsta virsotne no saraksta
    gen_virsotnes.pop(0)

#########################################################################

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

#########################################################################
#                        Minimax funkcija                               #

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

#########################################################################
#                        AlphaBeta funkcija                             #

def alphabeta(virs, alpha, beta, generets):
    #Ja virsotne ir gala līmenī, tad tiek atgriezta novērtējuma vērtība
    if virs[4] > dzilums:
        generets = True
    if not generets:
        if virs[4] == dzilums or (virs[1] <= 10) or (virs[1] %2 != 0 and virs[1] %3 != 0):
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
                break
        return svars

#########################################################################
#                           Spēles loģika                               #

def rezultats(virsotne):
    if virsotne[2] == virsotne[3]:
        print(f"Rezultāts ir neizšķirts {virsotne[2]}:{virsotne[3]}")
    elif virsotne[2] > virsotne[3]:
        print(f"Uzvar pirmais spēlētājs {virsotne[2]}:{virsotne[3]}")
    elif virsotne[2] < virsotne[3]:
        print(f"Uzvar otrais spēlētājs {virsotne[2]}:{virsotne[3]}")

def pirmais_gajiens_minimax():
    global sacejs
    sacejs = input("izvēlieties, kurš sāks pirmais. Ievadiet 1, lai spēli sāktu dators vai 2, lai spēli sāktu cilvēks\n1. dators\n2. cilvēks\n")
    if sacejs == "1":
        spele_minimax("dators", atk_virsotnes[0],False)
    elif sacejs == "2":
        spele_minimax("cilvēks", atk_virsotnes[0],False)

def pirmais_gajiens_alphabeta():
    global sacejs
    sacejs = input("izvēlieties, kurš sāks pirmais. Ievadiet 1, lai spēli sāktu dators vai 2, lai spēli sāktu cilvēks\n1. dators\n2. cilvēks\n")
    if sacejs == "1":
        spele_alphabeta("dators", atk_virsotnes[0],False)
    elif sacejs == "2":
        spele_alphabeta("cilvēks", atk_virsotnes[0],False)

def izvelies_algoritmu():
    algoritms = input("Izvēlies algoritmu, ar kuru vēlies spēlēt: 1 - MiniMax, 2 - AlphaBeta\n")
    if algoritms == "1":
        pirmais_gajiens_minimax()
    elif algoritms == "2":
        pirmais_gajiens_alphabeta()

def spele_minimax(kurs_sak, virsotne,gen):
    print(f"{kurs_sak} iet un spēles skaitlis ir {str(virsotne[1])}")
    if (virsotne[1] %2 != 0 and virsotne[1] %3 !=0) or virsotne[1] <= 10:
        rezultats(virsotne)
        return
    else:
        if kurs_sak == "dators":
            print("Dators domā...")
            nakosais_gajiens = berni(virsotne)
            if virsotne[4] == dzilums:
                gen = True
                result = minimax(virsotne,gen)
            else:
                gen = False
                result = minimax(virsotne,gen)
            if nakosais_gajiens == virsotne:
                for x in sp.virsotnes:
                    if x.limenis > dzilums:
                        gen = True
                        atk_virsotnes.append([x.id,x.skaitlis,x.speletajs1,x.speletajs2,x.limenis])
                for y in atk_virsotnes:
                    if y[4] > dzilums:
                        minimax(y,gen)
                nakosais_gajiens = berni(virsotne)
            if len(nakosais_gajiens) == 2:
                pirmais = minimax(nakosais_gajiens[0],gen)
                otrais = minimax(nakosais_gajiens[1],gen)
                if pirmais == otrais == result:
                    izv1 = nakosais_gajiens[0]
                    izv2 = nakosais_gajiens[1]
                    if (virsotne[1]/izv1[1]) > (virsotne[1]/izv2[1]):
                        datora_izvele = nakosais_gajiens[1]
                        datora_dalitajs = virsotne[1]/datora_izvele[1]
                        print("Dators izvēlējās dalīt ar: ", datora_dalitajs)
                        spele_minimax("cilvēks", nakosais_gajiens[0],gen)
                    else:
                        datora_izvele = nakosais_gajiens[0]
                        datora_dalitajs = virsotne[1]/datora_izvele[1]
                        print("Dators izvēlējās dalīt ar: ", datora_dalitajs)
                        spele_minimax("cilvēks", nakosais_gajiens[0],gen)
                elif (pirmais == result) and (otrais != result):
                    datora_izvele = nakosais_gajiens[0]
                    datora_dalitajs = virsotne[1]/datora_izvele[1]
                    print("Dators izvēlējās dalīt ar: ", datora_dalitajs)
                    spele_minimax("cilvēks", nakosais_gajiens[0],gen)
                elif (otrais == result) and (pirmais != result):
                    datora_izvele = nakosais_gajiens[1]
                    datora_dalitajs = virsotne[1]/datora_izvele[1]
                    print("Dators izvēlējās dalīt ar: ", datora_dalitajs)
                    spele_minimax("cilvēks", nakosais_gajiens[1],gen)
            elif len(nakosais_gajiens) == 1:
                datora_izvele = nakosais_gajiens
                datora_dalitajs = virsotne[1]/datora_izvele[0][1]
                print("Dators izvēlējās dalīt ar: ", datora_dalitajs)
                spele_minimax("cilvēks", nakosais_gajiens[0],gen)
        if kurs_sak == "cilvēks":
            print("Jūsu gājiens")
            nakama_virsotne = 0
            cilveka_gajiens = input("Ievadiet skaitli, ar kuru vēlaties dalīt pašreizējo skaitli: 2 vai 3\n")
            if ((virsotne[1] % int(cilveka_gajiens)) == 0) and ((cilveka_gajiens == "2") or (cilveka_gajiens == "3")):
                result = virsotne[1] / int(cilveka_gajiens)
                if sacejs == "1":
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
                            if x.limenis > dzilums:
                                gen = True
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
                            if x.limenis > dzilums:
                                gen = True
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
                spele_minimax("dators", nakama_virsotne,gen)
            else:
                print("Nepareiza gājiena izvēle")
                spele_minimax("cilvēks", virsotne,gen)

def spele_alphabeta(kurs_sak, virsotne, generets):
    print("Pašreizejais skaitlis:",virsotne[1])
    if virsotne[1] %2 != 0 and virsotne[1] %3 or virsotne[1] <= 10:
        rezultats(virsotne)
        return
    else:
        if kurs_sak == "dators":
            print("Datora gajiens:")
            result = alphabeta(virsotne,float('-inf'), float('inf'), generets)
            nakosais_gajiens = berni(virsotne)
            if virsotne[4] == dzilums:
                generets = True
                result = alphabeta(virsotne,float('-inf'), float('inf'), generets)
            else:
                generets = False
                result = alphabeta(virsotne,float('-inf'), float('inf'), generets)
            if virsotne[4] == dzilums:
                generets = True
                result = alphabeta(virsotne,float('-inf'), float('inf'), generets)
            else:
                generets = False
                result = alphabeta(virsotne,float('-inf'), float('inf'), generets)
            if nakosais_gajiens[0] == virsotne:
                for x in sp.virsotnes:
                        if x.limenis > dzilums:
                            generets = True
                            atk_virsotnes.append([x.id,x.skaitlis,x.speletajs1,x.speletajs2,x.limenis])
                for y in atk_virsotnes:
                    if y[4] >= dzilums:
                        alphabeta(y,float('-inf'), float('inf'), generets)
                nakosais_gajiens = berni(virsotne)
                result = alphabeta(virsotne,float('-inf'), float('inf'), generets)
            if len(nakosais_gajiens) == 2:
                if nakosais_gajiens[0][5] == nakosais_gajiens[1][5] == result:
                    pirma_virsotne = virsotne[1]/nakosais_gajiens[0][1]
                    otra_virsotne = virsotne[1]/nakosais_gajiens[1][1]
                    if pirma_virsotne > otra_virsotne:
                        datora_izvele = nakosais_gajiens[0]
                        datora_dalitajs = virsotne[1]/datora_izvele[1]
                        print("Dators izvēlējās sadalit ar:", datora_dalitajs)
                        spele_alphabeta("cilvēks", nakosais_gajiens[0], generets)
                    else:
                        datora_izvele = nakosais_gajiens[1]
                        datora_dalitajs = virsotne[1]/datora_izvele[1]
                        print("Dators izvēlējās sadalit ar:", datora_dalitajs)
                        spele_alphabeta("cilvēks", nakosais_gajiens[1], generets)
                elif nakosais_gajiens[0][5] == result and nakosais_gajiens[1][5] != result:
                    datora_izvele = nakosais_gajiens[0]
                    datora_dalitajs = virsotne[1]/datora_izvele[1]
                    print("Dators izvēlējās sadalit ar:", datora_dalitajs)
                    spele_alphabeta("cilvēks", nakosais_gajiens[0], generets)
                elif nakosais_gajiens[1][5] == result and nakosais_gajiens[0][5] != result:
                    datora_izvele = nakosais_gajiens[1]
                    datora_dalitajs = virsotne[1]/datora_izvele[1]
                    print("Dators izvēlējās sadalit ar:", datora_dalitajs)
                    spele_alphabeta("cilvēks", nakosais_gajiens[1], generets)
            elif len(nakosais_gajiens) == 1:
                    datora_izvele = nakosais_gajiens
                    datora_dalitajs = virsotne[1]/datora_izvele[0][1]
                    print("Dators izvēlējās sadalit ar:", datora_dalitajs)
                    spele_alphabeta("cilvēks", nakosais_gajiens[0], generets)
        elif kurs_sak == "cilvēks":
            nakama_virsotne = 0
            cilveka_gajiens = input("Ievadiet skaitli, ar kuru vēlaties dalīt pašreizējo skaitli: 2 vai 3\n")
            if virsotne[1] % int(cilveka_gajiens) == 0:
                result = virsotne[1] / int(cilveka_gajiens)
                if sacejs == "1":
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
                            if x.limenis > dzilums:
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
                            if x.limenis > dzilums:
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
                spele_alphabeta("dators", nakama_virsotne, generets)
            else:
                print("Ar jusu skaitli:", cilveka_gajiens, "nevar iegut veselo rezulatatu")
                spele_alphabeta("cilvēks", virsotne, generets)

def sak_spele():
    speles_sakums = input("Ievadiet 1, lai sāktu spēli un 2 lai beigtu spēli\n1. Sākt\n2. Beigt\n")
    if speles_sakums == "1":
        izvelies_algoritmu()

sak_spele()