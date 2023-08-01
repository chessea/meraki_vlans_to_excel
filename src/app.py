import os
from dotenv import load_dotenv
from meraki_api import get_all_networks, get_vlans_of_network
from excel_utils import create_vlan_table

# Cargar variables de entorno()
load_dotenv()

# Guardar variables
API_KEY = os.getenv("API_KEY")
ORGANIZATION_ID = os.getenv("ORGANIZATION_ID")


all_networks = get_all_networks(API_KEY, ORGANIZATION_ID)

if not all_networks:
    print("No se encontraron redes")
else:
    # Crear una lista de diccionarios para almacenar los datos de las redes y VLAN
    data = []

    # Iterar sobre todas las redes para obtener sus VLAN
    for network in all_networks:
        network_id = network["id"]
        network_name = network["name"]

        vlans = get_vlans_of_network(API_KEY, network_id)
        if vlans:
            for vlan in vlans:
                vlan_id = vlan["id"]
                vlan_name = vlan["name"]
                subnet = vlan["subnet"]

                # Agregar los datos a la lista de diccionarios
                data.append({
                    "Network Name": network_name,
                    "VLAN Name": f"vlan{vlan_id}_{vlan_name}",  # Modificar el nombre de la VLAN
                    "VLAN Subnet": subnet
                })
        else:
            print(f"No se encontraron VLAN para la red con ID {network_id}")

    pivot_table = create_vlan_table(data)

    # Guardar el DataFrame en un archivo Excel
    output_file = "meraki_data.xlsx"
    pivot_table.to_excel(output_file)
    print(f"Archivo {output_file} creado correctamente.")