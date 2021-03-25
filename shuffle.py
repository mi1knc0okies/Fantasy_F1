import random

a = "sam"
b = 'stew'
c = 'jesse'
d = 'alex'

choices = a, b, c, d
picks = list(range(0, 4))
random.shuffle(picks)
for person in picks:
    print(choices[person])