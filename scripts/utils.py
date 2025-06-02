import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
import ta

def load_csv(filepath, date_column):
    try:
        return pd.read_csv(filepath, parse_dates=[date_column])
    except FileNotFoundError:
        print(f"[ERROR] File not found: {filepath}")
        return None

def train_model(df, features):
    df = df.dropna(subset=features + ["target"])
    X = df[features]
    y = df["target"]
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)
    clf = RandomForestClassifier()
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)
    report = classification_report(y_test, y_pred)
    return clf, report

def ensure_indicators(df):
    missing = []
    if "SMA_14" not in df.columns:
        df["SMA_14"] = ta.trend.sma_indicator(df["Close"], window=14)
        missing.append("SMA_14")
    if "RSI_14" not in df.columns:
        df["RSI_14"] = ta.momentum.rsi(df["Close"], window=14)
        missing.append("RSI_14")
    if "MACD" not in df.columns:
        df["MACD"] = ta.trend.macd(df["Close"])
        missing.append("MACD")
    if "MACD_Signal" not in df.columns:
        df["MACD_Signal"] = ta.trend.macd_signal(df["Close"])
        missing.append("MACD_Signal")
    
    if missing:
        print(f"[INFO] Computed missing indicators: {', '.join(missing)}")
    else:
        print("[INFO] All indicators already present.")
    return df