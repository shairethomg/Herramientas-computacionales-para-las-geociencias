#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from tkinter import *
import math

root = Tk() # root (main) window
root.title('CLasificación de suelos')
top = Frame(root) # create frame
top.pack(side='left')

def clasificacion(grava,arena,finos,cu,cc,ip,LL):
    if finos<50:
        if grava>arena: #Se clasifica como grava (G)
            if finos>12: #Porcentaje de finos mayor a 12%
                if ip<(0.73*(LL-20)) or ip>7: #indice de plasticidad mayor a 7
                    a="GC"
                    if arena < 15:
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
                        b="GRAVA LIMO-ARCILLOSA"
                    else:
                        b="GRAVA LIMO-ARCILLOSA CON ARENA"
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
                        b=("ARENA LIMO-ARCILLOSA")
                    else:
                        b=("ARENA LIMO-ARCILLOSA CON GRAVA")
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
                        b=("ARCILLA LIGERA");
                    else:
                        if arena>=grava:
                            b=('ARCILLA LIGERA CON ARENA');
                        else:
                            b=('ARCILLA LIGERA CON GRAVA');
                else: # excede No. 200 > 30%
                    if arena>grava:
                        if grava < 15:
                            b=('ARCILLA LIGERA ARENOSA')
                        else:
                            b=('ARCILLA LIGERA ARENOSA CON GRAVA')    
                    else:
                        if grava < 15:
                            b=('ARCILLA LIGERA Y TIPO GRAVA')
                        else:
                            b=('ARCILLA LIGERA Y TIPO GRAVA CON ARENA')                   
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
                            b=('ARCILLA LIMO-ARENOSA ')
                        elif grava>=15:
                            b=('ARCILLA LIMO-ARENOSA CON GRAVA')
                    else:
                        if arena<15:
                            b=('ARCILLA LIMOSA Y TIPO GRAVA')
                        elif arena >=15:
                            b=('ARCILLA LIMOSA Y TIPO GRAVA CON ARENA')
        else:
            if ip>= (0.73*(LL-20)):
                a='CH'
                if (100-finos)<30:
                    if (100-finos)<15:
                        b=('ARCILLA DENSA')
                    else:
                        if arena>=grava:
                            b=('ARCILLA DENSA CON ARENA')
                        elif arena<grava:
                            b=('ARCILLA DENSA CON GRAVA')
                else:
                    if arena>=grava and grava<15:
                        b=('ARCILLA DENSA ARENOSA')
                    elif arena>=grava and grava>=15:
                        b=('ARCILLA DENSA ARENOSA CON GRAVA')
                    elif arena < grava and arena<15:
                        b=('ARCILLA DENSA Y TIPO GRAVA')
                    elif arena<grava and arena>=15:
                        b=('ARCILLA DENSA Y TIPO GRAVA CON ARENA')
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
                        b=('LIMO ELÁSTICO Y TIPO GRAVA')
                    elif arena<grava and arena>=15:
                        b='LIMO ELÁSTICO Y TIPO GRAVA ARENOSO'
    return [a,b]

def comp_s():
    global s,d

    a=clasificacion(float(grava.get()),float(arena.get()),float(finos.get()),float(cu.get()),float(cc.get()),float(ip.get()),float(LL.get()))
    d.set(a[1])
    s.set(a[0])




hwtext = Label(top, text='Clasificación suelos U.S.C.S \n ELABORADO POR: Yesid Paul Goyes / yesid.goyes@gmail.com').grid(row=0,column=0,pady=15)
hwtext1 = Label(top, text='grava %').grid(row=1,column=0)
hwtext2 = Label(top, text='arena %').grid(row=2,column=0)
hwtext3 = Label(top, text='finos %').grid(row=3,column=0)
hwtext4 = Label(top, text='cu (Coeficiente de uniformidad)').grid(row=4,column=0)
hwtext5 = Label(top, text='cc (Coeficiente de curva)').grid(row=5,column=0)
hwtext6 = Label(top, text='IP (indice de plasticidad)').grid(row=6,column=0)
hwtext7 = Label(top, text='LL (límite líquido)%').grid(row=7,column=0)

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
grava_entry = Entry(top, width=6, textvariable=grava).grid(row=1,column=1)
arena_entry = Entry(top, width=6, textvariable=arena).grid(row=2,column=1)
finos_entry = Entry(top, width=6, textvariable=finos).grid(row=3,column=1)
cu_entry = Entry(top, width=6, textvariable=cu).grid(row=4,column=1)
cc_entry = Entry(top, width=6, textvariable=cc).grid(row=5,column=1)
ip_entry = Entry(top, width=6, textvariable=ip).grid(row=6,column=1)
LL_entry = Entry(top, width=6, textvariable=LL).grid(row=7,column=1)


s = StringVar() # variable to be attached to s_label
d = StringVar() # variable to be attached to s_label

compute = Button(top, text=' CLASIFICAR', command=comp_s).grid(row=8,column=0,pady=10)

s_label = Label(top, textvariable=s, width=18,background='green',font='times 14 bold').grid(row=9,columnspan=3)
d_label =Label(top, textvariable=d, width=40,background='yellow',font='times 10 bold').grid(row=10,columnspan=3,pady=10)

root.mainloop()


