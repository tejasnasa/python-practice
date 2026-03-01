dict = {}

n = int(input("Enter num: "))

for i in range(0,n):
  key = input("Enter key: ")
  val = input("Enter value: ")
  dict.update({key: val})

for item in dict.items():
  print(item)