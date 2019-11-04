import os

def get_path():
	while True:
		try:
			route = str(input('Enter the route: '))
			os.chdir(route)
			return route
			break
		except:
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
	path = get_path()
	scan(path)
	check_status()

while True:
	main()
	try_again = str(input("Scan another Drive (reply \"y\" for Yes and \"n\" for No:)"))
	if try_again.lower() == "n" :
		break
	elif try_again.lower=="y":
		continue
