import myers


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
	for line in message_line:
		quantity, product = line.split(" ",1)

		for product_catalog, price in catalog_map.items():
			difference = myers.diff(product, product_catalog)


	return 0

message = """
2 Berlinesas de Queso Mascarpone
2 Roles de Xoconostle
2 Croissants de Higo
2 Chocolatines
2 Rol de Almendra
4 Media Luna de Jamón y Queso
2 conchas vainilla ***
2 roles glaseados
"""
catalog_file = "catalog.csv"

total_order = calculate_total(message, catalog_file)
print(total_order)









