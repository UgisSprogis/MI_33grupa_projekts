from main import *
from tkinter import *
import tkinter.font as font
import tkinter as tk
from tkinter import messagebox

# Pamācība un koda struktūra ņemta no https://www.geeksforgeeks.org/python-gui-tkinter/
# https://www.geeksforgeeks.org/tkinter-application-to-switch-between-different-page-frames/


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

        # ChatGPT query:
        # How do I update "pasreizejais_speles_skaitlis" when switching to a new frame in tkinter?
        # <klases "Spele" kods
        if Skaitli.izveletais_skaitlis != 0:
            datora_gajiens = Skaitli.izveletais_skaitlis/Skaitli.koka_return[1]
            if datora_gajiens > 1:
                frame.datora_gajiens.config(text=str('Dators izvēlējās: '+str(int(datora_gajiens))))
            frame.pasreizejais_speles_skaitlis.config(text=Skaitli.izveletais_skaitlis)
            frame.gajiena_status.config(text='Šobrīd gājienu veic: CILVĒKS')
            if datora_gajiens > 1:
                frame.punkti.config(text=str(Skaitli.koka_return[3])+':'+str(Skaitli.koka_return[2]))

        if Skaitli.koka_return:
            frame.pasreizejais_speles_skaitlis.config(text=int(Skaitli.koka_return[1]))

        if Skaitli.generet_skaitli and hasattr(frame, 'skaitlis1'):
            if Intervals.num_from and Intervals.num_to:
                Skaitli.pieci_skaitli = speles_skaitli(Intervals.num_from,Intervals.num_to)
            else:
                Skaitli.pieci_skaitli = speles_skaitli()
            frame.pieci_skaitli = Skaitli.pieci_skaitli
            frame.skaitlis1.config(text=Skaitli.pieci_skaitli[0])
            frame.skaitlis2.config(text=Skaitli.pieci_skaitli[1])
            frame.skaitlis3.config(text=Skaitli.pieci_skaitli[2])
            frame.skaitlis4.config(text=Skaitli.pieci_skaitli[3])
            frame.skaitlis5.config(text=Skaitli.pieci_skaitli[4])
            Skaitli.generet_skaitli = None
        
        if Spele.uzvaretajs:
            if Spele.uzvaretajs[1][2] < Spele.uzvaretajs[1][3]:
                frame.teksts_small.config(text='DIEMŽĒL')
                frame.teksts_big.config(text='TU ZAUDĒJI')
            if Spele.uzvaretajs[1][2] == Spele.uzvaretajs[1][3]:
                frame.teksts_small.config(text='REZULTĀTS')
                frame.teksts_big.config(text='IR NEIZŠĶIRTS!')
            frame.rezultats.config(text='Rezultāts: '+str(Spele.uzvaretajs[1][2])+':'+str(Spele.uzvaretajs[1][3]))
            Spele.uzvaretajs = None
            

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
        Label(self, text = 'Sandijs', 
                        font=font.Font(family='Arial', size=18), background='white').grid(column=4, row=2, sticky='se', padx=7)
        Label(self, text = 'Sīlis', 
                        font=font.Font(family='Arial', size=18), background='white').grid(column=4, row=3, sticky='ne', padx=7)

