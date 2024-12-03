#importações
import requests

#obtenção das informações da url
url1 = requests.get('https://reqres.in/api/users?page=1').json()
url2 = requests.get('https://reqres.in/api/users?page=2').json()

#triagem de informações da página
url1 = url1["data"]
url2 = url2["data"]