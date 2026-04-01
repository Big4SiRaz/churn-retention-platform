from fastapi import FastAPI
import joblib
import pandas as pd
from services.context_engine import build_user_context
from services.action_engine import get_recommended_action
from services.metric_engine import *
from services.persona_engine import get_persona
from services.action_engine import get_action

app = FastAPI()

# Load model once when app starts
model = joblib.load("model/churn_model_week5.pkl")


@app.get("/")
def root():
    return {"message": "Churn Retention API is running"}


# Helper function to assign risk bucket
def risk_bucket(prob):
    if prob < 0.3:
        return "Low"
    elif prob < 0.6:
        return "Medium"
    else:
        return "High"


@app.post("/predict")
def predict(features: dict):

    # Step 1: Get expected columns
    expected_cols = model.feature_name_

    # Step 2: Fill missing features with 0
    full_features = {col: features.get(col, 0) for col in expected_cols}

    df = pd.DataFrame([full_features])

    prob = model.predict_proba(df)[0][1]

    context = build_user_context(features)

    action = get_recommended_action(
        risk_bucket(prob),
        context
    )

    return {
        "churn_probability": float(prob),
        "risk_segment": risk_bucket(prob),
        "user_context": context,
        "recommended_action": action
    }

@app.post("/recommend")
def recommend(features: dict):

    # 1. Bucket metrics
    user_context = {
        "payment": bucket_payment_status(
            features["days_to_expiry"],
            features["is_auto_renew"],
            features["is_cancel"]
        ),
        "lifecycle": bucket_lifecycle(features["tenure_days"]),
        "engagement": bucket_engagement(features["engagement_score"]),
        "volatility": bucket_volatility(features["volatility_score"])
    }

    # 2. Persona
    persona, priority = get_persona(user_context)

    # 3. Risk (model)
    risk = features["risk"]

    # 4. Time bucket
    time_bucket = get_time_bucket(features["days_to_expiry"])

    # 5. Action
    actions = get_action(persona, risk, time_bucket)

    return {
        "persona": persona,
        "risk": risk,
        "time_bucket": time_bucket,
        "actions": actions
    }