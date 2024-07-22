#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from tkinter import * #interfas grafica
import math #calculos mayematicos

#para crear la interfas grafica
root = Tk() # root (main) window
root.title('CLasificación de suelos')
top = Frame(root) # create frame
top.pack(side='left')

#funcion de clasificacion de suelos
def clasificacion(grava,arena,finos,cu,cc,ip,LL):
    if finos<50:
        if grava>arena: #Se clasifica como grava (G)
            if finos>12: #Porcentaje de finos mayor a 12%
                if ip<(0.73*(LL-20)) or ip>7: #indice de plasticidad mayor a 7
                    a="GC"
                    if arena < 15:  #de donde sale este 
                        b="GRAVA ARCILLOSA"
                    else:
                        b="GRAVA ARCILLOSA CON ARENA"
                elif ip<(0.73*(LL-20)) or ip<4: #indice de plasticidad menor a 4
                    a="GM"
                    if arena < 15:
                        b="GRAVA LIMOSA"
                    else:
                        b="GRAVA LIMOSA CON ARENA"
                elif ip>4 and ip<7: #indice de plasticidad entre 4 y 7
                    a="GC-GM"
                    if arena < 15:
                        b="GRAVA LIMOSA-ARCILLOSA"
                    else:
                        b="GRAVA LIMOSA-ARCILLOSA CON ARENA"
            elif finos<5: #Porcentaje finos menor a 5%
                if cu>=4 and (cc<3 or cc>1):
                    a="GW"
                    if arena < 15:
                        b=("GRAVA BIEN GRADUADA")
                    else:
                        b=("GRAVA BIEN GRADUADA CON ARENA")
                else:
                    a="GP"
                    if arena < 15:
                        b=("GRAVA MAL GRADUADA")
                    else:
                        b=("GRAVA MAL GRADUADA CON ARENA")
            else: # Porcentaje finos entre 5% y 12%
                if cu>=4 and (cc>=1 and cc<=3):
                    if ip<(0.73*(LL-20)) or ip<4:
                        a="GW-GM";
                        if arena < 15:
                            b=("GRAVA BIEN GRADUADA CON LIMO")
                        else:   
                            b=("GRAVA BIEN GRADUADA CON LIMO Y ARENA")
                    else:
                        a="GW-GC";
                        if arena < 15:
                            b=("GRAVA BIEN GRADUADA CON ARCILLA")
                        else:
                            b=("GRAVA BIEN GRADUADA CON ARCILLA Y ARENA")
                elif cu<4 or (cc<1 or cc>3):
                    if ip<(0.73*(LL-20)) or ip<4:
                        a="GP-GM";
                        if arena < 15:
                            b=("GRAVA MAL GRADUADA CON LIMO")
                        else:
                            b=("GRAVA MAL GRADUADA CON LIMO Y ARENA")
                    else:
                        a="GP-GC";
                        if arena < 15:
                            b=("GRAVA MAL GRADUADA CON ARCILLA")
                        else:
                            b=("GRAVA MAL GRADUADA CON ARCILLA Y ARENA")
        else:           #Se clasifica como arena  (S)
            b=("ARENA")
            if finos>12: #Porcentaje de finos mayor a 12%
                if ip>(0.73*(LL-20)) and ip>7: #indice de plasticidad mayor a 7
                    a="SC"
                    if grava < 15:
                        b=("ARENA ARCILLOSA")
                    else:
                        b=("ARENA ARCILLOSA CON GRAVA")
                elif ip<(0.73*(LL-20))or ip<4: #indice de plasticidad menor a 4
                    a="SM"
                    if grava < 15:
                        b=("ARENA LIMOSA")
                    else:
                        b=("ARENA LIMOSA CON GRAVA")
                elif ip>4 and ip<7: #indice de plasticidad entre 4 y 7
                    a="SC-SM"
                    if grava < 15:
                        b=("ARENA LIMOSA-ARCILLOSA")
                    else:
                        b=("ARENA LIMOSA-ARCILLOSA CON GRAVA")
            elif finos<5: #Porcentaje finos menor a 5%
                if cu>=6 and (cc<3 or cc>1):
                    a="SW"
                    if grava < 15:
                        b=("ARENA BIEN GRADUADA")
                    else:
                        b=("ARENA BIEN GRADUADA CON GRAVA")
                else:
                    a="SP"
                    if grava < 15:
                        b=("ARENA MAL GRADUADA")
                    else:
                        b=("ARENA MAL GRADUADA CON GRAVA")
            else: # Porcentaje finos entre 5% y 12%
                if cu>=6 and (cc>=1 and cc<=3):
                    if ip<(0.73*(LL-20)) or ip<4:
                        a="SW-SM"
                        if grava < 15:
                            b=("ARENA BIEN GRADUADA CON LIMO")
                        else:
                            b=("ARENA BIEN GRADUADA CON LIMO Y GRAVA")
                    elif ip>(0.73*(LL-20)) or ip>7:
                        a="SW-SC"
                        if grava< 15:
                            b=("ARENA BIEN GRADUADA CON ARCILLA")
                        else:
                            b=("ARENA BIEN GRADUADA CON ARCILLA Y GRAVA")
                else:
                    if ip<(0.73*(LL-20)) or ip<4:
                        a="SP-SM"
                        if grava< 15:
                            b=("ARENA MAL GRADUADA CON LIMO")
                        else:
                            b=("ARENA MAL GRADUADA CON LIMO Y GRAVA")
                    elif ip>(0.73*(LL-20)) or ip>7:
                        a="SP-SC"
                        if grava< 15:
                            b=("ARENA MAL GRADUADA CON ARCILLA")
                        else:
                            b=("ARENA MAL GRADUADA CON ARCILLA Y GRAVA")        
    
    else:
        if LL<50: #Limite liquido menor del 50%
            if ip>7 and ip>(0.73*(LL-20)): # indice de plasticidad mayor a 7
                a="CL"
                if (100-finos)<30: # excede No. 200 < 30%
                    if (100-finos)<15:
                        b=("ARCILLA DE BAJA COMPRESIBILIDAD");
                    else:
                        if arena>=grava:
                            b=('ARCILLA DE BAJA COMPRESIBILIDAD CON ARENA');
                        else:
                            b=('ARCILLA DE BAJA COMPRESIBILIDAD CON GRAVA');
                else: # excede No. 200 > 30%
                    if arena>grava:
                        if grava < 15:
                            b=('ARCILLA DE BAJA COMPRESIBILIDAD ARENOSA')
                        else:
                            b=('ARCILLA DE BAJA COMPRESIBILIDAD ARENOSA CON GRAVA')    
                    else:
                        if grava < 15:
                            b=('ARCILLA DE BAJA COMPRESIBILIDAD Y TIPO GRAVA')
                        else:
                            b=('ARCILLA DE BAJA COMPRESIBILIDAD Y TIPO GRAVA CON ARENA')                   
            elif ip<4 or ip<(0.73*(LL-20)): # indice de plasticidad menor a 4
                a="ML"
                if (100-finos)<30:
                    if (100-finos)<15:
                        b=('LIMO')
                    else:
                        if arena>=grava:
                            b=('LIMO CON ARENA')
                        else:
                            b=('LIMO CON GRAVA')
                else:
                    if arena>=grava:
                        if grava<=15:
                            b=('LIMO ARENOSO')
                        elif grava>15:
                            b=('LIMO ARENOSO CON GRAVA')
                    else:
                        if arena<=15:
                            b=('LIMO Y TIPO GRAVA')
                        elif arena>15:
                            b=('LIMO Y TIPO GRAVA CON ARENA')
            else: # ip entre 4 y 5
                a='CL-ML'
                if (100-finos)<30:
                    if (100-finos)<15:
                        b=('ARCILLA LIMOSA')
                    else:
                        if arena>grava:
                            b=('ARCILLA LIMOSA CON ARENA')
                        else:
                            b=('ARCILLA LIMOSA CON GRAVA')
                else:
                    if arena > grava:
                        if grava<15:
                            b=('ARCILLA LIMOSA CON ARENA ')
                        elif grava>=15:
                            b=('ARCILLA ARENOSA-LIMOSA CON GRAVA')
                    else:
                        if arena<15:
                            b=('ARCILLA GRAVOSA-LIMOSA')
                        elif arena >=15:
                            b=('ARCILLA GRAVOSA-LIMOSA CON ARENA')
        else:
            if ip>= (0.73*(LL-20)):
                a='CH'
                if (100-finos)<30:
                    if (100-finos)<15:
                        b=('ARCILLA DE ALTA COMPRESIBILIDAD')
                    else:
                        if arena>=grava:
                            b=('ARCILLA GRUESA CON ARENA')
                        elif arena<grava:
                            b=('ARCILLA GRUESA CON GRAVA')
                else:
                    if arena>=grava and grava<15:
                        b=('ARCILLA GRUESA ARENOSA')
                    elif arena>=grava and grava>=15:
                        b=('ARCILLA GRUESA ARENOSA CON GRAVA')
                    elif arena < grava and arena<15:
                        b=('ARCILLA GRUESA GRAVOSA')
                    elif arena<grava and arena>=15:
                        b=('ARCILLA GRUESA GRAVOSA CON ARENA')
            else:
                a='MH'
                if (100-finos)<30:
                    if (100-finos)<15:
                        b=('LIMO ELASTICO')
                    else:
                        if arena>=grava:
                            b=('LIMO ELÁSTICO CON ARENA')
                        elif arena<grava:
                            b=('LIMO ELÁSTICO CON GRAVA')
                else:
                    if arena>=grava and grava<15:
                        b=('LIMO ELÁSTICO ARENOSO')
                    elif arena>=grava and grava>=15:
                        b=('LIMO ELÁSTICO ARENOSO CON GRAVA')
                    elif arena < grava and arena<15:
                        b=('LIMO ELÁSTICO GRAVOSO')
                    elif arena<grava and arena>=15:
                        b='LIMO ELÁSTICO GRAVOSO CON ARENA'
    return [a,b]

