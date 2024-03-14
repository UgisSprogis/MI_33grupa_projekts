#Tiek importēts random, lai varētu izvēlēties nejaušus skaitļus
import random
#Spēles skaitļu ģenerators
def speles_skaitli():
    #Izveido sarakstus skaitlu_saraksts un pieci_skaitli
    skaitlu_saraksts = set()
    pieci_skaitli = set()
    #Izvēlas skaitļus no 10000 līdz 20000
    #Ja skaitlis dalās ar 6 (dalās ar 2 un 3), tad to pievieno sarakstam
    for i in range(10000,20000):
        if i%6==0:
            skaitlu_saraksts.add(i)
            #Izvēlas 5 nejaušus skaitļus no saraksta
            #Izvēlētos skaitļus pievieno pieci_skaitli
            #Tiek izmantots sorted, lai nebūtu konflikti ar random.sample
    pieci_skaitli = random.sample(sorted(skaitlu_saraksts), 5)
    return pieci_skaitli

#Pārbaude
print(speles_skaitli())