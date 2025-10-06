import pandas as pd
import numpy as np

from pine2py.translator import translate
from pine2py.executor import execute_translated_code


def test_translate_rsi_strategy():
    pine = """
//@version=5
strategy(title="RSI Strategy", overlay=false)
len = input.int(14)
r = ta.rsi(close, len)
if r < 30
    strategy.entry("L", strategy.long, 1)
else if r > 70
    strategy.close("L")
"""
    code = translate(pine)
    dates = pd.date_range("2020-01-01", periods=200, freq="D")
    prices = np.sin(np.linspace(0, 20, 200)) * 5 + 100
    df = pd.DataFrame({
        'open': prices,
        'high': prices + 0.5,
        'low': prices - 0.5,
        'close': prices,
        'volume': np.ones(200) * 1000,
    }, index=dates)
    res = execute_translated_code(code, df)
    assert 'orders' in res and 'positions' in res



