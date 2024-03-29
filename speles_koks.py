from speles_skaitli import *
#Virsotnes klase ar atribūtiem id, skaitlis, speletajs1 punkti, speletajs2 punkti, limenis
class Virsotne:
    def __init__(self, id, skaitlis, speletajs1, speletajs2, limenis):
        self.id=id
        self.skaitlis=skaitlis
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
#funkcija, kas parbauda gājienu, kā parametrus saņem gājiena tipu, visu virsotņu sarakstu un pašreizējo virsotni
def gajiens(gajiena_tips,gen_virsotnes,pasreizeja_virsotne):
    #Ja gājiens ir 2, tad dalītājs ir 2, ja 3, tad dalītājs ir 3
    if gajiena_tips=='2':
        dalitajs = 2
    else:
        dalitajs = 3
    #Ja skaitlis dalās ar dalītāju, tad turpmākais kods izveidos jaunu virsotni un atjaunos informāciju par virsotnes datiem
    if (pasreizeja_virsotne[1]%dalitajs==0) and (pasreizeja_virsotne[1]>10):
        global j
        id_new = 'A'+str(j)
        j+=1
        #jaunais skaitlis ir pašreizējās virsotnes saraksta pirmais elements, kas norāda uz skaitli.
        jaunais_skaitlis = pasreizeja_virsotne[1]
        #Šeit tiek iegūts jaunais skaitlis atbilstoši gājienu tipam
        if (gajiena_tips=='2') and (pasreizeja_virsotne[1]%2==0):
            jaunais_skaitlis = pasreizeja_virsotne[1]/2
        elif (gajiena_tips=='3') and (pasreizeja_virsotne[1]%3==0):
            jaunais_skaitlis = pasreizeja_virsotne[1]/3
        #Šajā koda blokā tiek pārvaudīts, kāds ir spēles līmenis, un tad tiek atbilstosi veiktajam gājienam un spēles nosacījumiem tiek piesķirti spēlētājiem punkti.
        if (gajiena_tips=='2'):
            if (pasreizeja_virsotne[4]%2)==0:
                speletajs1_new=pasreizeja_virsotne[2]+int(gajiena_tips)
                speletajs2_new=pasreizeja_virsotne[3]
            else:
                speletajs1_new=pasreizeja_virsotne[2]
                speletajs2_new=pasreizeja_virsotne[3]+int(gajiena_tips)
        else:
            if (pasreizeja_virsotne[4]%2)==0:
                speletajs1_new=pasreizeja_virsotne[2]
                speletajs2_new=pasreizeja_virsotne[3]+int(gajiena_tips)
            else:
                speletajs1_new=pasreizeja_virsotne[2]+int(gajiena_tips)
                speletajs2_new=pasreizeja_virsotne[3]
        #Tiek atjaunots spēles līmenis
        limenis_new=pasreizeja_virsotne[4]+1
        #Izveido jauno virsotni
        jauna_virsotne=Virsotne(id_new,jaunais_skaitlis,speletajs1_new,speletajs2_new,limenis_new)
        #Pārbauda duplikātu virsotnes
        virsotnes_parbaude=False
        #i norāda uz virsotni ejot cauri visām iterācijām
        i=0
        #Kamēr nav pārbaudītas visas virsotnes un nav atrasts neviens dublikāts, tad tiek turpināts cikls
        while (not virsotnes_parbaude) and (i<=len(sp.virsotnes)-1):
            if (sp.virsotnes[i].skaitlis==jauna_virsotne.skaitlis) and (sp.virsotnes[i].speletajs1==jauna_virsotne.speletajs1) and (sp.virsotnes[i].speletajs2==jauna_virsotne.speletajs2) and (sp.virsotnes[i].limenis==jauna_virsotne.limenis):
                virsotnes_parbaude=True
            else:
                i+=1
        #Ja nav atrasts neviens dublikāts, tad tiek pievienota jauna virsotne un loks
        if not virsotnes_parbaude:
            sp.pievienot_virsotni(jauna_virsotne)
            gen_virsotnes.append([id_new,jaunais_skaitlis,speletajs1_new,speletajs2_new,limenis_new])
            sp.pievienot_loku(pasreizeja_virsotne[0],id_new)
        else:
            j-=1
            sp.pievienot_loku(pasreizeja_virsotne[0],sp.virsotnes[i].id)

    

#Izveido spēles koka objektu
sp=SpelesKoks()
#Izveido sarakstu, kurā tiks glabātas virsotnes
gen_virsotnes = []

speles_skaitlis = skaitla_izvele()
#Izvada izvēlēto skaitli
print("Spēles skaitlis ir:", speles_skaitlis)

#Pievieno pirmo virsotni
sp.pievienot_virsotni(Virsotne("A1", speles_skaitlis, 0, 0, 1))
#Pievieno pirmo virsotni sarakstam
gen_virsotnes.append(["A1", speles_skaitlis, 0, 0, 1])
#Šis mainīgais skaita virsotnes. Sākas ar 2, tāpēc ka pirmā virsotne jau ir pievienota
j=2
#Kamēr virsotņu saraksts nav tukšs, tad tiek veikti gājieni
while len(gen_virsotnes)>0:
    pasreizeja_virsotne=gen_virsotnes[0]
    #Tiek veikti gājieni, pēc kārtas 2 un 3, ja tie ir iespējami
    gajiens('2',gen_virsotnes,pasreizeja_virsotne)
    gajiens('3',gen_virsotnes,pasreizeja_virsotne)
    #Pēc gājiena tiek izdzēsta virsotne no saraksta
    gen_virsotnes.pop(0)

print("Virsotnes:")
#Ciklam beidzoties tiek izvadīta virsotņu kopa, parādod visus atribūtus
for x in sp.virsotnes:
    print(x.id,"| skaitlis tagad = " + str(x.skaitlis),"| spēlētāja 1 punkti = " + str(x.speletajs1),"| spēlētāja 2 punkti = " + str(x.speletajs2),"| līmenis = " + str(x.limenis))
print("Loki:")
#Tiek izvadīti visi loki
for x, y in sp.loki.items():
    print(x, y)
