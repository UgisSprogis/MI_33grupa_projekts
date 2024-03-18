from speles_koks import *

sak_dators = True
def svara_pieskirsana(sak_seciba):
    virsotnu_svari = []
    for x in sp.virsotnes:
        if sak_dators and x.limenis%2 == 0:
            print("Sobridejais limenis: " + str(x.limenis))
            virsotnes_svars = x.limenis + x.speletajs1 - x.speletajs2
            virsotnu_svari.append([x.id, virsotnes_svars])
        if not sak_dators and x.limenis%2 != 0 and x.limenis != 1:
            print("Sobridejais limenis: " + str(x.limenis))
            virsotnes_svars = x.limenis + x.speletajs1 - x.speletajs2
            virsotnu_svari.append([x.id, virsotnes_svars])
    return virsotnu_svari
print("Virsotņu svari:")
print(svara_pieskirsana(sak_dators))


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
        
print("Virsotnes loki ar svaru:")
print(masivs_ar_svaru(svara_pieskirsana(sak_dators),index_uz_masivu()))