from data_stark import *
import re
import os

def normalizar_datos(lista_heroes:list)->list:
    """Funcion que recibe una lista por parametro , copia y retorna una lista
    nueva la que no modifica la lista origen.

    Args:
        lista_heroes (list): list

    Returns:
        list: retorna lista copia
    """
    lista_copia=list()
    for item in lista_heroes:
        lista_copia.append(item.copy())
    return lista_copia  #check

#1.1
def extraer_iniciales(nombre_heroe:str)->str:
    """Esta funcion extrae las iniciales de todos los heroes

    Args:
        nombre_heroe (str): nombre del heroe

    Returns:
        str: iniciales
    """
    if len(nombre_heroe) > 0:
        if "-" in nombre_heroe:
            nombre_heroe = nombre_heroe.replace("-", " ")
        if "the" in nombre_heroe:
            nombre_heroe = nombre_heroe.replace("the", "")
        iniciales = ""
        for palabra in nombre_heroe.split():
            iniciales += palabra[0].upper() + "."
        retorno = iniciales
    else: retorno = "N/A"
    return retorno
#1.2
def definir_iniciales_nombre(heroe:dict)->bool:
    """Funcion que crea nueva clave , recibe diccionario y una clave que sera 
    una nueva llave dentro del dicc , devuelve True si no hubo error ,
    False si hubo algun error 

    Args:
        heroe (dict): diccionario
        clave (str): nueva clave

    Returns:
        bool: true|false
    """
    if type(heroe) == dict and "nombre" in heroe.keys():
        heroe["iniciales"]=extraer_iniciales(heroe["nombre"])
        return heroe
    else:
        return False
#1.3
def agregar_iniciales_nombre(lista_heroes:list)->list:
    """Funcion que añade las iniciales del nombre a la lista

    Args:
        lista_heroes (list): lista heroes

    Returns:
        list: appendea las iniciales
    """
    control=list()
    if type(lista_heroes) == list and len(lista_heroes)>0:
        for item in lista_heroes:
            control.append(definir_iniciales_nombre(item))
            if(control == False):
                print("El origen de datos no contiene el formato correcto")
        return control
#1.4
def stark_imprimir_nombres_con_iniciales(lista_heroes:list)->None:
    """Funcion que recibe por parametro lista heroes,añade las iniciales a diccionario 
    en la lista , imprime la lista completa con los nombres y las iniciales encerradas
    en parentesis .
    Args:
        lista_heroes (list): _description_
    """
    item=list()
    if type(lista_heroes) == list and len(lista_heroes)>0:
        grupo=agregar_iniciales_nombre(lista_heroes)
        for item in grupo:
            dato=f"     * {item['nombre']} ({item['iniciales']})"
            print(dato)
#2.1
def generar_codigo_heroe(genero_heroe:str, id_heroe:int)->str:
    """Funcion que recibe por parametro la id del heroe ,el genero del heroe
    la funcion que genera un string con formaato GENERO-000…000ID , valida 
    que el identificador del heroe sea numerico y que el genero no se 
    encuentre vacio.

    Args:
        genero_heroe (str): M|NB|F
        id_heroe (int): id heroe

    Returns:
        str: formato GENERO-000…000ID 
    """
    if (type(id_heroe) == int) and (genero_heroe != "") and (genero_heroe == "M" or genero_heroe == "F" or genero_heroe == "NB"):
            return ("{0}-{1:08d}".format(genero_heroe,id_heroe))
    else:
        return "N/A"
#2.2
def agregar_codigo_heroe(heroe:dict , id_heroe:int)->dict:
    """Funcion que recibe como parametro un diccionario heroe y 
    id de heroe que representa le identificador del heroe.
    La funcion agrega una nueva clave llamado "codigo_heroe al
    diccionario heroe y lo retorna .

    Args:
        heroe (dict): diccionario
        id_heroe (int): id heroe

    Returns:
        dict: nuevo clave "codigo_heroe" y valro
    """
    if len(heroe) > 0:
        guardado=generar_codigo_heroe(heroe["genero"] ,id_heroe)
        if len(guardado) < 11 :
            heroe["codigo_heroe"] = guardado
            return heroe
        else:
            print("Codigo no menor a 10 caracteres")
    else:
        return False
