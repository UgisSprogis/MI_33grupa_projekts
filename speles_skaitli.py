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

def skaitla_izvele():
    pieci_skaitli = speles_skaitli()
    print("Spēles skaitļi ir:")
    l = 1
    for x in pieci_skaitli:
        print(f"{pieci_skaitli.index(x)+1}. ", x)
    izveletais_skaitlis = int(input("Izvēlieties skaitli no spēles skaitļiem: "))-1
    sk = pieci_skaitli[izveletais_skaitlis]
    print(f"Jūsu izvēlētais skaitlis ir: {sk}")
    return sk
