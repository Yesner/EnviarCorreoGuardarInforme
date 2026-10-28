import pandas as pd #leer el archivo csv, manipular o transformacion la información

from pathlib import Path

#leer el archivo csv y vamos a guardar su contenido en una tabla
archivo="transacciones.csv" 


datos = pd.read_csv(archivo)

total_original = len(datos)

#Cantidad de registros
print(archivo, "Filas: ", total_original)

#Eliminar duplicados
datos = datos.drop_duplicates(subset="TransactionID").copy()

#usando la columna del monto de la transaccion, pasamos los valores a numeero, y los faltantes vamos a pasarlos a cero.
datos["TransactionAmount"] = pd.to_numeric(datos["TransactionAmount"], errors="coerce")

#
datos["LoginAttempts"] = pd.to_numeric(datos["LoginAttempts"], errors="coerce").fillna(0)

datos["TransactionDate"] = pd.to_datetime(datos["TransactionDate"], errors="coerce")

datos = datos.dropna(subset=["TransactionAmount","TransactionDate"]).copy()

datos = datos[datos["TransactionAmount"]>=0].copy()

datos["Mes"] = datos["TransactionDate"].dt.strftime("%Y-%m")

print(len(datos), "Filas descartadas", total_original-len(datos))



