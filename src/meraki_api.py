import requests


# Obtener las netwoks
def get_all_networks(api_key, org_id):
    url = f"https://api.meraki.com/api/v1/organizations/{org_id}/networks"
    headers = {
        "Accept": "application/json",
        "X-Cisco-Meraki-API-Key": api_key
    }
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error en la solicitud de redes: Código de estado {response.status_code}")
        return None


# Obtener vlan 
def get_vlans_of_network(api_key, network_id):
    url = f"https://api.meraki.com/api/v1/networks/{network_id}/appliance/vlans"
    headers = {
        "Accept": "application/json",
        "X-Cisco-Meraki-API-Key": api_key
    }
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error en la solicitud de VLAN: Código de estado {response.status_code}")
        return None