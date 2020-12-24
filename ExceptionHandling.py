try:
    def division():
         x=int(input("Enter the number: "))
         y=int(input("Enter the 2nd number: "))
         return  x/y
    print(division())
except ZeroDivisionError:
    print("Division by zero not possible")
except ValueError:
    print("Invalid input")

finally:
    print(pow(4,2))

locals()['__builtins__']#Lists all the built in exceptions