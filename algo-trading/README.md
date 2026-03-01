# Algo Trading (Trading Algorítmico) 📈

Esta carpeta contiene scripts y modelos de Machine Learning aplicados a los mercados financieros (Criptomonedas, Acciones, Forex).

## Proyectos Destacados

### 1. SMA Crossover Bot (`sma_crossover_bot.py`)
Un bot introductorio que utiliza una de las estrategias cuantitativas más clásicas: el Cruce de Medias Móviles Simples (SMA).
- Calcula dos medias móviles: rápida (ej. 5 periodos) y lenta (ej. 20 periodos).
- Genera señales de Compra cuando la media rápida cruza hacia arriba a la lenta.
- Genera señales de Venta cuando la media rápida cruza hacia abajo a la lenta.
- Incluye un módulo básico de **Backtesting** para probar la rentabilidad con datos históricos.

### Cómo ejecutarlo
Instala dependencias:
```bash
pip install pandas numpy
```

Ejecuta el bot:
```bash
python sma_crossover_bot.py
```

### Próximos pasos para escalar:
*   Conectar a la API de Binance o Alpaca Markets para datos en tiempo real.
*   Implementar modelos de Machine Learning (XGBoost) para predecir la dirección del precio.
*   Añadir manejo de riesgos avanzado (Stop Loss y Take Profit).
