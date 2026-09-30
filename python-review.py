# Auto-generated from python-review.ipynb (percent format). Edit the notebook, not this file.

# %% [markdown]
# # Assigment (FEOMI) - Python Review

# %% [markdown]
# ## Lab 2.2.

# %%
# Supplied code
print("    *")
print("   * *")
print("  *   *")
print(" *     *")
print("***   ***")
print("  *   *")
print("  *   *")
print("  *****")

# %%
#2.2 (1) Minimize the code
print("    *\n   * *\n  *   *\n *     *\n***   ***\n  *   *\n  *   *\n  *****")

# %%
#2.2 (2) Make the arrow twice as large
print("        **\n\n      **  **\n\n    **      **\n\n  **          **\n\n******      ******\n\n    **      **\n\n    **      **\n\n    **********")

# %%
#2.2 (3) Duplicate the arrow and put both arrows side - Trial 1 failed, I duplicated the entire block but couldn't get it to the side

print("        **\n\n      **  **\n\n    **      **\n\n  **          **\n\n******      ******\n\n    **      **\n\n    **      **\n\n    **********\n" * 2)

# %%
#2.2 (3) Duplicate the arrow and put both arrows side - Worked

print(("        **        " * 2) + "\n\n" +
      ("      **  **      " * 2) + "\n\n" +
      ("    **      **    " * 2) + "\n\n" +
      ("  **          **  " * 2) + "\n\n" +
      ("******      ******" * 2) + "\n\n" +
      ("    **      **    " * 2) + "\n\n" +
      ("    **      **    " * 2) + "\n\n" +
      ("    **********    " * 2))

# %%
#2.2 (4) Remove any quotes and observe the error

"""
print(("        **         * 2) + "\n\n" +
      ("      **  **      " * 2) + "\n\n" +
      ("    **      **    " * 2) + "\n\n" +
      ("  **          **  " * 2) + "\n\n" +
      ("******      ******" * 2) + "\n\n" +
      ("    **      **    " * 2) + "\n\n" +
      ("    **      **    " * 2) + "\n\n" +
      ("    **********    " * 2))
"""
# Error: SyntaxError: unexpected character after line continuation character
# Removing a quotation mark causes a SyntaxError. The error marker may appear later in the line rather than exactly where the missing quote is, because Python continues parsing until it reaches an invalid sequence.

# %%
#2.2 (5) Remove any parentheses and observe the error

"""
print(("        **        " * 2) + "\n\n" +
      ("      **  **      " * 2) + "\n\n" +
      ("    **      **    " * 2) + "\n\n" +
      ("  **          **  " * 2 + "\n\n" +
      ("******      ******" * 2) + "\n\n" +
      ("    **      **    " * 2) + "\n\n" +
      ("    **      **    " * 2) + "\n\n" +
      ("    **********    " * 2))
"""

# Error: IncompleteInputError: incomplete input

# Removing a parenthesis can make Python think the statement is unfinished. It may report the error at the end of the code rather than exactly where the missing parenthesis should have been.

# %%
#2.2 (6) Change the print() function to Print()

"""
Print(("        **        " * 2) + "\n\n" +
      ("      **  **      " * 2) + "\n\n" +
      ("    **      **    " * 2) + "\n\n" +
      ("  **          **  " * 2) + "\n\n" +
      ("******      ******" * 2) + "\n\n" +
      ("    **      **    " * 2) + "\n\n" +
      ("    **      **    " * 2) + "\n\n" +
      ("    **********    " * 2))
"""

# NameError: name 'Print' is not defined

# Python is case-sensitive. print() is valid, while Print() is treated as a different name and causes a NameError if it has not been defined.

# %%
#2.2 (7) Change some of the double quotes to apostrophes/single quotes.


print(("        **        " * 2) + "\n\n" +
      ("      **  **      " * 2) + "\n\n" +
      ('    **      **    ' * 2) + "\n\n" +
      ("  **          **  " * 2) + "\n\n" +
      ("******      ******" * 2) + "\n\n" +
      ('    **      **    ' * 2) + "\n\n" +
      ('    **      **    ' * 2) + "\n\n" +
      ("    **********    " * 2))


# No Error

# Python accepts both single quotes '...' and double quotes "..." for strings. They behave the same in normal cases, but the opening and closing quote must match.

# %%
#2.2 (7) Change some of the double quotes to apostrophes and double quotes combination.

"""
print(("        **        " * 2) + "\n\n" +
      ("      **  **      " * 2) + "\n\n" +
      ('    **      **    " * 2) + "\n\n" +
      ("  **          **  " * 2) + "\n\n" +
      ("******      ******" * 2) + "\n\n" +
      ("    **      **    ' * 2) + "\n\n" +
      ('    **      **    ' * 2) + "\n\n" +
      ("    **********    " * 2))
"""

