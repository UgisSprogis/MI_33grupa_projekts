from main import *
from tkinter import *
import tkinter.font as font
import tkinter as tk
from tkinter import messagebox

# Pamācība un koda struktūra ņemta no https://www.geeksforgeeks.org/python-gui-tkinter/
# https://www.geeksforgeeks.org/tkinter-application-to-switch-between-different-page-frames/

izveletais_algoritms = None
izveletais_sacejs = None


class tkinterApp(tk.Tk):
    # tkinterApp klases inicializēšana
    def __init__(self, *args, **kwargs): 
        # Tk klases inicializēšana
        tk.Tk.__init__(self, *args, **kwargs)
        # Rāmja izveide ar visiem pamata parametriem
        container = tk.Frame(self)  
        container.pack(side = "top", fill = "both", expand = True)
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)
        self.title("MI 33 praktiskais darbs")

        # Loga pozicionēšanas kods ekrāna centrā, kods ņemts no
        # https://coderslegacy.com/tkinter-center-window-on-screen/
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = (screen_width/2) - (640/2)
        y = (screen_height/2) - (480/2)
        self.geometry('%dx%d+%d+%d' % (640, 480, x, y))

        self.frames = {}
        # Katras lapas rāmja piešķiršana
        for F in (Sakumlapa, Izvelne, Skaitli, Intervals, Beigas, Spele):
            frame = F(container, self)
            self.frames[F] = frame 
            frame.grid(row = 0, column = 0, sticky ="nsew")
        self.show_frame(Sakumlapa)
        self.mainloop()

    # Funkcija, kas grafiski izvala lapu
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

class Sakumlapa(tk.Frame):
    # Sākumlapa, kas satur vienu pogu un pamata informāciju par autoriem
    def __init__(self, parent, controller):
        # Rāmja inicializācija un loga sadalījums režģos
        tk.Frame.__init__(self, parent)
        Sakumlapa.configure(self, bg='gray')
        Frame.columnconfigure(self, 0, weight=1)
        Frame.columnconfigure(self, 1, weight=1)
        Frame.columnconfigure(self, 2, weight=1)
        Frame.columnconfigure(self, 3, weight=1)
        Frame.columnconfigure(self, 4, weight=1)
        Frame.rowconfigure(self, 0, weight=3)
        Frame.rowconfigure(self, 1, weight=3)
        Frame.rowconfigure(self, 2, weight=1)
        Frame.rowconfigure(self, 3, weight=1)
        # Pogu un uzrakstu izveidošana
        # Vienīgā poga, kas noved pie nākošā loga "Izvēlne"
        Button(self, text = 'SĀKT', bd=0, borderwidth=2, width=10, command = 
                    lambda : controller.show_frame(Izvelne), font=font.Font(family='Arial', size=26, weight="bold")).grid( row=1, columnspan=5)
        Label(self, text = 'MIP 33. GRUPAS 1. PRAKTISKAIS DARBS', 
                        font=font.Font(family='Arial', size=18), background='white').grid(row=0, columnspan=5)
        Label(self, borderwidth=2, text = 'Dāniels', 
                        font=font.Font(family='Arial', size=18), background='white').grid(column=0, row=2, sticky='sw', padx=7)
        Label(self, borderwidth=2, text = 'Dūda', 
                        font=font.Font(family='Arial', size=18), background='white').grid(column=0, row=3, sticky='nw', padx=7)
        Label(self, borderwidth=2, text = 'Aleksandrs', 
                        font=font.Font(family='Arial', size=18), background='white').grid(column=1, row=2, sticky='s', padx=7)
        Label(self, borderwidth=2, text = 'Jančevskis', 
                        font=font.Font(family='Arial', size=18), background='white').grid(column=1, row=3, sticky='n', padx=7)
        Label(self, borderwidth=2, text = 'Uģis Raimonds', 
                        font=font.Font(family='Arial', size=18), background='white').grid(column=2, row=2, sticky='s', padx=7)
        Label(self, borderwidth=2, text = 'Sproģis', 
                        font=font.Font(family='Arial', size=18), background='white').grid(column=2, row=3, sticky='n', padx=7)
        Label(self, borderwidth=2, text = 'Bernhards', 
                        font=font.Font(family='Arial', size=18), background='white').grid(column=3, row=2, sticky='s', padx=7)
        Label(self, text = 'Arnītis', 
                        font=font.Font(family='Arial', size=18), background='white').grid(column=3, row=3, sticky='n', padx=7)
        Label(self, text = 'Sandijs', 
                        font=font.Font(family='Arial', size=18), background='white').grid(column=4, row=2, sticky='se', padx=7)
        Label(self, text = 'Sīlis', 
                        font=font.Font(family='Arial', size=18), background='white').grid(column=4, row=3, sticky='ne', padx=7)

