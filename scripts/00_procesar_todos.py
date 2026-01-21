"""
SCRIPT MASTER: LIMPIAR TODOS LOS DATASETS DEL MDI
==================================================
Fuente: Ministerio del Interior - Ecuador
Datos: 100% reales
"""

import pandas as pd
import os
from datetime import datetime

RUTA_BASE = r"C:\Users\Erick Zambrano\Desktop\linkedin\PROYECTOS\DATOS SUCIOS"
RUTA_SALIDA = r"C:\Users\Erick Zambrano\Desktop\linkedin\PROYECTOS\02_criminalidad_ecuador\datos_limpios"
os.makedirs(RUTA_SALIDA, exist_ok=True)

def procesar_dataset(nombre, archivo_hist, archivo_2025, archivo_salida):
    """Procesa un dataset: lee histórico + 2025, unifica y exporta"""
    print(f"\n{'='*80}")
    print(f"📊 PROCESANDO: {nombre}")
    print("="*80)
    
    # Leer histórico
    print(f"\n📁 Leyendo histórico: {os.path.basename(archivo_hist)}")
    xl1 = pd.ExcelFile(archivo_hist)
    sheet = '1' if '1' in xl1.sheet_names else xl1.sheet_names[-1]
    df_hist = pd.read_excel(archivo_hist, sheet_name=sheet, header=0, skiprows=1)
    print(f"   Registros: {df_hist.shape[0]:,}, Columnas: {df_hist.shape[1]}")
    
    # Leer 2025
    print(f"\n📁 Leyendo 2025: {os.path.basename(archivo_2025)}")
    xl2 = pd.ExcelFile(archivo_2025)
    sheet2 = '1' if '1' in xl2.sheet_names else xl2.sheet_names[-1]
    df_2025 = pd.read_excel(archivo_2025, sheet_name=sheet2, header=0, skiprows=1)
    print(f"   Registros: {df_2025.shape[0]:,}, Columnas: {df_2025.shape[1]}")
    
    # Agregar origen
    df_hist['fuente'] = 'historico'
    df_2025['fuente'] = 'actual_2025'
    
    # Unificar
    df = pd.concat([df_hist, df_2025], ignore_index=True, sort=False)
    
    # Limpiar Unnamed
    cols_drop = [c for c in df.columns if 'Unnamed' in str(c)]
    if cols_drop:
        df = df.drop(columns=cols_drop)
    
    # Buscar fecha y provincia
    col_fecha = None
    col_provincia = None
    for c in df.columns:
        c_lower = str(c).lower()
        if 'fecha' in c_lower and col_fecha is None:
            col_fecha = c
        if 'provincia' in c_lower and col_provincia is None:
            col_provincia = c
    
    # Crear año/mes si hay fecha
    if col_fecha:
        df[col_fecha] = pd.to_datetime(df[col_fecha], errors='coerce')
        df['año'] = df[col_fecha].dt.year
        df['mes'] = df[col_fecha].dt.month
    
    # Normalizar provincia
    if col_provincia:
        df[col_provincia] = df[col_provincia].astype(str).str.upper().str.strip()
    
    # Exportar
    df.to_csv(archivo_salida, index=False, encoding='utf-8-sig')
    size_mb = os.path.getsize(archivo_salida) / 1024 / 1024
    
    print(f"\n✅ {nombre}: {df.shape[0]:,} registros → {os.path.basename(archivo_salida)} ({size_mb:.2f} MB)")
    return df.shape[0]

# ============================================================================
# PROCESAR TODOS LOS DATASETS
# ============================================================================

total_registros = 0

# 1. Armas Ilícitas
total_registros += procesar_dataset(
    "ARMAS ILÍCITAS",
    os.path.join(RUTA_BASE, "ARMAS ILICITAS", "MDI_ArmasIlicitas_PM_Historico_2017_2024.xlsx"),
    os.path.join(RUTA_BASE, "ARMAS ILICITAS", "MDI_ArmasIlicitas_PM_2025_Enero_Noviembre.xlsx"),
    os.path.join(RUTA_SALIDA, "02_armas_ilicitas_unificado.csv")
)

# 2. Personas Desaparecidas
total_registros += procesar_dataset(
    "PERSONAS DESAPARECIDAS",
    os.path.join(RUTA_BASE, "PERSONAS DESAPARECIDAS", "MDI_PersonasDesaparecidas_PM_2017_2024.xlsx"),
    os.path.join(RUTA_BASE, "PERSONAS DESAPARECIDAS", "MDI_PersonasDesaparecidas_PM_2025_Enero_Noviembre.xlsx"),
    os.path.join(RUTA_SALIDA, "03_personas_desaparecidas_unificado.csv")
)

# 3. Drogas (procesar antes de detenidos porque es más pequeño)
total_registros += procesar_dataset(
    "DROGAS INCAUTADAS",
    os.path.join(RUTA_BASE, "DROGA EN EL ECUADOR INCAUTACION", "MDI_SustanciasDestruccion_PM_2016_2024.xlsx"),
    os.path.join(RUTA_BASE, "DROGA EN EL ECUADOR INCAUTACION", "MDI_SustanciasDestruccion_PM_2025_Enero_Noviembre.xlsx"),
    os.path.join(RUTA_SALIDA, "05_drogas_incautadas_unificado.csv")
)

# 4. Detenidos (archivo grande - al final)
print("\n⚠️ Procesando DETENIDOS - archivo grande, puede tomar varios minutos...")
total_registros += procesar_dataset(
    "DETENIDOS/APREHENDIDOS",
    os.path.join(RUTA_BASE, "PERSONAS PRESAS", "MDI_DetenidosAprehendidos_PM_2019_2024.xlsx"),
    os.path.join(RUTA_BASE, "PERSONAS PRESAS", "MDI_DetenidosAprehendidos_PM_2025_Enero_Noviembre.xlsx"),
    os.path.join(RUTA_SALIDA, "04_detenidos_unificado.csv")
)

print("\n" + "="*80)
print("🎉 TODOS LOS DATASETS PROCESADOS")
print("="*80)
print(f"\nTotal registros procesados: {total_registros:,}")
print(f"(+ 38,930 homicidios ya procesados)")
print(f"\nTotal aproximado: {total_registros + 38930:,} registros")
