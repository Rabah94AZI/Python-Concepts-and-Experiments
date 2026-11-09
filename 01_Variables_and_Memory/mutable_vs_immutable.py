
"""
Topic: Mutable vs Immutable Objects
"""

# TEST 1: Immutable - Integer
print("\n--- TEST 1: Integer ---")

a = 10
print("Before:", a, id(a))

a = a + 5
print("After:", a, id(a))

# A new integer object is referenced


# TEST 2: Immutable - String
print("\n--- TEST 2: String ---")

text = "Python"
print("Before:", text, id(text))

text = text + " Programming"
print("After:", text, id(text))

# Strings cannot be modified in place


# TEST 3: Mutable - List
print("\n--- TEST 3: List ---")

numbers = [1, 2, 3]
print("Before:", numbers, id(numbers))

numbers.append(4)
print("After:", numbers, id(numbers))

# Same object, modified content


# TEST 4: Mutable - Dictionary
print("\n--- TEST 4: Dictionary ---")

person = {"name": "Rabah"}
print("Before:", person, id(person))

person["age"] = 30
print("After:", person, id(person))

# Same dictionary object


# TEST 5: Shared references
print("\n--- TEST 5: Shared references ---")

a = [10, 20]
b = a

b.append(30)

print("a:", a)
print("b:", b)
print("a is b:", a is b)


# TEST 6: Copy a list
print("\n--- TEST 6: Copy ---")

a = [10, 20]
b = a.copy()

b.append(30)

print("a:", a)
print("b:", b)
print("a is b:", a is b)


# TEST 7: Tuple containing a list
print("\n--- TEST 7: Tuple ---")

data = (10, [20, 30])

print("Before:", data)
data[1].append(40)
print("After:", data)

# Tuple is immutable,
# but its nested list is mutable