# Error: SyntaxError: unterminated string literal

# Single quotes and double quotes both work for Python strings. However, each string must use matching opening and closing quotation marks. Mixing them incorrectly causes a SyntaxError.

# %%
print('"I\'m" \n' '""Learning"" \n' '"""Python"""')

# %%
print(0.0000000000000000000001)

#Python displays very small floating-point #s using scientific notation

# %%
print(0o123)

#0o means the # is written in octal (base 8). Python prints the decimal value.

# %%
print(0x123)

#0x means the # is hexadecimal (base 16). Python prints its decimal value.

# %%
print("2")

# 2 here is a string

# %%
print(2)

# 2 here is an integer

# %%
print('"Hello" is a string \n')

print('"007" is a string \n')

print('"1.5" is a string \n')

print(2.0)
print("2.0 is a float \n")

print(528)
print("528 is an integer \n")

print(False)
print("False is a boolean \n")

# %% [markdown]
# ## Lab 2.3 Exercise

# %%
john = 3
mary = 5
adam = 6

total_apples=john+mary+adam

print(f"The no. of Apples for John, Mary and Adam are the following respectively: {john}, {mary}, {adam} ")
print(f"The total no. of apples is = {total_apples}")

#f before the string allows variables inside { } to be replaced with their actual values

# %% [markdown]
# ### Personal Experimentation of Lab 2.3's Exercise

# %%
john = 3
mary = 5
adam = 6

total_apples=john+mary+adam

equal_div=round(total_apples/3, 2) #limits the float to 2dp

new_total=(john*3)+mary+adam

print(f"The no. of Apples for John, Mary and Adam are the following respectively: {john}, {mary}, {adam} ")
print(f"The total no. of apples is = {total_apples}.\n If the total is shared equally amongst the 3, it will be: {equal_div} apples per person")

print(f"If John has thrice the current # of apples, the new total will be: {new_total}")

#f before the string allows variables inside { } to be replaced with their actual values

# %% [markdown]
# ## Lab 2.4 Exercise

# %%
kms=12.25
miles=7.38
conv_val=1.61

miles_to_kms=miles*conv_val
kms_to_miles=kms/conv_val

#Miles to Kms
print(miles, "miles is", round(miles_to_kms,2), "kilometers")

#Kms to Miles
print(kms, "kms is", round(kms_to_miles, 2), "miles")

# %% [markdown]
# The optimized version improves readability by storing the conversion factor in a separate variable, avoiding repeated values. It also uses f-strings for clearer output formatting and :.2f to display results to two decimal places.

# %% [markdown]
# ## Lab 2.6 Exercise

# %%
#Improved Code

#Calculates # of seconds in a set # of hrs

hrs=2
sec_in_1hr=3600

print("Num of hours is:", hrs)

print(hrs*sec_in_1hr, "seconds are in", hrs, "hours")

print("Kwaheri")

# %% [markdown]
# ####Lab 2.6 mini-tests

# %%
#a

var=2
var=3

print(var)

#It'll print the last value. The 2nd assignment overwrites the 1st one.

# %%
#b

a='1'
b='1'

print(a+b)

# + here performs string concatenation not numerical addition since both values are now strings this if a=3 and b=8; a+b=38 

# %%
#c
a=6
b=3
a/=2*b

print(a)

# a= (a= 6/(2*3))
# new a=6/6=1

# %%
#d

"""
my_var
m 
101
averylongvariablen
ame 
m101
m 101
Del 
del 
"""

#Error: SyntaxError: invalid syntax (m 101)

# %%
"""
my_var
# Valid variable name
# Underscores are allowed.

m
# Valid variable name
# A single letter can be a variable name.

101
# Invalid variable name
# A variable name cannot begin with a number.

averylongvariablename
# Valid variable name
# Variable names can be long.

m101
# Valid variable name
# Digits are allowed after the first character.

m 101
# Invalid variable name
# Spaces are not allowed in variable names.

Del
# Valid variable name
# Python is case-sensitive, so "Del" is different from the keyword "del".

del
# Invalid variable name
# "del" is a reserved Python keyword.
"""

# %%
#e

# print("String #1")
print("String #2")

#The first line is commented thus it won't be rendered

# %%
#f

# This is a multiline comment. #
print("Hello!")

#That is not a multi-line comment that's why it has rendered the print hello function.

# %% [markdown]
# ## Lab 2.7 Execises

# %%
#lab 2.7 - task 1
start_hour = int(input("Enter the starting hour: "))
start_minute = int(input("Enter the starting minute: "))
duration = int(input("Enter the duration in minutes: "))

total_minutes = (start_hour * 60 + start_minute + duration) % 1440

