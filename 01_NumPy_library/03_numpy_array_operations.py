import numpy as np


# 1. Identity Matrix
# An identity matrix has 1s on the diagonal and 0s elsewhere.
a = np.eye(4)
print("Identity Matrix:\n", a)


# 2. Diagonal Matrix
# A diagonal matrix is created by placing given values on the diagonal.
a = np.diag([10, 20, 30, 40])
print("Diagonal Matrix:\n", a)


# 3. Random Numbers
# randint generates random integers in a range.
# rand generates random float values between 0 and 1.

a = np.random.randint(1, 50, 5)
print("Random Integers:", a)

b = np.random.rand(5)
print("Random Floats:", b)


# 4. Seed
# Seed is used to get the same random values every time.
np.random.seed(2)
a = np.random.randint(1, 10, 5)
print("Seed Output:", a)


# 5. View vs Copy
# View shares memory with original array.
# Copy creates a new separate array.

a = np.array([1, 2, 3, 4, 5, 6])

view = a[1:4]
view[0] = 100
print("After View Change:", a)

a = np.array([1, 2, 3, 4, 5, 6])
copy = a[1:4].copy()
copy[0] = 100
print("Original after Copy:", a)
print("Copy Array:", copy)


# 6. arange
# arange creates values in a range (similar to a loop).

a = np.arange(1, 11)
print("Arange:", a)


# 7. Conditions / Filtering
# We can filter values using conditions.

a = np.arange(1, 21)

print("Greater than 10:", a[a > 10])
print("Even numbers:", a[a % 2 == 0])


# 8. Reshaping
# reshape changes the shape of array without changing total elements.

a = np.arange(1, 13)

print("2x6 Matrix:\n", a.reshape(2, 6))
print("3x4 Matrix:\n", a.reshape(3, 4))
