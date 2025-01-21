import os
import pandas as pd

def get_directory_structure(root_dir):
    directory_structure = []

    for dirpath, dirnames, _ in os.walk(root_dir):
        level = dirpath.replace(root_dir, '').count(os.sep)
        indent = ' ' * 4 * level
        directory_structure.append({
            "Path": f"{indent}{os.path.basename(dirpath)}",
            "Type": "Folder"
        })

    return directory_structure

def export_to_excel(directory_structure, output_file):
    df = pd.DataFrame(directory_structure)
    with pd.ExcelWriter(output_file, engine='openpyxl') as writer:
        df.to_excel(writer, index=False)

# Ejemplo de uso
root_dir = r"M:\AUDITORIA MITES\Evidencias Auditoría Interna 2024"
output_file = r"C:\Users\09773491d\Documents\BBDD\Para_Sorolla2\estructura_directorio_arbol2.xlsx"

directory_structure = get_directory_structure(root_dir)
export_to_excel(directory_structure, output_file)

print(f"Estructura de directorios exportada a {output_file}")