class Izvelne(tk.Frame):
    # Klases inicializēšana
    def __init__(self, parent, controller):
        # Rāmja inicializācija un loga sadalījums režģos
        tk.Frame.__init__(self, parent)
        self.speletajs_status = False
        self.algoritms_status = False
        self.speletajs = ""
        self.algoritms = ""
        Frame.columnconfigure(self, 0, weight=2)
        Frame.columnconfigure(self, 1, weight=2)
        Frame.columnconfigure(self, 2, weight=1)
        Frame.columnconfigure(self, 3, weight=2)
        Frame.columnconfigure(self, 4, weight=2)
        Frame.rowconfigure(self, 0, weight=1)
        Frame.rowconfigure(self, 1, weight=1)
        Frame.rowconfigure(self, 2, weight=1)
        Frame.rowconfigure(self, 3, weight=1)
        Frame.configure(self, bg='gray')
        # Pogu un uzrakstu izveidošana
        Label(self, text = 'KURŠ UZSĀKS SPĒLI?', 
                    font=font.Font(family='Arial', size=26, weight="bold"), background='white').grid(row=0, columnspan=5)
        
        poga_speletajs = Button(self, text = 'SPĒLĒTĀJS', bd=0, borderwidth=0, width=10, background='white', command = 
                lambda:mainit_krasu_speletajs("Speletajs"), font=font.Font(family='Arial', size=18, weight="bold"))
        poga_speletajs.grid( row=1, padx=5, column=2, columnspan=2, sticky='nw')

        poga_dators = Button(self, text = 'DATORS', bd=0, borderwidth=0, width=10, background='white', command = 
                lambda: mainit_krasu_speletajs("Dators"), font=font.Font(family='Arial', size=18, weight="bold"))
        poga_dators.grid( row=1, padx=25, column=0, columnspan=2, sticky='ne')

        Label(self, text = 'ALGORITMS', 
                    font=font.Font(family='Arial', size=26, weight="bold"), background='white').grid(row=2, columnspan=5)
        
        poga_minimax = Button(self, text = 'MINIMAX', bd=0, borderwidth=0, width=10, background='white', command = 
                lambda: mainit_krasu_algoritms("Minimax"), font=font.Font(family='Arial', size=18, weight="bold"))
        poga_minimax.grid( row=3, padx=5, column=2, columnspan=2, sticky='nw')

        poga_alfabeta = Button(self, text = 'ALFA-BETA', bd=0, borderwidth=0, width=10, background='white', command = 
                lambda: mainit_krasu_algoritms("Alfabeta"), font=font.Font(family='Arial', size=18, weight="bold"))
        poga_alfabeta.grid( row=3, padx=25, column=0, columnspan=2, sticky='ne')

        poga_turpinat = Button(self, text = '>>>>>>>', bd=0, borderwidth=0, width=10, background='white', command = 
                lambda: turpinat("Skaitli"), font=font.Font(family='Arial', size=18, weight="bold"))
        poga_turpinat.grid( row=4, padx=25, column=0, columnspan=5, sticky='s')

        poga_papildus = Button(self, text = "PAPILDUS", bd=0, borderwidth=0, width=10, background='white', command = 
                lambda: turpinat("Papildus"), font=font.Font(family='Arial', size=18, weight="bold"))
        poga_papildus.grid( row=5, padx=25, column=0, columnspan=5, sticky='se')
        
        # Funkcija maina krāsu izvēlētā spēlētāja pogai uz zaļu
        def mainit_krasu_speletajs(speletajs):
            global izveletais_sacejs
            self.speletajs_status = True
            if speletajs == "Speletajs":
                self.speletajs = "speletajs"
                poga_speletajs.configure(background='green')
                poga_dators.configure(background='white')
                izveletais_sacejs = "2"
                print(izveletais_sacejs)
            elif speletajs == "Dators":
                self.speletajs = "dators"
                poga_speletajs.configure(background='white')
                poga_dators.configure(background='green')
                izveletais_sacejs = "1"
                print(izveletais_sacejs)
        
        # Funkcija maina krāsu izvēlētā algoritma pogai uz zaļu
        def mainit_krasu_algoritms(algoritms):
            global izveletais_algoritms
            self.algoritms_status = True
            if algoritms == "Minimax":
                self.algoritms = "minimax"
                poga_minimax.configure(background='green')
                poga_alfabeta.configure(background='white')
                izveletais_algoritms = "minimax"
                print(izveletais_algoritms)
            elif algoritms == "Alfabeta":
                self.algoritms = "alfabeta"
                poga_alfabeta.configure(background='green')
                poga_minimax.configure(background='white')
                izveletais_algoritms = "alfabeta"
                print(izveletais_algoritms)
        
        # Funkcija, kas pārbauda, vai viens no katra dotā parametra ir izvēlēts un ved uz nākošo lapu
        # Gadījumā, ja nav izvēlēts kāds no nepieciešamajiem parametriem, tiek izvadīta kļūda
        def turpinat(parametrs):
            if parametrs == "Skaitli":
                if not self.algoritms_status and not self.speletajs_status:
                    messagebox.showerror('Spēles kļūda', 'Izvēlieties spēles algoritmu un kurš uzsāks spēli.')
                elif not self.algoritms_status:
                    messagebox.showerror('Spēles kļūda', 'Izvēlieties spēles algoritmu.')
                elif not self.speletajs_status:
                    messagebox.showerror('Spēles kļūda', 'Izvēlieties, kurš uzsāks spēli.')
                else:
                    controller.show_frame(Skaitli)
                reset()
            elif parametrs == "Papildus":
                controller.show_frame(Intervals)
                reset()
        
        # Funkcija, kas atjauno noklusējuma parametrus, kad logs tiek pamests
        def reset():
            self.algoritms_status = False
            self.speletajs_status = False
            poga_alfabeta.configure(background='white')
            poga_minimax.configure(background='white')
            poga_dators.configure(background='white')
            poga_speletajs.configure(background='white')




