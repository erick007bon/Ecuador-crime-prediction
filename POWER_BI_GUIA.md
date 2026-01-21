# 📊 Guía: Conectar Power BI con el Proyecto

## Opción 1: Conexión Directa a CSV (Más Simple)

### Paso 1: Abrir Power BI Desktop
- Si no lo tienes, descárgalo gratis de: https://powerbi.microsoft.com/

### Paso 2: Conectar al CSV
1. Clic en **Obtener datos** → **Texto/CSV**
2. Navegar a: `PROYECTOS/02_criminalidad_ecuador/`
3. Seleccionar: `dataset_final_limpio.csv`
4. Clic en **Cargar**

### Paso 3: Crear Visualizaciones
Ahora puedes crear:
- 📈 Gráfico de líneas: Homicidios por año
- 🗺️ Mapa: Homicidios por provincia
- 📊 Barras: Comparación entre provincias
- 📉 Tendencias: Evolución mensual

---

## Opción 2: Actualización Automática con Python

Para actualización automática, Power BI necesita conectarse a una fuente que se actualice.

### A) Usando Power BI + Script Python

1. En Power BI: **Obtener datos → Script Python**
2. Pegar este código:

```python
import pandas as pd
df = pd.read_csv(r"C:\Users\Erick Zambrano\Desktop\linkedin\PROYECTOS\02_criminalidad_ecuador\dataset_final_limpio.csv")
```

3. Power BI ejecutará el script cada vez que actualices

---

## Opción 3: API con FastAPI (Recomendado para Webapp)

Para conectar Power BI a una API:

1. **Crear API** (ya incluida en el proyecto webapp)
2. **Power BI → Obtener datos → Web**
3. **URL:** `http://localhost:8000/api/datos`

---

## 📊 Visualizaciones Recomendadas

| Visualización | Datos a usar |
|---------------|--------------|
| Línea temporal | año, mes, count_homicidios |
| Mapa de calor | provincia, count_homicidios |
| Tabla resumen | Todos los count_* |
| Indicador KPI | Total homicidios 2025 |
| Comparativo | count_armas vs count_homicidios |

---

## ⚠️ Para Actualización en Tiempo Real

Necesitas:
1. **Power BI Pro** (versión paga) para publicar
2. **Power BI Service** para programar actualizaciones
3. O bien, crear una **webapp** que muestre los datos (más flexible)

---

## 💡 Recomendación

Para LinkedIn, es mejor crear una **webapp** con Next.js/React que:
- Muestre los gráficos interactivamente
- Se actualice automáticamente
- Sea accesible desde cualquier navegador
- No requiera que el usuario tenga Power BI

¿Quieres que creemos la webapp en lugar de Power BI?
