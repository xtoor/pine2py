pine2py
========

An open-source Python library that translates TradingView Pine Script (v5/v6) strategies and indicators into executable Python code that runs on pandas, NumPy, and TA-Lib.

Features
--------
- Parse Pine v5/v6 (e.g., `//@version=6`) and common constructs
- Map built-ins (`close`, `open`, `high`, `low`, `volume`, `time`, `bar_index`, `na`)
- Map indicators (`ta.sma`, `ta.ema`, `ta.rsi`, `ta.macd`, etc.) to TA-Lib
- Translate `plot()` to matplotlib stubs or console logs
- Translate `strategy.entry/exit/close` to a Python `Strategy` class with simple order/position simulation
- Emit a Python class you can execute on a pandas DataFrame with OHLCV columns

Quick Start
-----------
1. Install dependencies (ensure TA-Lib is installed in your system):

```bash
pip install -r requirements.txt
```

2. Translate a Pine Script string to Python code:

```python
from pine2py.translator import translate
pine_code = """
//@version=5
indicator(title="SMA Demo", overlay=true)
len = input.int(14)
s = ta.sma(close, len)
plot(s)
"""

code_str = translate(pine_code)
print(code_str)
```

3. Execute the translated strategy against a DataFrame:

```python
import pandas as pd
from pine2py.executor import execute_translated_code

df = pd.DataFrame({...})  # must include 'open','high','low','close','volume' indexed by datetime
result = execute_translated_code(code_str, df)
```

App Integration Snippet
-----------------------
In your trading app editor:

```python
from pine2py.translator import translate
from pine2py.executor import execute_translated_code

def on_run_button(pine_script_text: str, df):
    py_code = translate(pine_script_text)
    result = execute_translated_code(py_code, df)
    return result
```

Project Structure
-----------------
- `pine2py/parser.py`: Pine tokenizer/lightweight parser
- `pine2py/mapper.py`: Mapping dictionaries and helpers
- `pine2py/translator.py`: `translate(pine_code: str) -> str`
- `pine2py/executor.py`: Base `Strategy` and execution helpers
- `pine2py/plotting.py`: Plot stubs
- `tests/`: Unit/integration tests

Status
------
This is a pragmatic MVP that supports a large subset of Pine commonly used in indicators/strategies. Unknown or unmapped functions raise descriptive errors.

License
-------
MIT



