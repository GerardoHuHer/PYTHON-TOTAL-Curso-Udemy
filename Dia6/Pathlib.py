from pathlib import Path
carpeta = Path('C:\\Users\\huert\\OneDrive\\Escritorio\\alternativo\\pruebaalternativa.txt')

#.read_text() lee el archivo
#.name nos da el nombre del archivo
#.suffix nos da el tipo de archivo por ejemplo txt
#.stem nos da el nombre sin terminación

if not carpeta.exists():
    print('Este archivo no existe')
else:
    print('Genial sí existe')