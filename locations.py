from color import Color
from game_objects import Object

class Location:
    def __init__(self, name, description, exits=None, objects=None):
        self.name = name
        self.description = description
        self.exits = exits if exits else {}
        self.objects = objects if objects else []

    def describe(self):
        obj_list = ", ".join([obj.name for obj in self.objects]) if self.objects else "nothing of interest"
        exit_list = ", ".join(self.exits.keys())
        return f"{Color.OKGREEN}{self.description}\nYou see: {obj_list}.\nExits: {exit_list}.{Color.ENDC}"

    def add_object(self, obj):
        self.objects.append(obj)

    def remove_object(self, obj):
        self.objects.remove(obj)

    def to_dict(self):
        """Convert location to a dictionary for saving."""
        return {
            "name": self.name,
            "description": self.description,
            "exits": self.exits,
            "objects": [obj.to_dict() for obj in self.objects]
        }

    @staticmethod
    def from_dict(data):
        """Recreate location from a dictionary."""
        return Location(
            data["name"],
            data["description"],
            data["exits"],
            [Object.from_dict(obj) for obj in data["objects"]]
        )
