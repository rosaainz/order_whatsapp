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
	#message_line = message.strip().split("\n")
	#message_line.sort()
	total = 0
	print(message)
	for tupla in message:
		print(tupla)
		quantity = tupla[0]
		product = tupla[1]

		print(quantity)
		print(product)
		
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
- 1 concha de vainilla **
"""
catalog_file = "catalog.csv"

# Eliminar guiones y asteriscos
result = re.sub(r"[[^...]]+", "", message)

# Eliminar espacios
result = re.sub(r"^\s+|\s+$", "", result, flags=re.MULTILINE)

# Extraer el número y el texto
result = re.findall(r"(\d+)\s*(.*)", result)

print(type(result))
print(result)
total_order = calculate_total(result, catalog_file)
print(total_order)









