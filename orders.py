from binance.client import Client
from binance.enums import *
from config import *

# Connect to binance
client = Client(api_key, api_secret)

def buy_order(symbol, quantity):
    # Place Market Buy Order
    client.order_market_buy(
        symbol= f'{symbol}BNB',
        quantity= quantity)
    
def sell_order(symbol, quantity):
    # Place Market Sell Order
    client.order_market_sell(
        symbol= f'{symbol}BNB',
        quantity= quantity)
    
def get_current_price(symbol):
    # Returns current price
    price = client.get_avg_price(symbol=f'{symbol}USDT')
    return float(price['price'])

def get_balance_bnb():
    # Returns BNB Balance
    balance = client.get_asset_balance(asset='BNB')
    return float(balance['free'])

def get_balance_ticker():
    # Returns ticker Balance
    balance = client.get_asset_balance(asset=TICKER)
    return float(balance['free'])

def get_current_price_bnb(symbol):
    # Get current price in BNB
    return float(client.get_avg_price(symbol=f'{symbol}BNB')['price'])
