n = int(input("N: "))
sum = 0

for i in range (0,n):
  x = int(input("val" + str(i) + ": "))
  sum += x

print("Sum = " + str(sum))