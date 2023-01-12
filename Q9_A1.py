num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd number: "))
a = 0
l = []
if num1>num2 :
  a = num1
else:
  a= num2
for i in range(1,a):
  if num1%i == 0 and num2%i == 0:
    l.append(i)
print("Gcd is: ",l[-1])
print("Lcm is: ",l[0])
