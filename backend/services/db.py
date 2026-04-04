import duckdb
import os

# -----------------------------
# PATH
# -----------------------------
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATA_PATH = os.path.abspath(
    os.path.join(BASE_DIR, "..", "data", "processed", "membersTransactionsUserAggregated.csv")
)

# -----------------------------
# CONNECTION (GLOBAL)
# -----------------------------
con = duckdb.connect()

# -----------------------------
# LOAD TABLE ONCE
# -----------------------------
con.execute(f"""
CREATE OR REPLACE TABLE users AS
SELECT * FROM '{DATA_PATH}'
""")