print(f"End time: {total_minutes // 60:02d}:{total_minutes % 60:02d}")

# %% [markdown]
# The optimized version combines the conversion to minutes, duration addition, and 24-hour wrap-around into one calculation. It also uses an f-string instead of .format(), making the output shorter and easier to read. The // operator extracts the hour, while % extracts the remaining minutes.

# %%
#lab 2.7 - task 2

print("My name is %s %d %f." % ('Anshuman',1,14.6), "That's it \n")

# %s → inserts a string: 'Anshuman'
# %d → inserts an integer: 1
# %f → inserts a float: 14.6, displayed by default as 14.600000
# The values are substituted in the same order they appear in the tuple.

print("episode:{}/{}, time: {}, rep: {}, Session: {:.2}".format("friends", 13, 12.30, 2, 5.786), "\n")

# {} inserts values in order.
# {:.2} formats the number to 2 significant digits.
# .format() supplies values to the placeholders from left to right.

name="ABX"
type_of_company="XYZ"
print(f"{name} is an {type_of_company} company.")

# The f before the string enables f-string formatting.
# Values inside { } are replaced with the current values of the variables.

# %% [markdown]
# ### Table 1 (Lab 2.7)
# -------------------------------------------------------------------------------------------

# %%
2 == 2

# %%
#lab 2.7 - task 2

2 ==2

# %%
x=5
y=10
z=8

print(x>y)
print(y>z)

# %%
x,y,z = 5, 10, 8

print(x>y)
print((y - 5) == x)

# %%
x,y,z = 5, 10, 8
x,y,z = z, y, x #new values: x=8, y=10, z=5

print(x > z)
print((y-5) == x)

# %%
x = 10
if x == 10:
    print(x == 10)
    #True
if x > 5:
    print(x > 5)
    # True
if x < 10:
    print(x < 10)
else:
    print("else")

# %% [markdown]
# ### Table 2 (Lab 2.7)
# -------------------------------------------------------------------------------------------

# %%
n = 3

while n > 0:
    print(n + 1)
    n -= 1
else:
        print(n)

# The loop runs while n is greater than 0.
# Each iteration prints n + 1, then decreases n by 1.
# When n becomes 0, the while condition becomes False and the else block runs.
# Output: 4, 3, 2, 0

# %%
n = range(4)

for num in n:
    print(num - 1)
else:
    print(num)

# range(4) produces 0, 1, 2, 3.
# The loop prints each value minus 1, giving -1, 0, 1, 2.
# After the loop finishes normally, the else block runs.
# num keeps its last value, 3, so the final output is 3.

# %%
for i in range(0,6,3):
    print(i)

# range(start, stop, step) starts at 0, increases by 3, and stops before 6.
# Therefore, the values printed are 0 and 3.

# %%
x = 1
y = 0

z = ((x == y) and (x == y)) or not (x == y)
print(not(z))

# x == y is False because 1 is not equal to 0.
# False and False gives False.
# not(False) gives True.
# False or True gives True, so z becomes True.
# not(z) therefore prints False.

# %%
x = 4
y = 1

a = x & y
b = x | y
c = ~x
d = x ^ 5
e = x >> 2
f = x << 2

print(a, b, c, d, e, f)

# & performs bitwise AND, so 4 & 1 gives 0.
# | performs bitwise OR, so 4 | 1 gives 5.
# ~ performs bitwise NOT, and in Python ~x = -(x + 1), so ~4 gives -5.
# ^ performs bitwise XOR, so 4 ^ 5 gives 1.
# >> shifts bits to the right, so 4 >> 2 gives 1.
# << shifts bits to the left, so 4 << 2 gives 16.
# Output: 0 5 -5 1 1 16

# %%
lst = [1, 2, 3, 4, 5]
lst.insert(1,6)
del lst[0]
lst.append(1)
print(lst)

# insert(1, 6) places 6 at index 1.
# del lst[0] removes the first element.
# append(1) adds 1 to the end of the list.
# Final output: [6, 2, 3, 4, 5, 1]

# %%
lst = [1, 2, 3, 4, 5]
lst_2 = []
add = 0
for number in lst:
    add += number
    lst_2.append(add)
print(lst_2)

# add stores a running total of the values in lst.
# After each addition, the current total is appended to lst_2.
# The cumulative totals are 1, 3, 6, 10, and 15.
# Output: [1, 3, 6, 10, 15]

# %%
"""
lst = []
del lst
print(lst)
"""

# del lst removes the variable itself, not just the contents of the list.
# After deletion, lst no longer exists.
# Trying to print it causes a NameError.

# %%
lst = [1, [2, 3], 4]
print(lst[1])
print(len(lst))

