import os
import hashlib

def get_file_hash(file_path):
    """Genera un hash SHA-256 para un archivo."""
    hasher = hashlib.sha256()
    try:
        with open(file_path, 'rb') as f:
            while chunk := f.read(8192):
                hasher.update(chunk)
        return hasher.hexdigest()
    except Exception as e:
        print(f"Error al calcular hash de {file_path}: {e}")
        return None

def get_files_with_hash(directory):
    """Obtiene un diccionario con los nombres de los archivos y sus hashes."""
    file_hashes = {}
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            file_hash = get_file_hash(file_path)
            if file_hash:
                if file_hash in file_hashes:
                    file_hashes[file_hash].append(file_path)
                else:
                    file_hashes[file_hash] = [file_path]
    return file_hashes

def compare_subfolder_with_others(main_directory, subfolder):
    """Compara los archivos de una subcarpeta con el resto de las subcarpetas dentro del directorio principal."""
    subfolder_path = os.path.join(main_directory, subfolder)
    subfolder_files = get_files_with_hash(subfolder_path)
    
    all_other_files = {}
    for root, dirs, _ in os.walk(main_directory):
        for dir_name in dirs:
            dir_path = os.path.join(root, dir_name)
            if dir_path != subfolder_path:
                other_files = get_files_with_hash(dir_path)
                all_other_files.update(other_files)
    
    matches = {hash_: paths for hash_, paths in subfolder_files.items() if hash_ in all_other_files}
    
    print(f"Archivos en {subfolder} que tienen coincidencias en otras subcarpetas:")
    for hash_, paths in matches.items():
        print(f"Archivo en {subfolder}: {paths}")
        print(f"Coincidencias en otras carpetas: {all_other_files[hash_]}")

# Uso del script
main_directory = "M:/AUDITORIA MITES/Evidencias Auditoría Interna 2024/Brais Arias"
subfolder = "M:/AUDITORIA MITES/Evidencias Auditoría Interna 2024/Brais Arias/20250211"
compare_subfolder_with_others(main_directory, subfolder)