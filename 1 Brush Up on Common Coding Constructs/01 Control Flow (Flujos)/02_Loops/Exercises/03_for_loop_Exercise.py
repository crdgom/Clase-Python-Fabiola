multiples = [x for x in range(20) if x % 3 == 0]

sum = 0
for num in multiples:
sum += num
print("Sum of multiples of 3 below 20 is:", sum)