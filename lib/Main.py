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
	result = re.sub(r"[[^...]]+", "", message)
	result = re.sub(r'\n\s*\n', '\n', result)
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
				print(price ,"*",quantity, product_catalog )
				total_product = int(price) * int(quantity)
				total += total_product
	return total

message = """
Buenos días, te doy mi pedido 😬😬😬
2 Berlinesas
2 roles de xoconostle 
2 chocolatines
1 rol de almendras 
4 medias luna 
3 roles glaseados
1 concha de vainilla **
"""
#catalog_file = "../catalog.csv"

#total_order = calculate_total(message, catalog_file)
#print("Total: ",total_order)