def comp_s():
    global s,d

    a=clasificacion(float(grava.get()),float(arena.get()),float(finos.get()),float(cu.get()),float(cc.get()),float(ip.get()),float(LL.get()))
    d.set(a[1])
    s.set(a[0])


#configuracion del cuadro de dialogo

root.configure(bg='white')  # Establecer fondo blanco para la ventana principal
top = Frame(root, bg='white')  # Establecer fondo blanco para el Frame
top.pack(side='left', padx=10, pady=10)

hwtext = Label(top, text='Clasificación de suelos U.S.C.S \n Elaborado por: Yesid Paul Goyes \n goyes.yesid@gmail.com', font=("Times New Roman", 14, "bold"), bg='white').grid(row=0,column=0,pady=15)
hwtext1 = Label(top, text='% Grava', bg='white', font=("Helvetica", 10)).grid(row=1,column=0)
hwtext2 = Label(top, text='% Arena', bg='white', font=("Helvetica", 10)).grid(row=2,column=0)
hwtext3 = Label(top, text='% Finos', bg='white', font=("Helvetica", 10)).grid(row=3,column=0)
hwtext4 = Label(top, text='cu (Coeficiente de uniformidad)', bg='white', font=("Helvetica", 10)).grid(row=4,column=0)
hwtext5 = Label(top, text='cc (Coeficiente de curva)', bg='white', font=("Helvetica", 10)).grid(row=5,column=0)
hwtext6 = Label(top, text='IP (indice de plasticidad)', bg='white', font=("Helvetica", 10)).grid(row=6,column=0)
hwtext7 = Label(top, text='LL (%límite líquido)', bg='white', font=("Helvetica", 10)).grid(row=7,column=0)

