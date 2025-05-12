# utils.py

def log_input(text, flagged):
    """
    Logs flagged input for audit and research purposes.
    
    Args:
        text (str): User input.
        flagged (bool): Whether the input was flagged or not.
    """
    with open("log.txt", "a") as file:
        file.write(f"Flagged: {flagged} | Input: {text}\n")