class Izvelne(tk.Frame):
    speletajs = ""
    algoritms = ""
    # Klases inicializēšana
    def __init__(self, parent, controller):
        # Rāmja inicializācija un loga sadalījums režģos
        tk.Frame.__init__(self, parent)
        self.speletajs_status = False
        self.algoritms_status = False
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
        
        self.poga_speletajs = Button(self, text = 'SPĒLĒTĀJS', bd=0, borderwidth=0, width=10, background='white', command = 
                lambda:mainit_krasu_speletajs("Speletajs"), font=font.Font(family='Arial', size=18, weight="bold"))
        self.poga_speletajs.grid( row=1, padx=5, column=2, columnspan=2, sticky='nw')

        self.poga_dators = Button(self, text = 'DATORS', bd=0, borderwidth=0, width=10, background='white', command = 
                lambda: mainit_krasu_speletajs("Dators"), font=font.Font(family='Arial', size=18, weight="bold"))
        self.poga_dators.grid( row=1, padx=25, column=0, columnspan=2, sticky='ne')

        Label(self, text = 'ALGORITMS', 
                    font=font.Font(family='Arial', size=26, weight="bold"), background='white').grid(row=2, columnspan=5)
        
        self.poga_minimax = Button(self, text = 'MINIMAX', bd=0, borderwidth=0, width=10, background='white', command = 
                lambda: mainit_krasu_algoritms("Minimax"), font=font.Font(family='Arial', size=18, weight="bold"))
        self.poga_minimax.grid( row=3, padx=5, column=2, columnspan=2, sticky='nw')

        self.poga_alfabeta = Button(self, text = 'ALFA-BETA', bd=0, borderwidth=0, width=10, background='white', command = 
                lambda: mainit_krasu_algoritms("Alfabeta"), font=font.Font(family='Arial', size=18, weight="bold"))
        self.poga_alfabeta.grid( row=3, padx=25, column=0, columnspan=2, sticky='ne')

        self.poga_turpinat = Button(self, text = '>>>>>>>', bd=0, borderwidth=0, width=10, background='white', command = 
                lambda: turpinat("Skaitli"), font=font.Font(family='Arial', size=18, weight="bold"))
        self.poga_turpinat.grid( row=4, padx=25, column=0, columnspan=5, sticky='s')

        self.poga_papildus = Button(self, text = "PAPILDUS", bd=0, borderwidth=0, width=10, background='white', command = 
                lambda: turpinat("Papildus"), font=font.Font(family='Arial', size=18, weight="bold"))
        self.poga_papildus.grid( row=5, padx=25, column=0, columnspan=5, sticky='se')
        
        # Funkcija maina krāsu izvēlētā spēlētāja pogai uz zaļu
        def mainit_krasu_speletajs(in_speletajs):
            self.speletajs_status = True
            if in_speletajs == "Speletajs":
                Izvelne.speletajs = "cilvēks"
                self.poga_speletajs.configure(background='green')
                self.poga_dators.configure(background='white')
                izveletais_sacejs = "2"
                print(izveletais_sacejs)
            elif in_speletajs == "Dators":
                Izvelne.speletajs = "dators"
                self.poga_speletajs.configure(background='white')
                self.poga_dators.configure(background='green')
        
        # Funkcija maina krāsu izvēlētā algoritma pogai uz zaļu
        def mainit_krasu_algoritms(in_algoritms):
            global izveletais_algoritms
            self.algoritms_status = True
            if in_algoritms == "Minimax":
                Izvelne.algoritms = "minimax"
                self.poga_minimax.configure(background='green')
                self.poga_alfabeta.configure(background='white')
                izveletais_algoritms = "minimax"
                print(izveletais_algoritms)
            elif in_algoritms == "Alfabeta":
                Izvelne.algoritms = "alfabeta"
                self.poga_alfabeta.configure(background='green')
                self.poga_minimax.configure(background='white')
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
                    Skaitli.generet_skaitli = True
                    controller.show_frame(Skaitli)
                reset()
            elif parametrs == "Papildus":
                controller.show_frame(Intervals)
                reset()
        
        # Funkcija, kas atjauno noklusējuma parametrus, kad logs tiek pamests
        def reset():
            self.algoritms_status = False
            self.speletajs_status = False
            self.poga_alfabeta.configure(background='white')
            self.poga_minimax.configure(background='white')
            self.poga_dators.configure(background='white')
            self.poga_speletajs.configure(background='white')


