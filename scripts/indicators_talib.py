import pandas as pd
import talib

# ✅ Load your real stock data
df = pd.read_csv('data/cleaned_GOOG_historical_data.csv', parse_dates=['Date'])

# ✅ Set 'Date' as index
df.set_index('Date', inplace=True)

# ✅ Check required columns exist
required_cols = ['Open', 'High', 'Low', 'Close', 'Volume']
for col in required_cols:
    if col not in df.columns:
        raise ValueError(f"Missing required column: {col}")

# ✅ Calculate technical indicators
df['SMA_20'] = talib.SMA(df['Close'], timeperiod=20)
df['RSI_14'] = talib.RSI(df['Close'], timeperiod=14)
macd, macd_signal, macd_hist = talib.MACD(df['Close'])
df['MACD'] = macd
df['MACD_signal'] = macd_signal
df['MACD_hist'] = macd_hist

# ✅ Save result
df.to_csv('data/GOOG_with_technical_indicators.csv')

print("✅ Technical indicators saved to 'data/GOOG_with_technical_indicators.csv'")