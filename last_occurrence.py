arr = [2, 4, 6, 4, 8]

key = 4

last = len(arr) - 1 - arr[::-1].index(key)

print("Last Occurrence:", last)
