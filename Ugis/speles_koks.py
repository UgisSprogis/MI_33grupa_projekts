#Virsotnes klase ar atribūtiem id, virkne, speletajs1, speletajs2, limenis
class Virsotne:
    def __init__(self, id, virkne, speletajs1, speletajs2, limenis):
        self.id=id
        self.virkne=virkne
        self.speletajs1=speletajs1
        self.speletajs2=speletajs2
        self.limenis=limenis


#Spēles koka klase
class SpelesKoks:
    def __init__(self):
        self.virsotnes = []
        self.loki=dict()
    
    def pievienot_virsotni(self, virsotne):
        self.virsotnes.append(virsotne)

    def pievienot_loku(self, sak_virsotne_id, beig_virsotne_id):
        self.loki[sak_virsotne_id] = self.loki.get(sak_virsotne_id, []) + [beig_virsotne_id]