class Skaitli(tk.Frame):
    izveletais_skaitlis = 0
    koka_return = None
    generet_skaitli = False
    def __init__(self, parent, controller): 
        tk.Frame.__init__(self, parent)
        self.skailtlis_status = False
        self.pieci_skaitli = speles_skaitli()
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
        self.skaitlis1 = Button(self, text = self.pieci_skaitli[0], bd=0, borderwidth=0, width=10, background='white', command = 
                lambda:[mainit_krasu_skaitlis("skaitlis1"),set_skaitlis(self.pieci_skaitli[0])], font=font.Font(family='Arial', size=18, weight="bold"))
        self.skaitlis1.grid( row=1, column=1, padx=5, pady=5, sticky='n')

        self.skaitlis2 = Button(self, text = self.pieci_skaitli[1], bd=0, borderwidth=0, width=10, background='white', command = 
                lambda:[mainit_krasu_skaitlis("skaitlis2"),set_skaitlis(self.pieci_skaitli[1])], font=font.Font(family='Arial', size=18, weight="bold"))
        self.skaitlis2.grid(row=2, column=1, padx=5, pady=5, sticky='n')

        self.skaitlis3 = Button(self, text = self.pieci_skaitli[2], bd=0, borderwidth=0, width=10, background='white', command = 
                lambda:[mainit_krasu_skaitlis("skaitlis3"),set_skaitlis(self.pieci_skaitli[2])], font=font.Font(family='Arial', size=18, weight="bold"))
        self.skaitlis3.grid( row=3, column=1, padx=5, pady=5, sticky='n')

        self.skaitlis4 = Button(self, text = self.pieci_skaitli[3], bd=0, borderwidth=0, width=10, background='white', command = 
                lambda:[mainit_krasu_skaitlis("skaitlis4"),set_skaitlis(self.pieci_skaitli[3])], font=font.Font(family='Arial', size=18, weight="bold"))
        self.skaitlis4.grid( row=4, column=1, padx=5, pady=5, sticky='n')

        self.skaitlis5 = Button(self, text = self.pieci_skaitli[4], bd=0, borderwidth=0, width=10, background='white', command = 
                lambda:[mainit_krasu_skaitlis("skaitlis5"),set_skaitlis(self.pieci_skaitli[4])], font=font.Font(family='Arial', size=18, weight="bold"))
        self.skaitlis5.grid( row=5, column=1, padx=5, pady=5, sticky='n')

        self.poga_turpinat = Button(self, text = '>>>>>>>', bd=0, borderwidth=0, width=10, background='white', command = 
                lambda: turpinat(), font=font.Font(family='Arial', size=18, weight="bold"))
        self.poga_turpinat.grid( row=5, column=2, padx=5, pady=5, sticky='se')

        self.poga_turpinat = Button(self, text = '<<<<<<<', bd=0, borderwidth=0, width=10, background='white', command = 
                lambda: atpakal(), font=font.Font(family='Arial', size=18, weight="bold"))
        self.poga_turpinat.grid( row=5, column=0, padx=5, pady=5, sticky='sw')


        def set_skaitlis(skaitlis):
            Skaitli.izveletais_skaitlis = skaitlis

        def mainit_krasu_skaitlis(skaitlis):
            self.skailtlis_status = True
            self.skaitlis_buttons = [self.skaitlis1, self.skaitlis2, self.skaitlis3, self.skaitlis4, self.skaitlis5]

            #cikls ģenerēts ar chat GPT
            for index, button in enumerate(self.skaitlis_buttons):
                button.configure(background='green' if index + 1 == int(skaitlis[-1]) else 'white')
        
        def turpinat():
            if not self.skailtlis_status:
                messagebox.showerror('Spēles kļūda', 'Izvēlieties spēles skaitli.')
                reset()
            else:
                Skaitli.koka_return = taisi_koku(self.izveletais_skaitlis, Izvelne.speletajs, Izvelne.algoritms)
                controller.show_frame(Spele)
                reset()

        def atpakal():
            controller.show_frame(Izvelne)
            reset()

        def reset():
            self.skailtlis_status = False
            self.skaitlis_buttons = [self.skaitlis1, self.skaitlis2, self.skaitlis3, self.skaitlis4, self.skaitlis5]

            # ChatGPT
            for index, button in enumerate(self.skaitlis_buttons):
                button.configure(background='white')