#2.3
def stark_generar_codigos_heroes(lista_personajes:list)->list:
    """Funcion que itera la lista de personajes y agrega el diccionario
    a la lista , la funcion valida que la lista contenta almenos un elemento,
    que todos los elementos de la lista sean de tipo diccionario y que todos
    los elementos contengan la clave genero.

    Args:
        lista_personajes (list): lista de personajes

    Returns:
        list: returna la lista con una nueva clave y valor
    """
    poscicion=0
    muestreo=list()
    if  len(lista_personajes) > 0:
        for item in lista_personajes:
            if type(item) == dict and ("genero" in item.keys()):
                poscicion+=1
                muestreo.append(agregar_codigo_heroe(item,poscicion))
              
    print(f"Se asignaron {poscicion} codigos ")
    print(f"* El código del primer héroe es:{muestreo[0]['codigo_heroe']}")
    print(f"* El código del último héroe es:{muestreo[23]['codigo_heroe']}")
    return muestreo
#3.1
def sanitizar_entero(numero_str:str)->int:
    """La funcion analiza el string que representa un numero entero 
    y determina si es un numero entero. Si contiene caracteres numericos
    retorna -1 , si el numero es negativo ,retorna -2 y si no se pueden 
    convertir a entero entonces retorna -3. Si no pasa ninguno de estos 3 
    casos retorna el string convertido a entero.

    Args:
        numero_str (str): str a convertir

    Returns:
        int: numero convertido a entero
    """
    try:
        numero_str=int(numero_str)
        if type(numero_str) == str:
            return -1
        elif numero_str < 0:
            return -2
        else:
            return numero_str
        
    except ValueError:
        return -3
#3.2  
def sanitizar_flotante(numero_str:float):
    """La funcion analiza el string que representa un numero flotante 
    y determina si es un numero es float. Si contiene caracteres numericos
    retorna -1 , si el numero es negativo ,retorna -2 y si no se pueden 
    convertir a entero entonces retorna -3. Si no pasa ninguno de estos 3 
    casos retorna el string convertido a entero.

    Args:
        numero_str (str): str a convertir

    Returns:
        float: numero convertido a float
    """
    try:
        numero_str=float(numero_str)
        if type(numero_str) == str:
            return -1
        elif numero_str < 0:
            return -2
        else:
            return numero_str
        
    except ValueError:
        return -3
#3.3
def sanitizar_string(valor_str :str)->str:
    """La funcion analiza el string que representa un texto a validar  
    y determina si es un str.La funcion analiza si el string recibido
    es solo texto(sin numeros).En caso de encontrarse numeros retorna 
    N/A.En caso de que el valor_str contenta una / se reemplaza por un 
    espacio.En caso de que texto se encuentre vacio se pone una valor 
    por defecto "-" y se retorna .

    Args:
        numero_str (str): str a convertir

    Returns:
        str: str convertido a texto en mayusculas | valor por defecto "-"
    """
    valor_por_defecto="-"
    if valor_str.isdigit():#validar que no entee numero
        return "N/A"
    if len(valor_str) > 0:
        if "/" in valor_str:
            valor_str=valor_str.replace("/" , "")
            valor_str=valor_str.lower()
            return valor_str
        
        return valor_str
    else:
        return valor_por_defecto
