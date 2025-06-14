# 📈 KAIM Week 1 – Sentiment & Stock Technical Indicator Analysis

This project explores the relationship between stock prices and news sentiment using quantitative analysis, technical indicators (like RSI, MACD), and machine learning.

---

## 🎯 Objective

Analyze sentiment-scored news and correlate it with Google stock technical indicators to classify next-day price movement.

---

## 📁 Project Structure

```
KAIM-week1-sentiment-stock Analysis/
├── data/                     # Raw & cleaned CSVs
├── notebooks/
│   └── task3_sentiment_analysis/
│       └── sentiment_analysis.ipynb
├── scripts/
│   ├── utils.py              # Reusable functions (load_csv, train_model, ensure_indicators)
│   └── indicators_talib.py   # TA-Lib-based indicator generation (optional)
├── reports/
│   └── interim_report_week1.md
├── requirements.txt
├── README.md
└── .github/
    └── workflows/
        └── test.yml          # GitHub Actions for notebook execution test
```

---

## ⚙️ How to Run

1. **Install Dependencies**

```bash
pip install -r requirements.txt
```

2. **Run Analysis**

```bash
jupyter notebook notebooks/task3_sentiment_analysis/sentiment_analysis.ipynb
```

3. **(Optional) Run from Python Script**

You can modularize and call the functions in `utils.py` from a separate script for automation.

---

## 🔁 CI/CD

GitHub Actions is configured to:
- Install requirements
- Execute the notebook as a test using:

```yaml
jupyter nbconvert --execute --to notebook notebooks/task3_sentiment_analysis/sentiment_analysis.ipynb
```

See `.github/workflows/test.yml` for config.

---

## 🧠 Technologies Used

- pandas, scikit-learn
- TA-Lib (optional)
- TextBlob / sentiment_score CSV
- GitHub Actions for CI

---

## ✅ Output

- Model classification report
- Notebook with annotated insights
- Technical indicator-enhanced dataset

---

## 🔍 Results Snapshot

- Classification accuracy: 0.74
- Most important feature: `MACD`
- Daily sentiment score correlates with next-day price movement by ~0.42 (Pearson)