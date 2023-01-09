print("TThis is Calculator, please insert in next step two numbers and you will receive result.")

x = int(input("Insert the first number:"))
y = int(input("Insert the second number:"))
z = input("What type of operator you want to use(+,-,*,/,**)")

operators = {"+": x+y, "-": x-y, "*": x*y, "/": x/y, "**": x**y}

if z == "+":
    print(operators["+"])
elif z == "-":
    print(operators["-"])
elif z == "*":
    print(operators["*"])
elif z == "/":
    print(operators["/"])
elif z == "**":
    print(operators["**"])
else:
    print("Error: operator not found(make sure you used the designated operators)")
