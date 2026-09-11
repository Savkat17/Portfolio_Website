from config import TARGET

def score_listing(title, description="", year=None):
    # Combine all available text
    text = f"{title} {description}".lower()
    score = 0
    reasons = []

    # -----------------------------------------
    # HARD FILTER: PAJERO
    # -----------------------------------------
    if "pajero" not in text:
        return 0, ["Not a Pajero"]
    score += 30
    reasons.append("Pajero")

    # -----------------------------------------
    # HARD FILTER: MANUAL
    # -----------------------------------------
    if "manual" not in text:
        return 0, [
            "Rejected: Manual transmission not confirmed"
        ]
    # Reject known automatic vehicles
    automatic_terms = [
        "automatic",
        " auto ",
        "cvt"
    ]
    if any(term in text for term in automatic_terms):
        return 0, [
            "Rejected: Automatic transmission"
        ]
    score += 40
    reasons.append("Manual transmission")

    # -----------------------------------------
    # ENGINE
    # -----------------------------------------
    engine_matches = [
        term
        for term in TARGET["engine_terms"]
        if term in text
    ]
    if engine_matches:
        score += 20
        reasons.append("3.2 DI-D / DID engine")

    # -----------------------------------------
    # SWB / 3 DOOR
    # -----------------------------------------
    body_matches = [
        term
        for term in TARGET["body_terms"]
        if term in text
    ]
    if body_matches:
        score += 25
        reasons.append("SWB / 3-door")

    # -----------------------------------------
    # 4X4
    # -----------------------------------------
    drivetrain_matches = [
        term
        for term in TARGET["drivetrain_terms"]
        if term in text
    ]
    if drivetrain_matches:
        score += 10
        reasons.append("4x4")

    # -----------------------------------------
    # EXCLUSIONS
    # -----------------------------------------
    if "pajero sport" in text:
        return 0, [
            "Rejected: Pajero Sport"
        ]

    # -----------------------------------------
    # YEAR
    # -----------------------------------------
    if year is not None:
        if TARGET["year_min"] <= year <= TARGET["year_max"]:
            score += 15
            reasons.append("Preferred year")
        else:
            reasons.append("Outside preferred year")
    return score, reasons