import pandas as pd
import numpy as np

from pine2py.translator import translate
from pine2py.executor import execute_translated_code


def test_translate_simple_crossover_strategy():
    pine = """
//@version=5
strategy(title="Cross Strategy", overlay=true)
fast = input.int(5)
slow = input.int(10)
f = ta.sma(close, fast)
s = ta.sma(close, slow)
if f > s
    strategy.entry("L", strategy.long, 1)
else
    strategy.close("L")
"""
    code = translate(pine)
    dates = pd.date_range("2020-01-01", periods=100, freq="D")
    prices = np.linspace(1, 10, 100)
    df = pd.DataFrame({
        'open': prices,
        'high': prices + 0.5,
        'low': prices - 0.5,
        'close': prices,
        'volume': np.ones(100) * 1000,
    }, index=dates)
    res = execute_translated_code(code, df)
    assert 'orders' in res and isinstance(res['orders'], list)



