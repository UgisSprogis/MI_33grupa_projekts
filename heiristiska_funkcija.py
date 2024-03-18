from speles_koks import *


def svara_pieskirsana():
    virsotnu_svari = []
    for x in sp.virsotnes:
        virsotnes_svars = x.limenis + x.speletajs1 - x.speletajs2
        virsotnu_svari.append([x.id, virsotnes_svars])
    return virsotnu_svari

print(svara_pieskirsana())


# def heiristiska_funckija(sak_virsotne,beigu_virsotne,sak_seciba):
#     celi = []
#     uzvarosais_cels = []
#     next_inline = []
#     next_inline_temp = []
#     print("heiristiska_funckija")
#     for x in sp.loki:
#         for y in sp.loki[x]:
#             celi.append([x,y])
#     for x in celi:
#         if x[1] == beigu_virsotne[0]:
#             uzvarosais_cels.append(x)
#             next_inline.append(x[0])
#     #lol
#     print(celi)
#     print(uzvarosais_cels)
#     print(next_inline)
    
    

heiristiska_funckija('A1', uzvaras_strupceli(sakums), sakums)