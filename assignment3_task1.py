num = int(input("Enter a number: "))

# Method 1 : Calculates the factorial using a for loop.

def factorial1(n):
    f = 1
    for i in range(1, n + 1):
        f *= i
    return f

result1 = factorial1(num)
print("\nOutput using Method 1")
print("Factorial of 5 is:",result1)

# Method 2 : Calculates the factorial using a while loop.

def factorial2(n):
    f = 1; i = 1
    while i <= n:
        f *= i
        i += 1
    return f

result2 = factorial2(num)
print("\nOutput using Method 2")
print("Factorial of 5 is:",result2)

# Method 3 : Calculates the factorial using a recursion.

def factorial3(n):
    if n < 2:
        return 1
    else:
        return n * factorial3(n - 1)

result3 = factorial3(num)
print("\nOutput using Method 3")
print("Factorial of 5 is:",result3)