class Skaitli(tk.Frame):
    def __init__(self, parent, controller): 
        tk.Frame.__init__(self, parent)
        self.skailtlis_status = False
        self.izveletais_skaitlis = 0
        pieci_skaitli = speles_skaitli()
        Frame.columnconfigure(self, 0, weight=0)
        Frame.columnconfigure(self, 1, weight=2)
        Frame.columnconfigure(self, 2, weight=0)
        Frame.rowconfigure(self, 0, weight=1)
        Frame.rowconfigure(self, 1, weight=1)
        Frame.rowconfigure(self, 2, weight=1)
        Frame.rowconfigure(self, 3, weight=1)
        Frame.rowconfigure(self, 4, weight=1)
        Frame.configure(self, bg='gray')
        Label(self, text = 'IZVĒLIES SKAITLI', 
                    font=font.Font(family='Arial', size=26, weight="bold"), background='white').grid(row=0, columnspan=5)
        skaitlis1 = Button(self, text = pieci_skaitli[0], bd=0, borderwidth=0, width=10, background='white', command = 
                lambda:[mainit_krasu_skaitlis("skaitlis1"),set_skaitlis(pieci_skaitli[0])], font=font.Font(family='Arial', size=18, weight="bold"))
        skaitlis1.grid( row=1, column=1, padx=5, pady=5, sticky='n')

        skaitlis2 = Button(self, text = pieci_skaitli[1], bd=0, borderwidth=0, width=10, background='white', command = 
                lambda:[mainit_krasu_skaitlis("skaitlis2"),set_skaitlis(pieci_skaitli[1])], font=font.Font(family='Arial', size=18, weight="bold"))
        skaitlis2.grid(row=2, column=1, padx=5, pady=5, sticky='n')

        skaitlis3 = Button(self, text = pieci_skaitli[2], bd=0, borderwidth=0, width=10, background='white', command = 
                lambda:[mainit_krasu_skaitlis("skaitlis3"),set_skaitlis(pieci_skaitli[2])], font=font.Font(family='Arial', size=18, weight="bold"))
        skaitlis3.grid( row=3, column=1, padx=5, pady=5, sticky='n')

        skaitlis4 = Button(self, text = pieci_skaitli[3], bd=0, borderwidth=0, width=10, background='white', command = 
                lambda:[mainit_krasu_skaitlis("skaitlis4"),set_skaitlis(pieci_skaitli[3])], font=font.Font(family='Arial', size=18, weight="bold"))
        skaitlis4.grid( row=4, column=1, padx=5, pady=5, sticky='n')

        skaitlis5 = Button(self, text = pieci_skaitli[4], bd=0, borderwidth=0, width=10, background='white', command = 
                lambda:[mainit_krasu_skaitlis("skaitlis5"),set_skaitlis(pieci_skaitli[4])], font=font.Font(family='Arial', size=18, weight="bold"))
        skaitlis5.grid( row=5, column=1, padx=5, pady=5, sticky='n')

        poga_turpinat = Button(self, text = '>>>>>>>', bd=0, borderwidth=0, width=10, background='white', command = 
                lambda: turpinat(), font=font.Font(family='Arial', size=18, weight="bold"))
        poga_turpinat.grid( row=5, column=2, padx=5, pady=5, sticky='se')

        poga_turpinat = Button(self, text = '<<<<<<<', bd=0, borderwidth=0, width=10, background='white', command = 
                lambda: atpakal(), font=font.Font(family='Arial', size=18, weight="bold"))
        poga_turpinat.grid( row=5, column=0, padx=5, pady=5, sticky='sw')


        def set_skaitlis(skaitlis):
            self.izveletais_skaitlis = skaitlis

        def mainit_krasu_skaitlis(skaitlis):
            self.skailtlis_status = True
            skaitlis_buttons = [skaitlis1, skaitlis2, skaitlis3, skaitlis4, skaitlis5]

            #cikls ģenerēts ar chat GPT
            for index, button in enumerate(skaitlis_buttons):
                button.configure(background='green' if index + 1 == int(skaitlis[-1]) else 'white')
        
        def turpinat():
            if not self.skailtlis_status:
                messagebox.showerror('Spēles kļūda', 'Izvēlieties spēles skaitli.')
                taisi_koku(self.izveletais_skaitlis, self.speletajs.get())
                print("Speletajs get")
                print(self.speletajs.get())
                reset()
            else:
                controller.show_frame(Spele)
                reset()
        def atpakal():
            controller.show_frame(Izvelne)
            reset()

        def reset():
            self.skailtlis_status = False
            skaitlis_buttons = [skaitlis1, skaitlis2, skaitlis3, skaitlis4, skaitlis5]

            for button in enumerate(skaitlis_buttons):
                button.configure(background='white')



