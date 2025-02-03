import pandas as pd

# Datos corregidos con las combinaciones de hardware y los juegos asociados
juegos_detallados_data = {
    "Combinación": [
        "Gigabyte B650 AORUS Elite AX + AMD Ryzen 5 7600 + AMD Radeon RX 6600",
        "MSI MAG Z890 TOMAHAWK WIFI + Intel Core i5-12400F + NVIDIA GeForce GTX 1660 Super",
        "Gigabyte X670 EAGLE WIFI7 + AMD Ryzen 5 7500F + AMD Radeon RX 6650 XT"
    ],
    "Tarjeta Gráfica": [
        "AMD Radeon RX 6600", "NVIDIA GeForce GTX 1660 Super", "AMD Radeon RX 6650 XT"
    ],
    "Juegos Óptimos": [
        "Assassin’s Creed Valhalla (70-80 FPS en calidad alta 1080p), Cyberpunk 2077 (50-60 FPS en calidad media 1080p), Far Cry 6 (60-80 FPS en calidad alta 1080p), Battlefield V (80-100 FPS en calidad alta 1080p), Fortnite (120+ FPS en calidad alta 1080p), League of Legends (200+ FPS), Valorant (200+ FPS), Rocket League (120-150 FPS en calidad alta), Minecraft (100-150 FPS)",
        "Shadow of the Tomb Raider (60-80 FPS en calidad alta 1080p), Forza Horizon 5 (60 FPS en calidad alta 1080p), Call of Duty: Warzone (50-70 FPS en calidad media 1080p), Doom Eternal (100+ FPS en calidad alta 1080p), Watch Dogs Legion (60-80 FPS en calidad media 1080p), Fortnite (100-120 FPS en calidad alta 1080p), Valorant (100-150 FPS), League of Legends (200+ FPS), Apex Legends (60-80 FPS en calidad media 1080p), Minecraft (100-150 FPS)",
        "Horizon Zero Dawn (70-90 FPS en calidad alta 1080p), Far Cry 6 (60-70 FPS en calidad alta 1080p), Call of Duty: Modern Warfare II (70-90 FPS en calidad alta 1080p), Cyberpunk 2077 (50-60 FPS en calidad media-alta 1080p), Battlefield 2042 (50-70 FPS en calidad media-alta 1080p), Fortnite (100-150 FPS en calidad alta 1080p), Valorant (150-200 FPS), League of Legends (200+ FPS), Rocket League (120+ FPS en calidad alta), Minecraft (100-150 FPS)"
    ],
    "Juegos No Óptimos": [
        "Cyberpunk 2077 (No alcanzará 60 FPS en ultra a 1080p), Metro Exodus (Bajo rendimiento en calidad ultra a 1440p), Red Dead Redemption 2 (Pueden no llegar a 60 FPS en calidad alta)",
        "Cyberpunk 2077 (Bajo rendimiento a calidad media o baja), Red Dead Redemption 2 (Pueden no llegar a 60 FPS en calidad alta), Metro Exodus (Bajo rendimiento en calidad ultra)",
        "Cyberpunk 2077 (Puede no mantener 60 FPS en calidad ultra a 1080p), Red Dead Redemption 2 (Rendimiento limitado en calidad ultra a 1440p)"
    ]
}

# Crear el DataFrame con los datos
df_juegos_detallados = pd.DataFrame(juegos_detallados_data)

# Guardar el archivo Excel
file_path_juegos_detallados = "P:/Mis_Cosas/juegos_combinaciones_hardware_completos.xlsx"
df_juegos_detallados.to_excel(file_path_juegos_detallados, index=False)

# Proporcionar el enlace para descarga
file_path_juegos_detallados

