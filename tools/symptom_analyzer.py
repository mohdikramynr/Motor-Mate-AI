import re

KEYWORDS = {
    # Battery issues
    "dead battery": ("need new battery", 0.9),
    
    #not started problem
    "Bike/Scooty not start": ("battery problem, plug problem, current problem, ignition switch problem ", 0.9),

    # Engine start issues
    "engine not start": ("empty engine oil, big valve problem, head problem", 0.9),
    "engine problem": ("needs checking", 0.7),
    "engine is not in good starting": ("Engine not in good condition - needs checking", 0.85),
    "engine not give good response":("needs checking and it's not in good condition", 0.85),

    # Smoke issues
    "silencer smoke": ("need checking on mechanic", 0.9),
    "silencer give black smoke": ("Excess fuel burning - Black Smoke", 0.85),
    "silencer give white smoke": ("Engine oil burning - White Smoke", 0.85),
    "engine give smoke": ("Engine Smoke Issue - Check piston & oil", 0.9),

    # Sound issues
    "strange noise": ("not a big problem if you are free then check on mechanic", 0.8),
    "engine noise": ("serious problem now check on mechanic", 0.8),

    # Overheating
    "engine heat": ("less engine oil and service needed", 0.9),
    "overheat": ("dangerous checking on mechanic", 0.9),

    # Oil
    "oil leak near engine": ("Oil leakage near engine block - Possible gasket damage", 0.95),
    "oil leak from silencer": ("Oil leakage from silencer - Piston ring issue", 0.95),
    "oil leak near tyre":("gear box leakage",0.95),'''only for activa'''
    "oil leak chain side": ("Oil leakage near chain - Gear box seal problem", 0.9),
    "oil leak": ("General oil leakage - Full inspection needed", 0.8),


    # Brake
    "brake not working": ("brake tight and need new brake shoe ' this is not have issue ' now you check your wheel drum", 0.9),
    "brake work slow": ("Brake adjustment needed", 0.8),
}


def symptom_analyzer(symptom_text: str):
    symptom_text = symptom_text.lower().strip()

    results = []

    for key, value in KEYWORDS.items():
        if re.search(key, symptom_text):
            results.append(value)

    # ✅ Fallback if nothing matches
    if not results:
        return [("Unknown issue - Manual inspection required", 0.5)]

    return results
