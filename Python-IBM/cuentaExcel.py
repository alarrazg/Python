import pandas as pd
import os

def count_non_empty_cells_in_column(directory, column_name):
    total_non_empty_cells = 0
    
    # Iterar sobre todos los archivos Excel en el directorio que comienzan con el prefijo especificado
    for filename in os.listdir(directory):
        if (filename.startswith("8 - Bienes_Muebles") and 
            (filename.endswith(".xlsx") or filename.endswith(".xls"))):
            # Cargar el archivo Excel
            file_path = os.path.join(directory, filename)
            excel_file = pd.ExcelFile(file_path)
            
            # Iterar sobre todas las hojas en el archivo Excel
            for sheet_name in excel_file.sheet_names:
                df = pd.read_excel(file_path, sheet_name=sheet_name)
                
                # Eliminar espacios en blanco adicionales de los nombres de las columnas
                df.columns = df.columns.str.strip()
                
                # Imprimir los nombres de las columnas para verificar
                print(f"Procesando archivo: {filename}, hoja: {sheet_name}")
                print(f"Columnas disponibles: {df.columns.tolist()}")
                
                # Contar celdas no vacías en la columna especificada
                if column_name in df.columns:
                    non_empty_cells = df[column_name].dropna().shape[0]
                    total_non_empty_cells += non_empty_cells
                    print(f"Celdas no vacías en '{column_name}': {non_empty_cells}")
                else:
                    print(f"Columna '{column_name}' no encontrada en la hoja '{sheet_name}'")
    
    return total_non_empty_cells

# Ejemplo de uso
directory = r"C:\Users\09773491d\Documents\BBDD\Para_Sorolla2"
column_name = "Órgano Gestor *"
total_non_empty_cells = count_non_empty_cells_in_column(directory, column_name)
print(f"Total de celdas no vacías en la columna '{column_name}': {total_non_empty_cells}")


