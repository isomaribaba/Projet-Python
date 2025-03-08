import os
import requests
import scapy



print(f"Vous etez dans le répertoire {os.getcwd()}")
print(os.listdir())
requet = requests.get('https://gsimel.com/')
print(requet.content)