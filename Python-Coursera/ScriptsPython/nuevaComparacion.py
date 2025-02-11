import os
import hashlib

def get_file_hash(file_path):
    """Genera un hash SHA-256 para un archivo."""
    hasher = hashlib.sha256()
    try:
        with open(file_path, 'rb') as f:
            while True:
                chunk = f.read(8192)
                if not chunk:
                    break
                hasher.update(chunk)
        print(f"Hash generado para {file_path}: {hasher.hexdigest()}")
        return hasher.hexdigest()
    except Exception as e:
        print(f"Error al calcular hash de {file_path}: {e}")
        return None

def get_files_with_hash(directory):
    """Obtiene un diccionario con los nombres de los archivos y sus hashes."""
    file_hashes = {}
    if not os.path.exists(directory):
        print(f"Error: La carpeta {directory} no existe.")
        return file_hashes
    
    print(f"Procesando archivos en {directory}")
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            file_hash = get_file_hash(file_path)
            if file_hash:
                file_hashes.setdefault(file_hash, []).append(file_path)
    return file_hashes

def compare_subfolder_with_others(main_directory, subfolder):
    """Compara los archivos de una subcarpeta con el resto de las subcarpetas dentro del directorio principal."""
    if not os.path.exists(main_directory) or not os.path.exists(subfolder):
        print("Error: Una de las rutas no existe.")
        return
    
    print(f"Comparando archivos en {subfolder} con otras subcarpetas dentro de {main_directory}")
    subfolder_files = get_files_with_hash(subfolder)
    all_other_files = {}
    
    for root, dirs, _ in os.walk(main_directory):
        for dir_name in dirs:
            dir_path = os.path.join(root, dir_name)
            if os.path.abspath(dir_path) != os.path.abspath(subfolder):
                print(f"Procesando subcarpeta {dir_path}")
                other_files = get_files_with_hash(dir_path)
                for hash_, paths in other_files.items():
                    all_other_files.setdefault(hash_, []).extend(paths)
    
    matches = {hash_: paths for hash_, paths in subfolder_files.items() if hash_ in all_other_files}
    
    if matches:
        print(f"Archivos en {subfolder} que tienen coincidencias en otras subcarpetas:")
        for hash_, paths in matches.items():
            print(f"Archivo en {subfolder}: {paths}")
            print(f"Coincidencias en otras carpetas: {all_other_files[hash_]}")
    else:
        print("No se encontraron coincidencias.")

# Uso del script
if __name__ == "__main__":
    main_directory = r"M:/AUDITORIA MITES/Evidencias Auditoría Interna 2024/Brais Arias"
    subfolder = r"M:/AUDITORIA MITES/Evidencias Auditoría Interna 2024/Brais Arias/20250211"
    compare_subfolder_with_others(main_directory, subfolder)
