def sum_to(num):
  total = 0
  for n in range(1, num + 1):
    total += n
  return total

# print(sum_to(6))
# print(sum_to(10))

def largest(*args):
  return max(*args)


# print(largest([1, 2, 3, 4, 0]))  # returns 4
# print(largest([10, 4, 2, 231, 91, 54])) # returns 231
