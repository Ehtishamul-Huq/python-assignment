#1 Given a list of numbers, write a Python program to find the sum of all the elements in the list.?
i = 1
j = 3
arr = [2,4,5,10]
n = 0
while i<=j:
	n += arr[i]
	i += 1
print(n)

#2 Given an array of integers arr[] of size N and an integer, the task is to rotate the array elements to the left by d positions.? 
d = 2
arr = [1,2,3,4,5,6,7]
print(arr[d:] + arr[:d])

#3 Second most repeated word in a sequence in Python?
arr = ["aaa", "bbb", "ccc", "bbb",
"aaa", "aaa"]
from collections import Counter
import imp
dict_arr = Counter(arr)
value = sorted(dict_arr.values(), reverse=True)
second_large = value[1]
for key,val in dict_arr.items():
	if val == second_large:
		print(key)
		break

#4 Difference between two lists ?
list1 = [10, 15, 20, 25, 30, 35, 40]
list2 = [25, 40, 35]
new_list = []
[new_list.append(i) for i in list1 if i not in list2]
even_list = [i for i in new_list if i % 2 == 0]
odd_list = [i for i in new_list if i%2 != 0]
print(even_list + odd_list)

#5 Print all positive numbers from given list using for loop Iterate each element in the list using for loop and check if number is
# greater than or equal to 0. If the condition satisfies, then only print the number.?
list1 = [12, -7, 5, 64, -14]
print([i for i in list1 if i >= 0])

#6 Write a Python program to flatten a given nested list structure.?
original_list =    [0, 10, [20, 30], 40, 50, [60, 70, 80], [90, 100, 110, 120]]
flat_list = []
for num in original_list:
	if type(num) is list:
		for i in num:
			flat_list.append(i)
	else:
		flat_list.append(num)
print(flat_list)

# Strings
#1 Missing characters to make a string Pangram.?
string1 = 'welcome to geeksforgeeks'

alphabets = 'abcdefghijklmnopqrstuvwxyz'
new_string = ''
for i in alphabets:
	if i not in string1:
		new_string += i
print(new_string)

#2  Find total number of non-empty substrings of a string with N characters.?
string2 = 'abcd'

n = len(string2)
print(n*(n+1)/2)

#3 Write a Python program that accepts a comma separated sequence of words as input and prints the unique words in sorted form.
words = list(input("Enter words (separated by comma): ").split(','))
print('Unique words in sorted form: ', sorted(set(words)))

#4 Write a Python program to count the number of characters (character frequency) in a string.
string5 = 'google.com'
count_result = {}
for i in string5:
	if i not in count_result:
		count_result[i] = 1
	else:
		count_result[i] += 1
print(count_result)

#5 find the frequency of minimum occurring character in a python string 
string6 = 'google.com'
count_result = Counter(string6)
res = min(count_result, key = count_result.get)
print(res)

#6  Write a program extract all the string characters which have odd number of occurrences
string7 = 'geekforgeeks is best for geeks'
uniq_char = set(string7)
res = []
for i in uniq_char:
	if string7.count(i) % 2 != 0:
		res.append(i)
print(res)

#Dictionary
#1 Given a list and dictionary, map each element of list with each item of dictionary, forming nested dictionary as value.
test_dict = {'Gfg' : 4, 'best' : 9}
test_list = [8, 2]
result = {}
for key,val in zip(test_list,test_dict.items()):
	result[key] = dict([val])
print(result)

#2 Sort Dictionary key and values List
test_dict = {'c': [3], 'b': [12, 10], 'a': [19, 4]}
print(dict(sorted(test_dict.items())))

#3 Remove all duplicates words from a given sentence 
string5 = 'Python is great and Java is also great'
string_dict = dict(Counter(string5.split()))
print(' '.join(string_dict))

#4 Inversion in nested dictionary?
from collections import defaultdict
test_dict = {'b': {'a': {}}, 'e': {'d': {}}, 'g': {'f': {}}}
flipped = defaultdict(dict)
for key, val in test_dict.items():
    for subkey, subval in val.items():
        flipped[subkey][key] = subval
print(dict(flipped))

#5 Given an array of n string containing lowercase letters. Find the size of largest subset of string which are anagram of each others. 
# An anagram of a string is another string that contains same characters, only the order of characters can be different. 
# For example, “abcd” and “dabc” are anagram of each other.?
anagram_input = 'ant magenta magnate tan gnamate'
splitted_list = anagram_input.split()
sorted_list = []
for i in range(len(splitted_list)):
	sorted_list.append(''.join(sorted(splitted_list[i])))
print(max(dict(Counter(sorted_list)).values()))

