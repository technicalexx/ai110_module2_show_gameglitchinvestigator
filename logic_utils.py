# def get_range_for_difficulty(difficulty: str):
#     """Return (low, high) inclusive range for a given difficulty."""
#     raise NotImplementedError("Refactor this function from app.py into logic_utils.py")


# def parse_guess(raw: str):
#     """
#     Parse user input into an int guess.

#     Returns: (ok: bool, guess_int: int | None, error_message: str | None)
#     """
#     raise NotImplementedError("Refactor this function from app.py into logic_utils.py")


# def check_guess(guess, secret):
#     """
#     Compare guess to secret and return (outcome, message).

#     outcome examples: "Win", "Too High", "Too Low"
#     """
#     raise NotImplementedError("Refactor this function from app.py into logic_utils.py")


# def update_score(current_score: int, outcome: str, attempt_number: int):
#     """Update score based on outcome and attempt number."""
#     raise NotImplementedError("Refactor this function from app.py into logic_utils.py")



# logic_utils.py

def get_range_for_difficulty(difficulty: str):
    """Return (low, high) inclusive range for a given difficulty."""

    # FIX: This file originally raised NotImplementedError, which broke pytest and prevented
    # logic from being testable outside the Streamlit UI. We implement the real function here.
    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Normal":
        # FIX: Updated difficulty range per your change request.
        return 1, 50
    if difficulty == "Hard":
        # FIX: Updated difficulty range per your change request.
        return 1, 100

    # FIX: Fallback should be safe and predictable.
    return 1, 50


def parse_guess(raw: str):
    """
    Parse user input into an int guess.

    Returns: (ok: bool, guess_int: int | None, error_message: str | None)
    """

    # FIX: Keep input validation inside logic so app.py stays focused on UI.
    if raw is None or raw == "":
        return False, None, "Enter a guess."

    try:
        # FIX: If user types a decimal ("10.7"), convert to float then int (10).
        # This avoids crashing on float-like strings.
        if "." in raw:
            value = int(float(raw))
        else:
            value = int(raw)
    except Exception:
        # FIX: Provide a clean user-facing error instead of crashing.
        return False, None, "That is not a number."

    return True, value, None


def check_guess(guess: int, secret: int):
    """
    Compare guess to secret and return (outcome, message).

    outcome examples: "Win", "Too High", "Too Low"
    """

    # FIX: The original app.py had a try/except TypeError and sometimes compared strings.
    # That created random behavior (string comparisons). We enforce int-only logic here.
    if guess == secret:
        return "Win", "🎉 Correct!"

    # WRONG (from original app.py):
    # if guess > secret:
    #     return "Too High", "📈 Go HIGHER!"
    # else:
    #     return "Too Low", "📉 Go LOWER!"

    # FIX: Hint messages must match the outcome direction:
    # - Too High => go LOWER
    # - Too Low  => go HIGHER
    if guess > secret:
        return "Too High", "📉 Go LOWER!"
    else:
        return "Too Low", "📈 Go HIGHER!"


def update_score(current_score: int, outcome: str, attempt_number: int):
    """Update score based on outcome and attempt number."""

    # NOTE: attempt_number is now treated as "guess count so far" (1 for first valid guess, etc.)
    # FIX: Previously app.py started attempts at 1 and incremented early, causing confusing scoring.
    if outcome == "Win":
        # FIX: Reward decreases as attempts increase; keep a floor so it never hits 0.
        points = 100 - 10 * attempt_number
        if points < 10:
            points = 10
        return current_score + points

    # (Kept the rest of the original scoring behavior; only moved here for testability.)
    if outcome == "Too High":
        if attempt_number % 2 == 0:
            return current_score + 5
        return current_score - 5

    if outcome == "Too Low":
        return current_score - 5

    return current_score