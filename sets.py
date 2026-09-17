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

#access elements in dic
std= {"name": "bhargavi", "age": 21, "grade": 85.5}
print(std["name"])
print(std["age"])
print(std["grade"])

#change value in dic
std["age"] = 11
print(std["age"])


#add new data to a dic
std["city"] = "vijaywada"
print(std)

#remove data
std.pop("city")
print(std)


std= {"name": "bhargavi", "age": 21, "course": "python"}
print(std.items())
#items() return all key-value pairs
print(std.get("name"))
#get() returns the value of specified key

std.update({"age": 17})
#update() updates the value of the specified key

print(std)

std.pop("age")
#pop() removes the specified key and its value

print(std)

#popitem() removes the last inserted key value pair
std= {"name": "bhargavi", "age": 21, "course": "python"}
std.popitem()
print(std)

std.setdefault("age", 21)
print(std)

#clear method
std.clear()
print(std)

new_std = std.copy()
print(new_std)




