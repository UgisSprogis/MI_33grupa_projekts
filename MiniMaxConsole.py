import random
from speles_koks import *
from MiniMax import minimax, berni
from HNF import hnf


max_limenis = sp.virsotnes[len(sp.virsotnes)-1].limenis
if max_limenis % 2 == 0:
    dzilums = max_limenis / 2
else:
    dzilums = (max_limenis / 2) + 1

atk_virsotnes=[]
for x in sp.virsotnes:
    if x.limenis <= dzilums:
        atk_virsotnes.append([x.id,x.skaitlis,x.speletajs1,x.speletajs2,x.limenis])


def rezultats(virsotne):
    if virsotne[2] == virsotne[3]:
        print(f"Rezultāts ir neizšķirts {virsotne[2]}:{virsotne[3]}")
    elif virsotne[2] > virsotne[3]:
        print(f"Uzvar pirmais speletajs {virsotne[2]}:{virsotne[3]}")
    elif virsotne[2] < virsotne[3]:
        print(f"Uzvar otrais speletajs {virsotne[2]}:{virsotne[3]}")

def pirmais_gajiens():
    global sacejs
    sacejs = input("izvēlieties, kurš sāks pirmais. Ievadiet pc, lai dators būtu pirmais vai human, lai jūs\n1. dators\n2. human\n")
    if sacejs == "1":
        spele("dators", atk_virsotnes[0],False)
    elif sacejs == "2":
        spele("cilvēks", atk_virsotnes[0],False)
    

def spele(kurs_sak, virsotne,gen):
    print(f"{kurs_sak} iet un spēles skaitlis ir {str(virsotne[1])}")
    if (virsotne[1] %2 != 0 and virsotne[1] %3 !=0) or virsotne[1] <= 10:
        rezultats(virsotne)
        return
    else:
        if kurs_sak == "dators":
            print("Dators domā...")
            result = minimax(virsotne,gen)
            nakosais_gajiens = berni(virsotne)
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
                        spele("cilvēks", nakosais_gajiens[0],gen)
                    else:
                        datora_izvele = nakosais_gajiens[0]
                        datora_dalitajs = virsotne[1]/datora_izvele[1]
                        print("Dators izvēlējās dalīt ar: ", datora_dalitajs)
                        spele("cilvēks", nakosais_gajiens[0],gen)
                elif (pirmais == result) and (otrais != result):
                    datora_izvele = nakosais_gajiens[0]
                    datora_dalitajs = virsotne[1]/datora_izvele[1]
                    print("Dators izvēlējās dalīt ar: ", datora_dalitajs)
                    spele("cilvēks", nakosais_gajiens[0],gen)
                elif (otrais == result) and (pirmais != result):
                    datora_izvele = nakosais_gajiens[1]
                    datora_dalitajs = virsotne[1]/datora_izvele[1]
                    print("Dators izvēlējās dalīt ar: ", datora_dalitajs)
                    spele("cilvēks", nakosais_gajiens[1],gen)
            elif len(nakosais_gajiens) == 1:
                datora_izvele = nakosais_gajiens
                datora_dalitajs = virsotne[1]/datora_izvele[0][1]
                print("Dators izvēlējās dalīt ar: ", datora_dalitajs)
                spele("cilvēks", nakosais_gajiens[0],gen)

        if kurs_sak == "cilvēks":
            print("Jūsu gājiens")
            nakama_virsotne = 0
            cilveka_gajiens = input("Ievadiet skaitli, ar kuru vēlaties dalīt pašreizējo skaitli: 2 vai 3\n")
            if ((virsotne[1] % int(cilveka_gajiens)) == 0) and ((cilveka_gajiens == "2") or (cilveka_gajiens == "3")):
                result = virsotne[1] / int(cilveka_gajiens)
                a = 2
                b = 3
                if sacejs == "1":
                    if cilveka_gajiens == "2":
                        for x in atk_virsotnes:
                            if (x[1] == result) and ((virsotne[2]+a)==x[2]) and ((virsotne[3])==x[3]):
                                nakama_virsotne = x
                                break
                    else:
                        for x in atk_virsotnes:
                            if (x[1] == result) and ((virsotne[2])==x[2]) and ((virsotne[3]+b)==x[3]):
                                nakama_virsotne = x
                                break
                    if nakama_virsotne == 0:
                        for x in sp.virsotnes:
                            if x.limenis > dzilums:
                                gen = True
                                atk_virsotnes.append([x.id,x.skaitlis,x.speletajs1,x.speletajs2,x.limenis])
                        if cilveka_gajiens == "2":
                            for y in atk_virsotnes:
                                if (y[1] == result) and ((virsotne[2]+a)==y[2]) and ((virsotne[3])==y[3]):
                                    nakama_virsotne = y
                                    break
                        else:
                            for y in atk_virsotnes:
                                if (y[1] == result) and ((virsotne[2])==y[2]) and ((virsotne[3]+b)==y[3]):
                                    nakama_virsotne = y
                                    break
                else:
                    if cilveka_gajiens == "2":
                        for x in atk_virsotnes:
                            if (x[1] == result) and ((virsotne[2])==x[2]) and ((virsotne[3]+a)==x[3]):
                                nakama_virsotne = x
                                break
                    else:
                        for x in atk_virsotnes:
                            if (x[1] == result) and ((virsotne[2]+b)==x[2]) and ((virsotne[3])==x[3]):
                                nakama_virsotne = x
                                break
                    if nakama_virsotne == 0:
                        for x in sp.virsotnes:
                            if x.limenis > dzilums:
                                gen = True
                                atk_virsotnes.append([x.id,x.skaitlis,x.speletajs1,x.speletajs2,x.limenis])
                        if cilveka_gajiens == "2":
                            for y in atk_virsotnes:
                                if (y[1] == result) and ((virsotne[2])==y[2]) and ((virsotne[3]+a)==y[3]):
                                    nakama_virsotne = y
                                    break
                        else:
                            for y in atk_virsotnes:
                                if (y[1] == result) and ((virsotne[2]+b)==y[2]) and ((virsotne[3])==y[3]):
                                    nakama_virsotne = y
                                    break
                spele("dators", nakama_virsotne,gen)
            else:
                print("Nepareizs gajiens")
                spele("cilvēks", virsotne,gen)


def sak_spele():
    speles_sakums = input("Ievadiet start, lai sāktu spēli, vai exit, lai izietu\n1. Start\n2. Exit\n")
    if speles_sakums == "1":
        pirmais_gajiens()


sak_spele()