import user_gui
class Izvelies2(tk.Frame):
    from speles_skaitli import speles_skaitli


    
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
        Label(self, text = 'Izvēlies skaitli:', 
                    font=font.Font(family='Arial', size=26, weight="bold"), background='white').grid(row=0, columnspan=5)
        poga_turpinat = Button(self, text = '>>>>>>>', bd=0, borderwidth=0, width=10, background='white', command = 
                lambda: turpinat(), font=font.Font(family='Arial', size=18, weight="bold"))
        poga_turpinat.grid( row=4, padx=25, column=0, columnspan=5, sticky='s')
        poga_turpinat = Button(self, text = '<<<<<<', bd=0, borderwidth=0, width=10, background='white', command = 
                lambda: turpinat(), font=font.Font(family='Arial', size=18, weight="bold"))
        poga_turpinat.grid( row=4, padx=0, column=0, columnspan=5, sticky='s')
        
        # Funkcija, kas pārbauda, vai viens no katra dotā parametra ir izvēlēts un ved uz nākošo lapu
        # Gadījumā, ja nav izvēlēts kāds no nepieciešamajiem parametriem, tiek izvadīta kļūda
    