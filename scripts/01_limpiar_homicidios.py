"""
SCRIPT 01: LIMPIAR Y UNIFICAR HOMICIDIOS (CORREGIDO)
=====================================================
Fuente: Ministerio del Interior - Ecuador
Datos: 100% reales
"""

import pandas as pd
import os
from datetime import datetime

RUTA_BASE = r"C:\Users\Erick Zambrano\Desktop\linkedin\PROYECTOS\DATOS SUCIOS"
RUTA_SALIDA = r"C:\Users\Erick Zambrano\Desktop\linkedin\PROYECTOS\02_criminalidad_ecuador\datos_limpios"
os.makedirs(RUTA_SALIDA, exist_ok=True)

print("=" * 80)
print("📊 LIMPIEZA Y UNIFICACIÓN: HOMICIDIOS INTENCIONALES")
print("=" * 80)

# Leer datos históricos
print("\n📁 Leyendo datos históricos (2014-2024)...")
archivo_hist = os.path.join(RUTA_BASE, "mdi_homicidios_intencionales_pm_2014_2024.xlsx")
df_hist = pd.read_excel(archivo_hist, sheet_name='1', header=0, skiprows=1)
print(f"   ✅ Registros: {df_hist.shape[0]:,}")
print(f"   ✅ Columnas: {df_hist.shape[1]}")

# Leer datos 2025
print("\n📁 Leyendo datos actuales (2025)...")
archivo_2025 = os.path.join(RUTA_BASE, "MDI_HomicidiosIntencionalse_PM_2025_Enero_Noviembre.xlsx")
df_2025 = pd.read_excel(archivo_2025, sheet_name='1', header=0, skiprows=1)
print(f"   ✅ Registros: {df_2025.shape[0]:,}")
print(f"   ✅ Columnas: {df_2025.shape[1]}")

# Ver columnas de cada uno
print("\n📋 Columnas del histórico:")
for i, c in enumerate(df_hist.columns[:10]):
    print(f"   {c}")

print("\n📋 Columnas de 2025:")
for i, c in enumerate(df_2025.columns[:10]):
    print(f"   {c}")

# Agregar columna de origen
df_hist['fuente'] = 'historico_2014_2024'
df_2025['fuente'] = 'actual_2025'

# Unificar con todas las columnas (concat maneja columnas diferentes)
print("\n🔄 Unificando datasets...")
df_unificado = pd.concat([df_hist, df_2025], ignore_index=True, sort=False)
print(f"   Total: {df_unificado.shape[0]:,} registros x {df_unificado.shape[1]} columnas")

# Limpiar columnas sin nombre
cols_unnamed = [c for c in df_unificado.columns if 'Unnamed' in str(c)]
if cols_unnamed:
    df_unificado = df_unificado.drop(columns=cols_unnamed)
    print(f"   Columnas Unnamed eliminadas: {len(cols_unnamed)}")

# Identificar columnas clave
print("\n🔍 Buscando columnas de fecha y provincia...")
col_fecha = None
col_provincia = None

for c in df_unificado.columns:
    c_lower = str(c).lower()
    if 'fecha' in c_lower and col_fecha is None:
        col_fecha = c
        print(f"   Columna de fecha: {c}")
    if 'provincia' in c_lower and col_provincia is None:
        col_provincia = c
        print(f"   Columna de provincia: {c}")

# Crear columnas año y mes si hay fecha
if col_fecha:
    df_unificado[col_fecha] = pd.to_datetime(df_unificado[col_fecha], errors='coerce')
    df_unificado['año'] = df_unificado[col_fecha].dt.year
    df_unificado['mes'] = df_unificado[col_fecha].dt.month
    print(f"   Columnas 'año' y 'mes' creadas")

# Normalizar provincia
if col_provincia:
    df_unificado[col_provincia] = df_unificado[col_provincia].astype(str).str.upper().str.strip()

# Mostrar resumen
print("\n" + "=" * 80)
print("📊 RESUMEN FINAL")
print("=" * 80)
print(f"\n📏 Dimensiones: {df_unificado.shape[0]:,} filas x {df_unificado.shape[1]} columnas")

if 'año' in df_unificado.columns:
    print("\n🗓️ Por año:")
    for año, count in df_unificado['año'].value_counts().sort_index().items():
        if pd.notna(año):
            print(f"   {int(año)}: {count:,}")

if col_provincia:
    print(f"\n🗺️ Top 10 provincias:")
    for prov, count in df_unificado[col_provincia].value_counts().head(10).items():
        print(f"   {prov}: {count:,}")

# Exportar
archivo_salida = os.path.join(RUTA_SALIDA, "01_homicidios_unificado.csv")
df_unificado.to_csv(archivo_salida, index=False, encoding='utf-8-sig')
print(f"\n💾 Guardado: {archivo_salida}")
print(f"   Tamaño: {os.path.getsize(archivo_salida) / 1024 / 1024:.2f} MB")

print("\n✅ COMPLETADO")
