def FizzBuzz(n):
    num = 0
    for i in range(1, n + 1):
        if i % 15 == 0:
            print("FizzBuzz")
        elif i % 5 == 0:
            print("Buzz")
        elif i % 3 == 0:
            print("Fizz")
        else:
            print(i)
        num = i
    return num


while True:
    n = int(input())
    num = FizzBuzz(n)
    if num % 15 == 0:
        break
