"""
SCRIPT 06B: AGREGAR DATOS - VERSIÓN MEJORADA
=============================================
Maneja CSVs con headers incorrectos detectando columnas por contenido
"""

import pandas as pd
import numpy as np
import os
from datetime import datetime

RUTA_LIMPIOS = r"C:\Users\Erick Zambrano\Desktop\linkedin\PROYECTOS\02_criminalidad_ecuador\datos_limpios"
RUTA_SALIDA = r"C:\Users\Erick Zambrano\Desktop\linkedin\PROYECTOS\02_criminalidad_ecuador"

# Mapeo de códigos a nombres de provincia
PROVINCIAS = {
    '01': 'AZUAY', '02': 'BOLIVAR', '03': 'CAÑAR', '04': 'CARCHI',
    '05': 'CHIMBORAZO', '06': 'COTOPAXI', '07': 'EL ORO', '08': 'ESMERALDAS',
    '09': 'GUAYAS', '10': 'IMBABURA', '11': 'LOJA', '12': 'LOS RIOS',
    '13': 'MANABI', '14': 'MORONA SANTIAGO', '15': 'NAPO', '16': 'PASTAZA',
    '17': 'PICHINCHA', '18': 'TUNGURAHUA', '19': 'ZAMORA CHINCHIPE',
    '20': 'GALAPAGOS', '21': 'SUCUMBIOS', '22': 'ORELLANA',
    '23': 'SANTO DOMINGO', '24': 'SANTA ELENA', '90': 'ZONAS NO DELIMITADAS'
}

print("=" * 80)
print("📊 AGREGACIÓN MEJORADA DE DATOS")
print("=" * 80)

def detectar_columna_fecha(df):
    """Detecta la columna que contiene fechas"""
    for col in df.columns:
        # Verificar si el nombre de columna parece fecha
        col_str = str(col)
        if '2017' in col_str or '2018' in col_str or '2019' in col_str or '2020' in col_str or '2021' in col_str or '2022' in col_str or '2023' in col_str or '2024' in col_str or '2025' in col_str:
            return col
        # O si los valores parecen fechas
        try:
            sample = df[col].dropna().head(100)
            parsed = pd.to_datetime(sample, errors='coerce')
            if parsed.notna().sum() > 50:
                return col
        except:
            pass
    return None

def detectar_columna_provincia(df):
    """Detecta la columna con códigos o nombres de provincia"""
    provincias_nombres = set(PROVINCIAS.values())
    provincias_codigos = set(PROVINCIAS.keys())
    
    for col in df.columns:
        # Ver si el nombre de columna es una provincia
        col_str = str(col).upper()
        if col_str in provincias_nombres:
            return col
        if col_str in provincias_codigos or col_str.zfill(2) in provincias_codigos:
            return col
        
        # Ver valores de la columna
        try:
            sample = df[col].astype(str).str.upper().unique()[:50]
            matches = sum(1 for v in sample if v in provincias_nombres or v.zfill(2) in provincias_codigos)
            if matches > 5:
                return col
        except:
            pass
    return None

def procesar_dataset_robusto(archivo, nombre):
    """Lee y agrega un dataset de forma robusta"""
    print(f"\n📁 Procesando: {nombre}")
    
    try:
        df = pd.read_csv(archivo, low_memory=False)
        print(f"   Registros: {df.shape[0]:,}, Columnas: {df.shape[1]}")
    except Exception as e:
        print(f"   ❌ Error leyendo: {e}")
        return None
    
    # Si ya tiene año y mes, usarlas directamente
    if 'año' in df.columns and 'mes' in df.columns:
        col_año = 'año'
        col_mes = 'mes'
        print(f"   ✅ Columnas año/mes encontradas")
    else:
        # Detectar columna de fecha
        col_fecha = detectar_columna_fecha(df)
        if col_fecha:
            print(f"   📅 Columna fecha detectada: {col_fecha}")
            df['fecha_parsed'] = pd.to_datetime(df[col_fecha], errors='coerce')
            df['año'] = df['fecha_parsed'].dt.year
            df['mes'] = df['fecha_parsed'].dt.month
            col_año = 'año'
            col_mes = 'mes'
        else:
            print(f"   ⚠️ No se detectó columna de fecha")
            return None
    
    # Detectar columna de provincia
    col_prov = None
    
    # Primero buscar si ya hay columna 'provincia' o similar
    for c in df.columns:
        if 'provincia' in str(c).lower():
            col_prov = c
            break
    
    if col_prov is None:
        col_prov = detectar_columna_provincia(df)
    
    if col_prov is None:
        print(f"   ⚠️ No se detectó columna de provincia")
        return None
    
    print(f"   🗺️ Columna provincia: {col_prov}")
    
    # Normalizar provincia
    df['provincia_norm'] = df[col_prov].astype(str).str.upper().str.strip()
    
    # Mapear códigos a nombres si es necesario
    def mapear_provincia(val):
        val_str = str(val).strip()
        if val_str in PROVINCIAS.values():
            return val_str
        if val_str.zfill(2) in PROVINCIAS:
            return PROVINCIAS[val_str.zfill(2)]
        # Intentar extraer código numérico
        try:
            codigo = str(int(float(val_str))).zfill(2)
            if codigo in PROVINCIAS:
                return PROVINCIAS[codigo]
        except:
            pass
        return val_str
    
    df['provincia_final'] = df['provincia_norm'].apply(mapear_provincia)
    
    # Agregar
    try:
        agregado = df.groupby([col_año, col_mes, 'provincia_final']).size().reset_index(name=f'count_{nombre}')
        agregado.columns = ['año', 'mes', 'provincia', f'count_{nombre}']
        
        # Limpiar NaN
        agregado = agregado.dropna(subset=['año', 'mes', 'provincia'])
        agregado['año'] = agregado['año'].astype(int)
        agregado['mes'] = agregado['mes'].astype(int)
        
        print(f"   ✅ Agregado: {agregado.shape[0]:,} filas")
        return agregado
    except Exception as e:
        print(f"   ❌ Error agregando: {e}")
        return None

