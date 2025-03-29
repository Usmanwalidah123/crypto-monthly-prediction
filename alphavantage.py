import requests
import json

# Dummy decorators to simulate API call and output formatting.
def _output_format(func):
    def wrapper(*args, **kwargs):
        # In your implementation, you might format the raw API response.
        return func(*args, **kwargs)
    return wrapper

def _call_api_on_func(func):
    def wrapper(self, *args, **kwargs):
        # Normally, here you would build the API request URL using:
        # - self.api_key
        # - the function key returned by func()
        # - additional parameters (symbol, market, etc.)
        # Then perform a request (e.g., using requests.get) and return the JSON.
        # For demonstration, we return dummy monthly data.
        function_key, data_key, meta_key = func(self, *args, **kwargs)
        # Dummy response: a dictionary with dates as keys and a nested dict containing a close price.
        dummy_data = {
            "2024-01-31": {"4. close": "20000.00"},
            "2024-02-29": {"4. close": "21000.00"},
            "2024-03-31": {"4. close": "22000.00"},
            "2024-04-30": {"4. close": "23000.00"},
        }
        return dummy_data
    return wrapper

class AlphaVantage:
    def __init__(self, api_key):
        self.api_key = api_key

    # Make these decorators available as class attributes
    _output_format = staticmethod(_output_format)
    _call_api_on_func = staticmethod(_call_api_on_func)

class CryptoCurrencies(AlphaVantage):
    """This class implements all the crypto currencies API calls."""

    @_output_format
    @_call_api_on_func
    def get_digital_currency_daily(self, symbol, market):
        _FUNCTION_KEY = 'DIGITAL_CURRENCY_DAILY'
        return _FUNCTION_KEY, 'Time Series (Digital Currency Daily)', 'Meta Data'

    @_output_format
    @_call_api_on_func
    def get_digital_currency_weekly(self, symbol, market):
        _FUNCTION_KEY = 'DIGITAL_CURRENCY_WEEKLY'
        return _FUNCTION_KEY, 'Time Series (Digital Currency Weekly)', 'Meta Data'

    @_output_format
    @_call_api_on_func
    def get_digital_currency_monthly(self, symbol, market):
        _FUNCTION_KEY = 'DIGITAL_CURRENCY_MONTHLY'
        return _FUNCTION_KEY, 'Time Series (Digital Currency Monthly)', 'Meta Data'

    @_output_format
    @_call_api_on_func
    def get_digital_currency_exchange_rate(self, from_currency, to_currency):
        _FUNCTION_KEY = 'CURRENCY_EXCHANGE_RATE'
        return _FUNCTION_KEY, 'Realtime Currency Exchange Rate', None

    @_output_format
    @_call_api_on_func
    def get_crypto_intraday(self, symbol, market, interval, outputsize='compact'):
        _FUNCTION_KEY = 'CRYPTO_INTRADAY'
        return _FUNCTION_KEY, f"Time Series Crypto ({interval})", 'Meta Data'