class Intervals(tk.Frame):
    num_from = None
    num_to = None
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
        self.from_entry = Entry(self, font=font.Font(family='Arial', size=18))
        self.from_entry.grid(row=1, column=1, sticky='w')

        tk.Label(self, text='Līdz:', font=font.Font(family='Arial', size=18), background='gray').grid(row=2, column=0, sticky='e')
        self.to_entry = Entry(self, font=font.Font(family='Arial', size=18))
        self.to_entry.grid(row=2, column=1, sticky='w')


        self.poga_manit = Button(self, text = 'mainīt', bd=0, borderwidth=0, width=10, background='white', command = 
                lambda: mainit(), font=font.Font(family='Arial', size=18, weight="bold"))
        self.poga_manit.grid( row=4, padx=25, column=0, columnspan=5, sticky='n')

        self.poga_manit = Button(self, text = '<<<<<<<', bd=0, borderwidth=0, width=10, background='white', command = 
                lambda: controller.show_frame(Izvelne), font=font.Font(family='Arial', size=18, weight="bold"))
        self.poga_manit.grid( row=5, column=0, padx=5, pady=5, sticky='sw')


        def mainit():
            text_from = self.from_entry.get()
            text_to = self.to_entry.get()
            if text_from is None or text_to is None:
                messagebox.showwarning(title='Tukšs', message='Ievadiet abas vērtības')
            elif text_from.isnumeric() and text_to.isnumeric():
                text_from = int(text_from)
                text_to = int(text_to)
                if text_from >= 10000 and text_to>text_from and text_to <= 50000 and text_to-text_from>=10000:
                    Intervals.num_from = text_from
                    Intervals.num_to = text_to
                    Skaitli.generet_skaitli = True
                    messagebox.showinfo(title='Intervāls', 
                                           message='Intervāls ir veiksmīgi samainīts')
                    controller.show_frame(Izvelne)
                    
                else:
                    messagebox.showwarning(title='Nepareizs intervāls', 
                                           message='Intervālam jābūt no 10000 līdz 50000 ar intervālu vienam no otra 10000')
            else:
                messagebox.showwarning(title='Nepareiza ievade', message='Ievadiet skaitliskas vērtības')
            self.from_entry.delete(0, 'end')
            self.to_entry.delete(0, 'end')


