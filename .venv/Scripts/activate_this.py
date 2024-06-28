
import pywhatkit as kit
import pandas as readMyCSV
import datetime

df = readMyCSV.read_csv('mi_csv.csv')


for index, row in df.iterrows():

    codigo_pais = ('+504'
                   '')
    numero_destino = str(codigo_pais) + str(row['Telefono'])
    mensaje = row['Mensaje']

    hora_actual = datetime.datetime.now().hour
    minuto_actual = datetime.datetime.now().minute + 5

    # Ajustar la hora y el minuto si es necesario
    if minuto_actual >= 60:
        hora_actual += 1
        minuto_actual %= 60

    kit.sendwhatmsg(numero_destino, mensaje, hora_actual, minuto_actual)
