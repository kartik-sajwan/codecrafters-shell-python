import sys
import os

PATH = os.environ.get("PATH")


def echo(args: list):
	echo_txt = " ".join(args)
	sys.stdout.write(echo_txt + "\n")


def exit(args: list):
	sys.exit(0)


def type(args: list, silent: bool = False):
	if isinstance(args, list):
		command = args[0]
	else:
		command = args

	path_list = PATH.split(":")
	if command in builtin_commands:
		sys.stdout.write(f"{command} is a shell builtin\n")
		return
	elif command:
		for path in path_list:
			if os.path.isfile(f"{path}/{command}"):
				if silent:
					return True
				sys.stdout.write(f"{command} is {path}/{command}\n")
				return
	if silent:
		return
	sys.stdout.write(f"{command}: not found\n")


def pwd(args: list):
	sys.stdout.write(f"{os.getcwd()}\n")


def cd(args: list):
	try:
		if args:
			os.chdir(args[0])
	except Exception:
		sys.stdout.write(f"cd: {args[0]}: No such file or directory\n")

builtin_commands = {
	"echo": echo,
	"exit": exit,
	"type": type,
	"pwd": pwd,
	"cd": cd
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
		elif type(command, silent=True):
			args_str = "".join(args)
			os.system(f"{command} {args_str}")
		else:
			sys.stdout.write(f"{command}: command not found\n")


if __name__ == "__main__":
    main()
