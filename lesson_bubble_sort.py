import numpy as np 
n = 6
bubbles = np.random.choice(10, n, replace=False)
print(list(bubbles))

# n = 6
# r0:max_idx5, r1:max_idx4, r2:max_idx3, r3:max_idx2 ==> r + max_idx = 5, idx <= n - 1 - r
# Time Complexity = O(n**2)
for round, _ in enumerate(bubbles):
    for index, _ in enumerate(bubbles):
        if index < n - round - 1:
            print(f"Round:{round}, i:{bubbles[index]}, j:{bubbles[index + 1]}")
            print(f"Bubbles before: {bubbles}")
            if bubbles[index] > bubbles[index + 1]:
                temp = bubbles[index + 1]
                bubbles[index + 1] = bubbles[index]
                bubbles[index] = temp
            print(f"Bubbles  after: {bubbles}")

# print(sorted(bubbles))