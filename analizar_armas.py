import pandas as pd

print("=" * 80)
print("📊 ANÁLISIS DE DATOS DE ARMAS ILÍCITAS")
print("=" * 80)

# Cargar datos de armas ilícitas
ruta_armas = r"C:\Users\Erick Zambrano\Desktop\linkedin\PROYECTOS\DATOS SUCIOS\ARMAS ILICITAS\MDI_ArmasIlicitas_PM_Historico_2017_2024.xlsx"

# Ver hojas disponibles
xl = pd.ExcelFile(ruta_armas)
print(f"\n📄 Hojas disponibles: {xl.sheet_names}")

# Leer hoja de datos (probablemente hoja '1')
if len(xl.sheet_names) > 1:
    df = pd.read_excel(ruta_armas, sheet_name=1, header=0, skiprows=1)
else:
    df = pd.read_excel(ruta_armas, sheet_name=0, header=0, skiprows=1)

print(f"\n📏 Dimensiones: {df.shape[0]:,} filas x {df.shape[1]} columnas")

print("\n📋 COLUMNAS DISPONIBLES:")
for i, col in enumerate(df.columns):
    print(f"   {i+1:2}. {col}")

print(f"\n📅 Primeras 3 filas:")
print(df.head(3).to_string())

# Guardar resumen
with open(r"C:\Users\Erick Zambrano\Desktop\linkedin\PROYECTOS\02_criminalidad_ecuador\ANALISIS_ARMAS.txt", 'w', encoding='utf-8') as f:
    f.write(f"ARMAS ILÍCITAS - {df.shape[0]:,} registros x {df.shape[1]} columnas\n\n")
    f.write("COLUMNAS:\n")
    for col in df.columns:
        f.write(f"  - {col}\n")

print("\n✅ Análisis completado")