#Sets
#1 Given two lists a, b. Check if two lists have at least one element common in them.
a = [1, 2, 3, 4,5]
b = [5, 6, 7, 8, 9]
combined_list = a + b
print(combined_list != list(set(combined_list)))

#2 Return a new set of identical items from two sets
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
result_set = set()
for i in set1:
	if i in set2:
		result_set.add(i)
print(result_set)

#3 Maximum and Minimum in a Set without use of inbuild max/min functions
set1 = ([8, 16, 24, 1, 25, 3, 10, 65, 55])
max_value = set1[0]
for i in range(1,len(set1)):
	if set1[i] > max_value:
		max_value = set1[i]
print(max_value)
set2 = ([4, 12, 10, 9, 4, 13])
min_value = set2[0]
for i in range(1,len(set2)):
	if set2[i] < min_value:
		min_value = set2[i]
print(min_value)

#4 Write a Python program to check if a set is a subset of another set 
# a set A is a subset of a set B if all elements of A are also elements of B; B is then a superset of A.
x= {'mango', 'apple'}
y= {'mango', 'orange'}
z= {'mango'}
print(x.issubset(y))
print(y.issubset(x))
print(y.issubset(z))
print(z.issubset(y))

#5 Write a Python program to remove the intersection of a 2nd set from the 1st set
a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}
for i in a.intersection(b):
	a.remove(i)
print(a)
print(b)

#Tuple
#1 Remove Tuples of Length K
test_list = [(4, 5), (4, ), (8, 6, 7), (1, ), (3, 4, 6, 7)]
K = 2
for i in test_list:
	if len(i) == K:
		test_list.remove(i)
print(test_list)

#2 Removing duplicates from tuple
original_tuple = (1, 3, 5, 2, 3, 5, 1, 1, 3)
print(tuple(set(original_tuple)))

#3 Flatten tuple of List to tuple
test_tuple = ([5], [6], [3], [8])
print(tuple(sum(test_tuple,[])))

#4 Remove nested records from tuple
nested_tuple = (1, 5, 7, (4, 6), 10)
res = []
for i in nested_tuple:
	if type(i) is not tuple:
		res.append(i)
print(tuple(res))

#5 Convert Binary tuple to Integer?
binary_tuple = (1, 1, 0, 1, 0, 0, 1)
x = ''.join(list(map(str,binary_tuple)))
res = int(x,2)
print(res)

# MAP & Lambda Function
#1 Write a Python program to add three given lists using Python map and lambda.?
nums1 = [1, 2, 3] 
nums2 = [4, 5, 6] 
nums3 = [7, 8, 9]
result = map(lambda x,y,z: x+y+z, nums1,nums2,nums3)
print(list(result))

#2 Write a Python program to convert a given list of tuples to a list of strings using map function?
original_list = [('red', 'pink'), ('white', 'black'), ('orange', 'green')]
result = list(map(' '.join, original_list))
print(result)

#3 Write a Python program to add two given lists and find the difference between lists. Use map() function
num1 = [6, 5, 3, 9]
num2 = [0, 1, 7, 7]
print(list(map(lambda x,y: (x + y, x - y) , num1, num2)))

#4 Write a Python program to find intersection of two given arrays using Lambda
array_nums1 = [1, 2, 3, 5, 7, 8, 9, 10]
array_nums2 = [1, 2, 4, 8, 9]
print(list(filter(lambda x: x in array_nums1, array_nums2)))

#5 Write a Python program to find palindromes in a given list of strings using Lambda
list1 = ['php', 'w3r', 'Python', 'abcd', 'Java', 'aaa']
print(list(filter(lambda x: x == x[::-1], list1)))

