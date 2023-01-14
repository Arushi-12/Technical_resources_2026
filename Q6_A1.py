n=int(input("Enter a number: "))
s = ''
while n>0:
  s += str(n%10)
  n //= 10
print(s)
