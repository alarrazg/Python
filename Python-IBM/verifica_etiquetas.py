import pandas as pd

def print_non_empty_values_sorted(file_path, sheet_name, column_letter, start_range, end_range):
    # Cargar el archivo Excel
    df = pd.read_excel(file_path, sheet_name=sheet_name)
    
    # Obtener los valores de la columna especificada por su letra
    column_index = ord(column_letter) - ord('A')
    column_values = df.iloc[:, column_index].dropna().astype(str).str.strip()
    
    # Filtrar valores no vacíos, no nulos y diferentes de 0
    filtered_values = column_values[(column_values != '') & (column_values != '0') & (column_values != 'null') & (column_values != '0.0')]
    
    # Convertir a enteros para ordenar correctamente y manejar errores de conversión
    valid_values = []
    for value in filtered_values:
        try:
            int_value = int(float(value))
            if start_range <= int_value <= end_range:
                valid_values.append(int_value)
        except ValueError:
            continue
    
    # Ordenar los valores y convertir de vuelta a texto
    sorted_values = sorted(valid_values)
    sorted_values = [str(value) for value in sorted_values]
    
    # Imprimir los valores filtrados y ordenados en bloques de 10 en 10
    print(f"Valores en la columna '{column_letter}' (excluyendo vacíos, null o 0) ordenados de menor a mayor dentro del rango {start_range}-{end_range}:")
    for i in range(0, len(sorted_values), 10):
        print(sorted_values[i:i+10])

# Ejemplo de uso
file_path = r"C:\Users\09773491d\Documents\BBDD\20241213-T_Sorolla_Export.xlsx"
sheet_name = "T_Sorolla_Export"
column_letter = "S"
start_range = 63651
end_range = 63750

print_non_empty_values_sorted(file_path, sheet_name, column_letter, start_range, end_range)