#6 Write a Python program to find the list with maximum and minimum length using lambda
list6 = [[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]
max_len = max(len(x) for x in list6)
max_list = max(list6, key= lambda i:len(i))
print(max_len,max_list)
min_len = min(len(x) for x in list6)
min_list = min(list6, key=lambda i: len(i))
print(min_len,min_list)

#7 Write a Python program to triple all numbers of a given list of integers.?
list7 = (1, 2, 3, 4, 5, 6, 7)
print(list(map(lambda x: x *3, list7)))

#List Comprehension
#1 Use a nested list comprehension to find all of the numbers from 1–101 that are divisible by any single digit besides 1 (2–9)
res = set([num for num in range(1,101) for n in range(2,10) if num % n == 0])
print(list(res))

#2 Use list comprehension to construct a new list but add 6 to each item
new_list = [x+6 for x in range(10)]
print(new_list)

#3 Suppose we want to create an output dictionary which contains only the odd numbers that are present in the input list as keys and
#  their cubes as values.
input1 = [1, 2, 3, 4, 5, 6, 7]
res = {i:i**3 for i in input1 if i%2 != 0}
print(res)

#4 Given two lists containing the names of states and their corresponding capitals, construct a dictionary which maps the states with
#  their respective capitals.
state = ['Gujarat', 'Maharashtra', 'Rajasthan']
capital = ['Gandhinagar', 'Mumbai', 'Jaipur']
print({state[i]:capital[i] for i in range(len(state))})

#5 Transpose of Matrix using Comprehension
matrix = [[1, 2, 3, 4], [4, 5, 6, 8]]
transpose = [[matrix[i][j] for i in range(len(matrix))] for j in range(len(matrix[0]))]
print(transpose)

#6 We have a string ‘2459a09b’ and we want to extract all integer literals, and use int() to cast them into integers.
string1 = '2459a09b'
res = (list(map(int, filter(lambda s: ord(s) >=49 and ord(s) <= 57, string1))))
print(res)

#7 Finding the elements in a list in which elements are ended with the letter ‘b’ and the length of that element is greater than 2?
names = ['Ch','Dh','Eh','cb','Tb','Td','Chb','Tdb']
print([i for i in names if i[-1] == 'b' and len(i)>2])

#8 Reverse each String in a Tuple using list comprehension
string_list = ('Hello', 'Analytics', 'Vidhya')
print([i[::-1] for i in string_list])

#Object oriented programming
#1 Define a property that must have the same value for every class instance (object)?
class Vehicle:
	def __init__(self,color,speed,mileage):
		self.color = color
		self.speed = speed
		self.mileage = mileage
Audi = Vehicle('White',200, 18)
print(Audi.color, Audi.speed,Audi.mileage)

#2 Create a class with property decorator with setter and getter functions.?
class Person:
	def __init__(self):
		self._age = 0
	@property
	def age(self):
		print('getter method called')
		return self._age
	@age.setter
	def age(self, a):
		if (a<18):
			raise ValueError('Sorry your age is below eligibility criteria')
		print('setter method called')
		self._age = a

Dad = Person()
Dad.age = 30
Son = Person()
Son.age = 19
print(Dad.age)
print(Son.age)

#3 Create a class with Multi-level Inheritance ?
class Student:
	def __init__(self):
		self.name = input('Name: ')
		self.gender = input('Gender: ')
	def printStudent(self):
		print(self.name)
		print(self.gender)
class StudentMarks(Student):
	def __init__(self):
		super(StudentMarks, self).__init__()
		self.test1 = int(input('Enter marks for test1: '))
		self.test2 = int(input('Enter marks for test2: '))
	def printMarks(self):
		print(self.test1)
		print(self.test2)
student1 = StudentMarks()
student1.printStudent()
student1.printMarks()

#4 write a decorator for a class?
class MyDecorator:
	def __init__(self,function):
		self.function = function
	def __call__(self):
		print('Welcome!')
		self.function()
		print('The End')
@MyDecorator
def function():
	print('GeeksforGeeks')
function()

#5 Explain What happens you create a object of a class (Inside python)?
'''
Each time when you create an object of class the copy of each data variables defined in that class is created. 
In simple language we can state that each object of a class has its own copy of data members defined in that class.
'''

#6 Create a class whose object should be called like a function.?
class Product:
	def __init__(self):
		print('Instance created')
	def __call__(self,x,y):
		return x*y
answer = Product()
print(answer(10,20))

#7 Implement a Queue
class Queue:
	def __init__(self):
		self.instack = []
		self.outstack = []
	def enqueue(self,element):
		self.instack.append(element)
	def dequeue(self):
		while self.instack:
			self.outstack.append(self.instack.pop())
		return self.outstack.pop()
q = Queue()
for i in range(5):
	q.enqueue(i)
for i in range(5):
	print(q.dequeue())

#8 Implement a Linked List
class Node(object):
	def __init__(self,value):
		self.value = value
		self.nextnode = None
a = Node(1)
b = Node(2)
c = Node(3)
a.nextnode = b
b.nextnode = c
print(a.nextnode)
print(a.value)
print(a.nextnode.value)
print(b.value)
print(b.nextnode.value)
print(c.value)

#9 Implement a stack
class Stack:
	def __init__(self):
		self.stack = []
	def push(self,value):
		self.stack.append(value)
	def pop(self):
		(self.stack.pop())
s = Stack()
for i in range(5):
	s.push(i)
print('Initial stack: {}'.format(s.stack))
for i in range(5):
	s.pop()
print('Stack after elements are popped: ',s.stack)

#Exception Handling
#1 Write Custom Exception to handle Zero division Error
try:
	9/0
except ZeroDivisionError:
	print('Division by zero is not possible')

#2 Catching specific exception in Python
try:
	strin = 'abcd'
	print(strin[4])
except Exception as e:
	print(e)