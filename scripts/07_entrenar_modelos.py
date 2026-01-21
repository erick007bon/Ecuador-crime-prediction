"""
SCRIPT 07: ENTRENAR MODELOS ML PARA PREDICCIÓN DE CRIMINALIDAD
================================================================
Modelos: XGBoost, CatBoost, Random Forest, Ridge
Variable objetivo: count_homicidios (homicidios por mes/provincia)
"""

import pandas as pd
import numpy as np
import os
import pickle
from datetime import datetime

# Modelos
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.linear_model import Ridge
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

# Verificar instalación de XGBoost y CatBoost
try:
    import xgboost as xgb
    XGBOOST_OK = True
except ImportError:
    XGBOOST_OK = False
    print("⚠️ XGBoost no instalado - pip install xgboost")

try:
    from catboost import CatBoostRegressor
    CATBOOST_OK = True
except ImportError:
    CATBOOST_OK = False
    print("⚠️ CatBoost no instalado - pip install catboost")

import warnings
warnings.filterwarnings('ignore')

# Rutas
RUTA_DATOS = r"C:\Users\Erick Zambrano\Desktop\linkedin\PROYECTOS\02_criminalidad_ecuador\dataset_final_limpio.csv"
RUTA_SALIDA = r"C:\Users\Erick Zambrano\Desktop\linkedin\PROYECTOS\02_criminalidad_ecuador\modelos"
os.makedirs(RUTA_SALIDA, exist_ok=True)

print("=" * 80)
print("🤖 ENTRENAMIENTO DE MODELOS ML - PREDICCIÓN DE CRIMINALIDAD")
print("=" * 80)
print(f"Inicio: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

# ============================================================================
# PASO 1: CARGAR Y PREPARAR DATOS
# ============================================================================
print("\n📁 Cargando datos...")

df = pd.read_csv(RUTA_DATOS)
print(f"   Dimensiones: {df.shape[0]:,} filas x {df.shape[1]} columnas")

# Variable objetivo
TARGET = 'count_homicidios'

# Features a usar
FEATURES_NUMERICAS = [
    'año', 'mes', 'trimestre',
    'count_armas', 'count_desaparecidos', 'count_detenidos',
    'poblacion'
]

# Verificar qué columnas existen
features_disponibles = [f for f in FEATURES_NUMERICAS if f in df.columns]
print(f"\n📋 Features disponibles: {features_disponibles}")

# Limpiar datos
df = df.dropna(subset=[TARGET] + features_disponibles)
print(f"   Después de limpiar NaN: {df.shape[0]:,} filas")

# Crear features adicionales
if 'provincia' in df.columns:
    # Codificar provincia
    le = LabelEncoder()
    df['provincia_cod'] = le.fit_transform(df['provincia'].astype(str))
    features_disponibles.append('provincia_cod')
    
    # Guardar encoder
    with open(os.path.join(RUTA_SALIDA, 'label_encoder_provincia.pkl'), 'wb') as f:
        pickle.dump(le, f)

# Crear lag features (mes anterior)
df = df.sort_values(['provincia', 'año', 'mes']).reset_index(drop=True)
df['homicidios_lag1'] = df.groupby('provincia')[TARGET].shift(1)
df['homicidios_lag2'] = df.groupby('provincia')[TARGET].shift(2)
df['homicidios_lag3'] = df.groupby('provincia')[TARGET].shift(3)

# Media móvil
df['homicidios_ma3'] = df.groupby('provincia')[TARGET].transform(lambda x: x.rolling(3, min_periods=1).mean())

# Agregar lags a features
for lag_col in ['homicidios_lag1', 'homicidios_lag2', 'homicidios_lag3', 'homicidios_ma3']:
    if lag_col in df.columns:
        features_disponibles.append(lag_col)

# Rellenar NaN de lags con 0
df = df.fillna(0)

print(f"\n📊 Features finales: {len(features_disponibles)}")
for f in features_disponibles:
    print(f"   - {f}")

# ============================================================================
# PASO 2: SPLIT TRAIN/TEST (Temporal)
# ============================================================================
print("\n" + "=" * 80)
print("📊 DIVIDIENDO DATOS (80% train / 20% test)")
print("=" * 80)

X = df[features_disponibles]
y = df[TARGET]

# Split temporal (últimos datos para test)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, shuffle=False
)

print(f"   Train: {X_train.shape[0]:,} filas")
print(f"   Test:  {X_test.shape[0]:,} filas")

# Escalar para modelos lineales
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Guardar scaler
with open(os.path.join(RUTA_SALIDA, 'scaler.pkl'), 'wb') as f:
    pickle.dump(scaler, f)

# ============================================================================
# PASO 3: ENTRENAR MODELOS
# ============================================================================
print("\n" + "=" * 80)
print("🤖 ENTRENANDO MODELOS")
print("=" * 80)

resultados = []

def evaluar_modelo(nombre, y_true, y_pred):
    """Calcula métricas de evaluación"""
    rmse = np.sqrt(mean_squared_error(y_true, y_pred))
    mae = mean_absolute_error(y_true, y_pred)
    r2 = r2_score(y_true, y_pred)
    # MAPE (evitar división por 0)
    mask = y_true != 0
    if mask.sum() > 0:
        mape = np.mean(np.abs((y_true[mask] - y_pred[mask]) / y_true[mask])) * 100
    else:
        mape = 0
    
    return {
        'modelo': nombre,
        'R2': round(r2 * 100, 2),
        'RMSE': round(rmse, 2),
        'MAE': round(mae, 2),
        'MAPE': round(mape, 2)
    }

