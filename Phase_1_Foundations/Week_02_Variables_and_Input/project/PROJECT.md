# Week 2 Project: Unit Converter

> **Goal:** Build a real, useful program that takes input from the user, performs conversions, and prints results clearly.

---

## What You're Building

A Python program (`unit_converter.py`) that converts between common units of measurement. It will handle three categories:

1. **Temperature** (Fahrenheit ↔ Celsius)
2. **Length** (Miles ↔ Kilometers)
3. **Weight** (Pounds ↔ Kilograms)

For Week 2, your converter will do **all six conversions in a single run**, asking the user to type one value of each kind and showing the converted result.

(We'll make it interactive — letting the user *choose* which conversion to do — in Week 3, when we cover `if/else` decisions.)

---

## Sample Run

Here's what the program should do when run:

```
=== Unit Converter ===

TEMPERATURE
Enter a temperature in Fahrenheit: 72
72.0°F = 22.22°C

Enter a temperature in Celsius: 100
100.0°C = 212.0°F

LENGTH
Enter a distance in miles: 26.2
26.2 miles = 42.16 kilometers

Enter a distance in kilometers: 5
5.0 kilometers = 3.11 miles

WEIGHT
Enter a weight in pounds: 175
175.0 lbs = 79.38 kg

Enter a weight in kilograms: 70
70.0 kg = 154.32 lbs

=== All conversions complete! ===
```

Format the numbers to **2 decimal places** using f-strings (`{value:.2f}`).

---

## The Conversion Formulas

You'll need these. Don't worry about *why* they work — just use them.

| Conversion | Formula |
|---|---|
| Fahrenheit → Celsius | `(F - 32) * 5 / 9` |
| Celsius → Fahrenheit | `C * 9 / 5 + 32` |
| Miles → Kilometers | `miles * 1.609344` |
| Kilometers → Miles | `km / 1.609344` |
| Pounds → Kilograms | `pounds * 0.453592` |
| Kilograms → Pounds | `kg / 0.453592` |

---

## Requirements

Your program must:

1. **Use variables** with descriptive names (no single letters like `x` or `y`)
2. **Use `input()` and convert with `float()`** for every user input (so decimals work)
3. **Use f-strings** for every line of output (no `+` concatenation)
4. **Format all output values to 2 decimal places** (use `{value:.2f}`)
5. **Use blank `print()` calls** to space out sections cleanly
6. **Include section headers** ("TEMPERATURE", "LENGTH", "WEIGHT") to organize the output

---

## How to Build It (Suggested Approach)

**Build it one section at a time.** Run after every section. Don't write 50 lines and then try to debug.

1. **Step 1:** Create the file. Add the title print (`=== Unit Converter ===`) and run it.
2. **Step 2:** Do just the F → C conversion. Use `input()`, `float()`, and an f-string. Run it. Confirm it works.
3. **Step 3:** Add C → F. Run it. Confirm.
4. **Step 4:** Add the LENGTH section. Run it.
5. **Step 5:** Add the WEIGHT section. Run it.
6. **Step 6:** Read through the whole program. Polish formatting.

This **build-test-build** rhythm is the heart of professional development. Big things are built from small, verified pieces.

---

## Stretch Goals (Optional)

If the basic version felt easy, try one or more:

1. **Add a fourth conversion category** — your choice. Inches ↔ Centimeters? Gallons ↔ Liters? Hours ↔ Minutes? Pick something useful to you.

2. **Show the user's input rounded too:** notice in the sample output, `72°F` displays as `72.0°F` because of `:.2f` (which would show `72.00`) — actually, `:.2f` would show `72.00`. Try formatting the input value with `:.0f` (no decimals) when the user enters whole numbers. Subtle, but it teaches you formatting nuances.

3. **Make a fancier header** with ASCII art, like Week 1's `about_me.py`.

---

## Self-Review Checklist

Before calling it done:

- [ ] Program runs without errors when given valid number input
- [ ] All output uses f-strings (no `+` concatenation between text and variables)
- [ ] All numbers display to 2 decimal places
- [ ] Code uses meaningful variable names (`fahrenheit_value`, not `x`)
- [ ] Sections are visually separated with blank lines
- [ ] You typed it yourself, not copied from the lesson

---

## After You Build It

```
git add .
git commit -m "Add Week 2 project: unit converter"
git push
```

Update `progress_log.md` with:

- What clicked this week
- What was tricky (be specific — the more specific, the more helpful for future-you)
- One thing you're proud of

Then come back to chat: "Done with Week 2" + your repo link. I'll review your code and build Week 3 (conditionals — making programs make decisions).

---

You're going from "programs that print" to "programs that *interact*" this week. That's a real leap. Have fun. 🚀
