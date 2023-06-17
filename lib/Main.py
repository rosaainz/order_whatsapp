from fuzzywuzzy import fuzz
import re

    
def calculate_total(message):
	catalog_map = {}
	message_map = {}


	with open('catalog.csv','r') as file:
		lines = file.readlines()
	
	#process catalog
	for line in lines[1:]:
		line = line.strip()
		price, product = line.split(",",1)
		catalog_map[product] = int(price)
	
	#process message
	print(message,"\n\n")
	result = re.sub(r'\n\s*\n', '\n', message)
	result = re.sub(r"^\s+|\s+$", "", result, flags=re.MULTILINE)
	message_process = re.findall(r"(\d+)\s*(.*)", result)

	total = 0
	result=0
	for tupla in message_process:
		item = tupla[0]
		product = tupla[1]

		matches = {}
		for product_catalog, price in catalog_map.items():
			result = fuzz.ratio(product_catalog.lower(), product.lower())
			matches[product_catalog] = result
		print(matches)
		maxi = max(matches.values())
		print(maxi)
		simi = [key for key, value in matches.items() if value == int(maxi)]
		print(simi)
		matches[str(simi[0])] = item
	print(matches)
			
	return matches







