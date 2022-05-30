from matplotlib import image
import pandas as pd
import matplotlib.pyplot as plt
import math as m
import numpy as np
from pandas.core import groupby

plt.rcParams.update({'font.size': 12})

def cargar_datos(nombre_archivo:str)->pd.DataFrame:
    """ Carga los datos de un archivo csv y retorna el DataFrame con la informacion.
    Parametros:
        nombre_archivo (str): El nombre del archivo CSV que se debe cargar
    Retorno:
        (DataFrame) : El DataFrame con todos los datos contenidos en el archivo
    """
    carga_de_datos = pd.read_csv(nombre_archivo)

    return carga_de_datos


def histograma_descubrimiento(datos:pd.DataFrame)->None:
    """ Calcula y despliega un histograma con 30 grupos (bins) en el que debe
        aparecer la cantidad de planetas descubiertos por anho.
    Parametros:
        datos (DataFrame): el DataFrame con la informacion de los exoplanetas
    """
    descubrimientos = datos['DESCUBRIMIENTO']

    descubrimientos.plot(kind="hist",bins=30)
   
    plt.xlabel("Años")
    plt.ylabel("Cantidad de planetas descubiertos")
    plt.title("Cantidad de planetas decubiertos entre 1988 y 2018")
    plt.show()

    

def estado_publicacion_por_descubrimiento(datos:pd.DataFrame)->None:
    """ Calcula y despliega un BoxPlot donde aparecen la cantidad de planetas
        descubiertos por anho, agrupados de acuerdo con el tipo de publicacion.
    Parametros:
        datos (DataFrame): el DataFrame con la informacion de los exoplanetas
    """
    
    datos[['DESCUBRIMIENTO','ESTADO_PUBLICACION']].boxplot(by='ESTADO_PUBLICACION',rot=90, figsize=(8,10), fontsize= 10,color='blue')
    plt.ylabel("Años de publicación")
    plt.show()
   # datos[['ESTADO_PUBLICACION','DESCUBRIMIENTO']].boxplot()

    
    

def deteccion_por_descubrimiento(datos:pd.DataFrame)->None:
    """ Calcula y despliega un BoxPlot donde aparecen la cantidad de planetas
        descubiertos por anho, agrupados de acuerdo con el tipo de deteccion
    Parametros:
        datos (DataFrame): el DataFrame con la informacion de los exoplanetas
    """
    datos[['DESCUBRIMIENTO','TIPO_DETECCION']].boxplot(by='TIPO_DETECCION',rot=90, figsize=(8,10), fontsize= 10,color='blue')
    plt.ylabel("Años de publicación")
    plt.show()

def deteccion_y_descubrimiento(datos:pd.DataFrame,anho:int)->None:
    """ Calcula y despliega un diagrama de pie donde aparecen la cantidad de
        planetas descubiertos en un anho particular, clasificados de acuerdo
        con el tipo de publicacion.
        Si el anho es 0, se muestra la información para todos los planetas.
    Parametros:
        datos (DataFrame): el DataFrame con la informacion de los exoplanetas
        anho (int): el anho para el que se quieren analizar los planetas descubiertos
                    o 0 para indicar que deben ser todos los planetas.
    """
    #campos = datos['TIPO_DETECCION'].unique()
    if anho == 0:
       datos['TIPO_DETECCION'].value_counts().plot(kind='pie',autopct='%.2f')
    else:
       filtro= datos[datos['DESCUBRIMIENTO']==anho]
       filtro['TIPO_DETECCION'].value_counts().plot(kind='pie',autopct='%.2f')
    #datos[['DESCUBRIMIENTO','TIPO_DETECCION']].plot(kind='pie')
    
    plt.show()
def cantidad_y_tipo_deteccion(datos:pd.DataFrame)->None:
    """ Calcula y despliega un diagrama de lineas donde aparece una linea por
        cada tipo de deteccion y se muestra la cantidad de planetas descubiertos
        en cada anho, para ese tipo de deteccion.
    Parametros:
        datos (DataFrame): el DataFrame con la informacion de los exoplanetas
    """
    valores_columnas =['TIPO_DETECCION','DESCUBRIMIENTO','ESTADO_PUBLICACION']
    copia = datos[valores_columnas].copy()
    ordenados = copia.groupby(by=['TIPO_DETECCION','DESCUBRIMIENTO']).size().reset_index(name='veces')
    
    
    indices =copia['DESCUBRIMIENTO'].unique()
    indices_ordenados= sorted(indices)
    df = pd.DataFrame(index=indices_ordenados, columns=datos['TIPO_DETECCION'].unique())
    #diccionario = {      indices :}
    print(ordenados)
    columnas = list(df.columns)
    for i in df.index:
        for k in ordenados.index:
          for m in columnas : 
             if (i == ordenados["DESCUBRIMIENTO"][k]) & (m== ordenados['TIPO_DETECCION'][k]) :    
                df[m][i] = ordenados['veces'][k]
    
    df.plot(kind="line")
    plt.ylabel("Cantidad de planetas")
    plt.xlabel("Años de descubrimiento")
    plt.show()
   
     
  
         

    
    
    #for i in anhos:# para cada años filtre por año y cuente segun el tipo de
      
     #   filtro=datos[datos["DESCUBRIMIENTO"]==i]
      #  print(filtro)
      
        #print(filtro['TIPO_DETECCION'].value_counts(),i)
     

   
