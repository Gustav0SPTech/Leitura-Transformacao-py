# Biblioteca para capturar dados do pc
import psutil

# Biblioteca do csv
import csv

# Biblioteca para o timestamp
from datetime import datetime

# Biblioteca para o time sleep
import time


# Código que acha a pasta indicada e cria o arquivo csv
with open('./dados_ana.csv', 'w', newline='', encoding="utf-8") as csvfile:

    writer = csv.writer(csvfile)
    writer.writerow([f"USER;TIMESTAMP;CPU;RAM;DISCO"])


# For que captura os dados 10 vezes com intervalo de 10 segundos para cada leitura
for i in range(0, 10):

    # Coletando CPU
    cpu_p = psutil.cpu_percent(interval=2)

    # Coletando RAM
    ram = psutil.virtual_memory()
    ram_p = ram.percent

    # Coletando Disco
    disco = psutil.disk_usage('/')
    disk_p = disco.percent

    #Coletando data e hora
    date = datetime.now()
    data_hora = date.strftime("%Y-%m-%d %H:%M:%S")

    # Passando os parâmetros para a escrita no arquivo csv
    with open('./dados_ana.csv', 'a', encoding="utf-8") as csvfile:

        writer = csv.writer(csvfile)
        writer.writerow([f"ana;{data_hora};{cpu_p};{ram_p};{disk_p}"])