import os

route = str(input('Enter the route: '))
# os.chdir(route)
# # current working directory
# cwd = os.getcwd()
# print(f'Searching for virus in {cwd}')

virus_count=0

for current_dir,dirs,files in os.walk(route):
	print(f'Searching for virus in {current_dir}')
	print('\n')
	check_list = [os.path.basename(current_dir)+'.exe','New folder.exe']
	for item in check_list:
		if item in files:
			virus_count+=1
			virus_path = current_dir+'\\'+item
			print('Virus path: '+virus_path)
			print('Removing virus...!')
			os.remove(virus_path)
			print('Virus removed Succesfully...!')
			print("\n")
	# print(f'Virus: {check_list}')
	print("-"*22)

print('Scan Complete..!')
if virus_count>0:
	print(f'Total Virus found: {virus_count}')
else:
	print("No virus found..!")


# os.path.basename()
# os.isdir()
# os.walk()
# NEW Folder and parent folder name executables