t = int(input("Enter the number of times: "))
for i in range(t):
  c = 0
  n = int(input("Enter a number: "))
  for j in range(1,n+1):
    if n%j == 0:
      c+=1
  if c == 2:
    print('Prime')
  else:
    print("Not Prime")
