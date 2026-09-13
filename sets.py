#sets in python
#set is a collection of unique values that is unordered and mutable
numbers = {10,20,30,20,30}

print(numbers)

#why use sets
subjects = {"python", "java", "c++", "python"}
print(subjects)

#add valueto a set
subjects = {"python", "java", "c++"}
subjects.add("javascript")
print(subjects)

#remove value from a set
subjects = {"python", "java", "c++"}
subjects.remove("java")
print(subjects)

#dont allow duplicate values in a set
numbers = {10, 20, 30, 20, 30}
print(numbers)

#dictionary in python
#dictionary is a collection of key-value pairs that is unordered and mutable
student = {"name": "bhargavi", "age": 21, "grade": 85.5}

total_minutes = int(input("Enter total minutes: "))

hours = total_minutes // 60
minutes = total_minutes % 60
seconds = total_minutes % 60

print("Hours:", hours)
print("Minutes:", minutes)
print("Seconds:", seconds)


