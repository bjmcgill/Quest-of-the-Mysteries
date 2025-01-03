from locations import Location
from game_objects import Object
from color import Color

class WorldBuilder:
    @staticmethod
    def build_world():
        sword = Object("sword", "A sharp, shiny sword.")
        key = Object("key", "A small, rusty key.")
        
        garden = Location(
            "Garden",
            "A peaceful garden with blooming flowers.",
            {"north": "House"},
            [sword]
        )
        
        house = Location(
            "House",
            "A cozy little house with a warm fireplace.",
            {"south": "Garden"},
            [key]
        )
        
        return {"Garden": garden, "House": house}