# lst[1] accesses the second element, which is the nested list [2, 3].
# len(lst) counts the elements in the outer list only.
# The outer list has 3 elements: 1, [2, 3], and 4.
# Output: [2, 3] and 3

# %% [markdown]
# ### Table 3 (Lab 2.7)
# -------------------------------------------------------------------------------------------

# %%
list_1 = ["A", "B", "C"]
list_2 = list_1
list_3 = list_2

del list_1[0]
del list_2[0]

print(list_3)

# list_2 and list_3 reference the same list object as list_1.
# Deleting through any of these variables changes the same shared list.
# First "A" is removed, then "B" is removed.

# %%
list_1 = ["A", "B", "C"]
list_2 = list_1
list_3 = list_2

del list_1[0]
del list_2

print(list_3)

# All three variables initially reference the same list.
# del list_1[0] removes "A", leaving ["B", "C"].
# del list_2 deletes only the variable name list_2, not the actual list.
# list_3 still refers to the list.

# %%
list_1 = ["A", "B", "C"]
list_2 = list_1
list_3 = list_2

del list_1[0]
del list_2[:]

print(list_3)

# list_1, list_2 and list_3 all reference the same list.
# First "A" is removed.
# del list_2[:] removes every element from the shared list.
# Therefore list_3 also sees an empty list.

# %%
list_1 = ["A", "B", "C"]
list_2 = list_1[:]
list_3 = list_2[:]

del list_1[0]
del list_2[0]

print(list_3)

# [:] creates a new list instead of another reference to the same list.
# Changes to list_1 or list_2 therefore do not affect list_3.
# list_3 remains unchanged.

# %%
my_list = [1, 2, "in", True, "ABC"]

print(1 in my_list)
# Checks whether 1 exists in the list.
# Output: True

print("A" not in my_list)
# "A" is not an element of the list.
# Output: True

print(3 not in my_list)
# 3 does not exist in the list.
# Output: True

print(False in my_list)
# False is not present in the list.
# Output: False

# %%
lst = ["D", "F", "A", "Z"]
lst.sort()

print(lst)

# sort() rearranges the list in ascending/alphabetical order.
# It modifies the original list directly.

# %%
a = 3
b = 1
c = 2

lst = [a, c, b]
lst.sort()

print(lst)

# The list initially contains [3, 2, 1].
# sort() arranges numeric values in ascending order.

# %%
a = "A"
b = "B"
c = "C"
d = " "

lst = [a, b, c, d]
lst.reverse()

print(lst)

# reverse() reverses the current order of the list.
# It does not sort the values; it simply flips their positions.
# The space was last, so it becomes the first element.

# %% [markdown]
# ### Table 4 (Lab 2.7)
# -------------------------------------------------------------------------------------------

# %% [markdown]
# input() is a built-in Python function.
# It is provided by Python itself and does not need to be defined by the programmer.
# Answer: (b) built-in function

# %%
"""
hi()

def hi():
    print("hi!")
"""

# Python executes code from top to bottom.
# hi() is called before Python reaches its definition.
# Therefore, in a fresh program, this causes a NameError because hi is not yet defined.

# %%
"""
def hi():
    print("hi")

hi(5)
"""

# hi() is defined without parameters, so it expects 0 arguments.
# hi(5) passes one argument, which the function cannot accept.
# Result: TypeError.

# %%
def hi():
    return print("Hi!")

hi()

# print("Hi!") executes first, so "Hi!" is displayed.
# print() itself returns None, and the function returns that None value.

# %%
def intro(a="James Bond", b="Bond"):
    print("My name is", b + ".", a + ".")

intro()

# Both parameters have default values.
# Since intro() is called without arguments, Python uses a="James Bond" and b="Bond".
# The print() function combines them into: My name is Bond. James Bond.

# %%
"""
def add_numbers(a, b=2, c):
    print(a + b + c)

add_numbers(a=1, c=3)
"""

# b has a default value, but c does not.
# In Python, a required parameter cannot come after a parameter with a default value.
# Result: SyntaxError - non-default argument follows default argument.

# %% [markdown]
# ### A valid version of the above would be:

# %%
def add_numbers(a, c, b=2):
    print(a + b + c)

add_numbers(a=1, c=3)

# %%
def is_int(data):
    if type(data) == int:
        return True
    elif type(data) == float:
        return False

print(is_int(5))
print(is_int(5.0))
print(is_int("5"))

# 5 is an int, so the function returns True.
# 5.0 is a float, so the function returns False.
# "5" is a string, so neither condition is satisfied.
# When a function reaches the end without return, Python automatically returns None.

# %%
"""
def message():
    alt = 1
    print("Hello, World!")

print(alt)
"""

# %% [markdown]
# ###  A valid version of the code above would be:

# %%
def message():
    alt = 1
    print(alt)

message()
