class Object:
    def __init__(self, name, description, pickable=True):
        self.name = name
        self.description = description
        self.pickable = pickable

    def to_dict(self):
        """Convert object to a dictionary for saving."""
        return {"name": self.name, "description": self.description, "pickable": self.pickable}

    @staticmethod
    def from_dict(data):
        """Recreate object from a dictionary."""
        return Object(data["name"], data["description"], data["pickable"])
