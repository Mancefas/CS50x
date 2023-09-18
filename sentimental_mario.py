import cs50

# Prompt for user input with how height it need to be
while True:
    n = cs50.get_int("Positive number for height: ")
    if n >= 1 and n <= 8:
        break

# Building pyramids
for i in range(n):
    for e in range(n - i - 1):
        print(" ", end="")
    for k in range(i + 1):
        print("#", end="")
    print()
