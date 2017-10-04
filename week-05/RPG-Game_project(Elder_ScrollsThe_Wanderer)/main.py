from level_map import Map
from viewer import Viewer


class Game:
    
    def __init__(self):
        self.my_map = Map()
        self.my_view = Viewer()
        self.my_view.draw_area()
        self.my_view.display()

game = Game()