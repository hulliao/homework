# 20variables.py

# The hash mark means the rest of the line is a comment
# Comments should be colored 'differently' in a code editor
# If all the lines are the same color, change settings or editor

print('hello world') # as seen before, now with trailing comment
print("go home") 
# Strings are surrounded by single-quotes or double-quotes
# Variables are containers that hold text, numbers, and other things

s = 'some text' # 's' is a variable, it now holds some text
print(s)

# In computer-speak, text is called a 'string'
# Strings are surrounded by single-quotes, double-quotes, or triple quotes
# Usually single-quotes are used

# The rest of this program is a huge triple quoted string!
# Move the triple quotes downward to uncover each line of code
# That's how all the rest of the tutorial programs work


# You can replace the contents of a variable easily

s = 'yo'
print(s)

o = 'great'
print(o) 

# Variables come in different 'flavors' that don't always mix

a = 1     # integer
b = 1.0   # floating point
c = '1'   # text

print(a + a)
print(a + b)
print(c) 

g = 20 # integer 
h = 22.2 # floating point
i = '12' # text

print(g + h) 
print(i) 

# You can figure out what type a variable is with the type() function
# Although at this point, that might be confusing

print(type(a))
print(type(b))
print(type(c))

# You can convert a variable from one type to another
# The int() function converts floats and strings to integers
# The float() function converts integers and strings to floats
# The str() function converts integers and floats to strings

print(a + int(b) + int(c))
print(float(a) + b + float(c))
print(str(a) + str(b) + c)

print(g + int(h) + int(i)) 

# Note that print() can take more than one argument separated by commas

print(s, a, b, c, 'convenient')
print(o, g, h, i, 'true') 

# Sometimes you want to create a variable but not give it a specific value
# Use the value None in these cases
# When in doubt, setting a variable to None is a good idea

v = None
print(v)
print(type(v)) 