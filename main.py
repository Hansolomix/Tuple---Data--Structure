# Tuple items are enclosed in round brackets
# Tuple is ordered
# Tuple is immutable 
# Tuple elements do not need to be unique
# Elements can be of different data types

# '''
# Creating a tuple
# '''

# # Empty tuple
# tuple= ()
# # tuple can hold heterogeneous(different) data types
# tuple= ('cat', [4,3,2], (1,2,3))

# # plain comma-seperated values are tuples by default
# tuple= 1234, 4321, 'hello!'

# # single tuple
# tuple= 'hello', # <=== note trailing comma

# # single tuple parenthesis
# # it becomes just a string object without the trailing comma
# tuple= ('hello',) # <== note trailing comma 

# # looks like tuple, but not a tuple
# tuple= ('hello') # => <class 'str'>

'''
Access Tuple Elements
'''

# Accessing tuple elements by indexing
tuple= (  1234, 4321, 'Hello!' )
# access with index
tuple[0] 
print(tuple[0]) # output => 1234 
tuple[2]
print(tuple[2]) # output => Hello!

'''
Negative Indexing
'''

# Access with negative indexing
tuple= ( 1234, 4321, 'hello!' )
tuple[-1]
print(tuple[-1]) # output => hello!
tuple[-3]
print(tuple[-3]) # output # => 1234

'''
Slicing tuples in Python
'''

fruits= ('orange', 'apple', 'pear', 'grapes', 'banana' )

# beginning to the end
fruits[:]
print(fruits[:]) # => ('orange,'apple','pear','grapes','banana')

# index 2 to 5th item
fruits[2:5]
print(fruits[2:5]) # => ('pear','grapes','banana')

# remove last two items
fruits[:-2]
print(fruits[:-2]) # => ('orange','apple','pear')

# index 2 to the end
fruits[2:]
print(fruits[2:]) # => ('pear', 'grapes','banana')

# every nth(2nd) item
fruits[::2]
print(fruits[::2]) # => ('orange','pear','banana')

# reverse list
fruits[::-1]
print(fruits[::-1]) # => ('banana','grapes','pear','apple','orange')

'''
Changing a tuple
'''

fruits= ('orange', [1,2,3] )
# Attempt to change the immutable type
# fruits[0] = 'pear'# => TypeError: 'tuple' object does not support item assignment

# Change mustable list type
fruits[1][0] = 5
print(fruits) # => ('orange', [5,2,3] )

'''
Deleting a Tuple
'''

fruits= ('orange', [1,2,3] )
# cannot delete items
# del fruits[0] # output => TypeError: 'tuple' object does not support item deletion

# Can delete the entire tuple
# deletes successfully

# del fruits
# print(fruits)

'''
Tuple Methods
'''

# only has 2 in-built Methods
# print(dir(tuple))

fruits= ('orange', 'banana', 'orange')
fruits.count('orange')
print(fruits.count('orange'))
fruits.index('banana')
print(fruits.count('banana'))




