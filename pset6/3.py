a = "make a lot of money"
b = "buy now"
c = "subscribe this"
d = "click this"

s = input("Enter statement: ")

if (a in s or b in s or c in s or d in s):
  print("Keyword found!")