class Spele(tk.Frame):
    uzvaretajs = None
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
        self.algoritms_atbilde = None
        self.gen = False
        self.pirmais_gajiens = True
        self.uzvarosa_virsotne = None

        self.punkti = Label(self, text = '0:0', 
                    font=font.Font(family='Arial', size=15), background='white')
        self.punkti.grid(row=0, columnspan=5)

        self.text_speletajs = Label(self, text = 'SPĒLĒTĀJS', 
                    font=font.Font(family='Arial', size=15), background='white').grid(row=0, column=0)
        
        self.datora_gajiens = Label(self, text = 'Dators izvēlējās:', 
                    font=font.Font(family='Arial', size=15), background='white')
        self.datora_gajiens.grid(row=6, columnspan=5)
        
        self.text_speletajs = Label(self, text = 'DATORS', 
                    font=font.Font(family='Arial', size=15), background='white').grid(row=0, column=4)

        self.pasreizejais_speles_skaitlis = Label(self, text = Skaitli.izveletais_skaitlis, 
                    font=font.Font(family='Arial', size=26, weight="bold"), background='white')
        self.pasreizejais_speles_skaitlis.grid(row=3, columnspan=5)

        self.gajiena_status = Label(self, text = 'Šobrīd gājienu veic:', 
                    font=font.Font(family='Arial', size=15), background='white')
        self.gajiena_status.grid(row=4, columnspan=5, sticky='n')
        
        self.dali_2 = Button(self, text = ":2", bd=0, borderwidth=0, width=7, background='white', command = 
                lambda:dali(2), font=font.Font(family='Arial', size=18, weight="bold"))
        self.dali_2.grid( row=5, column=1)
        
        self.dali_3 = Button(self, text = ":3", bd=0, borderwidth=0, width=7, background='white', command = 
                lambda:dali(3), font=font.Font(family='Arial', size=18, weight="bold"))
        self.dali_3.grid( row=5, column=3)
        
        self.poga_atpakal = Button(self, text = "<<<<<<", bd=0, borderwidth=0, width=10, background='white', command = 
                lambda:atpakal(), font=font.Font(family='Arial', size=18, weight="bold")).grid( row=9, column=0)
        
        self.poga_beigt = Button(self, text = 'BEIGT', bd=0, borderwidth=0, width=10, background='white', command = 
                lambda:beigt(), font=font.Font(family='Arial', size=18, weight="bold")).grid( row=9, column=4)
        
        def beigt():
            atbilde = messagebox.askquestion("Iziet", "Vai jūs esat pārliecināts, ka vēlaties iziet?")
            if atbilde == 'yes':
                self.quit()

        def atpakal():
            atbilde = messagebox.askquestion("Atpakaļ", 
                                "Vai jūs esat pārliecināts, ka vēlaties atgriezties uz sākumu? Tas beigs šobrīdējo spēli")
            if atbilde == 'yes':
                Skaitli.izveletais_skaitlis = 0
                ieslegt_2(True)
                ieslegt_3(True)
                self.punkti.configure(text='0:0')
                self.pirmais_gajiens = True
                self.uzvarosa_virsotne = None
                Skaitli.koka_return = None
                self.datora_gajiens.config(text=str('Dators izvēlējās:'))
                controller.show_frame(Izvelne)

        def dali(dalitajs):
            if self.pirmais_gajiens:
                if Izvelne.algoritms == 'minimax':
                    self.algoritms_atbilde = spele_minimax('cilvēks', Skaitli.koka_return, self.gen,dalitajs)
                else:
                    self.algoritms_atbilde = spele_alphabeta('cilvēks', Skaitli.koka_return, self.gen,dalitajs)
                self.punkti.configure(text=str(self.algoritms_atbilde[1][2])+':'+str(self.algoritms_atbilde[1][3]))
                self.pirmais_gajiens = False
            else:
                if Izvelne.algoritms == 'minimax':
                    self.algoritms_atbilde = spele_minimax('cilvēks', self.algoritms_atbilde[1], self.gen,dalitajs)
                else:
                    self.algoritms_atbilde = spele_alphabeta('cilvēks', self.algoritms_atbilde[1], self.gen,dalitajs)
                self.punkti.configure(text=str(self.algoritms_atbilde[1][2])+':'+str(self.algoritms_atbilde[1][3]))
            if self.algoritms_atbilde is not None:
                self.pasreizejais_speles_skaitlis.configure(text=int(self.algoritms_atbilde[1][1]))
            else:
                speles_beigas(self.algoritms_atbilde)
                return
            mainit_speletaju('dators')
            ieslegt_2(False)
            ieslegt_3(False)
            if self.algoritms_atbilde is not None:
                self.uzvarosa_virsotne = self.algoritms_atbilde
                if Izvelne.algoritms == 'minimax':
                    algoritms_atbilde_temp = self.algoritms_atbilde[1]
                    self.algoritms_atbilde = spele_minimax('dators', self.algoritms_atbilde[1], self.gen,dalitajs)
                    if self.algoritms_atbilde is not None:
                        datora_gajiens_temp = algoritms_atbilde_temp[1]/self.algoritms_atbilde[1][1]
                        self.datora_gajiens.config(text=str('Dators izvēlējās: '+str(int(datora_gajiens_temp))))
                else:
                    algoritms_atbilde_temp = self.algoritms_atbilde[1]
                    self.algoritms_atbilde = spele_alphabeta('dators', self.algoritms_atbilde[1], self.gen,dalitajs)
                    if self.algoritms_atbilde is not None:
                        datora_gajiens_temp = algoritms_atbilde_temp[1]/self.algoritms_atbilde[1][1]
                        self.datora_gajiens.config(text=str('Dators izvēlējās: '+str(int(datora_gajiens_temp))))
                datora_gajiens()
            if self.algoritms_atbilde is not None:
                self.uzvarosa_virsotne = self.algoritms_atbilde
            if self.algoritms_atbilde is None or (self.algoritms_atbilde[1][1] %2 != 0 and self.algoritms_atbilde[1][1] %3 !=0) or self.algoritms_atbilde[1][1] <= 10:
                speles_beigas(self.uzvarosa_virsotne)
                return
            print(self.algoritms_atbilde)

        def mainit_speletaju(teksts):
            if teksts == 'dators':
                self.gajiena_status.configure(text="Šobrīd gājienu veic: DATORS")
            else:
                self.gajiena_status.configure(text="Šobrīd gājienu veic: CILVĒKS")

        def ieslegt_2(kondicija):
            if kondicija:
                self.dali_2.configure(text = ":2", command=lambda:dali(2), bg='white')
            else:
                self.dali_2.configure(text = "", command='', bg='gray')

        def ieslegt_3(kondicija):
            if kondicija:
                self.dali_3.configure(text = ":3", command=lambda:dali(3), bg='white')
            else:
                self.dali_3.configure(text = "", command='', bg='gray')
                
        def datora_gajiens():
            mainit_speletaju('cilvēks')
            if self.algoritms_atbilde is not None:
                self.pasreizejais_speles_skaitlis.config(text=int(self.algoritms_atbilde[1][1]))
                self.punkti.configure(text=str(self.algoritms_atbilde[1][2])+':'+str(self.algoritms_atbilde[1][3]))
                ieslegt_2(True)
                ieslegt_3(True)
                if self.algoritms_atbilde[1][1] % 2 != 0:
                    ieslegt_2(False)
                if self.algoritms_atbilde[1][1] % 3 != 0:
                    ieslegt_3(False)

        def speles_beigas(ievade):
            Spele.uzvaretajs = ievade
            Skaitli.izveletais_skaitlis = 0
            print(ievade)
            ieslegt_2(True)
            ieslegt_3(True)
            self.punkti.configure(text='0:0')
            self.pirmais_gajiens = True
            self.uzvarosa_virsotne = None
            print("Uzvarosa virsotne: " + str(ievade))
            Skaitli.koka_return = None
            controller.show_frame(Beigas)


