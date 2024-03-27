import random
from speles_skaitli import speles_skaitli
from speles_koks import SpelesKoks, Virsotne, gajiens
from MiniMax import minimax, berni

def skaitla_izvele():
    pieci_skaitli = speles_skaitli()
    print("Spēles skaitļi ir:")
    l = 1
    for x in pieci_skaitli:
        print(l+"." + " ", x)
    izveletais_skaitlis = int(input("Izvēlieties skaitli no spēles skaitļiem: "))
    return skaitlis



skaitla_izvele()