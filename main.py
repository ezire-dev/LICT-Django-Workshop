# str, int, float, bool, list, tuple, set, dict, NoneType, bytes
# str methods: upper(), lower(), strip(), split(), replace(), find(), count()

# list methods: append(), extend(), insert(), remove(), pop(), clear(), index(), count(), sort(), reverse() 
# tuple methods: count(), index()
# set methods: add(), remove(), discard(), clear(), union(), intersection(), difference()
# dict methods: keys(), values(), items(), get(), update(), pop(), clear()



# string data type
name = "john"
name = name.upper()
print(name)


# integer data type
age = 30
age = age / 2
print (age)


# boolean data type
is_raining = True
if is_raining:
    print("Take an umbrella")
if  not is_raining:
    print("Enjoy the sunshine")


# NoneType data type
profile_picture = None
print("Before upload:")
print(profile_picture)
profile_picture = "profile.png"
print("\nAfter upload:")
print(profile_picture)


# Lists

students = ["John", "Ram", "Hari"]
print("Original list:")
print(students)

students.append("Tom")

students.remove("Ram")

print("\nUpdated list:")
print(students)

print("\nFirst student:")
print(students[0])

print("\nAll students:")
for student in students:
    print(student)


# Tuples

location = (27.7172, 85.3240)

print("Latitude:")
print(location[0])
print("\nLongitude:")
print(location[1])

lat, long = location

print("\nUsing unpacking:")
print("Lat:", lat)
print("Lon:", long)


# Sets
visitors = {"Ram", "Hari", "Sita"}

print("Original visitors:")
print(visitors)

visitors.add("Ram")

visitors.add("Sita")

print("\nAfter additions:")
print(visitors)

name = "Bob"

if name in visitors:
    print(f"\n{name} visited the site")


# Dictionaries

user = {
    "name": "Alice",
    "age": 25,
    "country": "Nepal"
}

print("User name:")
print(user["name"])

user["email"] = "alice@example.com"

user["age"] = 26

print("\nUpdated dictionary:")
print(user)

print("\nAll details:")

for key, value in user.items():
    print(key, ":", value)

