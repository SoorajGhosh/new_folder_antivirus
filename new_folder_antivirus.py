import os

print('''Welcome to the New folder.exe virus removal tool. Plz specify the path or drive to scan..!
PATH example:- C:\\Users\\user\\Desktop\\my_folder
DRIVE example:- D:
	''')

def get_path():
	while True:
		route = str(input('Enter the route  or enter \'q\' to exit: '))
		if os.path.exists(route) or route=="q":
			return route
		else:
			print("Invalid path..!")
			continue

virus_count=0

def scan(path):
	for current_dir,dirs,files in os.walk(path):
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
		print("-"*22)

def check_status():
	print('Scan Complete..!')
	if virus_count>0:
		print(f'Total Virus found: {virus_count}')
	else:
		print("No virus found..!")


def main():
	while True:
		path = get_path()
		if path=="q":
			break
		scan(path)
		check_status()
		
		try_again = str(input("Scan another Drive (reply \"y\" for Yes and \"n\" for No:)"))
		if try_again.lower() == "n" :
			break
		elif try_again.lower=="y":
			continue
		else: 
			print("Please enter a valid input..!")
			continue

main()	