def masa_promedio_y_tipo_deteccion(datos:pd.DataFrame)->None:
    """ Calcula y despliega un diagrama de lineas donde aparece una linea por
        cada tipo de detección y se muestra la masa promedio de los planetas descubiertos
        en cada anho, para ese tipo de deteccion.
    Parametros:
        datos (DataFrame): el DataFrame con la informacion de los exoplanetas
    """
    valores_columnas =['TIPO_DETECCION','DESCUBRIMIENTO','MASA']
    copia = datos[valores_columnas].copy()
    ordenados = copia.groupby(by=['TIPO_DETECCION','DESCUBRIMIENTO'])['MASA'].mean().reset_index(name="PROMEDIO")
    print(ordenados)
    indices =copia['DESCUBRIMIENTO'].unique()
    indices_ordenados= sorted(indices)
    df = pd.DataFrame(index=indices_ordenados, columns=datos['TIPO_DETECCION'].unique())
    print(df)
    columnas = list(df.columns)
    for i in df.index:
        for k in ordenados.index:
          for m in columnas : 
             if (i == ordenados["DESCUBRIMIENTO"][k]) & (m== ordenados['TIPO_DETECCION'][k]) :    
                df[m][i] = ordenados['PROMEDIO'][k]
    print(df)    
    df.plot(kind="line")
    plt.ylabel("Masa Promedio")
    plt.xlabel("Años de descubrimiento")
    plt.show()
   

def masa_planetas_vs_masa_estrellas(datos: pd.DataFrame)->None:
    """ Calcula y despliega un diagrama de dispersión donde en el eje x se
        encuentra la masa de los planetas y en el eje y se encuentra el logaritmo
        de la masa de las estrellas. Cada punto en el diagrama correspondera
        a un planeta y estara ubicado de acuerdo con su masa y la masa de la
        estrella más cercana.
    Parametros:
        datos (DataFrame): el DataFrame con la informacion de los exoplanetas
    """
    valores_columnas =['MASA_ESTRELLA','MASA']
    copia = datos[valores_columnas].copy()
    copia.plot(kind="scatter", x=['MASA'], y=['MASA_ESTRELLA'])
    plt.yscale("log")
    plt.show()
    


def graficar_cielo(datos:pd.DataFrame)->list:
    """ Calcula y despliega una imagen donde aparece un pixel por cada planeta,
        usando colores diferentes que dependen del tipo de detección utilizado
        para descubirlo.
    Parametros:
        datos (DataFrame): el DataFrame con la informacion de los exoplanetas
    Retorno:
        Una matriz de pixeles con la representacion del cielo
    """
    matriz = []
    i = 0
    while i < 100: # alto
        fila = []
        for j in range(200): # ancho
            R = 0
            G = 0
            B = 0
            fila.append((R,G,B))
        matriz.append(fila) 
        i += 1

        
    for i in range(len(datos["NOMBRE"].unique())):
        
        ra = datos.loc[i]["RA"]
        dec = datos.loc[i]["DEC"]
        
        fila = int(99-abs(m.sin(ra) * m.cos(dec) * 100))
        columna = int(m.cos(ra) * m.cos(dec) * 100) + 100
        
        if datos.loc[i]["TIPO_DETECCION"] == "Microlensing":
            pixel = (0.94, 0.10, 0.10)
        elif datos.loc[i]["TIPO_DETECCION"] == "Radial Velocity":
            pixel = (0.1, 0.5, 0.94)
        elif datos.loc[i]["TIPO_DETECCION"] == "Imaging":
            pixel = (0.34, 0.94, 0.10)
        elif datos.loc[i]["TIPO_DETECCION"] == "Primary Transit":
            pixel = (0.10, 0.94, 0.85)
        elif datos.loc[i]["TIPO_DETECCION"] == "Other":
            pixel = (0.94, 0.10, 0.85)
        elif datos.loc[i]["TIPO_DETECCION"] == "Astrometry":
            pixel = (0.94, 0.65, 0.10)
        elif datos.loc[i]["TIPO_DETECCION"] == "TTV":
            pixel = (1.0, 1.0, 1.0)
            
        matriz[fila][columna] = pixel 
        
    plt.imshow(matriz)
    plt.show()
    return matriz



def filtrar_imagen_cielo(imagen:list)->None:
    """ Le aplica a la imagen un filtro de convolucion basado en la matriz
        [[-1,-1,-1],[-1,9,-1],[-1,-1,-1]]
    Parametros:
        imagen (list): una matriz con la imagen del cielo
    """
    mascara = [[-1, -1, -1],[-1, 9, -1], [-1, -1, -1]]
   
    # Crear una copia de la imagen que finalmente será retornada
    copia_img = imagen.copy()
    filas = len(imagen)
    columnas = len(imagen[0])
   
    # Recorrer las filas (i) y las columnas (j) de la imagen original
    # No se recorren las filas y columnas que se encuentran en el borde de 
    # la imagen porque no tienen vecinos completos para aplicar la máscara
    for i in range(1, filas-1):
      for j in range(1, columnas-1):
     
        # A partir de este punto se va a aplicar la máscara al pixel que
        # se encuentra en la fila i, columnas j.
        # La máscara es de 3x3: se hacen dos ciclos para recorrer todos sus elementos.
        rojo, verde, azul = (0,0,0)           
        for i_mascara in range(-1, 2):
          for j_mascara in range(-1, 2):
            # Se consultan los colores originales del pixel vecino
            rojo_vecino, verde_vecino, azul_vecino = imagen[i + i_mascara][j + j_mascara]
            valor_mascara = mascara[i_mascara + 1][j_mascara + 1]
           
            # Los colores originales se multiplican por el valor de la máscara
            # y se van sumando para encontrar el nuevo valor del color para
            # el pixel [i][j]
            rojo += rojo_vecino * valor_mascara
            verde += verde_vecino * valor_mascara
            azul += azul_vecino * valor_mascara
          
        nuevo_pixel = (max(rojo, 0.0), max(verde, 0.0), max(azul, 0.0))   
        copia_img[i][j] = nuevo_pixel    
    
    plt.imshow(copia_img)
    plt.show()




