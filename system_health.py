import os
def menu():
	print("1.Display avaliable ram")
	print("2.Display load average")
	print("3.Display host name details")
	print("4.All process count")
	print("5.Display uptime")
	print("6.Exit")
def avaliable_ram():
	command = 'free -m | tr -s " " | cut -d " " -f4 | head -n 2 | tail -n 1'
	result = os.popen(command).read()
	print(f"\t\tAvaliable ram on system is {result}" )
def disp_load_average():
	command = 'cat /proc/loadavg'
	result = os.popen(command).read()
	print(f"\t\t{result}")
def disp_host_name():
	command = 'hostnamectl status'
	result = os.popen(command).read()
	print(f"\t\t{result}")
def process_count():
	command = 'ps -a | wc -l'
	result = os.popen(command).read()
	print(f"\t\t{result}")	
def disp_uptime():
	command = 'uptime | cut -d " " -f2,3'
	result = os.popen(command).read()
	print(f"\t\t{result}")	
while True:
	menu()
	ch = input("Enter your choice :  ")
	if ch == '1':
		avaliable_ram()
	elif ch == '2':
		disp_load_average()
	elif ch == '3':
		disp_host_name()
	elif ch == '4':
		process_count()
	elif ch == '5':
		disp_uptime()
	elif ch == '6':
		break
	else:
		print("\t\tInvalid input, try again")
