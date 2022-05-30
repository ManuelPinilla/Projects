# -*- coding: utf-8 -*-
import exoplanetas as mod
import pandas as pd

def ejecutar_cargar_datos() -> pd.DataFrame:
    """
       Pide el nombre del archivo CSV que se quiere cargar y usa la funcion
       cargar_datos para construir el DataFrame.
       Retorno:
           Un DataFrame con los datos contenidos en el archivo.
    """
    nombre_archivo=input("Ingrese el nombre del archivo que desea cargar: ")
    datos=mod.cargar_datos(nombre_archivo)
    cantidad = len(datos)
    columnas = "\n - ".join(datos.columns)
    print(f"Un archivo con {cantidad} registros fue cargado.")
    print(f"Las columnas del conjunto de datos son: \n - {columnas}")
    return datos


def ejecutar_histograma_descubrimientos (datos:pd.DataFrame)->None:
    mod.histograma_descubrimiento(datos)


def ejecutar_estado_publicacion_por_descubrimiento(datos:pd.DataFrame)->None:
    mod.estado_publicacion_por_descubrimiento(datos)

def ejecutar_deteccion_por_descubrimiento(datos:pd.DataFrame)->None:
    mod.deteccion_por_descubrimiento(datos)

def ejecutar_deteccion_y_descubrimiento(datos:pd.DataFrame)->None:
    num = int(input("Ingrese el anho que quiere visualizar. Para visualizar todos los anhos ingrese 0: "))
    mod.deteccion_y_descubrimiento(datos,num)

def ejecutar_cantidad_y_tipo_deteccion(datos:pd.DataFrame)->None:
    mod.cantidad_y_tipo_deteccion(datos)

def ejecutar_masa_promedio_y_tipo_deteccion(datos:pd.DataFrame)->None:
    mod.masa_promedio_y_tipo_deteccion(datos)

def ejecutar_masa_planetas_vs_masa_estrellas(datos:pd.DataFrame)->None:
    mod.masa_planetas_vs_masa_estrellas(datos)

def ejecutar_graficar_cielo(datos:pd.DataFrame)->None:
    mod.graficar_cielo(datos)

def ejecutar_filtrar_imagen_cielo(datos:pd.DataFrame)->None:
    cielo = mod.graficar_cielo(datos)
    mod.filtrar_imagen_cielo(cielo)

def menu()->None:
    print("\n\nOPCIONES")
    print("0. Cargar datos")
    print("1. Numero de descubrimientos por anho (histograma)")
    print("2. Descubrimiento por estado de publicacion (boxplot)")
    print("3. Descubrimiento por tipo de deteccion (boxplot)")
    print("4. Tipo de deteccion por anho (pie)")
    print("5. Cantidad de descubrimientos por anho según el tipo de deteccion (lineas)")
    print("6. Masa promedio por anho y por tipo de deteccion (lineas)")
    print("7. Masa de los planetas vs. masa de la estrella mas cercana")
    print("8. Graficar cielo")
    print("9. Afinar la imagen del cielo")
    print("10. Salir")

def iniciar_aplicacion()->None:
    continuar=True
    while continuar:
        menu()
        elegido=int(input("Seleccione una opcion del menu: "))
        if elegido==0:
            datos=ejecutar_cargar_datos()
        elif elegido==1:
            ejecutar_histograma_descubrimientos(datos)
        elif elegido==2:
            ejecutar_estado_publicacion_por_descubrimiento(datos)
        elif elegido==3:
            ejecutar_deteccion_por_descubrimiento(datos)
        elif elegido==4:
            ejecutar_deteccion_y_descubrimiento(datos)
        elif elegido==5:
            ejecutar_cantidad_y_tipo_deteccion(datos)
        elif elegido==6:
            ejecutar_masa_promedio_y_tipo_deteccion(datos)
        elif elegido==7:
           ejecutar_masa_planetas_vs_masa_estrellas(datos)
        elif elegido==8:
            ejecutar_graficar_cielo(datos)
        elif elegido==9:
            ejecutar_filtrar_imagen_cielo(datos)
        elif elegido==10:
            continuar=False

        else:
            print("Seleccione una opcion del menu:")

iniciar_aplicacion()