class Beigas(tk.Frame):
    # Beigas, kur tiek atspoguļota uzvara vai zaude
    # Satur pogu "Iziet" un "Jauna spēle"
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
        self.teksts_small = Label(self, text = 'APSVEICAM!', 
                        font=font.Font(family='Arial', size=18), background='white', width=26)
        self.teksts_small.grid( row=0, columnspan=5, sticky='s', )

        self.teksts_big = Label(self, text = 'TU UZVARĒJI!', 
                        font=font.Font(family='Arial', size=36), background='white', width=13)
        self.teksts_big.grid( row=1, columnspan=5, sticky='n')

        self.rezultats = Label(self, text = 'Rezultāts: 0:0', 
                        font=font.Font(family='Arial', size=18), background='white', width=13)
        self.rezultats.grid( row=1, columnspan=5, sticky='')

        self.poga_iziet = Button(self, text = "IZIET", bd=0, borderwidth=0, width=10, background='white', command = 
                lambda:self.quit(), font=font.Font(family='Arial', size=18, weight="bold"))
        self.poga_iziet.grid( row=3, column=1, padx=5, pady=5, sticky='n')

        self.poga_jaunaspele = Button(self, text = "JAUNA SPĒLE", bd=0, borderwidth=0, width=13, background='white', command = 
                lambda:jauna_spele(), font=font.Font(family='Arial', size=18, weight="bold"))
        self.poga_jaunaspele.grid(row=3, column=3, padx=5, pady=5, sticky='n')

        def jauna_spele():
            Skaitli.generet_skaitli = True
            self.teksts_small.config(text='APSVEICAM!')
            self.teksts_big.config(text='TU UZVARĒJI!')
            controller.show_frame(Izvelne)



# Palaišanas kods
app = tkinterApp()