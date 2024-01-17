import os

ruta = "C:\\Users\\huert\\OneDrive\\Escritorio\\CarpetaPrueba"
for carpeta, subcarpeta, archivo in os.walk(ruta):
    print(f"En la carpeta: {carpeta}")
    print(f"Las subcarpetas son: ")
    for sub in subcarpeta:
        print(f"\t{sub}")
    print("Los archivos son:")
    for arch in archivo:
        print(f"\t{arch}")
    print("\n")

