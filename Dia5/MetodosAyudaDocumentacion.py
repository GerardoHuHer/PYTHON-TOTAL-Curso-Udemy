dic = {'c1':100, 'c2': 500  }
n = dic.popitem()
print(n)
print(dic)

text = ",:_#,,,,,,:::____##Pyt%on_ _Total,,,,,,::#"

n1 = text.lstrip(',:#_%')

print(n1)

#Ejercicio 2
lista = ['azul', 'verde', 'rojo']
lista.insert(3, 'naranja')


#Ejercio 3
marcas_smartphones = {"Samsung", "Xiaomi", "Apple", "Huawei", "LG"}
marcas_tv = {"Sony", "Philips", "Samsung", "LG"}

conjuntos_aislados = marcas_smartphones.isdisjoint(marcas_tv)
print(conjuntos_aislados)