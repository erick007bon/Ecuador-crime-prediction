import pandas as pd

ruta_2014_2024 = r"C:\Users\Erick Zambrano\Desktop\linkedin\PROYECTOS\DATOS SUCIOS\mdi_homicidios_intencionales_pm_2014_2024.xlsx"
ruta_2025 = r"C:\Users\Erick Zambrano\Desktop\linkedin\PROYECTOS\DATOS SUCIOS\MDI_HomicidiosIntencionalse_PM_2025_Enero_Noviembre.xlsx"

output = []

# Leer con header en fila 0, datos desde fila 1
df = pd.read_excel(ruta_2014_2024, sheet_name='1', header=0, skiprows=1)

output.append("=" * 100)
output.append("📊 RESUMEN EJECUTIVO - DATOS DE HOMICIDIOS ECUADOR 2014-2024")
output.append("=" * 100)

output.append(f"\n📁 Total registros: {df.shape[0]:,}")
output.append(f"📋 Total columnas: {df.shape[1]}")

output.append("\n" + "-" * 100)
output.append("📋 COLUMNAS DISPONIBLES:")
output.append("-" * 100)
for i, col in enumerate(df.columns):
    output.append(f" {i+1:2}. {col}")

# Extraer año de fecha_infraccion
if 'fecha_infraccion' in df.columns:
    df['año'] = pd.to_datetime(df['fecha_infraccion'], errors='coerce').dt.year
    df['mes'] = pd.to_datetime(df['fecha_infraccion'], errors='coerce').dt.month

output.append("\n" + "=" * 100)
output.append("📊 ESTADÍSTICAS CLAVE:")
output.append("=" * 100)

# Por año
if 'año' in df.columns:
    output.append("\n🗓️ HOMICIDIOS POR AÑO:")
    for idx, val in df['año'].value_counts().sort_index().items():
        output.append(f"   {int(idx)}: {val:,}")

# Por provincia (top 10)
if 'provincia' in df.columns:
    output.append(f"\n🗺️ TOP 10 PROVINCIAS (de {df['provincia'].nunique()} únicas):")
    for idx, val in df['provincia'].value_counts().head(10).items():
        output.append(f"   {idx}: {val:,}")

# Por arma
if 'arma' in df.columns:
    output.append(f"\n🔫 TIPO DE ARMA:")
    for idx, val in df['arma'].value_counts().head(10).items():
        output.append(f"   {idx}: {val:,}")

# Por sexo
if 'sexo' in df.columns:
    output.append(f"\n👤 SEXO VÍCTIMA:")
    for idx, val in df['sexo'].value_counts().items():
        output.append(f"   {idx}: {val:,}")

# Por motivación
if 'presunta_motivacion' in df.columns:
    output.append(f"\n⚠️ PRESUNTA MOTIVACIÓN:")
    for idx, val in df['presunta_motivacion'].value_counts().head(10).items():
        output.append(f"   {idx}: {val:,}")

# EL ORO
output.append("\n" + "=" * 100)
output.append("📌 ANÁLISIS ESPECIAL: EL ORO (MACHALA)")
output.append("=" * 100)

if 'provincia' in df.columns:
    df_oro = df[df['provincia'].astype(str).str.upper().str.contains('ORO', na=False)]
    output.append(f"\n📍 Total homicidios en El Oro: {len(df_oro):,}")
    
    if 'año' in df.columns:
        output.append("\n📅 Por año:")
        for idx, val in df_oro['año'].value_counts().sort_index().items():
            output.append(f"   {int(idx)}: {val:,}")
    
    if 'canton' in df.columns:
        output.append("\n🏙️ Por cantón:")
        for idx, val in df_oro['canton'].value_counts().items():
            output.append(f"   {idx}: {val:,}")

output.append("\n" + "=" * 100)
output.append("✅ ANÁLISIS COMPLETADO")
output.append("=" * 100)

# Guardar
result = '\n'.join(output)
with open(r"C:\Users\Erick Zambrano\Desktop\linkedin\PROYECTOS\02_criminalidad_ecuador\ANALISIS_DATOS.txt", 'w', encoding='utf-8') as f:
    f.write(result)
    
print(result)
