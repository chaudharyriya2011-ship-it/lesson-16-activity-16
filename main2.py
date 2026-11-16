try:
    num1,num2 = eval(input("Enter two numbers separated by a comma: "))
    result = num1/num2
    print("The result is:", result)
except ZeroDivisionError:
    print("Division with zero is an Error!")
except SyntaxError:
    print("You have to put a comma in between the numbers!")
except:
    print("Wrong input!")
else:
    print("no exception!")
finally:
    print("This will execute no matter what!")