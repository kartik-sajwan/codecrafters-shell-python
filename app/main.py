import sys


def main():
	while True:
		sys.stdout.write("$ ")

		# Wait for user input
		command = input()

		if "exit" in command:
			sys.exit(0)

		sys.stdout.write(f"{command}: command not found\n")




if __name__ == "__main__":
    main()
