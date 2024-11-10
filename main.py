match= input("Enter an arithmetic expression: ")

if '+' in match:
    num1, num2 = match.split('+')
    result = float(num1) + float(num2)
elif '-' in match:
    num1, num2 = match.split('-')
    result = float(num1) - float(num2)
elif '*' in match:
    num1, num2 = match.split('*')
    result = float(num1) * float(num2)
elif '/' in match:
    num1, num2 = match.split('/')
    if float(num2) == 0:
        print("Eror 303!")
    else:
        result = float(num1) / float(num2)
else:
    print("Z ne znay chto eto :)")
    result = None

if result is not None:
    print("result:", result)