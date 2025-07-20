import json
import pandas as pd

# Cargar el archivo JSON
with open("Wikipedia_Tabla.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# Obtener las tablas
tablas = data.get("tables", [])

# Crear un archivo Excel con varias hojas
with pd.ExcelWriter("salida_wikipedia.xlsx", engine="openpyxl") as writer:
    for i, tabla in enumerate(tablas):
        # Convertimos cada tabla en un DataFrame
        df = pd.DataFrame(tabla[1:], columns=tabla[0]) if len(tabla) > 1 else pd.DataFrame(tabla)
        df.to_excel(writer, sheet_name=f"Tabla_{i+1}", index=False)

print("Conversión completada. Archivo guardado como 'salida_wikipedia.xlsx'")