#3.4
def sanitizar_dato(heroe:dict , clave:str ,tipo_dato):
    """Funcion que recibe por parametro un diccionario heroe , una clave string
    que representa una clave y tipo_dato es un string que representa el tipo de
    dato a sanitizar , valida que la clave exista dentro del diccionario , si la
    clave no existe se imprime "la clave especificada no existe en el heroe".


    Args:
        heroe (dict): diccionario heroe
        clave (str): clave del diccionario
        tipo_dato (_type_): str|int|float

    Returns:
        str: string
    """
    if clave in heroe:
        if tipo_dato == int:
            print("(1)")
            a=sanitizar_entero(heroe[clave])
        elif tipo_dato == float:
            print("(2)")
            a=sanitizar_flotante(heroe[clave])
        elif tipo_dato == str:
            print("(3)",heroe[clave])
            a=sanitizar_string(heroe[clave])
        else:
            print("Tipo de dato no reconocido")
    else:
        print("La clave especificada no existe en el héroe")
    return a

#3.5
def stark_normalizar_datos(lista_heroes:list)->None:
    """Funcion que recibe la lista de heroes , recorre la lista de heroes y 
    sanatiza los valores solo de las claves altura|peso|color_pelo|color_pelo
    fuerza e inteligencia. Una vez finalizado el esto se imprime un mensaje de
    datos normalizados , valida que la lista de heroes no este vacia.
    Args:
        lista_heroes (list): lista heroes
    """
    if len(lista_heroes)>0 :
        for item in lista_heroes:
            sanitizar_dato(item , "nombre" , str)
        print("Datos normalizados")
    else:
        print("Error lista vacia ")
#4.1
def generar_indice_nombres(lista_personajes:list)->None:
    """Funcion que recibe por parametro la lista de heroes , la funcion itera
    la lista de personajes y genera una lista donde cada elemento es cada 
    palabra que componen el nombre de los personajes.
    La funcion valida que la lista contenga al menos un elemento ,que todos
    los elementos de la lista de heroes sean tipo diccionario y que todos
    los elementos contengan la clave "nombre".


    Args:
        lista_personajes (list): lista de personajes

    Returns:
        none: nada
    """
    lista_nueva=list()
    if len(lista_personajes) > 0:    
        for item in lista_personajes:
            if type(item) == dict and ("nombre" in item.keys()):
                item=re.findall("[a-zA-z]+",item["nombre"])
                lista_nueva.append(item.copy())
        return lista_nueva
    else:
        print("El origen de datos no contiene el formato correcto ")
#4.2
def stark_imprimir_indice_nombre(lista_heroes:list)->None:
    """Funcion que recibe la lista de personajes , muestra por pantalla el
    el indicegenerado por la funcion generar_indice_nombres con todos los 
    nombres separados con un guion.

    Args:
        lista_heroes (list): lista heroes  
    """
    lista_nombres=generar_indice_nombres(lista_heroes)
    for item in lista_nombres:
        item=str(item)
        item= item.replace(r"['", "").replace(r"']", "").replace(r"',","").replace("'","").replace(" ","-")#gward
        print(item)
#5.1
def convertir_cm_a_mtrs(valor_cm:float)->float:
    """Funcion que convierte un numero centimetros a metros , la funcion
    recibe el numero y lo convierte a metros  , valida si es numero es 
    positivo sino retorna -1.

    Args:
        valor_cm (float): numero centimetros

    Returns:
        float: retorna -1 o el numero convertido en flotante 
    """
    valor_cm=float(valor_cm)
    if (valor_cm > 0) and type(valor_cm)== (float):
        valor_mts=valor_cm* 0.01
        print(f"Valor a mts : {valor_mts}")
    else:
        return -1
#5.2   
def generar_separador(patron:str , largo:int , imprimir:bool):
    """Funcion que recibe un patron que se utiliza para generar un separador ,
    largo que representa un numero que representa la cantidad de catacteres que
    ocupa el separador , imprimir es un parametro opcional de tipo booleano.
    La funcion valida que el parametro patron tenga al menos un caracter y como
    maximo dos.
    Que el parametro largo se un entero entre 1 y 235.
    Si no se verifica esto devuelve N/A.


    Args:
        patron (str): patrol a eleccion
        largo (int): 1 a 235
        imprimir (bool): opcional

    Returns:
        None: None
    """
    if (len(patron)>0 and len(patron) < 3) and (largo > 0 and largo <= 235):     
        separador = patron * largo
        if imprimir ==False:
            return separador
        
        if imprimir ==True:
            print(separador)
            return separador
