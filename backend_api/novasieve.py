import requests
import pandas as pd
from typing import List, Optional, Literal

def urljoin(*args):
    return '/'.join(args)

class NovaSieve:
    def __init__(self, URL: str):
        self.URL = URL
        self.screener = self.Screener(URL=self.URL)

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
            
            return pd.DataFrame(resp.json()).set_index("Date")

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
        