class Intervals(tk.Frame):   
    def __init__(self, parent, controller): 
        tk.Frame.__init__(self, parent)
        self.skailtlis_status = False
        Frame.columnconfigure(self, 0, weight=1)
        Frame.columnconfigure(self, 1, weight=5)
        Frame.columnconfigure(self, 2, weight=2)
        
        Frame.rowconfigure(self, 0, weight=1)
        Frame.rowconfigure(self, 1, weight=1)
        Frame.rowconfigure(self, 2, weight=1)
        Frame.rowconfigure(self, 3, weight=1)
        Frame.rowconfigure(self, 4, weight=1)
      
        Frame.configure(self, bg='gray')

        Label(self, text = 'MAINĪT SKAITĻU INTERVALU', 
                    font=font.Font(family='Arial', size=26, weight="bold"), background='white').grid(row=0, columnspan=5)
        

        tk.Label(self, text='No:', font=font.Font(family='Arial', size=18), background='gray').grid(row=1, column=0, sticky='e')
        self.from_entry = tk.Entry(self, font=font.Font(family='Arial', size=18))
        self.from_entry.grid(row=1, column=1, sticky='w')

        tk.Label(self, text='Līdz:', font=font.Font(family='Arial', size=18), background='gray').grid(row=2, column=0, sticky='e')
        self.to_entry = tk.Entry(self, font=font.Font(family='Arial', size=18))
        self.to_entry.grid(row=2, column=1, sticky='w')


        poga_manit = Button(self, text = 'mainīt', bd=0, borderwidth=0, width=10, background='white', command = 
                lambda: mainit(), font=font.Font(family='Arial', size=18, weight="bold"))
        poga_manit.grid( row=4, padx=25, column=0, columnspan=5, sticky='n')

        poga_manit = Button(self, text = '<<<<<<<', bd=0, borderwidth=0, width=10, background='white', command = 
                lambda: controller.show_frame(Izvelne), font=font.Font(family='Arial', size=18, weight="bold"))
        poga_manit.grid( row=5, column=0, padx=5, pady=5, sticky='sw')


        def mainit():
            self.from_entry.delete(0, 'end')
            self.to_entry.delete(0, 'end')

