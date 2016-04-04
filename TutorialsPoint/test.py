
print ("Hello Python")
# this is a comment

# waiting for the user 
#input("\n\n Press the enter key to exit")

# multiple ways to assign variables
a = b = c = 1
d,e,f = 1,2,"john"
str = "Hello World"
print (str)
print (str[0])
print (str[2:3])
print (str[2:])
print (str * 2)
print (str + "TEST")

list = ['abcd', 786, 2.23, 'john', 70.2]
tinylist = [123, 'john']
print(list)
print(list[0])
print(list[1:3])
print(list[2:])
print(tinylist * 2)
print(list + tinylist)

#tuples section
#tuples are read only lists, i.e you cannot change them after instatntian

tuple = ('abcd', 786, 2.23, 'john', 70.2)
tinytuple = (123, 'jon')
print(tuple)
print(tuple[0])
print(tuple[1:3])
print(tuple[2:])

#dictionaries
#equivalent to hash tables
#dictionaries are undordered
dict = {}
dict['one'] = "This is one"
dict[2] = "This is two"
tinydict = {'name': 'john', 'code':6734, 'dept' : 'sales'}
print(dict['one'])
print(dict[2])
print(tinydict)
print(tinydict.keys())
print(tinydict.values())

# binary stuff
a = 60
b = 13
print(bin(a&b))
test = "string"
if "string" is test:
	print 1

var = 100
if(var == 100):
	print ("Value of expression is 100")
else:
	print 2

count = 0
while(count < 9):
	print 'The count is', count
	count = count + 1
else:
	print "done"

# for loops
for letter in 'Python':
	print 'Current letter is:', letter

fruits = ['banana', 'apple', 'mango']
for index in range(len(fruits)):
	print 'Current fruit:', fruits[index]

#break and continue examples
# pass examples
# pass is a null operation but nothing happens when it executes. 
# kind of like a stub
for letter in 'Python':
	if letter == 'h':
		pass
		print "this is a pass"
	print "this is the current letter", letter

#itertors
#String, Lists, tuples can be used by iterators
list = [1,2,3,4]
it = iter(list) # builds an iterataor object

print(next(it))

# Strings 
# you can update strings by reassigning the variable to another string
#e.g.
var1 = "Hello World"
print("Updated string:- ", var1[:6] + "Python")

#strings manipulation
print("My name is %s and weight is %d kg!" % ('Brian', 21))
para_str = """this is a long string that is made up of
several lines and non-printable characters such as 
TAB (\t) and they will show up that way when displayed.
NEWLINES within the string, whether explicitly given like this within
the brackets [\n], or just a NEWLINE within the variable assignment
will also show up"""
print(para_str)

#print the raw string using r
# bunch of didfferent string commands
print(r'C:\\nowhere')

# lists in depth

list1 = ['physics', 'chemistry', 1997, 2000]
list2 = [1,2,3,4,5,6,7]
print("list2[1:5]", list2[1:5])

# remove elements in list by del list1[index]
# usage of different list operations
list1 = [1,2,3,3,4,5]
print list1.count(3)
print max(list1)
print min(list1)

tup1 = ('physics', 'chemistry', ' 1997', 2000)

# dictionaries
dict = {'Name':'Zara', 'Age':7, 'Class':'First'}
print("dict[Name]", dict['Name'])
dict['Age'] = 8
print("dict['Age']", dict['Age'])
dict['School'] = 'DPS School'
print(dict.keys())
print(dict.has_key('Name'))
#clear dictionary dict.clear()
# delete entire dictionary del dict
# delete one entry del dict['Name']

#functions 
def printme(str):
	print(str)
	return

printme("hello")

def printinfo(name, age):
	print("Name is ", name)
	print("Age is ", age)
	return

def alwaysprintage35(name, age=35):
	print("Name", name)
	print("Age", age)
	return
alwaysprintage35("Brian")
alwaysprintage35("Brian", 50)

printinfo(age=50, name="Brian")


# all paramets in Python are passed by reference














