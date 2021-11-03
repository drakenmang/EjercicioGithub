import requests
import json
import pprint


response = requests.get(
    'https://api.github.com/search/repositories',
    params={'q': 'requests+language:python'},
    headers={'Accept': 'application/vnd.github.v3.text-match+json'},
)


token="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"

User=input("Introduce el nombre del usuario del cual quieras ver su repositorio: ")
url="https://api.github.com/users/{}/repos".format(User)

data = {"type" : "all" , "sort" : "full_name" , "direction" : "asc"}

output = requests.get(url,data=json.dumps(data))
output = json.loads(output.text)

for i in output:
	print(i["full_name"])

Q=input("quieres saber las líneas de código de cada fichero? contesta si o no. ")

if Q == "si":
    for i in output:   
        pprint.pprint( i["size"])
if Q != "si":
    pass


'''
SECCION EN CONSTRUCCIÓN.
W=input("quieres saber las extensiones de cada fichero? contesta si o no. ")

if W == "si":
    for i in output:   
        pprint.pprint( i["message"])
if W != "si":
    pass
'''

Rep=input("Introduce el nombre del repositorio del cual quieras ver sus commits: ")

url="https://api.github.com/repos/{}/{}/commits".format(User, Rep)



data = {"type" : "all" , "sort" : "full_name" , "direction" : "asc"}

output = requests.get(url,data=json.dumps(data))
output = json.loads(output.text)

for item in output:
    pprint.pprint("Autor del commit: " + item["commit"]["author"]["name"])
    print(" ")
    pprint.pprint("mensaje :" + item["commit"]["message"])
    print(" ")



