import duckdb

con = duckdb.connect()

USER_LOGS = "data/processed/user_churn_scored_week5.csv"
TRANSACTIONS = "data/raw/transactions.csv"
MEMBERS = "data/raw/members_v3.csv"

FINAL_T = "2016-08-23"

OUTPUT_PATH = "data/processed/membersTransactionsUserAggregated.csv"

query = f"""
COPY (
    WITH filtered_txn AS (
        SELECT *
        FROM '{TRANSACTIONS}'
        WHERE STRPTIME(CAST(transaction_date AS VARCHAR), '%Y%m%d') <= DATE '{FINAL_T}'
    ),

    latest_txn AS (
        SELECT *
        FROM (
            SELECT *,
                   ROW_NUMBER() OVER (
                       PARTITION BY msno
                       ORDER BY transaction_date DESC
                   ) as rn
            FROM filtered_txn
        )
        WHERE rn = 1
    )

    SELECT
    l.*,

    COALESCE(t.is_auto_renew, 0) AS is_auto_renew,
    COALESCE(t.is_cancel, 0) AS is_cancel,

    -- remaining_days with fallback
    COALESCE(
        DATE_DIFF(
            'day',
            DATE '{FINAL_T}',
            STRPTIME(CAST(t.membership_expire_date AS VARCHAR), '%Y%m%d')
        ),
        999
    ) AS remaining_days,

    -- tenure_days fallback
    COALESCE(
        DATE_DIFF(
            'day',
            STRPTIME(CAST(m.registration_init_time AS VARCHAR), '%Y%m%d'),
            DATE '{FINAL_T}'
        ),
        0
    ) AS tenure_days


    FROM '{USER_LOGS}' l

    LEFT JOIN latest_txn t
        ON l.msno = t.msno

    LEFT JOIN '{MEMBERS}' m
        ON l.msno = m.msno

) TO '{OUTPUT_PATH}' (FORMAT CSV, HEADER TRUE);
"""

print("Running scalable feature table creation...")

con.execute(query)

print(f"✅ Feature table saved at {OUTPUT_PATH}")