# 1. RIDGE REGRESSION
print("\n🔹 Entrenando Ridge Regression...")
ridge = Ridge(alpha=1.0, random_state=42)
ridge.fit(X_train_scaled, y_train)
y_pred_ridge = ridge.predict(X_test_scaled)
resultados.append(evaluar_modelo('Ridge Regression', y_test.values, y_pred_ridge))
print(f"   ✅ R²: {resultados[-1]['R2']}%")

with open(os.path.join(RUTA_SALIDA, 'modelo_ridge.pkl'), 'wb') as f:
    pickle.dump(ridge, f)

# 2. RANDOM FOREST
print("\n🔹 Entrenando Random Forest...")
rf = RandomForestRegressor(
    n_estimators=100,
    max_depth=10,
    min_samples_split=5,
    random_state=42,
    n_jobs=-1
)
rf.fit(X_train, y_train)
y_pred_rf = rf.predict(X_test)
resultados.append(evaluar_modelo('Random Forest', y_test.values, y_pred_rf))
print(f"   ✅ R²: {resultados[-1]['R2']}%")

with open(os.path.join(RUTA_SALIDA, 'modelo_random_forest.pkl'), 'wb') as f:
    pickle.dump(rf, f)

# 3. XGBOOST
if XGBOOST_OK:
    print("\n🔹 Entrenando XGBoost...")
    xgb_model = xgb.XGBRegressor(
        n_estimators=100,
        max_depth=6,
        learning_rate=0.1,
        random_state=42,
        n_jobs=-1
    )
    xgb_model.fit(X_train, y_train)
    y_pred_xgb = xgb_model.predict(X_test)
    resultados.append(evaluar_modelo('XGBoost', y_test.values, y_pred_xgb))
    print(f"   ✅ R²: {resultados[-1]['R2']}%")
    
    with open(os.path.join(RUTA_SALIDA, 'modelo_xgboost.pkl'), 'wb') as f:
        pickle.dump(xgb_model, f)
else:
    print("\n⚠️ XGBoost no disponible")

# 4. CATBOOST
if CATBOOST_OK:
    print("\n🔹 Entrenando CatBoost...")
    cat_model = CatBoostRegressor(
        iterations=100,
        depth=6,
        learning_rate=0.1,
        random_seed=42,
        verbose=0
    )
    cat_model.fit(X_train, y_train)
    y_pred_cat = cat_model.predict(X_test)
    resultados.append(evaluar_modelo('CatBoost', y_test.values, y_pred_cat))
    print(f"   ✅ R²: {resultados[-1]['R2']}%")
    
    cat_model.save_model(os.path.join(RUTA_SALIDA, 'modelo_catboost.cbm'))
else:
    print("\n⚠️ CatBoost no disponible")

# ============================================================================
# PASO 4: COMPARAR RESULTADOS
# ============================================================================
print("\n" + "=" * 80)
print("📊 COMPARACIÓN DE MODELOS")
print("=" * 80)

df_resultados = pd.DataFrame(resultados)
df_resultados = df_resultados.sort_values('R2', ascending=False).reset_index(drop=True)

print("\n" + df_resultados.to_string(index=False))

# Mejor modelo
mejor = df_resultados.iloc[0]
print(f"\n🏆 MEJOR MODELO: {mejor['modelo']}")
print(f"   R²:   {mejor['R2']}%")
print(f"   RMSE: {mejor['RMSE']}")
print(f"   MAE:  {mejor['MAE']}")
print(f"   MAPE: {mejor['MAPE']}%")

# Guardar resultados
df_resultados.to_csv(os.path.join(RUTA_SALIDA, 'comparacion_modelos.csv'), index=False)

# ============================================================================
# PASO 5: FEATURE IMPORTANCE (mejor modelo tree-based)
# ============================================================================
print("\n" + "=" * 80)
print("📊 IMPORTANCIA DE VARIABLES (Random Forest)")
print("=" * 80)

importancia = pd.DataFrame({
    'feature': features_disponibles,
    'importance': rf.feature_importances_
}).sort_values('importance', ascending=False)

print(importancia.to_string(index=False))

importancia.to_csv(os.path.join(RUTA_SALIDA, 'feature_importance.csv'), index=False)

# ============================================================================
# RESUMEN FINAL
# ============================================================================
print("\n" + "=" * 80)
print("✅ ENTRENAMIENTO COMPLETADO")
print("=" * 80)

print(f"\n📁 Modelos guardados en: {RUTA_SALIDA}")
print(f"   - modelo_ridge.pkl")
print(f"   - modelo_random_forest.pkl")
if XGBOOST_OK:
    print(f"   - modelo_xgboost.pkl")
if CATBOOST_OK:
    print(f"   - modelo_catboost.cbm")
print(f"   - comparacion_modelos.csv")
print(f"   - feature_importance.csv")

print(f"\n⏰ Fin: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
