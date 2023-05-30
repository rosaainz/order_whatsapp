import myers
import re


def calculate_total(message, catalog_file):
	catalog_map = {}
	message_map = {}


	with open(catalog_file) as file:
		lines = file.readlines()
	
	#process catalog
	for line in lines[1:]:
		line = line.strip()
		price, product = line.split(",",1)
		catalog_map[product] = int(price)
	
	#process message
	message_line = message.strip().split("\n")
	message_line.sort()
	total = 0
	for line in message_line:
		quantity, product = line.split(" ",1)
		
		for product_catalog, price in catalog_map.items():
			difference = myers.diff(product, product_catalog)
			acum = 0
			for result in difference:
				if result[0] == 'k':
					acum += 1
			
			if len(difference)/2 < acum < len(difference):
				print(product)
				print(product_catalog)
				price = catalog_map[product_catalog]
				total_product = int(price) * int(quantity)
				total += total_product
	return total

message = """
- 4 roles de canela 
- 4 chocolatines 
- 2 roles de Almendra 
- 2 conchas de vainilla **
"""
catalog_file = "catalog.csv"

result = re.sub(r'[-*]','',message)
print(result.strip())
print(type(result))
total_order = calculate_total(result, catalog_file)
print(total_order)









