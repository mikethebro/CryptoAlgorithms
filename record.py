#!/usr/bin/python
import requests
from datetime import datetime
class currency:
	def __init__ (self, name, symbol):
		self.name = name
		self.symbol = symbol

def get_json():
    r = requests.get('https://api.coinmarketcap.com/v1/ticker/?limit=20')
    return r.json()

def print_to_file(json):
    file_data = open("data.txt", "a")
    file_data.write(json["time"]["updated"])
    file_data.write("   ")
    file_data.write(get_current_bitcoin_price(json))
    file_data.write("\n")


json = get_json()
for each in json:
	string = "/home/michael/src/CryptoAlgorithms/"
	append = ".txt"
	file_name = each['id']
	total = string+file_name+append
	file_data = open(total, "w+")
