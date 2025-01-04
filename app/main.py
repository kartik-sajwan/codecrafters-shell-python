import sys
import os

PATH = os.environ.get("PATH")

def echo(args):
	echo_txt = " ".join(args)
	sys.stdout.write(echo_txt + "\n")


def exit(args):
	sys.exit(0)


def type(args):
	command = args[0]

	path_list = PATH.split(":")
	if command in builtin_commands:
		sys.stdout.write(f"{command} is a shell builtin\n")
		return
	elif command:
		for path in path_list:
			if os.path.isfile(f"{path}/{command}"):
				sys.stdout.write(f"{command} is {path}/{command}\n")
				return None

	sys.stdout.write(f"{command}: not found\n")



builtin_commands = {
	"echo": echo,
	"exit": exit,
	"type": type
}


def main():
	while True:
		# Wait for user input
		user_input = input("$ ")
		split_cmd_str = user_input.split(" ")
		command = split_cmd_str[0]
		args = split_cmd_str[1:]

		if command in builtin_commands:
			builtin_commands[command](args)
		else:
			sys.stdout.write(f"{command}: command not found\n")


if __name__ == "__main__":
    main()
