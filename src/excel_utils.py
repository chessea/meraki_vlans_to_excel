import pandas as pd


#Crear tabla con vlan_id y Nombre de la vlan
def create_vlan_table(data):
    df = pd.DataFrame(data)

    pivot_table = df.pivot_table(index="Network Name", columns="VLAN Name", values="VLAN Subnet", aggfunc="first")
    return pivot_table