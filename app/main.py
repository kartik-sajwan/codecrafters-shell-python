import sys


def main():
	while True:
		sys.stdout.write("$ ")

		# Wait for user input
		command = input()

		if "exit" in command:
			sys.exit(0)
		elif "echo" in command:
			split_string = command.split(" ")
			sys.stdout.write(" ".join(split_string[1:]))
		else:
			sys.stdout.write(f"{command}: command not found\n")




if __name__ == "__main__":
    main()
