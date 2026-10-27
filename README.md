<div align="center">

#  Monitor de Alertas Bancarias

### Análisis de transacciones, detección de alertas y reportes automáticos con Python

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Pandas-Análisis%20de%20datos-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![Microsoft Graph](https://img.shields.io/badge/Microsoft%20Graph-Correo-0078D4?style=for-the-badge&logo=microsoftoutlook&logoColor=white)](https://learn.microsoft.com/graph/overview)

**Una práctica de automatización bancaria: desde un archivo CSV hasta un reporte Excel enviado por correo.**

</div>

---

##  Descripción

Este proyecto procesa movimientos bancarios con **Python y pandas**, identifica operaciones que requieren revisión y genera un reporte en **Excel**. Como extensión, permite enviar las alertas por correo usando **Microsoft Graph**.

Las alertas se basan en reglas sencillas y **no constituyen una detección confirmada de fraude**.

##  Funcionalidades

- **Importación:** lectura de transacciones desde archivos CSV.
- **Depuración:** eliminación de duplicados y tratamiento de importes o fechas inválidos.
- **Análisis:** resúmenes por tipo de transacción, canal y mes.
- **Alertas:** selección de movimientos superiores a **US$5,000** o con **3 o más intentos de acceso**.
- **Reportes:** exportación de indicadores y resultados a un libro de Excel.
- **Notificaciones:** envío opcional del archivo de alertas mediante Microsoft Graph.

##  Tecnologías

| Tecnología | Uso |
| --- | --- |
| Python | Lógica y automatización |
| pandas | Lectura, limpieza y análisis de datos |
| openpyxl | Exportación de archivos Excel |
| Microsoft Graph | Envío de correos con OAuth 2.0 |
| MSAL y requests | Obtención de tokens y llamadas a la API |
| python-dotenv | Lectura de la configuración local |

##  Flujo de trabajo

```text
Dataset CSV
    ↓
Validación y limpieza
    ↓
Análisis de transacciones
    ↓
Reglas de alerta
    ↓
Reporte Excel ─────→ Envío por Microsoft Graph 
```

##  Instalación y ejecución

**1. Clona el repositorio y entra a su carpeta.**

```bash
git clone <URL_DEL_REPOSITORIO>
cd <NOMBRE_DEL_REPOSITORIO>
```

**2. Instala las dependencias.**

```bash
python -m pip install pandas openpyxl python-dotenv msal requests
```


**3. Prepara los datos.**

Descarga el [Bank Transaction Dataset for Fraud Detection](https://www.kaggle.com/datasets/valakhorasani/bank-transaction-dataset-for-fraud-detection) desde Kaggle y coloca `bank_transactions_data_2.csv` en la carpeta principal.

**4. Ejecuta el análisis.**

El script procesa las transacciones y genera los resultados. Si tienes habilitada la función de correo, también intentará enviar las alertas.

##  Configuración opcional del correo

Crea un archivo llamado `.env` en la raíz del proyecto:

```dotenv
GRAPH_CLIENT_ID=TU_ID_DE_APLICACION
GRAPH_TENANT_ID=TU_ID_DE_DIRECTORIO
GRAPH_CLIENT_SECRET=TU_SECRETO_DE_APLICACION
MAIL_USERNAME=cuenta-remitente@tu-organizacion.onmicrosoft.com
```

Para el envío por Microsoft Graph, la aplicación debe tener permisos de envío **autorizados por el administrador** y, preferiblemente, **restringidos al buzón remitente**. El permiso de aplicación `Mail.Send`, si se concede sin restricciones, puede permitir enviar desde otros buzones de la organización.

>  **Seguridad:** nunca subas `.env`, contraseñas, secretos, tokens, información bancaria real ni archivos de clientes al repositorio. Utiliza secretos del entorno cuando ejecutes el proyecto en GitHub Codespaces.

##  Resultado esperado

El análisis produce un libro Excel con estas hojas:

| Hoja | Contenido |
| --- | --- |
| `Resumen` | Indicadores generales del procesamiento |
| `Por tipo` | Cantidad e importe por tipo de transacción |
| `Por canal` | Actividad por canal bancario |
| `Por mes` | Totales mensuales |
| `Alertas` | Operaciones seleccionadas para revisión |
| `Transacciones` | Registros válidos procesados |

Las reglas y umbrales son **demostrativos** y pueden modificarse según el ejercicio.

##  Solución de problemas

| Mensaje | Qué revisar |
| --- | --- |
| `ModuleNotFoundError` | Instala las dependencias faltantes |
| `FileNotFoundError` | Comprueba el nombre y la ubicación del CSV |
| `403 ErrorAccessDenied` | Comprueba los permisos de Microsoft Graph y el buzón autorizado |
| Error de autenticación | Verifica los identificadores y el secreto de la aplicación, sin publicarlos |

##  Propósito

Proyecto de práctica para fortalecer habilidades en **automatización de procesos, análisis de datos, generación de reportes y consumo de APIs**.

---

<div align="center">

**Desarrollado con Python**

</div>
