from fastapi import FastAPI
import joblib
import pandas as pd
import warnings
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


from services.metric_engine import build_user_context, get_time_bucket, get_risk_bucket
from services.persona_engine import get_persona
from services.action_engine import get_action
from services.data_loader import get_user_features
from services.db import con

warnings.filterwarnings("ignore") # Ignore warnings for cleaner output, especially from model prediction on edge cases
app = FastAPI()

# -------------------------------
# LOAD MODEL + STATS
# -------------------------------
model = joblib.load("model/churn_model_week5.pkl")
stats = joblib.load("config/payment_stats.pkl")
FEATURE_ORDER = model.feature_name_


# -------------------------------
# FEATURE ORDER (VERY IMPORTANT)
# -------------------------------


@app.get("/")
def root():
    return {"message": "Churn Retention API is running"}


# -------------------------------
# Top Risky Users GET ENDPOINT
# -------------------------------

@app.get("/top_users")
def top_users():

    query = """
    SELECT *
    FROM users
    WHERE tenure_days >= 0
    LIMIT 500
    """

    df = con.execute(query).df()

    results = []

    for _, row in df.iterrows():

        features = row.to_dict()

        model_input = pd.DataFrame([{f: features.get(f, 0) for f in FEATURE_ORDER}])

        try:
            risk = model.predict_proba(model_input)[0][1]
        except:
            risk = 0.5

        results.append({
            "user_id": features["msno"],
            "risk": risk
        })

    # 🔥 sort by risk
    results = sorted(results, key=lambda x: x["risk"], reverse=True)

    return results[:20]



# -------------------------------
# SECONDARY ENDPOINT - NOT USER FACING, USED FOR TESTING ONLY
# -------------------------------
@app.post("/recommend")
def recommend(features: dict):

    FEATURE_ORDER = model.feature_name_
    model_input = pd.DataFrame([{f: features.get(f, 0) for f in FEATURE_ORDER}])

    # ---------------------------
    # 0. HANDLE INVALID USERS
    # ---------------------------
    if features["tenure_days"] < 0:
        return {
            "persona": "New & Uncertain",
            "risk": "N/A",
            "time_bucket": "N/A",
            "actions": ["Guided onboarding playlists", "Discover feeds"]
        }

    # ---------------------------
    # 1. MODEL RISK
    # ---------------------------
    try:
        model_input = pd.DataFrame([{f: features.get(f, 0) for f in FEATURE_ORDER}])
        risk = model.predict_proba(model_input)[0][1]
    except:
        risk = 0.5

    # ---------------------------
    # 2. BUILD CONTEXT
    # ---------------------------
    user_context = build_user_context(features, stats)

    # ---------------------------
    # 3. PERSONA
    # ---------------------------
    persona, priority = get_persona(user_context)

    # ---------------------------
    # 4. TIME BUCKET
    # ---------------------------
    time_bucket = get_time_bucket(features["remaining_days"])

    # ---------------------------
    # 5. ACTION ENGINE
    # ---------------------------
    risk_desc= "High" if risk >= 0.67 else "Medium" if risk >= 0.33 else "Low"
    actions = get_action(persona, risk_desc, time_bucket)

    # ---------------------------
    # 6. RESPONSE
    # ---------------------------
    return {
        "persona": persona,
        "priority": priority,
        "risk": round(risk, 3),
        "time_bucket": time_bucket,
        "context": user_context,
        "actions": actions
    }


# -------------------------------
# MAIN ENDPOINT - NOT USER FACING, USED FOR TESTING ONLY
# -------------------------------

@app.post("/recommend_by_user")
def recommend_by_user(user: dict):

    try:
        logger.info(f"Incoming request: {user}")

        user_id = user.get("user_id")
		
		# ---------------------------
		# 1. FETCH FEATURES
		# ---------------------------
        features = get_user_features(user_id)

        if features is None:
            raise ValueError("User not found")
		
		# ---------------------------
		# 1.5: Get Remaining Days Data from UI
		# ---------------------------		
        override_days = user.get("override_days_to_expiry")

        if override_days is not None:
            features["remaining_days"] = override_days
			
		# ---------------------------
		# 2. HANDLE INVALID USERS
		# ---------------------------	

        if features["tenure_days"] < 0:
            return {
				"user_id": user_id,
                "persona": "New & Uncertain",
                "risk": "N/A",
                "time_bucket": "N/A",
                "actions": ["Guided onboarding playlists"]
            }

		# ---------------------------
		# 3. MODEL INPUT
		# ---------------------------
        model_input = pd.DataFrame([{
            f: features.get(f, 0) for f in FEATURE_ORDER
        }])

        risk = model.predict_proba(model_input)[0][1]
		
		# ---------------------------
		# 4. CONTEXT
		# ---------------------------
        user_context = build_user_context(features, stats)
		
		# ---------------------------
		# 5. PERSONA
		# ---------------------------
        persona, priority = get_persona(user_context)

		# ---------------------------
		# 6. TIME BUCKET
		# ---------------------------		
        time_bucket = get_time_bucket(features["remaining_days"])

		# ---------------------------
		# 7. ACTION
		# ---------------------------
        risk_level = get_risk_bucket(risk)
        actions, explanation = get_action(persona, risk_level, time_bucket)
		



        logger.info(f"Success for user {user_id}")

        # ---------------------------
		# 8. RESPONSE
		# ---------------------------
        return {
            "user_id": user_id,
            "persona": persona,
            "priority": priority,
            "risk": round(risk, 3),
            "time_bucket": time_bucket,
            "context": user_context,
            "actions": actions,
            "explanation": explanation,
            "context": user_context
        }

    except Exception as e:
        logger.error(f"ERROR: {str(e)}")

        return {
            "error": str(e)
        }
