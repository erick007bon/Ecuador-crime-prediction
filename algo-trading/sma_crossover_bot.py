import pandas as pd
import numpy as np

class SMACrossoverBot:
    """
    Un bot de trading simple (MVP) basado en el Cruce de Medias Móviles Simples (SMA).

    Esta estrategia genera una señal de compra cuando una Media Móvil Corta
    cruza por encima de una Media Móvil Larga. Genera una señal de venta
    cuando la Corta cruza por debajo de la Larga.
    """
    def __init__(self, short_window=10, long_window=30):
        self.short_window = short_window
        self.long_window = long_window

    def generate_signals(self, data):
        """
        Genera las señales de trading (Compra/Venta) basándose en los datos históricos.

        Args:
            data (pd.DataFrame): DataFrame con precios históricos. Debe tener una columna 'Close'.

        Returns:
            pd.DataFrame: DataFrame original con las señales y medias móviles agregadas.
        """
        if 'Close' not in data.columns:
            raise ValueError("El DataFrame debe contener la columna 'Close'")

        # Calcular las medias móviles
        data['SMA_Short'] = data['Close'].rolling(window=self.short_window, min_periods=1).mean()
        data['SMA_Long'] = data['Close'].rolling(window=self.long_window, min_periods=1).mean()

        # Inicializar la señal a 0
        data['Signal'] = 0.0

        # Crear la señal: 1 cuando la corta es mayor a la larga, 0 de lo contrario
        # Ignoramos el inicio donde la media larga aún no se calcula bien
        data.loc[data.index[self.short_window:], 'Signal'] = np.where(
            data['SMA_Short'][self.short_window:] > data['SMA_Long'][self.short_window:], 1.0, 0.0
        )

        # Generar las posiciones de trading (diferencia entre señales)
        # 1.0 es una señal de COMPRA, -1.0 es una señal de VENTA
        data['Position'] = data['Signal'].diff()

        return data

    def backtest(self, data, initial_capital=10000.0, shares_per_trade=100):
        """
        Simula la ejecución de la estrategia en los datos históricos.

        Args:
            data (pd.DataFrame): Datos con señales ya generadas por `generate_signals`.
            initial_capital (float): Capital inicial en dólares.
            shares_per_trade (int): Cantidad de acciones/monedas a comprar/vender por operación.

        Returns:
            pd.DataFrame: El portafolio final con la curva de capital.
        """
        if 'Position' not in data.columns:
            raise ValueError("Ejecuta 'generate_signals' primero.")

        positions = pd.DataFrame(index=data.index).fillna(0.0)

        # Compramos `shares_per_trade` cada vez que hay señal (1).
        # Como Position es 1 en compra y -1 en venta, multiplicamos por las acciones.
        # Pero Signal nos dice si estamos dentro (1) o fuera (0).
        positions['Asset'] = shares_per_trade * data['Signal']

        # Calcular el valor de nuestras acciones
        portfolio = positions.multiply(data['Close'], axis=0)

        # Calcular la diferencia en las acciones para ver cuánto gastamos/ganamos
        pos_diff = positions.diff()

        # Añadir el efectivo
        portfolio['Cash'] = initial_capital - (pos_diff.multiply(data['Close'], axis=0)).cumsum()

        # Total
        portfolio['Total'] = portfolio['Asset'] + portfolio['Cash']

        return portfolio

if __name__ == "__main__":
    print("--- 🤖 Iniciando MVP de Algorithmic Trading: SMA Crossover ---")

    # 1. Crear datos falsos simulando el precio de una acción
    fechas = pd.date_range(start="2023-01-01", periods=100)
    # Precio base 100 con un paseo aleatorio
    np.random.seed(42)
    precios = 100 + np.random.randn(100).cumsum()

    df = pd.DataFrame({'Close': precios}, index=fechas)
    print(f"✅ Generados {len(df)} días de datos históricos simulados.")

    # 2. Inicializar el Bot
    bot = SMACrossoverBot(short_window=5, long_window=20)

    # 3. Generar Señales
    df_signals = bot.generate_signals(df.copy())
    compras = df_signals[df_signals['Position'] == 1.0].shape[0]
    ventas = df_signals[df_signals['Position'] == -1.0].shape[0]
    print(f"📈 Señales de COMPRA generadas: {compras}")
    print(f"📉 Señales de VENTA generadas: {ventas}")

    # 4. Backtesting
    print("💰 Ejecutando Backtesting con capital inicial de $10,000...")
    portfolio = bot.backtest(df_signals, initial_capital=10000.0, shares_per_trade=10)

    capital_final = portfolio['Total'].iloc[-1]
    retorno = ((capital_final - 10000.0) / 10000.0) * 100

    print(f"📊 Capital Final: ${capital_final:.2f}")
    print(f"🚀 Retorno de la estrategia: {retorno:.2f}%")

    print("\nEste script es un MVP. En la vida real conectarías esto a una API (ej. Binance, Alpaca) para descargar datos reales y enviar las órdenes.")
