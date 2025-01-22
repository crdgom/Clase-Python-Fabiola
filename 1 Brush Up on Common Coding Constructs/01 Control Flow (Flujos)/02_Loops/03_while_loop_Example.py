count = 5

""" while count > 0:
    print("Counting down:", count)
    count -= 1

print("Blast off!") """

sum = 0

while True:
    sum += count
    count -= 1

    if count == 0:
        break

print(f"Sum of first {5} natural numbers: {sum}")