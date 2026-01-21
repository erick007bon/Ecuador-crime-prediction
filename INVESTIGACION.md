# 🔴 PROYECTO: Predicción de Muertes Violentas en Ecuador

**Fecha:** 2026-01-13  
**Estado:** 📋 Investigación Inicial

---

## 📊 CONTEXTO: LA CRISIS DE SEGURIDAD EN ECUADOR

### Datos Duros (Fuentes Oficiales - Policía Nacional / Fiscalía):

| Año | Homicidios | Tasa x 100k hab | Cambio vs anterior |
|-----|------------|-----------------|-------------------|
| 2023 | ~8,248 | 46.18 | +75% vs 2022 |
| 2024 | ~6,964 | 38.76 | -16% vs 2023 |
| 2025 | ~9,300+ | 51+ | +47% vs 2024 |

> **Ecuador es actualmente el país más violento de América Latina** (superando a Venezuela y Honduras)

### Provincias más afectadas (83% de homicidios):
1. **Guayas** (Guayaquil) - Epicentro
2. **Manabí**
3. **Los Ríos**
4. **El Oro** (Machala - tu ciudad)
5. **Esmeraldas**

---

## 🎯 ENFOQUE DEL PROYECTO

### Pregunta de Investigación:
> "¿Es posible predecir la tasa de homicidios mensual por provincia en Ecuador usando variables socioeconómicas, demográficas y contextuales?"

### Variable Objetivo (Y):
- **Homicidios mensuales por provincia** (o tasa x 100k habitantes)

---

## 📈 VARIABLES PREDICTORAS (PROPUESTA)

### Grupo 1: Variables Socioeconómicas
| Variable | Descripción | Fuente |
|----------|-------------|--------|
| X1 | Tasa de desempleo | INEC / BCE |
| X2 | Pobreza por NBI (%) | INEC |
| X3 | Coeficiente de Gini (desigualdad) | INEC / Banco Mundial |
| X4 | PIB provincial | BCE |
| X5 | Salario promedio | INEC |

### Grupo 2: Variables Demográficas
| Variable | Descripción | Fuente |
|----------|-------------|--------|
| X6 | Población total | INEC |
| X7 | % Población joven (15-29 años) | INEC |
| X8 | Densidad poblacional | INEC |
| X9 | Tasa de urbanización | INEC |

### Grupo 3: Variables de Seguridad/Justicia
| Variable | Descripción | Fuente |
|----------|-------------|--------|
| X10 | # Policías por habitante | Min. Interior |
| X11 | Tasa de encarcelamiento | Fiscalía |
| X12 | # Denuncias previas | Fiscalía |
| X13 | Incautaciones de droga | Policía |

### Grupo 4: Variables Contextuales
| Variable | Descripción | Fuente |
|----------|-------------|--------|
| X14 | Mes del año (estacionalidad) | - |
| X15 | Homicidios rezagados (lag-1, lag-2) | Serie temporal |
| X16 | Presencia de puertos/fronteras | Geográfico |

---

## 📁 FUENTES DE DATOS OFICIALES

1. **Ministerio del Interior - Datos Abiertos**
   - https://datosabiertos.gob.ec
   - Homicidios por provincia (mensual)

2. **INEC - Instituto Nacional de Estadísticas**
   - Proyecciones poblacionales
   - Encuesta de empleo
   - Pobreza y desigualdad

3. **OECO - Observatorio Ecuatoriano de Crimen Organizado**
   - Boletines trimestrales con datos detallados
   - Desgloses por provincia y cantón

4. **Fiscalía General del Estado**  
   - https://www.fiscalia.gob.ec
   - Datos de denuncias y casos

5. **Banco Central del Ecuador**
   - PIB, empleo, indicadores económicos

---

## 🤖 METODOLOGÍA PROPUESTA

### Modelos a evaluar:
1. **Random Forest** - Robusto, interpretable
2. **XGBoost/CatBoost** - Alto rendimiento
3. **LSTM/GRU** - Para capturar patrones temporales
4. **Regresión Lineal** - Baseline interpretable

### Métricas:
- R² (explicación de varianza)
- RMSE (error cuadrático medio)
- MAE (error absoluto medio)
- MAPE (error porcentual)

### Validación:
- Train/Test split 80/20
- Cross-validation temporal (no aleatorio)

---

## ⚠️ CONSIDERACIONES ÉTICAS

1. Este proyecto es **SOLO PARA FINES ACADÉMICOS**
2. No se usará para estigmatizar provincias o poblaciones
3. El objetivo es entender patrones, NO señalar culpables
4. Datos agregados, nunca datos personales

---

## 📋 PRÓXIMOS PASOS

- [ ] Confirmar enfoque con el usuario
- [ ] Descargar datos de datosabiertos.gob.ec
- [ ] Recopilar variables socioeconómicas del INEC
- [ ] Integrar dataset unificado
- [ ] Entrenar modelos
- [ ] Crear webapp de visualización

---

**Tutor:** Gemini-Antigravity
