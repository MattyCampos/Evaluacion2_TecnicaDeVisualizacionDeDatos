import pandas as pd

# 1️⃣ Cargar el archivo CSV original
# Si tu archivo usa punto y coma (;) cámbialo en sep
df = pd.read_csv(r"C:\Users\Matty\Desktop\Eva2\partes CSV vigencia S\parte_1.csv")

# 2️⃣ Crear la nueva columna RUT_COMPLETO
df["RUT_COMPLETO"] = df["RUT"].astype(str).str.strip() + "-" + df["DV"].astype(str).str.strip()

# 3️⃣ Eliminar las columnas RUT y DV
df.drop(columns=["RUT", "DV"], inplace=True)

# 4️⃣ Seleccionar solo las columnas deseadas
columnas_finales = [
    "RUT_COMPLETO",
    "RAZON_SOCIAL",
    "CODIGO ACTIVIDAD",
    "VIGENCIA",
    "DESC. ACTIVIDAD ECONOMICA"
]
df = df[columnas_finales]

# 5️⃣ Guardar el nuevo CSV
df.to_csv("parte_1_Vig_S.csv", index=False, encoding="utf-8", sep=",")

print("✅ Archivo generado")