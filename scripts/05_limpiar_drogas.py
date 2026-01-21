"""
SCRIPT 05: LIMPIAR Y UNIFICAR DROGAS INCAUTADAS
================================================
Fuente: Ministerio del Interior - Ecuador
Datos: 100% reales, sin modificaciones inventadas
"""

import pandas as pd
import os
from datetime import datetime

RUTA_BASE = r"C:\Users\Erick Zambrano\Desktop\linkedin\PROYECTOS\DATOS SUCIOS\DROGA EN EL ECUADOR INCAUTACION"
RUTA_SALIDA = r"C:\Users\Erick Zambrano\Desktop\linkedin\PROYECTOS\02_criminalidad_ecuador\datos_limpios"
os.makedirs(RUTA_SALIDA, exist_ok=True)

print("=" * 80)
print("📊 LIMPIEZA Y UNIFICACIÓN: DROGAS INCAUTADAS")
print("=" * 80)

# Leer datos históricos
print("\n📁 Leyendo datos históricos (2016-2024)...")
archivo_hist = os.path.join(RUTA_BASE, "MDI_SustanciasDestruccion_PM_2016_2024.xlsx")
xl = pd.ExcelFile(archivo_hist)
print(f"   📄 Hojas: {xl.sheet_names}")
df_hist = pd.read_excel(archivo_hist, sheet_name='1' if '1' in xl.sheet_names else xl.sheet_names[-1], header=0, skiprows=1)
print(f"   ✅ Registros: {df_hist.shape[0]:,}")

# Leer datos 2025
print("\n📁 Leyendo datos actuales (2025)...")
archivo_2025 = os.path.join(RUTA_BASE, "MDI_SustanciasDestruccion_PM_2025_Enero_Noviembre.xlsx")
xl2 = pd.ExcelFile(archivo_2025)
df_2025 = pd.read_excel(archivo_2025, sheet_name='1' if '1' in xl2.sheet_names else xl2.sheet_names[-1], header=0, skiprows=1)
print(f"   ✅ Registros: {df_2025.shape[0]:,}")

# Columnas comunes
cols_comunes = list(set(df_hist.columns).intersection(set(df_2025.columns)))
print(f"\n🔍 Columnas comunes: {len(cols_comunes)}")

# Unificar
df_hist_c = df_hist[cols_comunes].copy()
df_2025_c = df_2025[cols_comunes].copy()
df_hist_c['fuente'] = 'historico'
df_2025_c['fuente'] = 'actual_2025'
df_unificado = pd.concat([df_hist_c, df_2025_c], ignore_index=True)

# Limpiar
df_unificado = df_unificado.dropna(how='all')
cols_unnamed = [c for c in df_unificado.columns if 'Unnamed' in str(c)]
if cols_unnamed:
    df_unificado = df_unificado.drop(columns=cols_unnamed)

# Exportar
archivo_salida = os.path.join(RUTA_SALIDA, "05_drogas_incautadas_unificado.csv")
df_unificado.to_csv(archivo_salida, index=False, encoding='utf-8-sig')

print(f"\n✅ Dataset unificado: {df_unificado.shape[0]:,} registros")
print(f"✅ Archivo: {archivo_salida}")
print(f"✅ Tamaño: {os.path.getsize(archivo_salida) / 1024 / 1024:.2f} MB")
