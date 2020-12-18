import sys
from os import system

try:
	def banner():
		print("To_do_Application : ")
		print("=================")
		print("[+] python todo.py add 'EVENT'    (add events)")
		print("[+] python todo.py delete 'NUMBER'   (delete events)")
		print("[+] python todo.py done 'NUMBER'  (add event)")
		print("[+] python todo.py ls 		  (list events)")
		print("[+] python todo.py delall         (delete all events)")
		print("[+] python todo.py help           (displays usage)")
		print("[+] python todo.py report         (Statistics)")
	
	def add(event):
		a = open('./todo.txt', 'a')
		a.write(str(event))
		a.write('\n')
		a.close()
		print("[+] The Event {} is added".format(event))
	
	def delete(num):
		try:
			a = open("./todo.txt", "r")
			b = a.readlines()
			data = str(b[num-1]).rstrip()
			b.pop(num-1)
			a.close()
		
			c = open("./todo.txt", "w")
			for i in range(len(b)):
				c.write(b[i])
			c.close()
			print("[+] The Event {} is deleted !".format(data))
		
		except IndexError:
			print("[+] No Event Found !")
	
	def lists():
		a = open("./todo.txt", 'r')
		b = a.readlines()
		print("List of all Saved Events ")
		print("=========================")
		for j,i in enumerate(range(len(b)), 1):
			print('{})'.format(j),b[i].rstrip())
	
	def helps():
		banner()

	def done(num):
		a = open("./todo.txt", "r")
		b = a.readlines()
		did = str(b[num-1]).rstrip()
		b.pop(num-1)
		a.close()

		d = open("./todo.txt", "w")
		for i in range(len(b)):
			d.write(b[i])
		d.close()

		c = open("./done.txt", "a")
		c.write(str(did))
		c.write('\n')
		c.close()

		print("[+] The Event {} marked as done".format(did))

	def report():
		a = open("./todo.txt", 'r')
		b = a.readlines()
		print("Report of your events")
		print("=====================")
		print("\n[+] To-Do\n---------")
		for j,i in enumerate(range(len(b)), 1):
			print('{})'.format(j),b[i].rstrip())
		try:
			c = open("./done.txt", 'r')
			d = c.readlines()
			print("\n[+] Done\n---------")
			for j,i in enumerate(range(len(d)), 1):
				print('{})'.format(j),d[i].rstrip())
		except FileNotFoundError:
			print("\n[+] No Events You have done !")


	def delall():
		system('rm todo.txt')
		system('rm done.txt')
		print("[+] All saved Events deleted !")


	if sys.argv[1] == 'add':
		add(sys.argv[2])
	elif sys.argv[1] == 'delete':
		delete(int(sys.argv[2]))
	elif sys.argv[1] == 'done':
		done(int(sys.argv[2]))
	elif sys.argv[1] == 'ls':
		lists()
	elif sys.argv[1] == 'help':
		banner()
	elif sys.argv[1] == 'report':
		report()
	elif sys.argv[1] == 'delall':
		delall()
	else:
		print("Invalid command ! Try again !")


except FileNotFoundError:
	print("[+] There are no events added")

except:
	banner()









	
	
	