# importing the required modules
import os
import argparse

def show_version():
	print("show version")
def attach(args):
	container_name=args.attach[0]
	print(container_name)
	print("attach a container")
def delete(args):
	print("delete speaker")
	command=args.delete[0]
	print(command)
def add(args):
	print(" add speaker")
	command=args.add[0]
	print(command)
	

def main():
	# create parser object
	parser = argparse.ArgumentParser(description = "v router manager")

	# defining arguments for parser object
	parser.add_argument("-a", "--attach", type = str, nargs = 1,
						metavar = "container_name", default = None,
						help = "attach a docker container.")
	
	parser.add_argument("-v", "--version",nargs = '*',
						help = "Shows git version")
	
	parser.add_argument("-d", "--delete", type = str, nargs =1,
						metavar = ('name'), help = "add  a apeaker")
	parser.add_argument("-add", "--add", type = str, nargs = 2,
						metavar = ('name','subnet'), help = "delete a apeaker")
	

	# parse the arguments from standard input
	args = parser.parse_args()
	
	# calling functions depending on type of argument
	if args.version != None:
		show_version()
	elif args.delete != None:
		delete(args)
	elif args.add !=None:
		add(args)
	elif args.attach !=None:
		attach(args)

if __name__ == "__main__":
	# calling the main function
	main()