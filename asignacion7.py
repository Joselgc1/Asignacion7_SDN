import request
from pprint import pprint
import json
from tabulate import tabulate

response = requests.post(
    'https://
    headers = {'Authorization':'Basic ZGV2bmV0dXNlcjpDaXNjbzEyMyE='})
payload = response.json()
pprint(payload)

response.raise_for_status()

value = payload.get('Token')

response1 = requests.get(
	'https://sandboxdnac.cisco.com/dna/intent/api/v1/network-device',
	headers = {'X-Auth-Token' : value})
payload1 = response1.json()
pprint(payload1)

A = payload1.get('response')
Equipos = []
for i in A:
	Equipo = []
	family = i.get('family')
	Equipo.append(family)
	hostname = i.get('hostname')
	Equipo.append(hostname)
	ip_address = i.get('managementIpAddress')
	Equipo.append(ip_address)
	update_date = i.get('lastUpdated')
	Equipo.append(update_date)
	status = i.get('reachabilityStatus')
	Equipo.append(status)
	Equipos.append(Equipo)
print(Equipos)
print('')
print(tabulate(Equipos, headers = 
	['Tipo de Equipo','Nombre del Host','IP del Administrador',
	'Ultima Actualizacion','Estatus del Equipo']))
