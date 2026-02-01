def factorial (num):
    if num == 1:
        return 1
    else:
        output = num * factorial(num-1)
        return output


value = int(input("Enter the value: "))
print (f"Factorial value for {value} is {factorial(value)}")

