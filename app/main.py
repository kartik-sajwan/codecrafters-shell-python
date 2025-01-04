import sys


def main():
	while True:
		sys.stdout.write("$ ")

		# Wait for user input
		command = input()

		if "exit" in command:
			sys.exit(0)
		elif "echo" in command:
			split_str = command.split(" ")
			echo_txt = " ".join(split_str[1:])
			sys.stdout.write(echo_txt + "\n")
		else:
			sys.stdout.write(f"{command}: command not found\n")




if __name__ == "__main__":
    main()
