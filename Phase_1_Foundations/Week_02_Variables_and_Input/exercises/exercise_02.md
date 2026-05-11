# Week 2 Exercises

> **Reminder:** Type out the code yourself. Don't paste from the lesson.

These exercises focus on the four big new skills: variables, types, f-strings, and `input()`. They get progressively harder. Don't skip — even the simple ones build muscle memory.

For each exercise, create a `.py` file named after the exercise (e.g., `exercise_02a.py`).

---

## Exercise 2A: Variables in Action

**Task:** Write a program that:

1. Creates a variable `first_name` with your first name
2. Creates a variable `last_name` with your last name
3. Creates a variable `birth_year` with the year you were born (an integer, no quotes)
4. Calculates your approximate age and stores it in a variable called `age` (use `2026` as the current year for now)
5. Prints a sentence using f-strings, like:

   ```
   Hi, my name is Chris Christy. I was born in 1993, so I'm about 33 years old.
   ```

**Hint:** Don't hardcode "33" — calculate it: `age = 2026 - birth_year`. Then put `{age}` in your f-string.

---

## Exercise 2B: Type Detective

**Task:** For each value below, predict what `type()` would return, then verify by running it:

```python
print(type(7))
print(type(7.0))
print(type("7"))
print(type(True))
print(type("True"))
print(type(7 + 0))
print(type(7 + 0.0))
print(type("7" + "0"))
```

**Bonus:** What's the difference between `True` and `"True"`? Why do they have different types? Write your answer in a comment at the bottom of the file.

---

## Exercise 2C: Input + Conversion Practice

**Task:** Write a program that:

1. Asks the user for a number (use `input()`)
2. Converts it to an integer
3. Prints the number doubled
4. Prints the number squared (`number ** 2`)
5. Prints whether the number is bigger than 100 — but use **f-strings** with the result of a comparison:

   ```python
   print(f"Is it bigger than 100? {number > 100}")
   ```

**Sample run:**

```
Enter a number: 7
Doubled: 14
Squared: 49
Is it bigger than 100? False
```

**Hint:** `number > 100` returns `True` or `False` — a `bool` value. F-strings happily display booleans.

---

## Exercise 2D: The Classic Mistake

**Task:** Type the following program *exactly as written* and run it:

```python
age = input("How old are you? ")
years_until_100 = 100 - age
print(f"You'll be 100 in {years_until_100} years.")
```

**It will crash.** Read the error message carefully.

Then:

1. In a comment at the top of the file, write what error you got and what line it pointed to.
2. Below that comment, write a corrected version of the program that works.
3. Run it to confirm.

**The lesson:** This is the #1 beginner bug. `input()` always returns a string. You must convert before doing math. Now you'll never forget.

---

## Exercise 2E: F-String Practice

**Task:** Write a program that creates these variables (with any values you want):

```python
name = "..."
favorite_food = "..."
years_coding = ...   # an integer
hours_per_week = ... # a float, like 8.5
```

Then print these four lines using a *single* `print()` call each, all using f-strings:

1. A simple greeting using `name`
2. A sentence stating your favorite food
3. A sentence using `years_coding * 52` to compute total weeks
4. A sentence using `:.1f` formatting on `hours_per_week` (one decimal place)

**Example output:**

```
Hi, I'm Chris.
My favorite food is pizza.
I've been coding for 0 years — that's 0 weeks of practice.
I plan to code 8.5 hours per week.
```

---

## Exercise 2F: Mini Calculator

**Task:** Build a simple calculator that:

1. Prompts the user for two numbers (each on its own line)
2. Converts both to `float` (so decimals work)
3. Prints the sum, difference, product, and quotient — each on its own line, using f-strings
4. Formats the quotient to 2 decimal places

**Sample run:**

```
First number: 10
Second number: 3
Sum: 13.0
Difference: 7.0
Product: 30.0
Quotient: 3.33
```

**Hint:** The quotient line should look like `print(f"Quotient: {a / b:.2f}")`.

**Stretch:** What happens if the user enters `0` for the second number? Run it and see. (Don't worry about handling the error yet — we'll cover that in Phase 2.)

---

## When You're Done

You should have these files:

- `exercise_02a.py` — Variables
- `exercise_02b.py` — Type detective
- `exercise_02c.py` — Input + conversion
- `exercise_02d.py` — The classic mistake (with comment explaining the error)
- `exercise_02e.py` — F-string practice
- `exercise_02f.py` — Mini calculator

Then move on to `project/PROJECT.md` for your weekly project. Then push everything to GitHub.
