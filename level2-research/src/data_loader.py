import pandas as pd

def load_qticks(s, limit=50000):

    df = s.run(f"""
        select *
        from loadTable("dfs://quota","qtick")
        limit {limit}
    """)

    df["time"] = pd.to_datetime(df["time"])

    return df