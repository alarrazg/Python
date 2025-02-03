import pandas as pd

# Datos de los componentes y sus precios estimados en euros
componentes = {
    "Componente": [
        "Placa Base (Gigabyte B650 AORUS Elite AX)", "Procesador (AMD Ryzen 5 7600)", "Tarjeta Gráfica (AMD Radeon RX 6600)", 
        "RAM (16GB DDR5 5600MHz)", "SSD NVMe 1TB Gen4", "Fuente de Alimentación 550W 80+ Bronze", 
        "Placa Base (MSI MAG Z890 TOMAHAWK WIFI)", "Procesador (Intel Core i5-12400F)", "Tarjeta Gráfica (NVIDIA GeForce GTX 1660 Super)", 
        "RAM (16GB DDR4 3200MHz)", "SSD NVMe 1TB Gen3", "Fuente de Alimentación 600W 80+ Bronze", 
        "Placa Base (Gigabyte X670 EAGLE WIFI7)", "Procesador (AMD Ryzen 5 7500F)", "Tarjeta Gráfica (AMD Radeon RX 6650 XT)", 
        "RAM (16GB DDR5 5200MHz)", "SSD NVMe 500GB Gen4", "Fuente de Alimentación 500W 80+ Bronze"
    ],
    "Precio (EUR)": [
        170, 210, 230, 70, 100, 55, 180, 150, 250, 65, 90, 65, 250, 210, 260, 60, 75, 50
    ]
}

# Crear el DataFrame
df_componentes = pd.DataFrame(componentes)

# Crear una nueva columna para cada combinación de equipo
df_componentes["Combinación 1: Gigabyte B650 AORUS Elite AX + AMD Ryzen 5 7600 + AMD Radeon RX 6600"] = [
    170, 210, 230, 70, 100, 55, None, None, None, None, None, None, None, None, None, None, None, None
]
df_componentes["Combinación 2: MSI MAG Z890 TOMAHAWK WIFI + Intel Core i5-12400F + NVIDIA GeForce GTX 1660 Super"] = [
    None, None, None, None, None, None, 180, 150, 250, 65, 90, 65, None, None, None, None, None, None, None
]
df_componentes["Combinación 3: Gigabyte X670 EAGLE WIFI7 + AMD Ryzen 5 7500F + AMD Radeon RX 6650 XT"] = [
    None, None, None, None, None, None, None, None, None, None, None, None, 250, 210, 260, 60, 75, 50
]

# Añadir columna para total por combinación
df_componentes["Precio Total Combinación 1"] = df_componentes["Combinación 1: Gigabyte B650 AORUS Elite AX + AMD Ryzen 5 7600 + AMD Radeon RX 6600"].sum()
df_componentes["Precio Total Combinación 2"] = df_componentes["Combinación 2: MSI MAG Z890 TOMAHAWK WIFI + Intel Core i5-12400F + NVIDIA GeForce GTX 1660 Super"].sum()
df_componentes["Precio Total Combinación 3"] = df_componentes["Combinación 3: Gigabyte X670 EAGLE WIFI7 + AMD Ryzen 5 7500F + AMD Radeon RX 6650 XT"].sum()

# Guardar el DataFrame en un archivo Excel
file_path_componentes = "P:/Mis_Cosas/Precios_Componentes_Combinaciones.xlsx"
df_componentes.to_excel(file_path_componentes, index=False)

file_path_componentes
