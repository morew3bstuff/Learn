# Also get the path to the script in the console so I space the output
print()
print("The print() function allows you to print text to the command line.")
print()

# Ex 1 - When you run the program it should print the following:

# Day 1 - Python Print Function
# The function is declared like this:
# print("Display text goes here")

print("Ex 1 - Printing")
print("-" * 50)
print("Day 1 - Python Print Function")
print("The function is declared like this:")
print("""print("Display text goes here")""")
print()

# \n - new line
print("Hello World!\nHello World!\nHello World!")
print()

# Concatenation
print("Hello" + " Alex")
print()

# Ex 2 - Debugging
print("Ex 2 - Debugging")
print("-" * 50)
print("""B: print(Day 1 - String Manipulation")""")
print("""C: print("Day 1 - String Manipulation")""")
print()
print("""B: print("String concatenation is done with the "+" sign.")""")
print("""C: print('String concatenation is done with the "+" sign.')""")
print()
print("""B: [space] print("Hello World.")""")
print("""C: [no space, it will cause an indent error] print("Hello World.")""")
print()
print("""B: print(("New lines can be created with a backslash and n.")""")
print("""C: print("New lines can be created with a backslash and n.")""")
print()

# input - ask for information; funtion runs before print
# variable to store the return of the input function
name = input("What's your name?\n")
print("Hello " + name + "!")
print()

# Ex 3 - Lenght of input string
print("Ex 3 - Lenght of input string")
print("-" * 50)
print("Given name has " + str(len(name)) + " characters")
print()

# Ex 4 - Switch values
a = input("a: ")
b = input("b: ")
c = b
b = a
a = c

print()
print("a: " + a)
print("b: " + b)