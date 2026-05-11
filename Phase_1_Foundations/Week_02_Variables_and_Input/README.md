# Week 2 — Variables, Data Types, and Talking to Users

> **Estimated time:** 8–12 hours, spread over the week.
> **Difficulty:** Beginner. Builds directly on Week 1.

---

## What You'll Learn This Week

By the end of Week 2, you will:

1. Understand and use **variables** — the most fundamental concept in programming
2. Know the four most common **data types** (and why types matter)
3. Get **input from a user** while your program runs
4. Convert between data types when needed
5. Use **f-strings** — the modern, clean way to combine text and values
6. Build a working **unit converter** that's actually useful

This week introduces the first concept that makes programs *interactive*. After Week 2, your code will respond to real human input. That's a huge leap.

---

# Part 1: Variables — The Most Important Concept You'll Ever Learn

If `print()` is how programs talk *out*, **variables** are how programs *remember*.

## The Idea

A variable is a **labeled box** that stores a value. You give the box a name, put something in it, and refer to it by that name later.

```python
name = "Chris"
age = 33
```

That's it. Two variables. `name` holds the text "Chris". `age` holds the number 33.

You can use them anywhere you'd use the value directly:

```python
name = "Chris"
print(name)             # prints: Chris
print("Hello, " + name) # prints: Hello, Chris
```

The variable name is just a *label*. The actual data is stored in your computer's memory; the label tells Python where to find it.

## Why This Matters So Much

Before variables, every value in your program had to be hardcoded. With variables:

- You can **change a value once** and have it update everywhere it's used
- You can **store the result of a computation** and reuse it
- You can **work with data you don't know in advance** (like user input — which you'll see in Part 4)

Programs without variables are like recipes that hardcode "350°F" in 47 places. With variables, you set `oven_temp = 350` once, and changing it updates everywhere.

## Variable Naming Rules

Python is picky here. A few rules:

| Allowed | Not Allowed |
|---|---|
| Letters, numbers, underscores | Spaces, dashes, special characters |
| Starts with a letter or underscore | Starts with a number |
| Case-sensitive (`age` ≠ `Age`) | Reserved words like `if`, `for`, `print` |

**Convention:** Python developers use `snake_case` — lowercase words separated by underscores. So `user_age`, not `UserAge` or `userage`.

```python
# Good
first_name = "Chris"
years_old = 33
total_hours = 21 * 52

# Avoid
firstName = "Chris"   # works but not Python style
n = "Chris"           # too short — what's "n"?
x1 = 33               # what does x1 mean?
```

**Rule of thumb:** Variable names should describe what they hold. `total_minutes` is better than `t`. Future-you will thank present-you.

## Reassigning Variables

You can change what a variable holds, any time:

```python
score = 0
print(score)   # 0
score = 5
print(score)   # 5
score = score + 10
print(score)   # 15
```

That last line is interesting — `score = score + 10` reads as: "Take the current value of `score`, add 10, and store the result back in `score`."

Python provides a shortcut for this:

```python
score = 0
score += 10   # same as score = score + 10
score += 5    # same as score = score + 5
print(score)  # 15
```

`+=`, `-=`, `*=`, `/=` are all valid shortcuts. Use them when the operation is "modify in place."

---

# Part 2: Data Types — Why Python Cares What's in the Box

Every value in Python has a **type**. The type tells Python what kind of operations are valid for that value.

## The Four You'll Use Most This Week

| Type | What it is | Example |
|---|---|---|
| `int` | Whole number (integer) | `33`, `0`, `-7`, `1092` |
| `float` | Decimal number (floating-point) | `3.14`, `0.5`, `-2.0` |
| `str` | Text (string) | `"Chris"`, `'hello'`, `""` |
| `bool` | True or False (Boolean) | `True`, `False` |

There are more types in Python (lists, dictionaries, tuples, sets — coming in Phase 2), but these four are 90% of what you'll write this week.

## Checking a Type

Python has a built-in `type()` function that tells you what type something is:

```python
print(type(42))         # <class 'int'>
print(type(3.14))       # <class 'float'>
print(type("hello"))    # <class 'str'>
print(type(True))       # <class 'bool'>
```

The output looks weird (`<class 'int'>`), but the meaningful word is the one in quotes.

## Why Types Matter (The Important Part)

Different types behave differently with the same operator. Watch:

