# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 11:03:31 2024

@author: 
"""
def classify_soil(LL, IP, finos, arena, grava):
    if LL >= 50:
        if IP >= 0.73 * (LL - 20):
            return "Orgánico"
        else:
            if grava >= 30:
                return "MH"
            else:
                if grava < 15:
                    return "MH"
                else:
                    if 15 <= grava <= 29:
                        if arena >= grava:
                            return "Limo elástico con arena"
                        else:
                            return "Limo elástico con grava"
    else:
        return "Clasificación no cubierta por este árbol de decisión"

# Ejemplo de uso
percent_gravel = 24
percent_sand = 10
percent_fines = 66
IP = 2
LL = 60

result = classify_soil(LL, IP, percent_fines, percent_sand, percent_gravel)
print(result)