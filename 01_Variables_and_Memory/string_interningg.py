
"""
Topic: String Interning in Python
"""

import sys

# TEST 1: Without interning
print("\n--- TEST 1: Without interning ---")

a = "hello world"
b = "".join(["hello", " world"])

print("a == b:", a == b)
print("a is b:", a is b)
print("id(a):", id(a))
print("id(b):", id(b))


# TEST 2: With sys.intern()
print("\n--- TEST 2: With interning ---")

a = sys.intern(a)
b = sys.intern(b)

print("a == b:", a == b)
print("a is b:", a is b)
print("id(a):", id(a))
print("id(b):", id(b))


# TEST 3: Multiple strings
print("\n--- TEST 3: Multiple strings ---")

words = [
    "".join(["python", " programming"])
    for _ in range(3)
]

interned_words = [
    sys.intern(word)
    for word in words
]

print("Before interning:",
      words[0] is words[1])

print("After interning:",
      interned_words[0] is interned_words[1])


# TEST 4: Memory size
print("\n--- TEST 4: Memory size ---")

text = "Python programming"

print("String size:", sys.getsizeof(text), "bytes")
