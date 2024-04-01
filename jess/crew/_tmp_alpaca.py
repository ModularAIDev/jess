import os
from dotenv import load_dotenv
from alpaca.trading.client import TradingClient

load_dotenv()
api_key_id = os.getenv('ALPACA_API_KEY_ID')
secret_key = os.getenv('ALPACA_SECRET_KEY')

trading_client = TradingClient(api_key_id, secret_key)

acc = trading_client.get_account()

from crewai_tools import tool


# @tool("Check accountounts restrict status")
# def check_account_status() -> str:
#     """Return message if accountount is restricted of None if accountount isn't restricted."""
#     if acc.trading_blocked:
#         return _check_account_status_logic()


# def _check_account_status_logic():
#     if acc.trading_blocked:
#         return 'Account is currently restricted from trading.'


@tool("Get string with accountount purchasing power")
def print_buying_power() -> str:
    """Returns a string with information about the purchasing power of the accountount."""
    return _print_buying_power_logic()


def _print_buying_power_logic():
    return f'{acc.buying_power}$ is available as buying power.'