import myers
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
	print(message)
	result = re.sub(r'\n\s*\n', '\n', message)
	result = re.sub(r"^\s+|\s+$", "", result, flags=re.MULTILINE)
	message_process = re.findall(r"(\d+)\s*(.*)", result)

	total = 0
	for tupla in message_process:
		quantity = tupla[0]
		product = tupla[1]
		
		for product_catalog, price in catalog_map.items():
			difference = myers.diff(product, product_catalog)
			acum = 0
			for result in difference:
				if result[0] == 'k':
					acum += 1
			
			if len(difference)/2 < acum < len(difference):
				price = catalog_map[product_catalog]
				total_product = int(price) * int(quantity)
				total += total_product
				cotizacion = total
	return cotizacion









