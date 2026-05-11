# Week 1 Exercises

> **Reminder:** Type out the code yourself. Don't copy and paste. The slow way is the fast way.

These exercises are small on purpose. Their goal is to make `print` and basic Python feel familiar — like a tool in your hand, not something foreign.

For each exercise, create a new `.py` file in the `project` folder named after the exercise (e.g., `exercise_01a.py`).

---

## Exercise 1A: Print Three Lines

**Task:** Write a program that prints these three lines, in this exact order:

```
My name is Chris.
I am learning to code.
This is my first week.
```

**Hints:**
- You'll need three `print()` calls.
- Each printed sentence is a *string*, so it needs quotes around it.

---

## Exercise 1B: Print With Numbers

**Task:** Write a program that prints these lines:

```
The year is 2026.
I will become a developer in about 12 months.
That means I'll be coding professionally in 2027.
```

**Hints:**
- Numbers inside a string don't need any special treatment — just type them as part of the text.
- Watch your punctuation; the periods are part of the strings.

---

## Exercise 1C: A Quick Math Test

**Task:** Use Python like a calculator. Write a program that prints the *result* of these three calculations:

- `15 + 27`
- `144 / 12`
- `2 ** 10` (this is "2 to the 10th power")

**Hints:**
- You don't put quotes around math. Quotes make it a string of characters; no quotes makes it actual math. Try both and see what happens.
- Inside `print(...)`, you can put a math expression directly: `print(5 + 3)` will print `8`.

**Bonus:** What do you think `print("5 + 3")` will print? Try it. The result might surprise you, and the *why* is important.

---

## Exercise 1D: Multi-line Output (Beware the Quotes)

**Task:** Write a program that prints exactly this output:

```
She said "Hello!" with a smile.
It's a beautiful day.
```

This sounds simple, but there's a trap. Notice the first line has *double quotes around "Hello!"* inside the sentence. The second line has an *apostrophe in "It's"*.

**The problem:** If you write `print("She said "Hello!" with a smile.")`, Python gets confused — it thinks the string ends at the second `"`. You need a way around this.

**Hint:** Python lets you use either `"double quotes"` or `'single quotes'` to make a string. So:

- For the first line, use single quotes around the whole string: `'She said "Hello!" with a smile.'`
- For the second line, use double quotes around the whole string so the apostrophe inside is fine: `"It's a beautiful day."`

This is your first taste of how programmers solve syntax problems with small workarounds. There are other ways too (called "escape characters"), and we'll meet them later.

---

## Exercise 1E: Predict the Output

This one is *just thinking*, no typing required.

For each of the following, **predict what Python will print** before you run it. Write your guesses in a comment at the top of a new file called `predictions.py`. Then run each one and check.

```python
print(10 + 5)
```

```python
print("10" + "5")
```

```python
print("Hello" * 3)
```

```python
print("Hello", "world")
```

```python
print(7 / 2)
```

```python
print(7 // 2)
```

**Why this exercise matters:** Predicting output is a core programming skill. Good developers can mentally simulate code before running it. Getting it wrong is *also* great — every wrong prediction teaches you something about how Python actually works.

When you're done, push your `predictions.py` to GitHub along with everything else. Don't worry if your guesses were wrong — the file is a record of your *learning*, which is exactly what GitHub is for.

---

## When You're Done

You should have these files in your `project` folder:

- `hello.py` (from the lesson)
- `exercise_01a.py`
- `exercise_01b.py`
- `exercise_01c.py`
- `exercise_01d.py`
- `predictions.py`

Then move on to `project/PROJECT.md` for your first weekly project. After that, push everything to GitHub.
