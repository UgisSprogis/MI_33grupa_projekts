import random
from speles_koks import *
from MiniMax import minimax, berni


atk_virsotnes=[]
for x in sp.virsotnes:
    atk_virsotnes.append([x.id,x.skaitlis,x.speletajs1,x.speletajs2,x.limenis])
max_limenis = sp.virsotnes[len(sp.virsotnes)-1].limenis



def pirmais_gajiens():
    speles_sakums = input("izvēlieties, kurš sāks pirmais. Ievadiet pc, lai dators būtu pirmais vai human, lai jūs\n1. dators\n2. human\n")
    if speles_sakums == "1":
        spele("pc", atk_virsotnes[0])
    elif speles_sakums == "2":
        spele("human", atk_virsotnes[0])



def spele(kurs_sak, virsotne):
    print(f"sāk {kurs_sak} un virsotne ir {virsotne}")



def sak_spele():
    speles_sakums = input("Ievadiet start, lai sāktu spēli, vai exit, lai izietu\n1. Start\n2. Exit\n")
    if speles_sakums == "1":
        pirmais_gajiens()



sak_spele()