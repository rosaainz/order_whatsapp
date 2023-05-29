import myers


def calculate_total(message, catalog_file):
	prices = {}

	file = open(catalog_file).readlines()

	#separar precio y producto en un diccionario
	for line in file:
		line = line.strip()
		print(line)
		price, product = line.split(" ", 1)
		price = price.strip("$")
		prices[product] = int(price)

	#calcular total
	#procesar el mensaje del pedido
	lines_message = message.strip().split("\n")
	print(lines_message)

	print(myers.diff("ola", "hola"))
	total = 0
	for line in lines_message:
		print(line)
		quantity, product = line.split(" ",1)
		product = product.strip()

		if product in prices:
			catalog_price = prices[product]
			total_product = int(quantity) * catalog_price
			total += total_product

	return total

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
catalog_file = "catalog.txt"

total_order = calculate_total(message, catalog_file)
print(total_order)









