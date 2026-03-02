# 🎮 Game Glitch Investigator: The Impossible Guesser

<hr>

---

## 🔍 PHASE 1 – Initial Observations

When I ran the game for the first time, it was clearly not working correctly. Below are the main issues I noticed.

---

### 🎯 1. Hint Logic Was Incorrect

I started by guessing **7**, and the game told me:

> “Go lower.”

Then I guessed **3, 2, and even 1**, and it _still_ said “Go lower.”

Since the range is supposed to be between 1 and 100, it makes no sense to keep saying “Go lower” after guessing 1.

🧠 **Conclusion:**  
The comparison logic inside `check_guess()` was likely reversed. The hint direction did not match the outcome.

---

### 📉 2. Score Went Negative

Every time I guessed incorrectly, the score decreased by 5 points.  
After several guesses, my score became **–25**.

This may not technically be a bug, but it felt questionable from a game design perspective. Most games don’t allow negative scores unless it’s intentional.

🧠 **Conclusion:**  
Score behavior needed review to determine if negative scoring was intended.

---

### 🔢 3. Attempts Tracking Was Inconsistent

![alt text](image.png)

Using the **Developer Debug Info**, I noticed:

- Attempts started at 0
- The “attempts left” display didn’t always match reality
- It sometimes said “Out of attempts” while still showing 1 attempt left

🧠 **Conclusion:**  
There was likely an off-by-one error in how attempts were initialized or incremented.

---

### 🔁 4. “New Game” Did Not Fully Reset

After clicking **New Game**, I observed:

- ✅ Secret number changed
- ❌ Score did not reset
- ❌ History was not cleared
- ❌ Game still said “Game over”
- ❌ Attempts display was inconsistent

🧠 **Conclusion:**  
The reset logic did not fully reinitialize session state.

---

### 🎚 5. Difficulty Levels Did Not Scale Logically

Original difficulty ranges:

- Easy → 1–20
- Normal → 1–100
- Hard → 1–50

This did not make logical sense.

I updated them to:

- Easy → 1–20
- Normal → 1–50
- Hard → 1–100

Now the difficulty increases progressively.

---

## 🛠 PHASE 2 – Repairs and Refactoring

After identifying the main issues, I focused on fixing the core logic and improving structure.

---

### ✅ Fix 1 – Corrected Hint Direction

In `check_guess()`:

Originally, when `guess > secret`, the game returned a hint saying “Go Higher,” which is incorrect.

I reversed the logic so now:

- If guess is too high → Hint says **“Go Lower”**
- If guess is too low → Hint says **“Go Higher”**

This resolved the main gameplay issue.

---

### ✅ Fix 2 – Updated Difficulty Ranges

I modified `get_range_for_difficulty()` to reflect logical scaling:

- Normal → 1–50
- Hard → 1–100

This makes the levels progressively more challenging.

---

### ✅ Fix 3 – Refactored Logic Into `logic_utils.py`

Originally, most of the game logic lived inside `app.py`.

I moved the following functions into `logic_utils.py`:

- `get_range_for_difficulty()`
- `parse_guess()`
- `check_guess()`
- `update_score()`

🧠 **Why?**

- The test file imports from `logic_utils.py`
- Pure logic functions are easier to test with `pytest`
- Separating UI from logic makes the code cleaner and more maintainable

---

## 🤖 AI as a Teammate

### ⚠️ Misleading Suggestion

One AI suggestion was:

> “Convert everything to string to avoid TypeError.”

While this might prevent an error, it introduces incorrect comparison logic (string comparisons behave differently than numeric comparisons).

I rejected this suggestion after thinking through the consequences.

---

### ✅ Helpful Suggestions

AI helped me understand:

- Why Streamlit reruns reset variables unless stored in `st.session_state`
- Why logic should be separated from UI
- Why `pytest` was failing even after fixing `app.py`

These explanations helped guide the refactor and debugging process.

---

## 🧪 Testing and Verification

To verify my fixes:

- I manually tested edge values like **1** and **100**
- I switched between difficulty levels to confirm ranges
- I ran `pytest` to confirm that the updated logic passed the tests

After these steps, the game behaved consistently and logically.

---

## 💡 Hints I Would Give Students

- Try guessing edge numbers (1 or the maximum value). Does the hint direction make sense?
- Switch difficulty levels and confirm the range changes properly.
- Open **Developer Debug Info** and watch how session state changes after each action.
- If something feels inconsistent, trace it step-by-step.

---

## 📘 PHASE 3 – Reflection

All observations, fixes, and reflections were documented at the top of this README file instead of using reflection.md.

---

<hr>

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable.

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: _"How do I keep a variable from resetting in Streamlit when I click a button?"_
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [ ] Describe the game's purpose.
- [ ] Detail which bugs you found.
- [ ] Explain what fixes you applied.

## 📸 Demo

- [ ] [Insert a screenshot of your fixed, winning game here]

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, insert a screenshot of your Enhanced Game UI here]
