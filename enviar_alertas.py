
import os
import base64
from io import BytesIO
import msal
import requests
from dotenv import load_dotenv

load_dotenv()

def enviar_alertas(alertas, destinatario):
    # Autenticación con Microsoft
    app = msal.ConfidentialClientApplication(
        os.getenv("GRAPH_CLIENT_ID"),
        authority="https://login.microsoftonline.com/" + os.getenv("GRAPH_TENANT_ID"),
        client_credential=os.getenv("GRAPH_CLIENT_SECRET")
    )

    token = app.acquire_token_for_client(
        scopes=["https://graph.microsoft.com/.default"]
    )

    if "access_token" not in token:
        print("Error de autenticación:", token.get("error_description"))
        return False

    # Crear Excel de alertas en memoria
    archivo = BytesIO()
    alertas.to_excel(archivo, index=False)

    # Preparar el correo
    mensaje = {
        "message": {
            "subject": "Reporte de alertas bancarias",
            "body": {
                "contentType": "Text",
                "content": "Se adjunta el reporte de alertas bancarias."
            },
            "toRecipients": [
                {"emailAddress": {"address": destinatario}}
            ],
            "attachments": [{
                "@odata.type": "#microsoft.graph.fileAttachment",
                "name": "alertas_bancarias.xlsx",
                "contentType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                "contentBytes": base64.b64encode(archivo.getvalue()).decode()
            }]
        }
    }

    # Enviar utilizando Microsoft Graph
    url = (
        "https://graph.microsoft.com/v1.0/users/"
        + os.getenv("MAIL_USERNAME") + "/sendMail"
    )

    respuesta = requests.post(
        url,
        headers={"Authorization": "Bearer " + token["access_token"]},
        json=mensaje,
        timeout=30
    )

    if respuesta.status_code == 202:
        print("Microsoft aceptó la solicitud de envío.")
        return True

    print("Error:", respuesta.status_code, respuesta.text)
    return False
