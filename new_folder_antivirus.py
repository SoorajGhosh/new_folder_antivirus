import os

route = str(input('Enter the route: '))
os.chdir(route)
# current working directory
cwd = os.getcwd()
print(f'Searching for virus in {cwd}')


for item in os.walk(cwd):
	print(item)
