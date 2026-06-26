"""
ddb_client.py

Utilities for connecting to the DolphinDB server
and executing database queries.

Author: Bella Zhu
Project:
A-share Level2 Opening Auction Microstructure Analysis
"""

import dolphindb as ddb
import os
from dotenv import load_dotenv\

load_dotenv()

def connect_ddb():
    s = ddb.session()
    s.connect(
        os.getenv("DDB_IP"),
        int(os.getenv("DDB_PORT")),
        os.getenv("DDB_USER"),
        os.getenv("DDB_PASSWORD")
    )
    return s