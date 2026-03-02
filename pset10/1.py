class Programmer:
	def __init__(self, name):
		self.name = name

harry = Programmer("Harry")
james = Programmer("James")

programmers = [harry, james]

for programmer in programmers:
	print(programmer.name)