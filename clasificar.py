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



#Contar y sumar los importes segun debito y credito

por_tipo = datos.groupby("TransactionType")["TransactionAmount"].agg(["count", "sum"]).reset_index()

por_tipo.columns = ["Tipo", "Cantidad", "Monto total"]

por_canal = datos.groupby("Channel")["TransactionAmount"].agg(["count", "sum"]).reset_index()

por_canal.columns = ["Canal", "Cantidad", "Monto total"]

por_mes = datos.groupby("Mes")["TransactionAmount"].sum().reset_index()

por_mes.columns = ["Mes", "Monto total"]

#### selección de movimientos superiores a US$5,000 o con 3 o más intentos de acceso.

monto_alto = datos["TransactionAmount"]>5000

muchos_intentos = datos["LoginAttempts"]>=3

alertas = datos[monto_alto | muchos_intentos].copy()

alertas["Motivo"] = "Monto mayor a 5000"

alertas.loc[alertas["LoginAttempts"] >=3, "Motivo"] = "Tres o mas intentos de acceso"

print("Alertas por avisar: ", len(alertas))

### Reportes: exportación de indicadores y resultados a un libro de Excel.

resumen = pd.DataFrame({"Indicador": ["Filas originales", "Transacciones validas", "Filas descartadas", "Monto total procesado", "Monto promedio", "Operaciones por revisar"],
                        "Valor": [total_original, len(datos), total_original-len(datos), datos["TransactionAmount"].sum(), round(datos["TransactionAmount"].mean(),2), len(alertas)]})

with pd.ExcelWriter("reporte_bancario.xlsx", engine="openpyxl") as excel:
    #Indicadores principales
    resumen.to_excel(excel, sheet_name="Resumen", index=False)
    #Hoja de totales por tipo de movimiento
    por_tipo.to_excel(excel, sheet_name="Por tipo", index=False)
    #Hoja de totales por canal
    por_canal.to_excel(excel, sheet_name="Por canal", index=False)
    #Hoja de totales por mes
    por_mes.to_excel(excel, sheet_name="Por mes", index=False)
    #Hoja de alertas
    alertas.to_excel(excel, sheet_name="Alertas", index=False)
    #Datos limpios
    datos.to_excel(excel, sheet_name="Transacciones", index=False)

print("Reporte de excel creado")