import myers


def calculate_total(message, catalog_file):
	prices = {}

	with open(catalog_file) as file:
		lines = file.readlines()
	
	#procesar mensaje 
	for line in lines[1:]:
		line = line.strip()
		price, product = line.split(",",1)
		print(price)
		print(product)
		prices[product] = int(price)

	print(prices)
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









