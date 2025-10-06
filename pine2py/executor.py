from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict, List, Optional

import numpy as np
import pandas as pd


@dataclass
class Order:
    id: str
    direction: str  # 'long' or 'short'
    qty: float
    price: Optional[float] = None


class Strategy:
    def __init__(self, df: pd.DataFrame):
        self.df = df
        self.orders: List[Order] = []
        self.positions: Dict[str, float] = {}

    def entry(self, id: str, direction: str, qty: float, price: Optional[float] = None):
        self.orders.append(Order(id=id, direction=direction, qty=float(qty), price=price))
        self.positions[id] = self.positions.get(id, 0.0) + (qty if direction == 'long' else -qty)

    def exit(self, id: str, from_entry: Optional[str] = None, qty: Optional[float] = None, price: Optional[float] = None):
        # Simplified: reduce position to zero if qty is None
        key = from_entry or id
        pos = self.positions.get(key, 0.0)
        if pos == 0:
            return
        if qty is None:
            qty = abs(pos)
        direction = 'short' if pos > 0 else 'long'
        self.orders.append(Order(id=id, direction=direction, qty=float(qty), price=price))
        new_pos = pos - (qty if pos > 0 else -qty)
        self.positions[key] = new_pos

    def close(self, id: str):
        pos = self.positions.get(id, 0.0)
        if pos == 0:
            return
        direction = 'short' if pos > 0 else 'long'
        self.orders.append(Order(id=id, direction=direction, qty=abs(pos)))
        self.positions[id] = 0.0


def execute_translated_code(code_str: str, df: pd.DataFrame) -> Dict[str, Any]:
    # Prepare execution namespace
    exec_globals: Dict[str, Any] = {}
    exec_locals: Dict[str, Any] = {}
    # Provide Strategy and dependencies
    exec_globals.update({
        'np': np,
        'pd': pd,
        'Strategy': Strategy,
    })
    # Execute code to define the TranslatedStrategy class
    exec(code_str, exec_globals, exec_locals)
    # Class may land in globals or locals depending on exec
    StrategyClass = exec_locals.get('TranslatedStrategy') or exec_globals.get('TranslatedStrategy')
    if StrategyClass is None:
        raise RuntimeError('Translated code did not define TranslatedStrategy')
    instance = StrategyClass(df)
    return instance.run()



