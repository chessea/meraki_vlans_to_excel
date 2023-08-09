import os
import pandas as pd
from meraki_api import get_all_networks, get_device_of_networks
from dotenv import load_dotenv

# Cargar variables de entorno()
load_dotenv()
allowed_models = ["MR20", "MR33", "MR36"]
API_KEY = os.getenv("API_KEY")
ORGANIZATION_ID = os.getenv("ORGANIZATION_ID_JUNJI")



all_networks = get_all_networks(API_KEY, ORGANIZATION_ID)

data = []

for network in all_networks:
    tags = network["tags"]
    if "OFICINA" in tags:
        name = network['name']
        network_id = network['id']

        devices = get_device_of_networks(API_KEY, network_id)

        for device in devices:
            if device["model"] in allowed_models:
                ap_info = {
                    "Network": name,
                    "AP Name": device.get('name', 'N/A'),
                    "MAC Address": device.get('mac', 'N/A'),
                    "Serial Number": device.get('serial', 'N/A'),
                    "IP Address": device.get('lanIp', 'N/A'),
                    "Model": device.get('model', 'N/A')
                }
                data.append(ap_info)

# Crear un DataFrame de pandas
df = pd.DataFrame(data)

# Guardar el DataFrame en un archivo Excel
excel_filename = "ap_info.xlsx"
df.to_excel(excel_filename, index=False)

print(f"Los resultados se han guardado en {excel_filename}")





