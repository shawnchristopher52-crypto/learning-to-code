# The correct way to acheive this
correct_age = int(input("How old are you? "))
correct_years_to_100 = 100 - correct_age
print(f"You'll be 100 in {correct_years_to_100} years.")

# This prompt received a TypeError on line 2 (now line 9). We did not set age to int so the input is treated as str. This breaks line 2 (line 9)
# because you cannot add an int to a str.
age = input("How old are you? ")
years_until_100 = 100 - age
print(f"You'll be 100 in {years_until_100} years.")
