from color import Color    

class CommandParser:
    def __init__(self, game):
        self.game = game

    def parse(self, command):
        command = command.strip().lower()
        aliases = {"n": "go north", "s": "go south", "e": "go east", "w": "go west"}
        command = aliases.get(command, command)

        if command.startswith("take"):
            item = command.split(" ", 1)[1]
            self.game.do_take(item)
        elif command.startswith("go"):
            direction = command.split(" ", 1)[1]
            self.game.do_go(direction)
        elif command == "inventory":
            self.game.do_inventory("")
        elif command == "look":
            self.game.do_look("")
        elif command == "save":
            self.game.do_save("")
        elif command == "load":
            self.game.do_load("")
        elif command == "quit":
            self.game.do_quit("")
        elif command.startswith("drop"):
            item = command.split(" ", 1)[1]
            self.game.do_drop(item)
        else:
            print(Color.FAIL+"I don't understand that command."+Color.ENDC)
