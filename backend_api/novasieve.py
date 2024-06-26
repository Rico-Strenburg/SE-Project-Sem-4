import requests
import pandas as pd
from typing import List, Optional, Literal

def urljoin(*args):
    return '/'.join(args)

class NovaSieve:
    def __init__(self, URL: str):
        self.URL = URL
        self.screener = self.Screener(URL=self.URL)
        self.backtest = self.Backtest(URL=self.URL)
        self.stock_list = self.Stock(URL=self.URL)

    class Screener:
        def __init__(self, URL: str):
            self.URL = urljoin(URL, "screener")
            self.SCREEN_URL = urljoin(self.URL, "screen")
            self.TA_URL = urljoin(self.URL, "technical_analysis")
            self.FA_URL = urljoin(self.URL, "fundamental_analysis")

        def screen(self, symbols: List[str], time_period: str, variables: List[dict], rules: List[dict]) -> pd.DataFrame:
            screener_payload = {
                "symbols": symbols,
                "time_period": time_period,
                "variables": variables,
                "rules": rules
            }

            resp = requests.post(self.SCREEN_URL, json=screener_payload)
            if resp.status_code != 200:
                raise Exception(f"Error got status code {resp.status_code}")
            
            res_df = pd.DataFrame(resp.json())
            if "Datetime" not in res_df.columns:
                res_df.rename(columns={"index": "Datetime", "Date": "Datetime"}, inplace=True)
        
            return res_df.set_index("Datetime")
        
        def get_technical_analysis(self) -> dict:
            resp = requests.get(self.TA_URL)
            return resp.json()

        def get_fundamental_analysis(self) -> dict:
            resp = requests.get(self.FA_URL)
            return resp.json()
        
        def check_analysis_method_category(self, variable_type: Literal['technical', 'fundamental'], method_name: str) -> Optional[str]:
            if variable_type == "technical":
                analysis_category = self.get_technical_analysis()
            elif variable_type == "fundamental":
                analysis_category = self.get_fundamental_analysis()
            else:
                return None
            
            for cat, methods in analysis_category.items():
                if method_name in methods:
                    return cat
            return None
        
    class Backtest:
        def __init__(self, URL: str):
            self.URL = urljoin(URL, "backtest")
            self.BACKTEST_URL = urljoin(self.URL, "backtest")

        def backtest(
            self, symbols: List[str], start_time_period: str, end_time_period: str, variables: List[str], rules: List[dict],
            trading_style:str, stoploss:str
            ) -> pd.DataFrame:
            backtest_payload = {
                "symbols": symbols,
                "start_period": start_time_period,
                "end_period": end_time_period,
                "variables": variables,
                "rules": rules,
                "trading_style": trading_style,
                # "stoploss": stoploss
            }
            # Logic to call backtest API
            resp = requests.post(self.BACKTEST_URL, json=backtest_payload)
            if resp.status_code != 200:
                raise Exception(f"Error got status code {resp.status_code}")
            
            return pd.DataFrame(resp.json()).T

        
    class Stock:
        def __init__(self, URL: str):
            self.URL = urljoin(URL, "stock")
            self.IDX_STOCKS = urljoin(self.URL, "IDX", "list")
        
        def get_idx_stock_list(self) -> dict:
            resp = requests.get(self.IDX_STOCKS)
            return {f"{code.replace('IDX:', '')}.JK": name for code, name in resp.json().items()}