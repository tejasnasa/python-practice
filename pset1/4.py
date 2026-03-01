import os

directory_path = "../"

# single line comment

"""multiple
line
comment"""

contents = os.listdir(directory_path)

for item in contents:
	print(item)