
import csv
import os
# Importamos los modulos csv y os

def leer_csv(ruta):
  """
  Abre y lee el csv de la ruta y crea una
  lista con diccionarios
  """
  datos = []
  with open(ruta, "r") as archivo:
    lector = csv.DictReader(archivo)
    for fila in lector:
      datos.append(fila)
  return datos

def calcular_promedio(datos, columna):
  """
  Recibe la lista de datos y la columna de
  temperatura. Se agregan a la lista valores
  los datos numericos y se calcula el promedio
  de los mismos
  """
  valores = []
  for fila in datos:
    try:
      valores.append(float(fila[columna]))
    except ValueError:
      pass
  if len(valores) == 0:
    return None
  return sum(valores) / len(valores)

def calcular_max_min(datos, columna):
  """
  Devuelve el valor maximo y minimo de
  los datos
  """
  valores = []
  for fila in datos:
    try:
      valores.append(float(fila[columna]))
    except ValueError:
      pass
  if len(valores) == 0:
    return None, None
  return max(valores), min(valores)

def guardar_resultados(ruta_salida, contenido):
  """
  Escribe los resultados en un archivo
  en la carpeta resultados
  """
  with open(ruta_salida, "w") as archivo:
    archivo.write(contenido)
  print(f"Resultados guardados en: {ruta_salida}.")

RUTA_DATOS = "datos/annual.csv"
RUTA_RESULTADO = "resultados/resumen_analisis.txt"

if not os.path.exists(RUTA_DATOS):
  print(f"No se encontro el archivo de datos en {RUTA_DATOS}")
else:
  datos = leer_csv(RUTA_DATOS)
  print(f"Registros cargados: {len(datos)}")

  columna_temperatura = "Mean"

  promedio = calcular_promedio(datos, columna_temperatura)
  maximo, minimo = calcular_max_min(datos, columna_temperatura)

  print(f"Temperatura promedio: {promedio:.2f}")
  print(f"Temperatura maxima: {maximo:.2f}")
  print(f"Temperatura minima: {minimo:.2f}")

  contenido = (
              "RESUMEN ANÁLISIS CLIMÁTICO\n"
        "==========================\n"
        f"Total de registros analizados : {len(datos)}\n"
        f"Temperatura promedio          : {promedio:.2f}\n"
        f"Temperatura máxima            : {maximo:.2f}\n"
        f"Temperatura mínima            : {minimo:.2f}\n"
        )
  
  guardar_resultados(RUTA_RESULTADO, contenido)
