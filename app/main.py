import sys


def main():
	while True:
		sys.stdout.write("$ ")

		# Wait for user input
		command = input()
		sys.stdout.write(f"{command}: command not found\n")

		if "exit" in command:
			sys.exit(0)



if __name__ == "__main__":
    main()
