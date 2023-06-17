import myers
import re

    
def calculate_total(message):
	catalog_map = {}
	message_map = {}
	matches = {}


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
	for tupla in message_process:
		item = tupla[0]
		product = tupla[1]
		
		for product_catalog, price in catalog_map.items():
			result = myers.diff(product.lower(), product_catalog.lower())
			count = sum(1 for tuple in result if tuple[0] == 'k')
			
			
			if len(difference)/2 < count < len(difference):
				price = catalog_map[product_catalog]
				matches[product_catalog] = item
				print(matches)
				total_product = int(price) * int(item)
				print(int(price), "*", int(item), product_catalog)
				total += total_product
	return matches







