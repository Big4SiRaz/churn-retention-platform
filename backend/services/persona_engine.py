from config.persona_rules import PERSONA_RULES


def match_conditions(user, rule_conditions):

    for key, allowed_values in rule_conditions.items():
        if user.get(key) not in allowed_values:
            return False
    return True


def get_persona(user_context):

    for rule in PERSONA_RULES:
        if match_conditions(user_context, rule["conditions"]):
            return rule["name"], rule["priority"]

    return "Unknown", -1