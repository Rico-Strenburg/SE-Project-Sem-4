from .novasieve import NovaSieve

BACKEND_API_URL = "http://127.0.0.1:8000"

novasieve = NovaSieve(BACKEND_API_URL)

analysis_options = {
    "technical": {method_code: f"{method_info['name']} [{cat.title().replace('_', ' ')}]" for cat, methods in novasieve.screener.get_technical_analysis().items() for method_code, method_info in methods.items()},
    "fundamental": {method_code: f"{method_info['name']} [{cat.title().replace('_', ' ')}]" for cat, methods in novasieve.screener.get_fundamental_analysis().items() for method_code, method_info in methods.items()}
}

analysis_options_reverse = {
    "technical": {f"{method_info['name']} [{cat.title().replace('_', ' ')}]": method_code for cat, methods in novasieve.screener.get_technical_analysis().items() for method_code, method_info in methods.items()},
    "fundamental": {f"{method_info['name']} [{cat.title().replace('_', ' ')}]": method_code for cat, methods in novasieve.screener.get_fundamental_analysis().items() for method_code, method_info in methods.items()}
}