class Spele(tk.Frame):
    # Klases inicializēšana
    def __init__(self, parent, controller):
        # Rāmja inicializācija un loga sadalījums režģos
        tk.Frame.__init__(self, parent)
        Frame.columnconfigure(self, 0, weight=2)
        Frame.columnconfigure(self, 1, weight=2)
        Frame.columnconfigure(self, 2, weight=1)
        Frame.columnconfigure(self, 3, weight=2)
        Frame.columnconfigure(self, 4, weight=2)
        Frame.rowconfigure(self, 0, weight=1)
        Frame.rowconfigure(self, 1, weight=1)
        Frame.rowconfigure(self, 2, weight=1)
        Frame.rowconfigure(self, 3, weight=1)
        Frame.rowconfigure(self, 4, weight=1)
        Frame.rowconfigure(self, 5, weight=1)
        Frame.rowconfigure(self, 6, weight=1)
        Frame.rowconfigure(self, 7, weight=1)
        Frame.rowconfigure(self, 8, weight=1)
        Frame.rowconfigure(self, 9, weight=1)
        Frame.configure(self, bg='gray')

        punkti = Label(self, text = '0:0', 
                    font=font.Font(family='Arial', size=15), background='white')
        punkti.grid_remove()

        pasreizejais_speles_skaitlis = Label(self, text = 'Spele', 
                    font=font.Font(family='Arial', size=26, weight="bold"), background='white')
        pasreizejais_speles_skaitlis.grid(row=1, columnspan=5)

        gajiena_status = Label(self, text = 'Šobrīd gājienu veic:', 
                    font=font.Font(family='Arial', size=15), background='white')
        gajiena_status.grid_remove()

        def next_move(gajiens,virsotne,generets):
            global next_virsotne
            global jauns_gajiens
            global punktu_skaits
            if izveletais_sacejs == "1":
                punktu_skaits = str(virsotne[2]) + ":" + str(virsotne[3])
            elif izveletais_sacejs == "2":
                 punktu_skaits = str(virsotne[3]) + ":" + str(virsotne[2])
            punkti.config(text = punktu_skaits)
            next_virsotne = virsotne[1]
            pasreizejais_speles_skaitlis.config(text = next_virsotne)
            jauns_gajiens = "Šobrīd gājienu veic:" + gajiens
            gajiena_status.config(text = jauns_gajiens)
            
            if izveletais_algoritms == "minimax":
                if gajiens == "dators":
                    print

                elif gajiens == "cilvēks":
                    print
            
            elif izveletais_algoritms == "alfabeta":
                if gajiens == "dators":
                    nakamais_gajiens = spele_alphabeta(gajiens,virsotne,generets)
                    next_move(nakamais_gajiens[0], nakamais_gajiens[1], nakamais_gajiens[2])


                elif gajiens == "cilvēks":
                    print


        def pirmais_gajiens():
            global my_text
            my_text = izveletais_algoritms
            pasreizejais_speles_skaitlis.config(text = my_text)
            nakamais_gajiens = speles_pirmais_gajiens(izveletais_algoritms, izveletais_sacejs)
            next_move(nakamais_gajiens[0], nakamais_gajiens[1], nakamais_gajiens[2])
                    
        def start():
            gajiena_status.grid(row=2, columnspan=5)
            punkti.grid(row=0, columnspan=5)
            poga_start.destroy()
            self.after(2000, lambda: pirmais_gajiens())
        
        poga_start = Button(self, text = "START", bd=0, borderwidth=0, width=10, background='white', command = start, 
               font=font.Font(family='Arial', size=18, weight="bold"))
        poga_start.grid(row=5, columnspan=5)


        

