import yfinance as yf
import pandas as pd
from typing import List, Dict, Any
from src.config import Config

def fetch_finance_data(tickers: List[str]) -> List[Dict[str, Any]]:
    results = []
    if not tickers: return results

    print(f"📉 Fetching data for: {tickers}...")
    
    try:
        data = yf.download(tickers, period="5d", progress=False, threads=False)
    except Exception as e:
        print(f"⚠️ Critical Error: {e}")
        return results

    if data is None or data.empty:
        for ticker in tickers:
            display_symbol = ticker.replace("=X", "")
            results.append({"symbol": display_symbol, "price": "N/A", "change_percent": 0.0, "date": "-"})
        return results

    for ticker in tickers:
        display_symbol = ticker.replace("=X", "")
        item = {"symbol": display_symbol, "price": "N/A", "change_percent": 0.0, "date": "-"}
        
        try:
            if len(tickers) == 1:
                if 'Close' in data.columns: series = data['Close']
                else: raise ValueError("Column 'Close' not found")
            else:
                if 'Close' in data.columns and ticker in data['Close'].columns:
                    series = data['Close'][ticker]
                else:
                    raise ValueError(f"Ticker {ticker} not found")

            series = series.dropna()
            
            # [UPDATED] Date format changed to '11 Jan 2026' (%d %b %Y)
            if len(series) < 2:
                if len(series) == 1:
                    item["price"] = round(float(series.iloc[-1]), 2)
                    item["date"] = series.index[-1].strftime('%d %b %Y')
            else:
                current_price = float(series.iloc[-1])
                prev_close = float(series.iloc[-2])
                change = ((current_price - prev_close) / prev_close) * 100
                
                item["price"] = round(current_price, 2)
                item["change_percent"] = round(change, 2)
                item["date"] = series.index[-1].strftime('%d %b %Y')
            
        except Exception as e:
            print(f"⚠️ Error processing {ticker}: {e}")
        
        results.append(item)
            
    return results

def fetch_all_finance():
    indices_data = fetch_finance_data(Config.INDICES) if Config.INDICES else []
    forex_data = fetch_finance_data(Config.FOREX_PAIRS) if Config.FOREX_PAIRS else []
    return indices_data, forex_data