```python
print(2 + 3)          # 5 (integer addition)
print(2.0 + 3.0)      # 5.0 (float addition)
print("2" + "3")      # "23" (string concatenation — sticks them together!)
print("Hello" * 3)    # "HelloHelloHello" (string multiplication — repeats it!)
```

The `+` symbol means **addition** for numbers but **concatenation** (sticking together) for strings. The `*` works for numbers, *and* for "string × number" to repeat. But `"2" + 3` would crash — you can't add a string and an integer.

> Remember Exercise 1E? `print("10" + "5")` printed `"105"` because both were strings and got stuck together. `print(10 + 5)` printed `15` because both were integers and got added. **Same `+` symbol, totally different behavior.** That's why types matter.

## Converting Between Types

Sometimes you need to change a value's type. Three common conversions:

```python
# String → integer
age_text = "33"
age_number = int(age_text)
print(age_number + 1)   # 34 (now you can do math)

# String → float
price_text = "9.99"
price = float(price_text)
print(price * 2)        # 19.98

# Number → string
year = 2026
message = "The year is " + str(year)
print(message)          # "The year is 2026"
```

**Why you need this:** when you ask a user for input (Part 4), Python *always* gives you back a string. If the user types `42`, you get the string `"42"`, not the number `42`. To do math with it, you have to convert.

This is one of the most common beginner stumbling blocks. We'll see it in action soon.

### When Conversion Fails

Python will refuse to convert nonsense:

```python
int("hello")    # ValueError: invalid literal for int() with base 10: 'hello'
int("3.14")     # ValueError — int() can't handle decimals directly
float("3.14")   # 3.14 (this works)
int(3.14)       # 3 (chops off the decimal — doesn't round!)
```

The last one is sneaky. `int(3.99)` is `3`, not `4`. Python truncates (cuts off), it doesn't round. If you want rounding, use `round(3.99)` which gives `4`.

---

# Part 3: F-Strings — The Best Way to Combine Text and Variables

Remember the comma-quirk in your `about_me.py` last week?

```python
print("So ", 21*52, " hours.")
# Output: So  1092  hours.   ← extra spaces
```

There's a much better way: **f-strings** (formatted strings). They're modern Python and they're a joy to use.

## The Syntax

Put an `f` immediately before a string. Then anywhere inside that string, you can put a variable or expression in **curly braces** `{}`, and Python will replace it with the value.

```python
name = "Chris"
age = 33
print(f"Hello, {name}! You are {age} years old.")
# Output: Hello, Chris! You are 33 years old.
```

That's it. The `f` tells Python "this is a formatted string." Everything in `{}` gets evaluated and inserted.

## You Can Put Any Expression Inside `{}`

```python
hours_per_week = 21
weeks = 52
print(f"Total: {hours_per_week * weeks} hours.")
# Output: Total: 1092 hours.

name = "chris"
print(f"Hi, {name.upper()}!")
# Output: Hi, CHRIS!
```

`name.upper()` is a *method* on the string — we'll dive deep into methods later, but for now just notice: anything that returns a value can go inside `{}`.

## Why F-Strings Win

Here's the same output four ways:

```python
name = "Chris"
hours = 1092

# 1. The hard way (concatenation with +):
print("Hi, " + name + "! You'll code " + str(hours) + " hours.")

# 2. The Week 1 way (commas):
print("Hi,", name + "! You'll code", hours, "hours.")

# 3. An older Python way (.format()):
print("Hi, {}! You'll code {} hours.".format(name, hours))

# 4. F-strings (the modern way):
print(f"Hi, {name}! You'll code {hours} hours.")
```

All four work. The fourth is **vastly easier to read**, which is why it's standard now. **Use f-strings whenever you're combining text and variables.** Forget the others exist.

## Formatting Numbers Inside F-Strings (Bonus)

You can control how numbers display:

```python
price = 9.876543
print(f"Price: ${price:.2f}")        # Price: $9.88 (2 decimal places)
print(f"Price: ${price:.0f}")        # Price: $10  (no decimals, rounded)

big_number = 1234567
print(f"Population: {big_number:,}") # Population: 1,234,567 (commas)
```

The colon `:` inside the curly braces starts a *format specification*. `.2f` means "show 2 decimal places, as a float." `,` means "use commas as thousands separators." We'll meet more of these as we go.

---

# Part 4: Getting Input From the User

Now for the big upgrade: programs that respond to humans.

