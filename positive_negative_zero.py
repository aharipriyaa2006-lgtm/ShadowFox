arr = [10, -5, 0, 20, -8, 0]

positive = negative = zero = 0

for i in arr:
    if i > 0:
        positive += 1
    elif i < 0:
        negative += 1
    else:
        zero += 1

print("Positive:", positive)
print("Negative:", negative)
print("Zero:", zero)
