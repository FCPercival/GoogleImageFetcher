import sys
import CommandHandler


def main(argv):
    command_handler = CommandHandler.CommandHandler()
    command_handler.handle_commands(argv)


if __name__ == "__main__":
    main(sys.argv[1:])