class Beigas(tk.Frame):
    # Beigas, kur tiek atspoguļota uzvara vai zaude
    # Satur pogu "Iziet" un "Jauna spēle"
    def __init__(self, parent, controller):
        # Rāmja inicializācija un loga sadalījums režģos
        tk.Frame.__init__(self, parent)
        Sakumlapa.configure(self, bg='gray')

        ############################
        teksts_small = "APSVEICAM!"# Šo parametrus ir jāiegūst no main.py atkarībā
        teksts_big = "TU UZVARĒJI!"# vai spēlētājs pēc spēles ir zaudējis, vai uzvarējis
        ############################

        Frame.columnconfigure(self, 0, weight=1)
        Frame.columnconfigure(self, 1, weight=1)
        Frame.columnconfigure(self, 2, weight=1)
        Frame.columnconfigure(self, 3, weight=1)
        Frame.columnconfigure(self, 4, weight=1)
        Frame.rowconfigure(self, 0, weight=3)
        Frame.rowconfigure(self, 1, weight=3)
        Frame.rowconfigure(self, 2, weight=1)
        Frame.rowconfigure(self, 3, weight=1)
        Label(self, text = teksts_small, 
                        font=font.Font(family='Arial', size=18), background='white', width=26).grid( row=0, columnspan=5, sticky='s', )
        Label(self, text = teksts_big, 
                        font=font.Font(family='Arial', size=36), background='white', width=13).grid( row=1, columnspan=5, sticky='n')
        poga_iziet = Button(self, text = "IZIET", bd=0, borderwidth=0, width=10, background='white', command = 
                lambda:app.destroy(), font=font.Font(family='Arial', size=18, weight="bold"))
        poga_iziet.grid( row=3, column=1, padx=5, pady=5, sticky='n')

        poga_jaunaspele = Button(self, text = "JAUNA SPĒLE", bd=0, borderwidth=0, width=13, background='white', command = 
                lambda:controller.show_frame(Izvelne), font=font.Font(family='Arial', size=18, weight="bold"))
        poga_jaunaspele.grid(row=3, column=3, padx=5, pady=5, sticky='n')



# Palaišanas kods
app = tkinterApp()
app.mainloop()