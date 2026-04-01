ACTIONS = {

    # =========================
    # 🔴 HIGH RISK
    # =========================
    "High": {

        "At-Risk Loyalist": {
            "T-7-": [
                "Fix payment (retry, alternate methods)",
                "SMS",
                "We value you messaging"
            ],
            "T-7:3": [
                "Smart payment retries + reminders",
                "Discount",
                "SMS"
            ],
            "T-2:0": [
                "Discount",
                "Extend membership by 5 days",
                "Upgrade for 3 days free"
            ],
            "T+1": [
                "Discount",
                "Extend membership by 1 day"
            ]
        },

        "Fading User": {
            "T-7-": [
                "Only extremely liked podcast",
                "Better cold-start recommendations"
            ],
            "T-7:3": [
                "Nudge to fill music preference form",
                "Notification songs matching preference"
            ],
            "T-2:0": [
                "Discount",
                "Free premium content"
            ],
            "T+1": [
                "Discount",
                "Free premium content"
            ]
        },

        "Payment-Friction User": {
            "T-7-": [
                "Fix payment (retry, alternate methods)",
                "SMS"
            ],
            "T-7:3": [
                "Smart payment retries + reminders",
                "SMS"
            ],
            "T-2:0": [
                "Discount",
                "Extend membership by 5 days"
            ],
            "T+1": [
                "Fix payment (retry, alternate methods)",
                "Discount"
            ]
        },

        "Impatient Explorer": {
            "T-7-": [
                "New automatic tailored feeds",
                "Notification new songs matching preference"
            ],
            "T-7:3": [
                "Aggressive UI mood settings",
                "Remix songs"
            ],
            "T-2:0": [
                "Discount",
                "Upgrade 10 days at current price"
            ],
            "T+1": [
                "Discount",
                "Free premium content"
            ]
        },

        "Bored Loyalist": {
            "T-7-": [
                "Reduce notification (No SMS)",
                "Remix songs"
            ],
            "T-7:3": [
                "Nudge to fill music preference form",
                "Highlight forgotten favorites"
            ],
            "T-2:0": [
                "Discount",
                "Upgrade 10 days"
            ],
            "T+1": [
                "Discount",
                "Free premium content"
            ]
        },

        "New & Uncertain": {
            "T-7-": [
                "Guided onboarding playlists",
                "Notification songs matching preference"
            ],
            "T-7:3": [
                "Nudge to fill music preference form",
                "SMS"
            ],
            "T-2:0": [
                "Discount",
                "Free premium content"
            ],
            "T+1": [
                "Discount",
                "Free premium content"
            ]
        },

        "Curious Explorer": {
            "T-7-": [
                "Experimental feeds",
                "Notification songs matching preference"
            ],
            "T-7:3": [
                "Nudge to fill music preference form",
                "Email"
            ],
            "T-2:0": [
                "Payment reminder (SMS + Email)"
            ],
            "T+1": [
                "Payment reminder (SMS + Email)"
            ]
        },

        "Loyal Enthusiast": {
            "T-7-": [
                "Premium content",
                "Referral programs"
            ],
            "T-7:3": [
                "Ask celebrity questions",
                "Email"
            ],
            "T-2:0": [
                "Payment reminder (SMS + Email)"
            ],
            "T+1": [
                "Premium content"
            ]
        },

        "Passive Listener": {
            "T-7-": [
                "Premium features",
                "Email"
            ],
            "T-7:3": [
                "Payment reminder (SMS + Email)"
            ],
            "T-2:0": [
                "Payment reminder (SMS + Email)"
            ],
            "T+1": [
                "Payment reminder (SMS + Email)"
            ]
        },

        "Balanced Power User": {
            "T-7-": [
                "Premium features",
                "Referral programs"
            ],
            "T-7:3": [
                "Early feature access",
                "Community engagement"
            ],
            "T-2:0": [
                "Payment reminder (SMS + Email)"
            ],
            "T+1": [
                "Premium content"
            ]
        }
    },

    # =========================
    # 🟠 MEDIUM RISK
    # =========================
    "Medium": {

        "At-Risk Loyalist": {
            "T-7-": ["Fix payment (retry, alternate methods)", "SMS"],
            "T-7:3": ["Smart payment retries + reminders", "Email", "SMS"],
            "T-2:0": ["Extend membership by 5 days"],
            "T+1": ["Extend membership by 1 day"]
        },

        "Fading User": {
            "T-7-": ["Reduce notification", "Better recommendations"],
            "T-7:3": ["Preference form", "Notification songs"],
            "T-2:0": ["Free premium content"],
            "T+1": ["Free premium content"]
        },

        "Payment-Friction User": {
            "T-7-": ["Fix payment", "SMS"],
            "T-7:3": ["Smart retries", "SMS"],
            "T-2:0": ["Extend membership by 5 days"],
            "T+1": ["Extend membership by 1 day"]
        },

        "Impatient Explorer": {
            "T-7-": ["Tailored feeds", "Notification songs"],
            "T-7:3": ["UI mood settings", "Remix songs"],
            "T-2:0": ["Upgrade 10 days at current price"],
            "T+1": ["Free premium content"]
        },

        "Bored Loyalist": {
            "T-7-": ["Reduce notification", "Remix songs"],
            "T-7:3": ["Preference form", "Highlight favorites"],
            "T-2:0": ["Upgrade 10 days"],
            "T+1": ["Free premium content"]
        },

        "New & Uncertain": {
            "T-7-": ["Onboarding playlists", "Notification songs"],
            "T-7:3": ["Preference form", "SMS"],
            "T-2:0": ["Free premium content"],
            "T+1": ["Free premium content"]
        },

        "Curious Explorer": {
            "T-7-": ["Experimental feeds", "Notification songs"],
            "T-7:3": ["Preference form", "Email"],
            "T-2:0": ["Payment reminder (SMS + Email)"],
            "T+1": ["Payment reminder (SMS + Email)"]
        },

        "Loyal Enthusiast": {
            "T-7-": ["Premium content", "Referral"],
            "T-7:3": ["Ask celebrity questions", "Email"],
            "T-2:0": ["Payment reminder (SMS + Email)"],
            "T+1": ["Premium content"]
        },

        "Passive Listener": {
            "T-7-": ["Premium features", "Email"],
            "T-7:3": ["Payment reminder (SMS + Email)"],
            "T-2:0": ["Payment reminder (SMS + Email)"],
            "T+1": ["Payment reminder (SMS + Email)"]
        },

        "Balanced Power User": {
            "T-7-": ["Premium features", "Referral"],
            "T-7:3": ["Early access", "Community"],
            "T-2:0": ["Payment reminder (SMS + Email)"],
            "T+1": ["Premium content"]
        }
    },

    # =========================
    # 🟢 LOW RISK
    # =========================
    "Low": {

        "At-Risk Loyalist": {
            "T-7-": ["Fix payment", "Email"],
            "T-7:3": ["Email", "Notification"],
            "T-2:0": ["Notification"],
            "T+1": ["Notification"]
        },

        "Fading User": {
            "T-7-": ["Better recommendations"],
            "T-7:3": ["Preference form"],
            "T-2:0": ["Better recommendations"],
            "T+1": ["Better recommendations"]
        },

        "Payment-Friction User": {
            "T-7-": ["Fix payment", "Email"],
            "T-7:3": ["Email", "Notification"],
            "T-2:0": ["Notification"],
            "T+1": ["Fix payment"]
        },

        "Impatient Explorer": {
            "T-7-": ["Experimental feeds"],
            "T-7:3": ["Remix songs"],
            "T-2:0": ["Better recommendations"],
            "T+1": ["Better recommendations"]
        },

        "Bored Loyalist": {
            "T-7-": ["Remix songs"],
            "T-7:3": ["Preference form"],
            "T-2:0": ["Better recommendations"],
            "T+1": ["Better recommendations"]
        },

        "New & Uncertain": {
            "T-7-": ["Onboarding playlists"],
            "T-7:3": ["Notification songs"],
            "T-2:0": ["Payment reminder (Email)"],
            "T+1": ["Better recommendations"]
        },

        "Curious Explorer": {
            "T-7-": ["Experimental feeds"],
            "T-7:3": ["Notification songs"],
            "T-2:0": ["Payment reminder (Email)"],
            "T+1": ["Payment reminder (Email)"]
        },

        "Loyal Enthusiast": {
            "T-7-": ["Premium features"],
            "T-7:3": ["Premium content"],
            "T-2:0": ["Payment reminder (Email)"],
            "T+1": ["Payment reminder (Email)"]
        },

        "Passive Listener": {
            "T-7-": ["Premium features"],
            "T-7:3": ["Payment reminder (Email)"],
            "T-2:0": ["Payment reminder (Email)"],
            "T+1": ["Payment reminder (Email)"]
        },

        "Balanced Power User": {
            "T-7-": ["Premium features"],
            "T-7:3": ["Early access"],
            "T-2:0": ["Payment reminder (Email)"],
            "T+1": ["Premium content"]
        }
    }
}
