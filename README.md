# 🐨 Daily Briefing Bot

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-Automated-green.svg)
![License](https://img.shields.io/badge/License-MIT-purple.svg)

> **Wake up to a smart, zero-cost daily digest.**  
> Automated weather, financial indices, and forex rates delivered straight to your inbox every morning.

---

## 📖 About

This project is a **serverless automation tool** designed to replace manual morning checks. It leverages **GitHub Actions** to run a Python script daily, fetching real-time data from various APIs, rendering a beautiful HTML email, and dispatching it via SMTP.

It is currently scheduled to run at **21:15 UTC** (Daily), which perfectly aligns with:
*   🇦🇺 **Melbourne Morning (07:15 / 08:15 AEDT)**
*   🇺🇸 **Post-Market Close (After 16:00 EST)**

## ✨ Features

*   **🌤️ Localized Weather**: Fetches real-time temperature, highs/lows, and weather conditions for your specific coordinates (via Open-Meteo).
*   **📉 Market Pulse**: Tracks key indices (SPY, QQQ, DIA, VIX) with "Green/Red" visual indicators for price changes.
*   **💱 Forex Watch**: Monitors AUD/CNY and AUD/USD exchange rates.
*   **🎨 HTML Template**: Sends a clean, mobile-responsive HTML email with a fun, randomized emoji title.
*   **🔒 Privacy First**: Your location (Latitude/Longitude) and credentials are stored securely in GitHub Secrets, never in the code.

---

## 📧 Snapshot

*What the email looks like:*

| **🐨 12 Jan 2026 Daily Briefing** |
| :--- |
| **🌤️ Weather (South Yarra)** |
| **22°C ⛅** (H: 26°C / L: 14°C) |
| |
| **📈 Market Indices** |
| **SPY** ....... $598.20 ... <span style="color:green">**+1.20%**</span> |
| **QQQ** ....... $402.50 ... <span style="color:red">**-0.45%**</span> |
| |
| **💱 Forex Rates** |
| **AUDCNY** .... 4.68 ...... <span style="color:gray">**0.00%**</span> |

---

## 🛠️ Deployment Guide

You don't need a server. Just fork this repo and configure the secrets.

### 1. Fork & Clone
Star ⭐ and Fork this repository to your own GitHub account.

### 2. Configure Secrets
Go to `Settings` -> `Secrets and variables` -> `Actions` -> `New repository secret`.
Add the following keys:

| Secret Key | Description | Example |
| :--- | :--- | :--- |
| `SMTP_SERVER` | SMTP Host | `smtp.gmail.com` |
| `SMTP_PORT` | SMTP Port | `465` |
| `SMTP_USER` | Your Email Address | `user@gmail.com` |
| `SMTP_PASSWORD` | **App Password** (Not login password) | `abcdefghijklmnop` |
| `RECEIVER_EMAIL` | Where to send the report | `user@gmail.com` |
| `LATITUDE` | Your Home Latitude | `-37.8136` |
| `LONGITUDE` | Your Home Longitude | `144.9631` |
| `LOCATION_NAME` | Display Name for Area | `Melbourne CBD` |

> **Note for Gmail Users:** You must enable 2-Step Verification and generate an **App Password** to use SMTP.

### 3. Schedule
The workflow is automatically scheduled in `.github/workflows/daily_schedule.yml`.
To test immediately, go to the **Actions** tab, select the workflow, and click **Run workflow**.

---

## 💻 Local Development

If you want to run this on your local machine (Mac/Windows/Linux):

1.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

2.  **Setup Environment:**
    Create a `.env` file in the root directory and fill in the variables listed in the "Secrets" section above.

3.  **Run:**
    ```bash
    python -m src.main
    ```

---

## ⚙️ Customization

Want to track different stocks? Open `src/config.py`:

```python
# Add your favorite tickers here
INDICES = ["TSLA", "AAPL", "BTC-USD"]

# Add your currency pairs
FOREX_PAIRS = ["EURUSD=X", "JPY=X"]