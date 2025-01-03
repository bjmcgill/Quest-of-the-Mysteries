import cmd
import shutil
import textwrap
import json
from player import Player
from world_builder import WorldBuilder
from command_parser import CommandParser
from locations import Location
from color import Color

class AdventureGame(cmd.Cmd):
    intro = Color.HEADER + "Welcome to Quest of the Mysteries! Type 'help' or '?' to list commands.\n" + Color.ENDC
    prompt = Color.WARNING + "---> " + Color.ENDC

    def __init__(self):
        super().__init__()
        self.player = Player()
        self.locations = WorldBuilder.build_world()
        self.current_location = self.locations["Garden"]
        self.parser = CommandParser(self)
        self.terminal_width = self.get_terminal_width()

    def get_terminal_width(self):
        """Determine terminal width, defaulting to 80 columns if an error occurs."""
        try:
            return shutil.get_terminal_size().columns
        except Exception:
            return 80  # Default width if unable to get terminal size

    def wrap_text(self, text):
        """Wrap text to fit the terminal width."""
        return textwrap.fill(text, width=self.terminal_width)

    def save_game(self, filename="savegame.json"):
        """Save the game state to a JSON file."""
        game_state = {
            "player": self.player.to_dict(),
            "locations": {name: loc.to_dict() for name, loc in self.locations.items()},
            "current_location": self.current_location.name
        }
        with open(filename, "w") as file:
            json.dump(game_state, file, indent=4)
        print(self.wrap_text(f"{Color.OKGREEN}Game saved successfully!{Color.ENDC}"))

    def load_game(self, filename="savegame.json"):
        """Load the game state from a JSON file."""
        try:
            with open(filename, "r") as file:
                game_state = json.load(file)
            self.player = Player.from_dict(game_state["player"])
            self.locations = {name: Location.from_dict(loc) for name, loc in game_state["locations"].items()}
            self.current_location = self.locations[game_state["current_location"]]
            print(self.wrap_text(f"{Color.OKGREEN}Game loaded successfully!{Color.ENDC}"))
            self.do_look("")

        except (FileNotFoundError, json.JSONDecodeError):
            print(self.wrap_text(f"{Color.FAIL}Failed to load the game. Save file may not exist or be corrupted.{Color.ENDC}"))
            
    def do_look(self, arg):
        """Look around the current area."""
        print(self.wrap_text(self.current_location.describe()))

    def do_take(self, arg):
        """Take an object. Usage: take [object_name]"""
        if not arg:
            print("Take what?")
            return
        obj = next((o for o in self.current_location.objects if o.name == arg), None)
        if obj:
            print(self.player.take_object(obj, self.current_location))
        else:
            print(f"{Color.FAIL}There is no {arg} here.{Color.ENDC}")

    def do_drop(self, arg):
        """Drop an object. Usage: drop [object_name]"""
        if not arg:
            print("Drop what?")
            return
        obj = next((o for o in self.player.inventory if o.name == arg), None)
        if obj:
            print(self.player.drop_object(obj, self.current_location))
        else:
            print(f"{Color.FAIL}You don't have a {arg}.{Color.ENDC}")

    def do_inventory(self, arg):
        """Show your inventory."""
        print(self.player.show_inventory())

    def do_go(self, arg):
        """Move in a direction. Usage: go [direction]"""
        if not arg:
            print("Go where?")
            return
        if arg in self.current_location.exits:
            next_location_name = self.current_location.exits[arg]
            self.current_location = self.locations[next_location_name]
            print(self.wrap_text(f"{Color.OKCYAN}You go {arg}.{Color.ENDC}"))
            self.do_look("")
        else:
            print(f"{Color.FAIL}You can't go that way.{Color.ENDC}")

    def do_save(self, arg):
        """Save the current game state."""
        self.save_game()

    def do_load(self, arg):
        """Load a previously saved game state."""
        self.load_game()

    def do_quit(self, arg):
        """Quit the game."""
        print(self.wrap_text(f"{Color.OKBLUE}Thank you for playing!{Color.ENDC}"))
        return True

    def default(self, line):
        """Handle commands through the CommandParser."""
        self.parser.parse(line)


if __name__ == "__main__":
    AdventureGame().cmdloop()
