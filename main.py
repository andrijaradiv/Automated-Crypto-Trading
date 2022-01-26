from binance.client import Client
from binance.enums import *
from config import *
from orders import *
from indicators import Strategy
import time

strategy = Strategy(TICKER, BUY_AMOUNT_PERCENT) # Establish Strategy 

# Loop variables
price_loop = False # Set to True for price update
main_loop = True # Set to True to run trading strategy

# Print info
print('\nBalance BNB:\n-----------')
print(get_balance_bnb())
print('-----------\nAsset Price:\n-----------')
print(str(get_current_price(TICKER)) + '\n')

# Get price every 5 seconds
while price_loop:
    print(get_current_price(TICKER))
    time.sleep(5)
    
# Main Loop
while main_loop:
    strategy.run_strategy()
    print('running')
    time.sleep(15)
