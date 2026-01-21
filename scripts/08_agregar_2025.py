"""
SCRIPT: AGREGAR DATOS DE 2025 - VERSIÓN 2
==========================================
"""

import pandas as pd
import os

RUTA_BASE = r"C:\Users\Erick Zambrano\Desktop\linkedin\PROYECTOS\DATOS SUCIOS"
RUTA_SALIDA = r"C:\Users\Erick Zambrano\Desktop\linkedin\PROYECTOS\02_criminalidad_ecuador"

print("=" * 60)
print("📊 AGREGANDO DATOS DE 2025 - VERSIÓN 2")
print("=" * 60)

# Cargar dataset actual
print("\n📁 Cargando dataset actual...")
df_actual = pd.read_csv(os.path.join(RUTA_SALIDA, "dataset_final_limpio.csv"))
print(f"   Filas: {len(df_actual)}, Años: {df_actual['año'].min()}-{df_actual['año'].max()}")

# Leer Excel 2025 sin skiprows para ver estructura
print("\n📁 Explorando estructura de archivo 2025...")
archivo_2025 = os.path.join(RUTA_BASE, "MDI_HomicidiosIntencionalse_PM_2025_Enero_Noviembre.xlsx")

# Leer con header=0 (primera fila como header)
df_2025 = pd.read_excel(archivo_2025, sheet_name='1', header=0)
print(f"   Filas: {len(df_2025)}")
print(f"   Columnas (primeras 5): {list(df_2025.columns)[:5]}")

# Buscar columnas que contengan fechas convirtiendo a string
print("\n🔍 Buscando columnas con datos de fecha y provincia...")

col_fecha = None
col_prov = None

for col in df_2025.columns:
    col_name = str(col)
    # Buscar columna de fecha
    if 'fecha' in col_name.lower():
        col_fecha = col
    # Buscar columna de provincia  
    if 'provincia' in col_name.lower():
        col_prov = col

print(f"   Columna fecha por nombre: {col_fecha}")
print(f"   Columna provincia por nombre: {col_prov}")

# Si no encontramos por nombre, usar las que sabemos del archivo original
# Basado en la estructura del archivo de homicidios 2014-2024
if col_fecha is None:
    # Buscar la primera columna con datos tipo fecha
    for col in df_2025.columns:
        try:
            sample = pd.to_datetime(df_2025[col].head(10), errors='coerce')
            if sample.notna().sum() > 5:
                col_fecha = col
                print(f"   Columna fecha detectada por contenido: {col}")
                break
        except:
            pass

if col_prov is None:
    # Buscar columna con nombres de provincia
    provincias = ['GUAYAS', 'PICHINCHA', 'MANABI', 'EL ORO', 'LOS RIOS', 'ESMERALDAS']
    for col in df_2025.columns:
        try:
            valores = df_2025[col].astype(str).str.upper().unique()[:20]
            if any(p in str(valores) for p in provincias):
                col_prov = col
                print(f"   Columna provincia detectada por contenido: {col}")
                break
        except:
            pass

if col_fecha and col_prov:
    print(f"\n✅ Usando: fecha='{col_fecha}', provincia='{col_prov}'")
    
    # Parsear fecha
    df_2025['fecha_parsed'] = pd.to_datetime(df_2025[col_fecha], errors='coerce')
    df_2025['año'] = df_2025['fecha_parsed'].dt.year
    df_2025['mes'] = df_2025['fecha_parsed'].dt.month
    df_2025['provincia'] = df_2025[col_prov].astype(str).str.upper().str.strip()
    
    # Filtrar 2025
    df_2025_clean = df_2025[df_2025['año'] == 2025].copy()
    print(f"\n   Registros de 2025: {len(df_2025_clean)}")
    print(f"   Meses: {sorted(df_2025_clean['mes'].dropna().unique())}")
    
    # Agregar
    agregado = df_2025_clean.groupby(['año', 'mes', 'provincia']).size().reset_index(name='count_homicidios')
    print(f"   Filas agregadas: {len(agregado)}")
    print(f"   Homicidios 2025: {agregado['count_homicidios'].sum()}")
    
    # Agregar columnas faltantes
    for col in df_actual.columns:
        if col not in agregado.columns:
            agregado[col] = 0
    
    agregado = agregado[df_actual.columns]
    
    # Concatenar
    df_nuevo = pd.concat([df_actual, agregado], ignore_index=True)
    df_nuevo = df_nuevo.sort_values(['año', 'mes', 'provincia']).reset_index(drop=True)
    
    # Guardar
    df_nuevo.to_csv(os.path.join(RUTA_SALIDA, "dataset_final_limpio.csv"), index=False)
    
    print(f"\n✅ DATASET ACTUALIZADO:")
    print(f"   Total filas: {len(df_nuevo)}")
    print(f"   Años: {int(df_nuevo['año'].min())} - {int(df_nuevo['año'].max())}")
    
    # Verificar
    for año in [2024, 2025]:
        datos = df_nuevo[df_nuevo['año'] == año]
        print(f"   {año}: {len(datos)} filas, {datos['count_homicidios'].sum()} homicidios")
else:
    print("\n❌ No se pudieron detectar columnas")
    print("   Mostrando primeras filas para debug:")
    print(df_2025.head(2).T)
