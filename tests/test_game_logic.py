from logic_utils import check_guess

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    # result = check_guess(50, 50)
    # assert result == "Win"

    # FIX: check_guess returns (outcome, message), not just "Win"
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    # result = check_guess(60, 50)
    # assert result == "Too High"

    outcome, msg = check_guess(60, 50)
    assert outcome == "Too High"
    # FIX: Validate the hint direction (this catches the original bug)
    assert "LOWER" in msg

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    # result = check_guess(40, 50)
    # assert result == "Too Low"

    outcome, msg = check_guess(40, 50)
    assert outcome == "Too Low"
    # FIX: Validate the hint direction (this catches the original bug)
    assert "HIGHER" in msg