#5.3
def generar_encabezado(titulo:str):
    """Recibe como parametro un string que contiene el titulo envuekto entre
    dos separadores.

    Args:
        titulo (str): titulo a eleccion
    """
    generar_separador("*",87,True)
    titulo=titulo.upper()
    print(titulo)
    generar_separador("*",87,True)

#5.4
def imprimir_ficha_heroe(heroe:dict):
    """Funcion que recibe un diccionario con datos de heroe

    Args:
        heroe (dict): diccionario
    """
    generar_encabezado("principal")
    print(f"NOMBRE DEL HEROE : {heroe['nombre']} ({heroe['iniciales']})")
    print(f"IDENTIDAD SECRETA: {heroe['identidad']}")
    print(f"CONSULTORA {heroe['empresa']}")
    print(f"CÓDIGO DE HÉROE : {heroe['codigo_heroe']}")
    generar_encabezado("fisico")
    print(f"ALTURA : {heroe['altura']}")
    print(f"PESO : {heroe['peso']}")
    print(f"FUERZA {heroe['fuerza']}")
    generar_encabezado("señas particulares")
    print(f"COLOR DE OJOS: {heroe['color_ojos']}")
    print(f"COLOR DE PELO: {heroe['color_pelo']}")

#5.5

def stark_navegar_fichas(lista_heroes:list)->None:
    """
    La funcion recibe como parametro la lista de heroes , la funcion imprime
    la ficha del primer personaje de la lista y luego solicita al usuario que 
    ingrese la opciones 1|2|S.
    Args:
        heroe (list): lista_heroes
    """
    i=0
    repeticion=True
    while repeticion: 
        imprimir_ficha_heroe(lista_heroes[i])
        dato=input(
        """
        Ingresar opcion
        [1] Ir a la izquierda
        [2] Ir a la derecha  
        [S] Salir
        """)

        match(dato).upper(): 
            case "1":  
                if i==0:
                    i=24
                i-=1
                os.system("cls")
            case "2":
                print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>",i)
                if i==23:
                    i=-1
                i+=1
                os.system("cls")
            case "S":
                os.system("cls")
                repeticion=False
            case _:
                print("ERROR INGRESE OTRO VALOR")
                os.system("cls")


def imprimir_menu(): 
    """
    Funcion que imprime menu
    """
    print("""
    1 - Imprimir la lista de nombres junto con sus iniciales
    2 - Generar códigos de héroes
    3 - Normalizar datos
    4 - Imprimir índice de nombres
    5 - Navegar fichas
    S - Salir
    """)

def stark_menu_principal()->None:
    """Funcion que recibe dato por usuario

    Returns:
        none: none
    """
    imprimir_menu()
    dato=input("Ingresar opcion >: ")
    return dato

def stark_marvel_app_3(lista_copia:list):
    """Funcion que recibe la lista de heroes , la funcion se encarga
    de la ejecucion del programa.

    Args:
        lista_copia (list): lista copia
    """
    repeticion=True
    flag_1=False
    flag_2=False
    while repeticion:
        os.system("cls")
        match(stark_menu_principal().upper()):
            case "1":
                stark_imprimir_nombres_con_iniciales(lista_copia)
                flag_1=True
            case "2":
                stark_generar_codigos_heroes(lista_copia)
                flag_2=True
            case "3":
                stark_normalizar_datos(lista_copia)
            case "4":
                stark_imprimir_indice_nombre(lista_copia)
            case "5":
                if(flag_1 and flag_2):
                    stark_navegar_fichas(lista_copia)
                else:
                    print("Faltan funciones 1.3 y 2.3")
            case "S":
                repeticion=False
        os.system("pause")   

def stark_marvel_app():
    print(f"""
    1.1-extraer_iniciales
    1.2-definir_iniciales_nombre
    1.3-Imprimir nombres heroes    
    """)
    opcion = input("    Ingresar opcion >: ")
    return opcion