arena = StringVar() # variable to be attached to arena_entry
grava = StringVar() # variable to be attacher to grava_entry
finos = StringVar() # variable to be attacher to finos_entry
cu = StringVar() # variable to be attacher to finos_entry
cc = StringVar() # variable to be attacher to finos_entry
ip = StringVar()
LL = StringVar()
arena.set('14') # default value
grava.set('0')
finos.set('86')
cu.set('0')
cc.set('0')
ip.set('28')
LL.set('55')
grava_entry = Entry(top, width=4, textvariable=grava, bd=0.5, relief='solid', font=("Helvetica", 10)).grid(row=1,column=1)
arena_entry = Entry(top, width=4, textvariable=arena, bd=0.5, relief='solid', font=("Helvetica", 10)).grid(row=2,column=1)
finos_entry = Entry(top, width=4, textvariable=finos, bd=0.5, relief='solid', font=("Helvetica", 10)).grid(row=3,column=1)
cu_entry = Entry(top, width=4, textvariable=cu, bd=0.5, relief='solid', font=("Helvetica", 10)).grid(row=4,column=1)
cc_entry = Entry(top, width=4, textvariable=cc, bd=0.5, relief='solid', font=("Helvetica", 10)).grid(row=5,column=1)
ip_entry = Entry(top, width=4, textvariable=ip, bd=0.5, relief='solid', font=("Helvetica", 10)).grid(row=6,column=1)
LL_entry = Entry(top, width=4, textvariable=LL, bd=0.5, relief='solid', font=("Helvetica", 10)).grid(row=7, column=1, padx=5, pady=5)


s = StringVar() # variable to be attached to s_label
d = StringVar() # variable to be attached to s_label

compute = Button(top, text='CLASIFICAR', command=comp_s, font=("Times New Roman", 12, "bold"), bg="#F4F6F6", fg="black", bd=1, relief='solid').grid(row=8, column=0, pady=10)

s_label = Label(top, textvariable=s, width=18,background='#D1F2EB',font='times 14 bold').grid(row=9,columnspan=3)
d_label =Label(top, textvariable=d, width=40,background='#F9E79F',font='times 10 bold').grid(row=10,columnspan=3,pady=10)
root.mainloop()