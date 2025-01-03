from game_objects import Object
from color import Color

class Player:
    def __init__(self):
        self.inventory = []

    def take_object(self, obj, location):
        if obj in location.objects:
            location.remove_object(obj)
            self.inventory.append(obj)
            return f"{Color.OKGREEN}You picked up the {obj.name}.{Color.ENDC}"
        else:
            return f"{Color.FAIL}There is no {obj.name} here.{Color.ENDC}"

    def drop_object(self, obj, location):
        if obj in self.inventory:
            self.inventory.remove(obj)
            location.add_object(obj)
            return f"{Color.OKGREEN}You dropped the {obj.name}.{Color.ENDC}"
        else:
            return f"{Color.FAIL}You don't have a {obj.name}.{Color.ENDC}"

    def show_inventory(self):
        if self.inventory:
            return f"{Color.OKBLUE}You are carrying: {', '.join([obj.name for obj in self.inventory])}{Color.ENDC}"
        else:
            return f"{Color.WARNING}Your inventory is empty.{Color.ENDC}"

    def to_dict(self):
        """Convert player to a dictionary for saving."""
        return {"inventory": [obj.to_dict() for obj in self.inventory]}

    @staticmethod
    def from_dict(data):
        """Recreate player from a dictionary."""
        player = Player()
        player.inventory = [Object.from_dict(obj) for obj in data["inventory"]]
        return player
