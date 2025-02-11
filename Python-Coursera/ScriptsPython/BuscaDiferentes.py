import os
import hashlib
import subprocess
import sys

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

def find_unique_files(directory):
    """Encuentra archivos únicos dentro de una carpeta y sus subcarpetas."""
    files = get_files_with_hash(directory)
    unique_files = {hash_: paths[0] for hash_, paths in files.items() if len(paths) == 1}
    
    print("Archivos únicos en", directory)
    for path in unique_files.values():
        print(path)

# Uso del script
directory = r"M:\AUDITORIA MITES\Evidencias Auditoría Interna 2024\Brais Arias"
find_unique_files(directory)
