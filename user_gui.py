from heiristiska_funkcija import *
from tkinter import *
import tkinter.font as font
import tkinter

#Pamācība ņemta no https://www.geeksforgeeks.org/python-gui-tkinter/

def otraisLogsAlgoritms():
    pass


#Izvēles lapa
def openOtraisLogs():
    def otraisLogsIzvele(param, poga):
        if param == 0:
            print("Hello world")

    root.destroy()
    otraisLogs = Tk()
    otraisLogs.title("Izvēlies algoritmu")
    otraisLogs.geometry('640x480')
    otraisLogs.columnconfigure(0, weight=2)
    otraisLogs.columnconfigure(1, weight=2)
    otraisLogs.columnconfigure(2, weight=1)
    otraisLogs.columnconfigure(3, weight=2)
    otraisLogs.columnconfigure(4, weight=2)
    otraisLogs.rowconfigure(0, weight=1)
    otraisLogs.rowconfigure(1, weight=1)
    otraisLogs.rowconfigure(2, weight=1)
    otraisLogs.rowconfigure(3, weight=1)
    otraisLogs.rowconfigure(4, weight=1)
    otraisLogs.configure(bg='gray')
    kurs_saks = Label(otraisLogs, text = 'KURŠ UZSĀKS SPĒLI?', 
                   font=font.Font(family='Arial', size=26, weight="bold"), background='white').grid(row=0, columnspan=5)
    poga_speletajs = Button(otraisLogs, text = 'SPĒLĒTĀJS', bd=0, borderwidth=0, width=10, command = 
              lambda: otraisLogsIzvele(1, poga_speletajs), font=font.Font(family='Arial', size=18, weight="bold")).grid( row=1, padx=5, columnspan=2, sticky='ne')
    poga_dators = Button(otraisLogs, text = 'DATORS', bd=0, borderwidth=0, width=10, command = 
              '', font=font.Font(family='Arial', size=18, weight="bold")).grid( row=1, padx=5, column=2, columnspan=2, sticky='nw')


#Galvenā lapa
root = Tk()
root_font = font.Font(family='Arial')
root.geometry('640x480') 
root.title("Sākt")
root.configure(bg='gray')
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.columnconfigure(2, weight=1)
root.columnconfigure(3, weight=1)
root.columnconfigure(4, weight=1)
root.rowconfigure(0, weight=3)
root.rowconfigure(1, weight=3)
root.rowconfigure(2, weight=1)
root.rowconfigure(3, weight=1)
poga = Button(root, text = 'SĀKT', bd=0, borderwidth=2, width=10, command = 
              openOtraisLogs, font=font.Font(family='Arial', size=26, weight="bold")).grid( row=1, columnspan=5)
virsraksts = Label(root, text = 'MIP 33. GRUPAS 1. PRAKTISKAIS DARBS', 
                   font=font.Font(family='Arial', size=18), background='white').grid(row=0, columnspan=5)
v_daniels = Label(root, borderwidth=2, text = 'Dāniels', 
                   font=font.Font(family='Arial', size=18), background='white').grid(column=0, row=2, sticky='sw', padx=7)
u_daniels = Label(root, borderwidth=2, text = 'Dūda', 
                   font=font.Font(family='Arial', size=18), background='white').grid(column=0, row=3, sticky='nw', padx=7)
v_aleksandrs = Label(root, borderwidth=2, text = 'Aleksandrs', 
                   font=font.Font(family='Arial', size=18), background='white').grid(column=1, row=2, sticky='s', padx=7)
u_aleksandrs = Label(root, borderwidth=2, text = 'Jančevskis', 
                   font=font.Font(family='Arial', size=18), background='white').grid(column=1, row=3, sticky='n', padx=7)
v_ugis = Label(root, borderwidth=2, text = 'Uģis Raimonds', 
                   font=font.Font(family='Arial', size=18), background='white').grid(column=2, row=2, sticky='s', padx=7)
u_ugis = Label(root, borderwidth=2, text = 'Sproģis', 
                   font=font.Font(family='Arial', size=18), background='white').grid(column=2, row=3, sticky='n', padx=7)
v_bernhards = Label(root, borderwidth=2, text = 'Bernhards', 
                   font=font.Font(family='Arial', size=18), background='white').grid(column=3, row=2, sticky='s', padx=7)
u_bernhards = Label(root, text = 'Arnītis', 
                   font=font.Font(family='Arial', size=18), background='white').grid(column=3, row=3, sticky='n', padx=7)
v_sandijs = Label(root, text = 'Sandijs', 
                   font=font.Font(family='Arial', size=18), background='white').grid(column=4, row=2, sticky='se', padx=7)
u_sandijs = Label(root, text = 'Sīlis', 
                   font=font.Font(family='Arial', size=18), background='white').grid(column=4, row=3, sticky='ne', padx=7)
root.mainloop()