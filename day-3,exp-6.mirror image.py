def solve(n):
   num_str = str(n)
   for i in range(len(num_str)):
      if num_str[i] not in ['0', '1', '8']:
         return False
   left = 0
   right = len(num_str) - 1
   while left < right:
      if num_str[left] != num_str[right]:
         return False
      left += 1
      right -= 1
   return True
n = 818
print(solve(n))
