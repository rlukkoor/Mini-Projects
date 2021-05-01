def linear_search(list1, n):
  i = 0
  
  while i < len(list1):
    if list1[i] == n:
      return True
    i = i+1
  return False   


list1 = [1, 2, 3, 9, 7, 4]

n = 7

if linear_search(list1, n):
  print("number found")
else:
  print("number not found")