import os

route = str(input('Enter the route: '))
os.chdir(route)
print(f'Searching for virus in {os.cwd()}')
