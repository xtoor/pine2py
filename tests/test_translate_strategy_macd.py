import pandas as pd
import numpy as np

from pine2py.translator import translate
from pine2py.executor import execute_translated_code


def test_translate_macd_strategy():
    pine = """
//@version=5
strategy(title="MACD Strategy", overlay=false)
fast = input.int(12)
slow = input.int(26)
sig = input.int(9)
macd = ta.macd(close, fast, slow, sig)
// use macd_macd from translation convention
if macd_macd > macd_signal
    strategy.entry("L", strategy.long, 1)
else
    strategy.close("L")
"""
    code = translate(pine)
    dates = pd.date_range("2020-01-01", periods=120, freq="D")
    prices = np.linspace(1, 20, 120)
    df = pd.DataFrame({
        'open': prices,
        'high': prices + 0.5,
        'low': prices - 0.5,
        'close': prices,
        'volume': np.ones(120) * 1000,
    }, index=dates)
    res = execute_translated_code(code, df)
    assert 'orders' in res and 'positions' in res