## The `input()` Function

`input()` does two things:

1. Pauses your program and waits for the user to type something
2. When the user presses Enter, returns whatever they typed as a **string**

```python
name = input("What is your name? ")
print(f"Hi, {name}!")
```

When you run this:

```
What is your name? Chris
Hi, Chris!
```

The text inside `input("...")` is the **prompt** — what gets shown to the user. Always include a prompt; otherwise the user sees a mysterious blinking cursor and has no idea what to do.

## `input()` Always Returns a String — Always

This is the #1 thing that trips up beginners. Watch:

```python
age = input("How old are you? ")
print(age + 10)   # ❌ TypeError!
```

The user types `33`. But `input()` returns the **string** `"33"`, not the **number** `33`. So `age + 10` is trying to add a string to an integer, which Python refuses to do.

**Fix:** convert with `int()`:

```python
age = int(input("How old are you? "))
print(age + 10)   # ✅ Works
```

Notice the *nesting*: `input(...)` runs first, gets the string, then `int(...)` converts it. The result is stored in `age`.

If you need a decimal, use `float()`:

```python
height = float(input("How tall are you in meters? "))
print(f"You are {height * 100} cm tall.")
```

## Putting It All Together

Here's a tiny but complete program using everything from this week:

```python
# Greeting calculator
print("Welcome to the Greeting Calculator!")
print()

name = input("What's your name? ")
age = int(input("How old are you? "))

birth_year_estimate = 2026 - age

print()
print(f"Hi, {name}!")
print(f"You were probably born in {birth_year_estimate}.")
print(f"In 10 years, you'll be {age + 10}.")
```

When run:

```
Welcome to the Greeting Calculator!

What's your name? Chris
How old are you? 33

Hi, Chris!
You were probably born in 1993.
In 10 years, you'll be 43.
```

Notice every concept in here:

- Variables (`name`, `age`, `birth_year_estimate`)
- Types (string from `name`, integer from `int(input(...))`)
- F-strings (`f"Hi, {name}!"`)
- Math with variables (`2026 - age`)

That's Week 2 in 10 lines.

---

# Part 5: A Word About Errors (You Will See Many This Week)

Now that you're working with types, you'll start seeing more error types. Here are the three most common, with what they mean:

## TypeError

Python's saying "you tried to do something that doesn't make sense for these types."

```python
"hello" + 5
# TypeError: can only concatenate str (not "int") to str
```

**Fix:** Convert one of them. Either `"hello" + str(5)` or remove the operation.

## ValueError

You asked Python to convert something it couldn't.

```python
int("hello")
# ValueError: invalid literal for int() with base 10: 'hello'
```

**Fix:** Make sure the string actually contains a number before converting.

## NameError

You used a variable that doesn't exist (often a typo).

```python
print(naem)  # typo of "name"
# NameError: name 'naem' is not defined
```

**Fix:** Check spelling. Python is case-sensitive: `Name` ≠ `name`.

**Pro tip:** When you get an error, **read the last line first**. That's where Python tells you what went wrong. The lines above show *where* in the code it happened. Reading errors well is one of the most underrated developer skills.

---

# Your Week 2 Tasks (In Order)

1. **Read this entire README.** Type out the example code yourself as you go — don't just skim.
2. **Complete the exercises** in `exercises/exercise_02.md`. There are six this week.
3. **Build the project** described in `project/PROJECT.md` — a real, useful unit converter.
4. **Update `progress_log.md`** with what you learned and what was tricky.
5. **Push everything to GitHub** using your new everyday workflow:
   ```
   git add .
   git commit -m "Add Week 2: variables, input, and unit converter"
   git push
   ```
6. **Come back to chat** with "Done with Week 2" + your repo link. I'll review and build Week 3 (which covers conditionals — making your programs *make decisions*).

---

# Quick Reference (Save This For Reuse)

```python
# Variables
name = "Chris"
age = 33

# Types
int(x), float(x), str(x), bool(x)
type(x)

# F-strings
print(f"Hi, {name}, age {age}!")
print(f"In 10 years: {age + 10}")
print(f"Price: ${price:.2f}")    # 2 decimal places

# Input
text = input("Prompt: ")           # always a string
number = int(input("How many? "))  # convert if you need a number
decimal = float(input("Price? "))  # convert for decimals
```

---

Off you go. By Friday, you'll have written your first program that real people could use. 🚀
