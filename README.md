# 🔍 Ecuador Crime Prediction - Machine Learning Analysis

<div align="center">

![Machine Learning](https://img.shields.io/badge/Machine%20Learning-XGBoost-blue?style=for-the-badge&logo=python)
![R² Score](https://img.shields.io/badge/R²%20Score-96.85%25-brightgreen?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3.10+-yellow?style=for-the-badge&logo=python)
![License](https://img.shields.io/badge/License-MIT-orange?style=for-the-badge)

**Análisis predictivo de criminalidad en Ecuador utilizando Machine Learning con datos del Ministerio del Interior (2014-2025)**

[🌐 Demo en Vivo](https://webapp-ten-cyan.vercel.app) | [📊 Datos](#-datos) | [📄 Documentación](#-documentación)

</div>

---

## 📋 Tabla de Contenidos

- [🎯 Descripción](#-descripción)
- [📊 Resultados](#-resultados)
- [🗂️ Estructura del Proyecto](#️-estructura-del-proyecto)
- [🚀 Instalación](#-instalación)
- [💻 Uso](#-uso)
- [🌐 Web App](#-web-app)
- [📈 Datos](#-datos)
- [🔬 Metodología](#-metodología)
- [📉 Hallazgos Clave](#-hallazgos-clave)
- [🤝 Contribución](#-contribución)
- [📄 Licencia](#-licencia)
- [📖 Citar este trabajo](#-citar-este-trabajo)
- [👤 Autor](#-autor)

---

## 🎯 Descripción

Este proyecto analiza y predice patrones de criminalidad en Ecuador utilizando técnicas de **Machine Learning**. Procesando más de **850,000 registros** del Ministerio del Interior, el modelo puede predecir tendencias de homicidios con alta precisión.

### ¿Por qué es importante?

- 🇪🇨 **Ecuador enfrenta una crisis de seguridad** sin precedentes
- 📈 La tasa de homicidios pasó de **5.7** (2017) a **47.8** (2025) por 100,000 habitantes
- 🔍 El análisis de datos puede ayudar a **anticipar** y **prevenir** crímenes
- 📊 Herramienta para **tomadores de decisiones** en políticas públicas

---

## 📊 Resultados

### Comparación de Modelos ML

| # | Modelo | R² | RMSE | MAE | MAPE |
|---|--------|-----|------|-----|------|
| 🥇 | **XGBoost** | **96.85%** | 2.71 | 1.15 | 27.35% |
| 🥈 | Random Forest | 95.32% | 3.31 | 1.35 | 25.52% |
| 🥉 | CatBoost | 91.55% | 4.45 | 2.31 | 57.44% |
| 4 | Ridge Regression | 90.45% | 4.73 | 0.94 | 18.87% |

### Configuración

| Parámetro | Valor |
|-----------|-------|
| Validación | Train 80% / Test 20% |
| Registros procesados | +850,000 |
| Período | 2014 - Noviembre 2025 |
| Variables | Homicidios, armas, desaparecidos, detenidos, drogas |

---

## 🗂️ Estructura del Proyecto

```
ecuador-crime-prediction/
├── 📁 scripts/
│   ├── 00_procesar_todos.py      # Limpieza de datos
│   ├── 06_agregar_datos.py       # Agregación
│   ├── 07_entrenar_modelos.py    # Entrenamiento ML
│   └── generar_graficos_linkedin.py  # Gráficos para redes
├── 📁 datos_limpios/
│   └── [datasets procesados]
├── 📁 modelos/
│   └── [modelos entrenados .pkl]
├── 📁 graficos_linkedin/
│   └── [visualizaciones PNG]
├── 📁 webapp/
│   ├── 📁 src/app/
│   │   ├── page.tsx              # Landing page
│   │   ├── dashboard/page.tsx    # Dashboard interactivo
│   │   └── prediccion/page.tsx   # Módulo de predicción
│   └── package.json
├── dataset_final_agregado.csv    # Dataset principal
├── LICENSE                       # Licencia MIT
├── CITATION.cff                  # Archivo de citación
└── README.md                     # Este archivo
```

---

## 🚀 Instalación

### Requisitos Previos

- Python 3.10 o superior
- Node.js 18+ (para la web app)
- pip (gestor de paquetes)

### Clonar Repositorio

```bash
git clone https://github.com/erick007bon/cuador-crime-prediction.git
cd cuador-crime-prediction
```

### Instalar Dependencias Python

```bash
pip install pandas numpy scikit-learn xgboost catboost matplotlib seaborn
```

### Para la Web App (Next.js)

```bash
cd webapp
npm install
npm run dev
```

---

## 💻 Uso

### Entrenar Modelos

```bash
python scripts/07_entrenar_modelos.py
```

### Generar Gráficos

```bash
python scripts/generar_graficos_linkedin.py
```

### Procesar Datos Nuevos

```bash
python scripts/00_procesar_todos.py
```

---

## 🌐 Web App

### Demo en Vivo

🔗 **https://webapp-ten-cyan.vercel.app**

### Páginas

| Página | Descripción |
|--------|-------------|
| `/` | Landing con gráfico combinado y tabla de modelos |
| `/dashboard` | Dashboard interactivo con filtros por año y provincia |
| `/prediccion` | Módulo de predicción por provincia/mes/año |

---

## 📈 Datos

### Fuente

Los datos provienen del **Ministerio del Interior del Ecuador** y son información pública.

| Campo | Valor |
|-------|-------|
| **Fuente** | Ministerio del Interior del Ecuador |
| **Período** | 2014 - Noviembre 2025 |
| **Registros** | +850,000 |
| **Variables** | Homicidios, armas de fuego, personas desaparecidas, detenidos, drogas incautadas |

### Variables Analizadas

- Homicidios intencionales
- Uso de armas de fuego
- Personas desaparecidas
- Personas detenidas
- Drogas incautadas
- Distribución por provincia
- Tendencias temporales

---

## 🔬 Metodología

### 1. Limpieza de Datos
- Unificación de datasets del MDI
- Estandarización de nombres de provincias
- Manejo de valores faltantes

### 2. Feature Engineering
- Agregación por año/mes/provincia
- Cálculo de tasas por 100,000 habitantes
- Variables derivadas temporales

### 3. Modelado
- División 80/20 (train/test)
- Comparación de 4 algoritmos
- Validación cruzada
- Optimización de hiperparámetros

### 4. Evaluación
- R² Score
- RMSE (Root Mean Square Error)
- MAE (Mean Absolute Error)
- MAPE (Mean Absolute Percentage Error)

---

## 📉 Hallazgos Clave

### Estadísticas Alarmantes

| Hallazgo | Valor |
|----------|-------|
| **Guayas concentra** | 47% de homicidios nacionales |
| **2023** | Año más violento: 8,248 homicidios |
| **2025 (Nov)** | 8,393 homicidios (superó récord) |
| **Tasa 2017 → 2025** | 5.7 → 47.8 por 100,000 hab. |

### Provincias más Afectadas

1. 🥇 Guayas (Guayaquil)
2. 🥈 Manabí
3. 🥉 Los Ríos
4. Esmeraldas
5. El Oro

---

## 🤝 Contribución

Las contribuciones son bienvenidas:

1. Fork del repositorio
2. Crear rama (`git checkout -b feature/nueva-funcionalidad`)
3. Commit (`git commit -m 'Agregar funcionalidad'`)
4. Push (`git push origin feature/nueva-funcionalidad`)
5. Abrir Pull Request

---

## 📄 Licencia

Este proyecto está bajo la **Licencia MIT**. Ver [LICENSE](LICENSE).

### Resumen

- ✅ Uso comercial permitido
- ✅ Modificación permitida
- ✅ Distribución permitida
- ⚠️ **Atribución requerida** (debes citar al autor)
- ⚠️ Los datos tienen su propia licencia (datos públicos del gobierno)

---

## 📖 Citar este Trabajo

### Formato BibTeX

```bibtex
@software{flores_ecuador_crime_2026,
  author = {Flores Zambrano, Erick Reinaldo},
  title = {Ecuador Crime Prediction: Machine Learning Analysis of Criminal Activity},
  year = {2026},
  url = {https://github.com/erick007bon/cuador-crime-prediction},
  version = {1.0.0}
}
```

### Formato APA

```
Flores Zambrano, E. R. (2026). Ecuador Crime Prediction: Machine Learning 
Analysis of Criminal Activity (Version 1.0.0) [Computer software]. 
https://github.com/erick007bon/cuador-crime-prediction
```

---

## 👤 Autor

<div align="center">

**Erick Reinaldo Flores Zambrano**

Estudiante de Economía | Universidad Técnica de Manabí

[![GitHub](https://img.shields.io/badge/GitHub-erick007bon-181717?style=for-the-badge&logo=github)](https://github.com/erick007bon)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Erick%20Flores-0A66C2?style=for-the-badge&logo=linkedin)](https://linkedin.com)

🇪🇨 Ecuador | 2026

</div>

---

<div align="center">

### ⭐ Si este proyecto te fue útil, ¡dale una estrella!

**#MachineLearning #DataScience #Ecuador #CrimeAnalysis #XGBoost**

</div>
