list = []

for i in range(0,6):
  marks = int(input("Enter marks: "))
  list.append(marks)

list.sort()

for marks in list:
  print(marks)