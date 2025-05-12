import re

# List of common prompt injection phrases
blacklist_phrases = [
    "ignore previous instructions",
    "you are now",
    "disregard earlier",
    "pretend to"
]

def detect_injection(text):
    """
    Checks if the input text contains any known prompt injection phrases.
    
    Args:
        text (str): Input text to analyze.

    Returns:
        (bool, str or None): Tuple of (flagged: True/False, matched phrase or None)
    """
    for phrase in blacklist_phrases:
        if re.search(phrase, text, re.IGNORECASE):
            return True, phrase
    return False, None
