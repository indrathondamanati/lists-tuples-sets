a = [1, 2, 3]
b = [4, 5, 6]
a.extend(b)
print(a)

#clear the list
numbers = [1, 2, 3, 4, 5]
numbers.clear()
print(numbers)  

#index method
numbers = [1, 2, 3, 4, 5]
print(numbers.index(3))  

#count method
numbers = [1, 2, 3, 4, 5, 3]
print(numbers.count(3))

#sort numbers
numbers = [5, 2, 9, 1, 5, 6]
numbers.sort()
print(numbers)  
numbers.sort(reverse=True)
print(numbers)

#reverse method
numbers = [1, 2, 3, 4, 5]
numbers.reverse()
print(numbers)

#copy method
a = [1, 2, 3]
b = a.copy()
print(b)

number = [10, 20, 30, 40, 50, 60, 70, 80]
print(number[1:7:2])  
print(number[:3])
print(number[2:7])
print(number[::-1])

#tuples in python
#tuple is a collection of multiple values that is ordered and cannot be changed after creation
student = ("bhargavi" , 98, "python")
print(student[0])

#access value in a tuple
student = ("bhargavi" , 21, 85.5)
print(student[0])
print(student[1])
print(student[2])

#all
numbers = (10, 20, 30, 40)
print(len(numbers))
print(max(numbers))
print(min(numbers))
print(sum(numbers))

