import os
from dotenv import load_dotenv
import pandas as pd
from meraki_api import get_all_networks, get_vlans_dns_networks

# Cargar variables de entorno
load_dotenv()

API_KEY = os.getenv("API_KEY")
ORGANIZATION_ID = os.getenv("ORGANIZATION_ID_AIEP")
NETWORK_ID = os.getenv("NETWORK_ID")

all_networks = get_all_networks(API_KEY, ORGANIZATION_ID)

# Crear listas para almacenar los datos
sede_list = []
red_colaboradores_list = []
dns_primario_list = []
dns_secundario_list = []

for networks in all_networks:
    id_network = networks.get("id")
    name_organization = networks.get("name")
    vlans = get_vlans_dns_networks(API_KEY, id_network)
    try:
        for vl in vlans:
            if vl["id"] == 45:
                vlan_colaboradores = vl["applianceIp"]
                dns = vl["dnsNameservers"].split("\n")  # Dividir DNS en una lista
                if len(dns) >= 2:
                    dns_primario = dns[0]
                    dns_secundario = dns[1]
                else:
                    dns_primario = dns[0]
                    dns_secundario = ""  # Si no hay DNS secundario
                # Agregar los datos a las listas
                sede_list.append(name_organization)
                red_colaboradores_list.append(vlan_colaboradores)
                dns_primario_list.append(dns_primario)
                dns_secundario_list.append(dns_secundario)
    except Exception as e:
        pass

# Crear un DataFrame de Pandas
data = {
    "sede": sede_list,
    "red_colaboradores": red_colaboradores_list,
    "dns_primario": dns_primario_list,
    "dns_secundario": dns_secundario_list
}

df = pd.DataFrame(data)

# Guardar el DataFrame en un archivo Excels
df.to_excel("datos_redes.xlsx", index=False)
print("Fin del programa")