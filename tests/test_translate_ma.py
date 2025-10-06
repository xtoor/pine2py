import pandas as pd
import numpy as np

from pine2py.translator import translate
from pine2py.executor import execute_translated_code


def test_translate_sma_indicator():
    pine = """
//@version=5
indicator(title="SMA Demo", overlay=true)
len = input.int(5)
s = ta.sma(close, len)
plot(s)
"""
    code = translate(pine)
    dates = pd.date_range("2020-01-01", periods=50, freq="D")
    df = pd.DataFrame({
        'open': np.arange(50) + 1.0,
        'high': np.arange(50) + 2.0,
        'low': np.arange(50),
        'close': np.arange(50) + 1.5,
        'volume': np.ones(50) * 1000,
    }, index=dates)
    res = execute_translated_code(code, df)
    assert 'orders' in res and 'positions' in res



