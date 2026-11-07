
"""
Python Concepts and Experiments
Topic: Equality (==) vs Identity (is)
"""

# TEST 1: Integers
print("\n--- TEST 1: Integers ---")

a = 1000
b = int("1000")

print("a == b:", a == b)
print("a is b:", a is b)
print("id(a):", id(a))
print("id(b):", id(b))


# TEST 2: Strings
print("\n--- TEST 2: Strings ---")

a = "hello world"
b = "".join(["hello", " world"])

print("a == b:", a == b)
print("a is b:", a is b)
print("id(a):", id(a))
print("id(b):", id(b))


# TEST 3: Lists
print("\n--- TEST 3: Lists ---")

a = [1, 2, 3]
b = [1, 2, 3]
c = a

print("a == b:", a == b)
print("a is b:", a is b)
print("a is c:", a is c)


# TEST 4: Dictionaries
print("\n--- TEST 4: Dictionaries ---")

a = {"name": "Python", "version": 3}
b = {"name": "Python", "version": 3}

print("a == b:", a == b)
print("a is b:", a is b)


# TEST 5: Tuples
print("\n--- TEST 5: Tuples ---")

a = tuple([1, 2, 3])
b = tuple([1, 2, 3])

print("a == b:", a == b)
print("a is b:", a is b)


# TEST 6: None
print("\n--- TEST 6: None ---")

a = None
b = None

print("a == b:", a == b)
print("a is b:", a is b)
