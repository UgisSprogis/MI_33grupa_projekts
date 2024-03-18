from speles_koks import *


def svara_pieskirsana():
    virsotnu_svari = []
    for x in sp.virsotnes:
        virsotnes_svars = x.limenis + x.speletajs1 - x.speletajs2
        virsotnu_svari.append([x.id, virsotnes_svars])
    return virsotnu_svari
print(svara_pieskirsana())


def index_uz_masivu():
    visi_loki = []
    for x in sp.virsotnes:
        try: 
            for y in sp.loki[x.id]:
                visi_loki.append([x.id, y])
        except KeyError:
            break
    return visi_loki

def masivs_ar_svaru(masivs, svars):
    masivs_ar_svaru = []
    for x in svars:
        for y in masivs:
            if x[1] == y[0]:
                masivs_ar_svaru.append([x[0],x[1],y[1]])
    return masivs_ar_svaru
        
    

print(index_uz_masivu())
print("Pavisam done")
print(masivs_ar_svaru(svara_pieskirsana(),index_uz_masivu()))