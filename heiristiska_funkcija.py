from speles_koks import *



def heiristiska_funckija(sak_virsotne,beigu_virsotne,sak_seciba):
    celi = []
    virsotnes = []
    print("heiristiska_funckija")
    for x in sp.virsotnes:
        virsotnes.append(x.id)
    for x in sp.loki:
        for y in sp.loki[x]:
            celi.append([x,y])
        
    print(celi)
    

heiristiska_funckija("A1", uzvaras_strupceli(sakums), sakums)