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
            beta = min(beta, svars)
            #Pārbaude: ja alfa ir lielāka vai vienāda ar beta, neapsveram ceļu tālāk
            if alpha >= beta:
                break
        return svars
    #Ja virsotnes līnenis ir nepāra skaitlis, tad tiek izvēlēts maksimizēšanas algoritms no minimax funkcijas
    elif (virs[4] % 2) == 1:
        #Tiek rekursīvi atgriezta maksimālā vērtība no visiem bērniem
        for stavoklis in nakosais_stavoklis:
            svars = alphabeta(stavoklis, alpha, beta)
            alpha = max(alpha, svars)
            #Pārbaude: ja alfa ir lielāka vai vienāda ar beta, neapsveram ceļu tālāk
            if alpha >= beta:
                break
        return svars

#Tiek izprintēta alphabeta funkcijas atgrieztā vērtība
print("Jādodas uz virsotni, kuras novērtējums pēc alphabeta funkcijas ir:")
print(alphabeta(atk_virsotnes[0],float('-inf'), float('inf')))

#spele()
