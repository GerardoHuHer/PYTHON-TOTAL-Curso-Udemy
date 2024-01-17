import re

texto = "No atendemos los lunes por la tarde"

buscar = re.search(r'^\D', texto)
print(buscar)