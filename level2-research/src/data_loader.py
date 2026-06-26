"""
data_loader.py

Functions for querying and loading Level2 market
data from DolphinDB.

Currently supports:

- qtick
- qorder
- qknock

Future:
More flexible date / stock filtering.
"""

import pandas as pd

def load_qticks(s, limit=50000):

    df = s.run(f"""
        select *
        from loadTable("dfs://quota","qtick")
        limit {limit}
    """)

    df["time"] = pd.to_datetime(df["time"])

    return df