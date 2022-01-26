import requests
from config import *
from params import *
from orders import *
import time

class Strategy:
    # Calculate indicator values and places trades
    
    def __init__(self, ticker, buy_amount_percent):
        self.ticker = ticker
        self.RSI_ENDPOINT = 'https://api.taapi.io/rsi?'
        self.CCI_ENDPOINT = 'https://api.taapi.io/cci?'
        self.rsi_value = float(requests.get(self.RSI_ENDPOINT, params=rsi_parameters).json()['value'])
        self.cci_value = float(requests.get(self.CCI_ENDPOINT, params=cci_parameters).json()['value'])
        self.buy_quantity = get_balance_bnb() * buy_amount_percent # buys 15% of your total balance
    
    def rsi_signal(self, rsi_value):
        # Calculates RSI strategy signal
        if rsi_value >= 60:
            return False
        elif rsi_value <= 40:
            return True
    
    def cci_signal(self, cci_value):
        # Calculates CCI strategy signal
        if cci_value >= 80:
            return True
        elif cci_value <= -80:
            return False

    def run_strategy(self):
        # Runs the strategy and places buy and sell orders
        rsi_value = float(requests.get(self.RSI_ENDPOINT, params=rsi_parameters).json()['value'])
        cci_value = float(requests.get(self.CCI_ENDPOINT, params=cci_parameters).json()['value'])
        
        if self.rsi_signal(rsi_value) == True and self.cci_signal(cci_value) == True:
            buy_order(self.ticker, self.buy_quantity)
            time.sleep(210) # Waits 210 seconds minimum to place order again
        elif self.rsi_signal(rsi_value) == False and self.cci_signal(cci_value) == False:
            if get_balance_ticker() > 50:
                sell_order(self.ticker, (get_balance_ticker()))
                
        print('RSI: ' + str(rsi_value) + ' CCI:' + str(cci_value)) # Print to console rsi and cci values
    