import requests
from pprint import pprint
import json
import time

response = requests.post(
    'https://sandboxdnac.cisco.com/dna/system/api/v1/auth/token',
    headers = {'Authorization':'Basic ZGV2bmV0dXNlcjpDaXNjbzEyMyE='})
payload = response.json()

value = payload.get('Token')

while True:
	response1 = requests.get(
		'https://sandboxdnac.cisco.com/dna/intent/api/v1/network-device',
		headers = {'X-Auth-Token' : value})
	payload1 = response1.json()

	A = payload1.get('response')
	JSONList = {}
	JSONList['Equipos'] = []
	for i in A:
		hostname = i.get('hostname')
		status = i.get('reachabilityStatus')
		JSONList['Equipos'].append({
			'hostname': hostname, 'reachabilityStatus': status})

	print(JSONList)
	with open('JSONList.json', 'w') as file:
		json.dump(JSONList, file)
	time.sleep(300)