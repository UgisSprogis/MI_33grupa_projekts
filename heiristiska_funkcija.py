from speles_koks import *



def heiristiska_funckija(sak_virsotne,beigu_virsotne,sak_seciba):
    celi = []
    uzvarosais_cels = []
    next_inline = []
    next_inline_temp = []
    print("heiristiska_funckija")
    for x in sp.loki:
        for y in sp.loki[x]:
            celi.append([x,y])
    for x in celi:
        if x[1] == beigu_virsotne[0]:
            uzvarosais_cels.append(x)
            next_inline.append(x[0])
    #lol
    print(celi)
    print(uzvarosais_cels)
    print(next_inline)
    loop = True
    while loop:
        for x in next_inline:
            for y in celi:
                if y[1] == x:
                    next_inline_temp.append(y[0])
                if y[0] == sak_virsotne:
                    loop = False
                    next_inline = next_inline_temp
    print("Next inline: " + str(next_inline))
    
    

heiristiska_funckija('A1', uzvaras_strupceli(sakums), sakums)