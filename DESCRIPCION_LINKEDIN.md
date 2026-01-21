# 🔴 PREDICCIÓN DE CRIMINALIDAD EN ECUADOR
## Modelo de Machine Learning con 96.85% de Precisión

---

## 📋 INFORMACIÓN DEL PROYECTO

| Campo | Valor |
|-------|-------|
| **Nombre del proyecto** | Modelo Predictivo de Criminalidad en Ecuador |
| **Autor** | Erick Reinaldo Flores Zambrano |
| **Período de análisis** | 2014 - Noviembre 2025 |
| **URL Demo** | https://webapp-ten-cyan.vercel.app |
| **Tecnologías** | Python, XGBoost, Next.js, Vercel |

---

## 📝 DESCRIPCIÓN DETALLADA

### Resumen Ejecutivo

Desarrollé un sistema integral de predicción de criminalidad para Ecuador utilizando técnicas avanzadas de Machine Learning. El proyecto analiza más de **850,000 registros oficiales** del Ministerio del Interior de Ecuador, abarcando el período 2014-2025, para predecir homicidios intencionales a nivel provincial con una precisión del **96.85% (R²)**.

### Problemática Abordada

Ecuador ha experimentado un incremento alarmante en la tasa de homicidios, pasando de **5.7 por cada 100,000 habitantes en 2017** a **47.8 en 2025**, convirtiéndose en uno de los países más violentos de América Latina. Esta crisis de seguridad requiere herramientas predictivas que permitan anticipar tendencias y asignar recursos de manera eficiente.

### Objetivos del Proyecto

1. Desarrollar un modelo predictivo de alta precisión para homicidios mensuales por provincia
2. Identificar las variables más influyentes en la criminalidad
3. Crear un dashboard interactivo para visualización de datos y predicciones
4. Proporcionar una herramienta de apoyo para políticas de seguridad pública

---

## 🔬 METODOLOGÍA

### 1. Recolección y Procesamiento de Datos

**Fuentes de datos oficiales:**
- Ministerio del Interior de Ecuador (MDI)
- Policía Nacional del Ecuador
- Instituto Nacional de Estadística y Censos (INEC)

**Variables utilizadas:**
| Variable | Descripción | Registros |
|----------|-------------|-----------|
| Homicidios Intencionales | Muertes violentas por provincia/mes | 38,932 |
| Armas Incautadas | Decomisos de armas ilegales | 69,686 |
| Personas Desaparecidas | Casos reportados | 75,459 |
| Detenidos | Aprehensiones por delitos | 556,206 |
| Drogas Incautadas | Operativos antinarcóticos | 112,848 |

### 2. Feature Engineering

Se crearon variables adicionales para mejorar la capacidad predictiva:
- **Temporales:** Año, mes, trimestre, día de la semana
- **Rezagos (Lags):** Homicidios del mes anterior (lag_1, lag_2, lag_3)
- **Medias móviles:** Promedio de 3 y 6 meses
- **Geográficas:** Codificación one-hot de 24 provincias

### 3. Modelos Evaluados

Se entrenaron y compararon 4 algoritmos de Machine Learning:

| # | Modelo | R² | RMSE | MAE | MAPE |
|---|--------|-----|------|-----|------|
| 🥇 | **XGBoost** | **96.85%** | 2.71 | 1.15 | 27.35% |
| 🥈 | Random Forest | 95.32% | 3.31 | 1.35 | 25.52% |
| 🥉 | CatBoost | 91.55% | 4.45 | 2.31 | 57.44% |
| 4 | Ridge Regression | 90.45% | 4.73 | 0.94 | 18.87% |

### 4. Validación

- **Método:** División temporal 80/20 (entrenamiento: 2014-2023, prueba: 2024-2025)
- **Cross-validation:** 5-fold con métricas consistentes
- **Prevención de data leakage:** Split cronológico estricto

---

## 📊 RESULTADOS PRINCIPALES

### Precisión del Modelo

El modelo XGBoost logró predecir homicidios mensuales por provincia con un error promedio de solo **2.71 homicidios** (RMSE), lo que representa una precisión excepcional considerando la complejidad del fenómeno.

### Hallazgos Clave

1. **Guayas concentra el 47%** de los homicidios a nivel nacional
2. La tasa de homicidios creció **738%** entre 2017 y 2025 (de 5.7 a 47.8 por 100k)
3. **2023 fue el año más violento** con 8,248 homicidios
4. Las variables más predictivas son: armas incautadas, mes anterior (lag_1), y provincia

### Impacto Potencial

- Optimización de asignación de recursos policiales
- Alertas tempranas por incrementos proyectados
- Apoyo a políticas públicas de seguridad basadas en evidencia

---

## 💻 TECNOLOGÍAS UTILIZADAS

### Backend / Machine Learning
- **Python 3.10**
- **Pandas** - Procesamiento de datos
- **Scikit-learn** - Preprocesamiento y modelos base
- **XGBoost** - Modelo principal
- **CatBoost** - Modelo alternativo
- **Matplotlib/Seaborn** - Visualización

### Frontend / Dashboard
- **Next.js 14** - Framework React
- **TypeScript** - Tipado estático
- **Tailwind CSS** - Estilos
- **Vercel** - Despliegue en producción

### Estructura del Proyecto
```
02_criminalidad_ecuador/
├── datos_limpios/          # Datasets procesados
├── scripts/                # Scripts de limpieza y ML
│   ├── 00_procesar_todos.py
│   ├── 06_agregar_datos.py
│   └── 07_entrenar_modelos.py
├── webapp/                 # Aplicación Next.js
│   └── src/app/
│       ├── page.tsx        # Página principal
│       ├── dashboard/      # Dashboard interactivo
│       └── prediccion/     # Módulo de predicción
└── graficos_linkedin/      # Gráficos exportados
```

---

## 🌐 DEMO EN VIVO

**URL:** https://webapp-ten-cyan.vercel.app

**Funcionalidades:**
- ✅ Dashboard interactivo con filtros por año
- ✅ Visualización de evolución histórica
- ✅ Comparación de 4 modelos ML
- ✅ Estadísticas por provincia (click para detalles)
- ✅ Módulo de predicción por provincia/mes/año

---

## 📈 GRÁFICOS INCLUIDOS

1. **01_evolucion_homicidios.png** - Evolución 2014-2025 con barras y línea de tasa
2. **02_comparacion_modelos.png** - Benchmarking de 4 modelos ML
3. **03_top_provincias.png** - Top 10 provincias con mayor criminalidad
4. **04_metricas_xgboost.png** - Dashboard de métricas del mejor modelo
5. **05_real_vs_prediccion.png** - Validación real vs predicción 2024

---

## 🔗 COMPETENCIAS DEMOSTRADAS

- Machine Learning supervisado
- Feature Engineering avanzado
- Análisis exploratorio de datos (EDA)
- Desarrollo web full-stack (Next.js)
- Visualización de datos profesional
- Despliegue en producción (Vercel)
- Trabajo con datos gubernamentales reales

---

## 📞 CONTACTO

**Erick Reinaldo Flores Zambrano**
- 📧 Email: [tu email]
- 💼 LinkedIn: [tu perfil]
- 🌐 Demo: https://webapp-ten-cyan.vercel.app

---

*Proyecto desarrollado como parte del portafolio profesional en Data Science e Inteligencia Artificial.*
