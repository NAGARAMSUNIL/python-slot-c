def sumDigits(num):
  if num == 0:
    return 0
  else:
    return num % 10 + sumDigits(int(num / 10))

x = int(input("enter the digits"))
print("Number: ", x)
print("Sum of digits: ", sumDigits(x))
print()
