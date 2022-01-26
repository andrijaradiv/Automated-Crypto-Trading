from config import *

# RSI indicator parameters
rsi_parameters = {
    'secret': taapi_api_key,
    'exchange': 'binance',
    'symbol': f'{TICKER}/BNB', # Enter symbol to trade
    'interval': '1h', # Enter time interval for RSI indicator
    'optInTimePeriod': 6,
}

# CCI indicator parameters
cci_parameters = {
    'secret': taapi_api_key,
    'exchange': 'binance', 
    'symbol': f'{TICKER}/BNB', # Enter symbol to trade
    'interval': '1h', # Enter time interval for CCI indicator
}