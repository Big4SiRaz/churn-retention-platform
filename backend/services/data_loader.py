import duckdb
import os

from services.db import con


# -------------------------------
# Used Previously to load data, now just a helper function to get user features
# -------------------------------
'''
# Path to dataset
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATA_PATH = os.path.join(
    BASE_DIR,
    "..",
    "data",
    "processed",
    "membersTransactionsUserAggregated.csv"
)

print(f"Data path: {DATA_PATH}")

# Create a connection once
con = duckdb.connect()



# LOAD ONCE INTO MEMORY
con.execute(f"""
CREATE OR REPLACE TABLE users AS
SELECT * FROM '{DATA_PATH}'
""")

'''
def get_user_features(user_id: str):

    query = """
    SELECT *
    FROM users
    WHERE msno = ?
    LIMIT 1
    """

    result = con.execute(query, [user_id]).fetch_df()

    if result.empty:
        return None

    return result.iloc[0].to_dict()