# ============================================================================
# PROCESAR TODOS LOS DATASETS
# ============================================================================

datasets = [
    ("01_homicidios_unificado.csv", "homicidios"),
    ("02_armas_ilicitas_unificado.csv", "armas"),
    ("03_personas_desaparecidas_unificado.csv", "desaparecidos"),
    ("04_detenidos_unificado.csv", "detenidos"),
    ("05_drogas_incautadas_unificado.csv", "drogas"),
]

agregados = []
for archivo, nombre in datasets:
    ruta = os.path.join(RUTA_LIMPIOS, archivo)
    if os.path.exists(ruta):
        result = procesar_dataset_robusto(ruta, nombre)
        if result is not None:
            agregados.append(result)

# ============================================================================
# UNIR TODOS
# ============================================================================
print("\n" + "=" * 80)
print("🔄 UNIENDO DATASETS")
print("=" * 80)

if len(agregados) > 0:
    df_final = agregados[0]
    for i, df_agg in enumerate(agregados[1:], 2):
        df_final = pd.merge(df_final, df_agg, on=['año', 'mes', 'provincia'], how='outer')
        print(f"   Unido dataset {i}: {df_final.shape[0]:,} filas")
    
    # Rellenar NaN
    df_final = df_final.fillna(0)
    
    # Convertir conteos a int
    for col in df_final.columns:
        if col.startswith('count_'):
            df_final[col] = df_final[col].astype(int)
    
    # Población por año (nacional, prorrateado por provincia)
    poblacion = {
        2014: 16027466, 2015: 16278844, 2016: 16528730, 2017: 16776977,
        2018: 17023408, 2019: 17267986, 2020: 17510643, 2021: 17751313,
        2022: 17989912, 2023: 18226312, 2024: 18460571, 2025: 18692745
    }
    
    n_prov = df_final['provincia'].nunique()
    df_final['poblacion'] = df_final['año'].map(poblacion).fillna(18500000)
    df_final['poblacion_prov_mes'] = df_final['poblacion'] / n_prov / 12
    
    # Calcular tasas
    for col in df_final.columns:
        if col.startswith('count_'):
            tasa_col = col.replace('count_', 'tasa_')
            df_final[tasa_col] = (df_final[col] / df_final['poblacion_prov_mes'] * 100000).round(2)
    
    # Total de eventos
    count_cols = [c for c in df_final.columns if c.startswith('count_')]
    df_final['count_total'] = df_final[count_cols].sum(axis=1)
    df_final['trimestre'] = ((df_final['mes'] - 1) // 3) + 1
    
    # Ordenar
    df_final = df_final.sort_values(['año', 'mes', 'provincia']).reset_index(drop=True)
    
    # Guardar
    archivo_salida = os.path.join(RUTA_SALIDA, "dataset_final_agregado.csv")
    df_final.to_csv(archivo_salida, index=False, encoding='utf-8-sig')
    
    print(f"\n📊 DATASET FINAL:")
    print(f"   Filas: {df_final.shape[0]:,}")
    print(f"   Columnas: {df_final.shape[1]}")
    print(f"   Años: {df_final['año'].min()} - {df_final['año'].max()}")
    print(f"   Provincias: {n_prov}")
    print(f"\n💾 Guardado: {archivo_salida}")
    
    # Resumen por variable
    print("\n📈 RESUMEN DE EVENTOS:")
    for col in count_cols:
        print(f"   {col}: {df_final[col].sum():,} total")

print("\n✅ COMPLETADO")
