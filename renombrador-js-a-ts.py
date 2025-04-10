import os

def rename_js_to_ts(directory):
    # Recorre todas las carpetas y archivos de manera recursiva
    for root, dirs, files in os.walk(directory):
        for file in files:
            # Si el archivo termina en .js
            if file.endswith('.js'):
                # Obtiene la ruta completa del archivo
                old_file = os.path.join(root, file)
                # Cambia la extensión de .js a .ts
                new_file = os.path.join(root, file[:-3] + '.ts')
                # Renombra el archivo
                os.rename(old_file, new_file)
                print(f'Renombrado: {old_file} -> {new_file}')

# Usar la función, pasando la ruta de la carpeta que deseas procesar
directory = "direccion_de_tu_catpeta"  # Cambia esta ruta por la ruta de tu carpeta
rename_js_to_ts(directory)
