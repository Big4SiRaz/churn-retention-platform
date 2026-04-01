import duckdb
import joblib

# -------------------------------
# INPUT
# -------------------------------
INPUT_PATH = "data/processed/membersTransactionsUserAggregated.csv"

con = duckdb.connect()

print("Running distribution computation...")

query = f"""
WITH base AS (
    SELECT *
    FROM '{INPUT_PATH}'
    WHERE tenure_days >= 0
      AND remaining_days >= 0
),

computed AS (
    SELECT
        *,

        -- total events
        (recent_num_985 + recent_num_100 + recent_num_75 +
         recent_num_50 + recent_num_25) AS total_events,

        -- safe denominators
        GREATEST(1, (90 - remaining_days)) AS safe_days,
        GREATEST(1, mid_total_secs) AS safe_mid,
        GREATEST(1, (recent_num_985 + recent_num_100)) AS safe_high,
        GREATEST(1, recent_num_100) AS safe_100

    FROM base
),

scores AS (
    SELECT

        -- =========================
        -- ENGAGEMENT (OLD USER DEF)
        -- =========================
        0.5 * (
            (recent_num_985 + recent_num_100 + recent_num_75) / NULLIF(total_events, 0)
        ) +
        0.5 * (
            (recent_total_secs / safe_days) / (safe_mid / 60)
        ) AS engagement_score,

        -- =========================
        -- VOLATILITY
        -- =========================
        (
            0.2 * (recent_num_25 / NULLIF(total_events, 0)) +
            0.2 * (recent_num_unq / NULLIF(total_events, 0)) +
            0.3 * (recent_num_25 / safe_high) +
            0.2 * (recent_num_unq / safe_100) +
            0.1 * ((recent_num_50 + recent_num_75) / NULLIF(total_events, 0))
        ) AS volatility_score,

        -- =========================
        -- TIME SIGNAL (NEW USERS)
        -- =========================
        (recent_total_secs / safe_days) AS time_signal

    FROM computed
)

SELECT
    -- =========================
    -- ENGAGEMENT THRESHOLDS
    -- =========================
    quantile_cont(engagement_score, 0.2) AS e20,
    quantile_cont(engagement_score, 0.4) AS e40,
    quantile_cont(engagement_score, 0.6) AS e60,
    quantile_cont(engagement_score, 0.8) AS e80,

    -- =========================
    -- VOLATILITY THRESHOLDS
    -- =========================
    quantile_cont(volatility_score, 0.2) AS v20,
    quantile_cont(volatility_score, 0.4) AS v40,
    quantile_cont(volatility_score, 0.6) AS v60,
    quantile_cont(volatility_score, 0.8) AS v80,

    -- =========================
    -- TIME SIGNAL THRESHOLDS
    -- =========================
    quantile_cont(time_signal, 0.2) AS t20,
    quantile_cont(time_signal, 0.4) AS t40,
    quantile_cont(time_signal, 0.6) AS t60,
    quantile_cont(time_signal, 0.8) AS t80

FROM scores
"""

result = con.execute(query).fetchone()

# -------------------------------
# SAVE DISTRIBUTIONS
# -------------------------------

distributions = {
    "engagement": list(result[0:4]),
    "volatility": list(result[4:8]),
    "time_signal": list(result[8:12])
}

joblib.dump(distributions, "backend/config/distributions.pkl")

print("✅ distributions.pkl created")
print(distributions)