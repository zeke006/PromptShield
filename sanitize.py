def sanitize_input(text):
    """
    Replaces known risky phrases with a redacted version.
    
    Args:
        text (str): Original user input.
    
    Returns:
        str: Sanitized version of the input.
    """
    dangerous_phrases = {
        "ignore previous instructions": "[REDACTED]",
        "you are now": "[REDACTED]",
        "disregard earlier": "[REDACTED]",
        "pretend to": "[REDACTED]"
    }
    for phrase, replacement in dangerous_phrases.items():
        text = text.replace(phrase, replacement)
    return text
