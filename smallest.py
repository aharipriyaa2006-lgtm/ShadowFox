arr = [10, 20, 5, 40, 15]

smallest = arr[0]

for i in arr:
    if i < smallest:
        smallest = i

print("Smallest element:", smallest)
