from funciones import *
from data_stark import lista_personajes
import os

lista_copia=list()
lista_copia= normalizar_datos(lista_personajes)
america=list()
flag_1=False
flag_2=False

while True:
    os.system("cls")
    match(stark_marvel_app()):
        case "1.1":
            for item in lista_copia:
                iniciales=extraer_iniciales(item["nombre"])
        case "1.2":
            definir_iniciales_nombre(lista_copia[0])
        case "1.3":
            flag_1=True
            lista_copia=agregar_iniciales_nombre(lista_copia)#
        case "1.4":
            stark_imprimir_nombres_con_iniciales(lista_copia)
        case "2.1":
            generar_codigo_heroe("M",1)
        case "2.2":
            agregar_codigo_heroe(lista_copia[6],12)#
        case "2.3":
            lista_copia=stark_generar_codigos_heroes(lista_copia)
            flag_2=True
        case "3.1":
            sanitizar_entero("valor")
        case"3.2":
            sanitizar_flotante("sex")
        case "3.3":
            sanitizar_string("")
        case "3.4":
            sanitizar_dato(lista_copia[8], "empresa" ,str)
        case "3.5":   
            stark_normalizar_datos(lista_copia)
        case "4.1":
            generar_indice_nombres(lista_copia)
        case "4.2":
            stark_imprimir_indice_nombre(lista_copia)
        case "5.1":
            convertir_cm_a_mtrs(200)
        case "5.2":
            generar_separador("*",87,True)
        case "5.3":
            generar_encabezado("principal")
        case "5.4":
            if(flag_1 and flag_2):
                imprimir_ficha_heroe(lista_copia[7])
            else:
                print("Faltan funciones 1.3 y 2.3")
        case"5.5":
            stark_navegar_fichas(lista_copia)
        case"6":
            stark_menu_principal()
        case"7":
            stark_marvel_app_3()
    os.system("pause")   




