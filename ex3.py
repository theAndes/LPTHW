# Exercise 3: Numbers and Math
# https://learnpythonthehardway.org/python3/ex3.html

# + plus
# - minus
# / slash
# * asterisk
# % percent
# < less-than
# > greater-than
# <= less-than-equal
# >= greater-than-equal

print("I will now count my chickens:")

# Order of operation:
# First: 30 / 6 = 5
# Nest: 25 + 5 = 30
print("Hens", 25 + 30 / 6)

# First: 25 * 3 = 75
# Next: 75 % 4 = 3  <<< 4 * 18 = 72 >>> 3 is remainder of 75 - 72
# Then: 100 - 3 = 97
print("Roosters", 100 - 25 * 3 % 4)

print("I will now count my eggs:")

# 3 + 2 + 1 (- 5) + (4 % 2) - (1 / 4) + 6
# 3 + 2 + 1 ((- 5) + 0) - .25 + 6
print(3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6)

print("Is it true that 3 + 2 < 5 -7?")
# Evaluate TRUE/FALSE
# First: 3 + 2 = 5
# Next: 5 - 7 = -2
# 5 is less than - 2 : FALSE!
print(3 + 2 < 5 - 7)

print("What is 3 + 2 ?", 3 + 2)
print("What is 5 - 7?", 5 - 7)

print("Oh, that's why it's False.")

print("How about some more.")

print("Is it greater?", 5 > -2)
print("Is is greater or equal?", 5 >= -2)
print("Is it less or equal?", 5 <= -2)
