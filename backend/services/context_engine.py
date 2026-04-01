def get_payment_state(is_auto_renew, is_cancel, days_to_expiry):

    if is_auto_renew == 1:
        if days_to_expiry <= 7:
            return "Friction-Exposed"
        else:
            return "Stable"

    else:
        if is_cancel == 1 or days_to_expiry <= 7:
            return "Critical"
        else:
            return "Voluntary-Exit-Prone"


def get_lifecycle_stage(tenure_days):

    if tenure_days <= 30:
        return "New"
    elif tenure_days <= 90:
        return "Activation"
    elif tenure_days <= 365:
        return "Steady"
    else:
        return "Late"


def get_engagement_strength(score):

    if score > 66:
        return "Strong"
    elif score >= 33:
        return "Moderate"
    else:
        return "Weak"


def get_volatility(score):

    if score > 66:
        return "Volatile"
    elif score >= 33:
        return "Balanced"
    else:
        return "Stable"


def get_loyalty(depth_p, exploration_p):

    if depth_p >= 66 and exploration_p < 33:
        return "Loyal"
    elif depth_p < 33 and exploration_p >= 66:
        return "Explorer"
    else:
        return "Balanced"


def get_fatigue(exploration_p, depth_p, lifecycle):

    if exploration_p < 33 and depth_p >= 66 and lifecycle == "Late":
        return True
    return False


def build_user_context(features):

    context = {}

    # PAYMENT
    context["payment_state"] = get_payment_state(
        features.get("is_auto_renew", 1),
        features.get("is_cancel", 0),
        features.get("days_to_expiry", 30)
    )

    # LIFECYCLE
    lifecycle = get_lifecycle_stage(
        features.get("tenure_days", 100)
    )
    context["lifecycle_stage"] = lifecycle

    # --- PROXY METRICS (TEMPORARY) ---

    # Engagement proxy (based on usage)
    engagement_score = features.get("recent_total_secs", 0) / 100
    context["engagement_strength"] = get_engagement_strength(engagement_score)

    # Volatility proxy
    volatility_score = features.get("num_transactions", 0) * 10
    context["volatility"] = get_volatility(volatility_score)

    # Loyalty proxy
    depth_p = features.get("recent_total_secs", 0) / 100
    exploration_p = features.get("num_transactions", 0) * 10

    context["loyalty"] = get_loyalty(depth_p, exploration_p)

    # Fatigue
    context["fatigue_flag"] = get_fatigue(
        exploration_p,
        depth_p,
        lifecycle
    )

    return context